import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
json = __import__("json")
audit = __import__("conditioning_v2.audit", fromlist=["uses"])
retention = __import__("conditioning_v2.retention", fromlist=["uses"])
conditioning = __import__("hle_unified.conditioning_audit", fromlist=["observations"])
energy = __import__("hle_unified.energy_audit", fromlist=["blocks", "data"])
axes = __import__("hle_unified.axes", fromlist=["load", "tilt", "axis_cells"])
model = __import__("hle.model_a", fromlist=["fields", "element_at"])
relations = __import__("hle.relations", fromlist=["landing_permutation"])
LABEL_PATH = ROOT / "baseline/HLE_Rebuild_R21B/baseline/crossing/sources/relation_labels.json"
LABELS = json.loads(LABEL_PATH.read_text())
WEAK = tuple(p for p in range(1, 9) if model.fields(p)["dimensionality"] <= 2)
BENEFIT = ("benefit", "benefit_inverse")


def actor_name(actor):
    return actor.namespace + ":" + actor.key


def relation_name(sender_tim, receiver_tim):
    entry = LABELS[sender_tim + ":" + receiver_tim]
    if tuple(entry["landing_permutation"]) != relations.landing_permutation(sender_tim, receiver_tim):
        raise ValueError("relation label landing permutation differs from kernel")
    return entry["relation"]


def dcnh(actor, tim, records):
    counts = dict.fromkeys(conditioning.ELEMENTS, 0)
    for row in records:
        counts[row["element"]] += 1
    field = {p: counts[model.element_at(tim, p)] for p in range(1, 9)}
    loads = axes.load(field)
    cells = axes.axis_cells(tim)
    return dict(actor=actor, tim=tim, counts=counts, axis_loads=loads,
                axis_tilts=axes.tilt(field), axis_cells=cells,
                cells_with_greatest_load=tuple(c for c, n in zip(cells, loads) if n == max(loads)),
                formula_sums={c: sum(field[p] for p in axes.formula_positions(tim, c)) for c in 'DCNH'},
                interpretation='cell with the greatest load; ties are ties; not a subtype',
                source_caveat='2+1 formulas via UMA section 15, not independently checked against Gulenko')


def summarize(profiles, records, episodes, episode_indices):
    """Pure aggregation of validated Batch 3 observations; IDs index records.

    A1 is applied literally: conditioning-index numerator and denominator both
    use actor-id sources at weak seats. This is degenerate (1 when defined),
    not the original all-source denominator. Tables disclose this explicitly.
    """
    profiles, records = dict(profiles), tuple(records)
    episodes, episode_indices = tuple(episodes), tuple(sorted(set(episode_indices)))
    if len(episodes) != len(records):
        raise ValueError("each use requires an episode")
    if any(type(e) is not int or e < 0 for e in (*episodes, *episode_indices)):
        raise ValueError("invalid episode index")
    if not set(episodes) <= set(episode_indices):
        raise ValueError("use episode absent from recorded episodes")
    for row in records:
        try:
            audit._validate_record(row, profiles)
            if type(row["kept"]) is not bool:
                raise ValueError("kept must be Boolean")
        except KeyError as exc:
            raise ValueError("incomplete use record") from exc

    received = tuple(i for i, r in enumerate(records) if r["source"] in profiles)
    by_actor = {}
    for actor, tim in sorted(profiles.items()):
        all_ids = tuple(i for i, r in enumerate(records) if r["actor"] == actor)
        incoming = tuple(i for i in received if records[i]["actor"] == actor)
        weak = tuple(i for i in incoming if records[i]["dim"] <= 2)
        held = tuple(i for i in incoming if records[i]["kept"])
        profile, suppliers = {}, {p: {} for p in WEAK}
        for i in all_ids:
            r = records[i]
            source = r["source"] if r["source"] in ("self", "world") else "other"
            profile.setdefault((r["seat"], source, r["kept"]), []).append(i)
        for i in weak:
            r = records[i]
            suppliers[r["seat"]].setdefault(r["source"], []).append(i)
        by_actor[actor] = dict(tim=tim, active=bool(all_ids), all_ids=all_ids,
                              profile=profile, incoming=incoming, held=held,
                              conditioning=(len(weak), len(weak)), conditioning_ids=weak,
                              hold=(len(held), len(incoming)), suppliers=suppliers,
                              all_dcnh=dcnh(actor, tim, (records[i] for i in all_ids)),
                              received_kept_dcnh=dcnh(actor, tim, (records[i] for i in held)))

    denominator = tuple((a, p) for a in sorted(profiles) for p in WEAK)
    qualifying = tuple(i for i in received if records[i]["dim"] <= 2
                       and model.fields(records[i]["source_seat"])["dimensionality"] >= 3)

    def coverage(ids):
        ids = tuple(ids)
        pairs = tuple(sorted({(records[i]["actor"], records[i]["seat"]) for i in ids}))
        return dict(ratio=(len(pairs), len(denominator)), pairs=pairs, ids=tuple(ids),
                    denominator=denominator)

    supplier_ids = {}
    for i in received:
        supplier_ids.setdefault(records[i]["source"], []).append(i)
    concentration = (sum(len(ids) ** 2 for ids in supplier_ids.values()), len(received) ** 2)
    pairs = []
    for sender in sorted(profiles):
        for receiver in sorted(profiles):
            if sender == receiver:
                continue
            forward = tuple(i for i in received if records[i]["source"] == sender
                            and records[i]["actor"] == receiver)
            reverse = tuple(i for i in received if records[i]["source"] == receiver
                            and records[i]["actor"] == sender)
            pairs.append(dict(sender=sender, receiver=receiver,
                              relation=relation_name(profiles[sender], profiles[receiver]),
                              forward=forward, reverse=reverse, sterile=not forward and not reverse))
    benefit_ids = tuple(sorted(i for pair in pairs if pair["relation"] in BENEFIT
                               for i in pair["forward"]))
    return dict(profiles=profiles, records=records, episodes=episodes, actors=by_actor,
                received=received, coverage=coverage(qualifying),
                episode_coverage={e: coverage(i for i in qualifying if episodes[i] <= e)
                                  for e in episode_indices},
                suppliers=supplier_ids, concentration=concentration, pairs=pairs,
                benefit_ids=benefit_ids, standalone_pair=None)


def locate_uses(transactions, events, records, profiles):
    """Join canonical paid blocks to explicit scheduler episode keys."""
    lookup, episode_indices = {}, set()
    for event in events:
        actor, key, episode = event["actor"], event["key"], event["episode"]
        if actor not in profiles or type(key) is not str or not key:
            raise ValueError("invalid episode actor/key")
        if type(episode) is not int or episode < 0:
            raise ValueError("invalid episode index")
        episode_indices.add(episode)
        for suffix in ("", ":movement", ":feedback", ":admission"):
            join = actor, key + suffix
            if join in lookup and lookup[join] != episode:
                raise ValueError("conflicting episode attribution")
            lookup[join] = episode
    heads, locations = {}, []
    for tx_index, tx in enumerate(transactions):
        for version in tx.versions:
            d = energy.data(version)
            if d.get("record_type") == "operation":
                previous = heads.get(version.ref.identity)
                before = 0 if previous is None else energy.data(previous).get("completed", 0)
                for _, end, _, element in energy.blocks(d):
                    if element is None or not before < end <= d["completed"]:
                        continue
                    join = d["actor"], d["key"]
                    if join not in lookup:
                        raise ValueError("paid use lacks recorded episode")
                    i = len(locations)
                    if i >= len(records) or (records[i]["actor"], records[i]["element"]) != (d["actor"], element):
                        raise ValueError("use trace differs from Batch 3 sequence")
                    locations.append(dict(transaction=tx_index, operation=version.ref,
                                          block_end=end, episode=lookup[join]))
            heads[version.ref.identity] = version
    if len(locations) != len(records):
        raise ValueError("use trace count differs from Batch 3")
    return tuple(locations), tuple(sorted(episode_indices))


def history(transactions, events):
    transactions = tuple(transactions)
    records = retention.uses(transactions)
    profiles, _ = conditioning.completed_use(transactions)
    locations, indices = locate_uses(transactions, events, records, profiles)
    result = summarize(profiles, records, [loc["episode"] for loc in locations], indices)
    reference = {row["actor"]: row for row in conditioning.observations(transactions)}
    for actor, row in result["actors"].items():
        if row["all_dcnh"] != reference[actor]:
            raise ValueError("all-use DCNH differs from Phase 7 observations")
    result["locations"] = locations
    return result
