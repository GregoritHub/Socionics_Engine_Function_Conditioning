import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
json = __import__("json")
hashlib = __import__("hashlib")
f = __import__("tests_u11.fixtures", fromlist=["setup11"])
tables = __import__("conditioning_v2.tables", fromlist=["load_histories"])
measures = tables.measures
audit = measures.audit
PROJECT = pathlib.Path(__file__).resolve().parents[1]
SEEDS = (17, 29, 43, 61)
COMPOSITIONS = {"pair": "iee", "pair-sterile": "eie"}
QUANTUM = {"ordinary_fixture_perform": 100, "collective_work": 10000000,
           "physical_step_advance": 1000}


def argument(value):
    """Exact invocation arguments, with engine/record handles represented by refs."""
    if isinstance(value, f.CollectiveEngine):
        return "engine"
    if type(value) is f.ObjectId:
        return measures.actor_name(value)
    if type(value) is f.ObjectRef:
        return measures.actor_name(value.identity) + "@" + str(value.revision)
    if isinstance(value, dict):
        if "ref" in value:
            return {"record_ref": argument(value["ref"])}
        return {str(k): argument(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [argument(v) for v in value]
    if value is None or type(value) in (str, int, bool):
        return value
    # OperationRequest is frozen and its repr contains every constructor field.
    return repr(value)


def build(composition, seed):
    """Parameterize the accepted circuit's public fixture calls, not its journal.

    The fixture has no random seed input. Matched seeds choose a nonbinding
    finite budget; they do not constitute independent stochastic workloads.
    Eve remains the fixture's inactive SLI profile in every supported pair.
    """
    if composition not in COMPOSITIONS or seed not in SEEDS:
        raise ValueError("undeclared composition or seed")
    calls = []
    def invoke(name, *args, **kwargs):
        calls.append(dict(function="tests_u11.fixtures." + name,
                          args=argument(args), kwargs=argument(kwargs)))
        return getattr(f, name)(*args, **kwargs)

    budget = 2000000 + 1000 * seed
    engine = invoke("setup11", budget=budget, train_bob=True, train_eve=False,
                    tim=COMPOSITIONS[composition])
    def current(ref):
        return engine.world.head(ref.identity).ref
    kit, repair_stock = f.ref("u11-kit-alice"), f.ref("u11-repair-alice")
    repair_members = invoke("group", engine, "repair-group", members=(),
                            resources=tuple(current(r) for r in (f.SHARED, kit, repair_stock)))
    repair_step = invoke("step", f.ALICE, "repair", target=f.SHARED,
                         tool=kit, stock=repair_stock)
    repair_plan = invoke("proposed", engine, repair_members, (repair_step,), key="repair-program")
    repair_run = invoke("instantiate", engine, repair_plan, key="repair-run", mode="aggregate", accept=True)
    repair_run = invoke("finish", engine, repair_run, key="repair")
    retained_repair = invoke("work", engine, "retain-repair", "retain", focus=repair_run["ref"])[0]

    # The accepted circuit renews its supplied demand using a paid damage action.
    invoke("expose", engine, f.ALICE, current(f.SHARED))
    request = f.OperationRequest("renew-demand", f.ALICE, "damage", f.ROOM,
                                target=current(f.SHARED), evidence=f.evidence(engine, f.ALICE, current(f.SHARED)))
    event = invoke("perform", engine, request, limit=100)
    invoke("receive", engine, event, f.ALICE, "renew-demand")

    team = invoke("group", engine, "workshop-team", members=(repair_members["ref"],),
                  resources=(current(f.SHARED), f.BOB_CARE))
    team = invoke("join", engine, team, actor=f.BOB, key="join")
    program = (("call", retained_repair["ref"]),
               invoke("step", f.ALICE, "transfer", target=f.SHARED, recipient=f.BOB),
               invoke("step", f.BOB, "use", target=f.SHARED),
               invoke("step", f.BOB, "care", target=f.SHARED, stock=f.BOB_CARE))
    plan = invoke("proposed", engine, team, program, key="team-program")
    invoke("work", engine, "before-summary", "summarize", focus=team["ref"])
    run = invoke("instantiate", engine, plan, key="team-run", mode="aggregate", accept=True)
    run = invoke("finish", engine, run, key="team")
    invoke("work", engine, "retain-team", "retain", focus=run["ref"])
    invoke("work", engine, "after-summary", "summarize", focus=team["ref"])
    if run["status"] != "succeeded":
        raise ValueError("collective circuit did not succeed: " + run["status"])
    if engine.resource_model != "legacy-r4":
        raise ValueError("delivery history must use legacy-r4")
    return engine, calls, run["status"]


def episode_events(transactions):
    """One explicitly bounded harness episode, including fixture preparation.

    These are manifest event records, not inferred Population scheduler events.
    Every exact operation actor/key is assigned to the single declared episode.
    """
    joins = set()
    for tx in transactions:
        for version in tx.versions:
            d = measures.energy.data(version)
            if d.get("record_type") == "operation":
                joins.add((d["actor"], d["key"]))
    return [dict(actor=measures.actor_name(a), key=k, episode=0) for a, k in sorted(joins)]


def first_delivery(transactions, observation):
    producers = {v.ref: (i, tx.actor) for i, tx in enumerate(transactions) for v in tx.versions}
    for i in observation["received"]:
        row, loc = observation["records"][i], observation["locations"][i]
        version = next(v for v in transactions[loc["transaction"]].versions if v.ref == loc["operation"])
        d = measures.energy.data(version)
        exact = []
        for ref in audit._semantic_sources(d):
            index, producer = producers[ref]
            if producer in row["source"]:
                exact.append(dict(ref=argument(ref), producer=measures.actor_name(producer), transaction=index))
        return dict(use=i, transaction=loc["transaction"], operation=d["key"],
                    operation_ref=argument(version.ref), actor=measures.actor_name(row["actor"]),
                    tim=row["tim"], element=row["element"], seat=row["seat"], dim=row["dim"],
                    sources=argument(row["source"]), source_seats=list(row["source_seat"]),
                    relations=[measures.relation_name(observation["profiles"][s], row["tim"]) for s in row["source"]],
                    exact_inputs=exact)
    return None


def composition_status():
    return [dict(name=name, status="produced", participant_types=[tim, "sli"],
                 participants=["workshop:alice", "workshop:bob"],
                 background_profiles={"workshop:eve": "sli"},
                 relation=measures.relation_name(tim, "sli"),
                 prediction=("sterile both ways: conflict example in Batch 6 Step 2" if name == "pair-sterile"
                             else "duality comparison; no quantitative delivery prediction supplied"),
                 setup11={"tim": tim, "train_bob": True, "train_eve": False,
                          "budget": "2000000 + 1000 * seed"}) for name, tim in COMPOSITIONS.items()] + [
        dict(name="triad", status="not producible", participant_types=["iee", "sli", "lie"],
             reason="setup11 passes tim only to Alice via setup5. Bob and Eve are fixed SLI; group/join change membership, not TIM. No allowed call produces a LIE third member.",
             evidence=["tests_u11/fixtures.py::setup11", "tests_u5/fixtures.py::setup5",
                       "hle_unified/collective.py::_derive11 (compose/join)"])]


def report(histories):
    representatives = {}
    for h in histories:
        representatives.setdefault(h["manifest"]["composition"], h)
    # Collapse rows across seeds only when the full observed measures agree.
    for h in histories:
        other = representatives[h["manifest"]["composition"]]["observation"]
        for field in ("actors", "coverage", "concentration", "pairs", "episode_coverage"):
            if h["observation"][field] != other[field]:
                raise ValueError("seed-dependent result requires explicit per-seed report rows")
    first = representatives["pair"]["manifest"]["first_delivery"]
    evidence = first["exact_inputs"][0]
    text = """# Function Conditioning — delivery report

## 1. Fixture and first delivery

The accepted Step 1 fixture is `tests_u11.fixtures.circuit11(flat=False)`;
Step 1 was not rerun. Its existing setup/group/join and circuit APIs generated
matched pair compositions on seeds 17, 29, 43 and 61, legacy-r4 only.
Each history is one harness episode including preparation. The same fixture
work limits apply in both compositions. Seeds choose finite, nonbinding budgets;
these are deterministic budget replicates, not distinct stochastic workloads.

"""
    text += (f"In `pair-seed-17`, use u{first['use']} at transaction {first['transaction']} "
             f"(`{first['operation']}`) is received by {first['actor']} ({first['tim']}), "
             f"{first['element']} at seat {first['seat']}, dim {first['dim']}. "
             f"Supplier {first['sources'][0]} holds it at seat {first['source_seats'][0]}; "
             f"relation: {first['relations'][0]}. Exact input `{evidence['ref']}` was "
             f"committed by that supplier at transaction {evidence['transaction']}.\n\n")
    text += ("Sources: [manifest](HISTORIES_DELIVERY.json), each history's exact calls, "
             "parameters and first-delivery join; [pair trace](TABLES/pair_per_actor_delivery.md#use-trace).\n\n")
    text += "## 2. Actor indices\n\nThe following values hold at every seed. Conditioning retains the accepted\nA1-literal ratio: received weak uses divided by received weak uses. It is\ndegenerate when defined. Hold is kept received / received.\n\n"
    rows = []
    for composition, h in representatives.items():
        for actor, row in h["observation"]["actors"].items():
            rows.append((composition, measures.actor_name(actor), row["tim"],
                         "active" if row["active"] else "inactive", tables.ratio(row["conditioning"]), tables.ratio(row["hold"])))
    text += tables.table(("Composition", "Actor", "TIM", "Status", "Conditioning (A1 literal)", "Hold"), rows)
    text += "\nSources: Actor indices in the [pair](TABLES/pair_per_actor_delivery.md#actor-indices) and [pair-sterile](TABLES/pair-sterile_per_actor_delivery.md#actor-indices) tables.\n\n"
    text += "## 3. Coverage across compositions\n\n"
    rows = [(c, tables.ratio(h["observation"]["coverage"]["ratio"])) for c, h in representatives.items()]
    rows.append(("triad (IEE/SLI/LIE)", "N/A — not producible"))
    text += tables.table(("Composition", "Coverage at every seed and through episode 0"), rows)
    ratios = [h["observation"]["coverage"]["ratio"] for h in representatives.values()]
    comparison = "differs" if len(set(ratios)) > 1 else "is identical"
    text += (f"\nCoverage {comparison} across the supported pair compositions at matched seeds. "
             "This is the observed composition contrast; the requested pair-versus-triad "
             "presence comparison is unavailable.\n\n"
             "Pair means Alice and Bob participate in the collective. The fixture also "
             "commits inactive Eve=SLI; her weak seats remain in the denominator. These "
             "are not worlds containing only two actor profiles. `setup11(tim=)` changes "
             "Alice only; group/join cannot make Eve a LIE.\n\n"
             "Sources: Population summary and episode rows in the [pair](TABLES/pair_per_population_delivery.md) "
             "and [pair-sterile](TABLES/pair-sterile_per_population_delivery.md) tables; "
             "the manifest records the unavailable triad.\n\n")
    text += "## 4. Sterile pairs and prediction\n\n"
    rows = []
    for c, h in representatives.items():
        for pair in h["observation"]["pairs"]:
            rows.append((c, measures.actor_name(pair["sender"]), measures.actor_name(pair["receiver"]),
                         pair["relation"], len(pair["forward"]), len(pair["reverse"]), pair["sterile"]))
    text += tables.table(("Composition", "Source", "Receiver", "Relation", "Forward", "Reverse", "Sterile"), rows)
    text += ("\nEvery row holds across seeds. The directive predicts conflict is sterile both ways; "
             "no separate yield-table artifact was located. `pair-sterile` names that prediction. "
             "These counts use A3/A4 provenance. Inactive Eve's zeros do not establish "
             "intrinsic relation sterility.\n\n"
             "Sources: Ordered pairs in both composition population tables.\n\n")
    text += "## 5. DCNH all-use versus received-and-kept\n\n"
    rows = []
    for c, h in representatives.items():
        for actor, row in h["observation"]["actors"].items():
            rows.append((c, measures.actor_name(actor), row["tim"], len(row["all_ids"]), len(row["held"]),
                         "agree" if row["all_dcnh"] == row["received_kept_dcnh"] else "diverge"))
    text += tables.table(("Composition", "Actor", "TIM", "All uses", "Received and kept", "Comparison"), rows)
    text += ("\nThese comparisons hold at every seed. Inactive Eve's agreement is between empty "
             "observations. All-use rows equal native Phase 7 observations exactly.\n\n"
             "Sources: [pair DCNH](TABLES/pair_dcnh_two_ways_delivery.md) and "
             "[pair-sterile DCNH](TABLES/pair-sterile_dcnh_two_ways_delivery.md).\n\n")
    text += """## 6. Limits

A3/A4 provenance counts **any exact operation input, including collective
evidence such as an invitation**. This is broader than delivery of one route's
semantic content. Every paid block of such an operation shares its producer
tuple. A listed producer need not have produced that block's information element;
its source seat is derived from its TIM. No causal learning claim follows.

These are generated, supplied circuit workloads, not historical observations.
The existing circuit includes paid damage to renew its supplied demand; no new
demand rule was added. The paired comparison changes Alice's TIM with Bob fixed;
it does not isolate a third member's presence. A true IEE/SLI/LIE triad was not
producible with the authorized fixture calls. Background Eve remains SLI and
inactive. Four matched seeds vary only nonbinding budgets, so they do not
establish workload robustness. The fixture has operation-specific work limits,
not a Population scheduler quantum; the manifest records the exact common limits.

The accepted conditioning-index denominator is still degenerate. Undefined
ratios remain N/A. No feedback, energy regeneration, practice pricing, Model G
seats, or new demand formation was added. The read repository is unchanged;
the accepted Batch 1 outputs regenerate byte-identically. Nothing is closed.
"""
    return text


def main():
    out = PROJECT / "OUT"
    out.mkdir(exist_ok=True)
    histories, entries = [], []
    for composition in COMPOSITIONS:
        for seed in SEEDS:
            engine, calls, status = build(composition, seed)
            txs = engine.world.journal()
            events = episode_events(txs)
            native_events = [dict(e, actor=f.ObjectId(*e["actor"].split(":", 1))) for e in events]
            obs = measures.history(txs, native_events)
            name = composition + "-seed-" + str(seed)
            raw = engine.world.checkpoint().encode()
            (out / (name + ".checkpoint")).write_bytes(raw)
            entry = dict(name=name, composition=composition, model="legacy-r4", seeds={"fixture": seed},
                         parameters=dict(budget=2000000 + 1000 * seed, episodes=1, quantum=QUANTUM,
                                         flat=False, mode="aggregate", seed_effect="finite initial budget only"),
                         actors={measures.actor_name(a): t for a, t in obs["profiles"].items()},
                         participants=["workshop:alice", "workshop:bob"],
                         transactions=len(txs), checkpoint_codec="OperationStore",
                         checkpoint_sha256=hashlib.sha256(raw).hexdigest(),
                         completed_paid_uses={measures.actor_name(a): len(r["all_ids"]) for a, r in obs["actors"].items()},
                         finite_stop=dict(status=status, episodes=1), calls=calls, events=events,
                         first_delivery=first_delivery(txs, obs))
            entries.append(entry)
            histories.append(dict(manifest=entry, observation=obs, transactions=txs, events=native_events))
            print(name + ": " + str(len(txs)) + " transactions; " + str(len(obs["received"]))
                  + " received; coverage " + tables.ratio(obs["coverage"]["ratio"]), flush=True)
    # Lossless JSON sharing, not a compressed payload: the same explicit
    # actor/key/episode records otherwise repeat once for every matched seed.
    event_sets = {}
    for entry in entries:
        events = entry.pop("events")
        identifier = hashlib.sha256(json.dumps(events, sort_keys=True).encode()).hexdigest()
        event_sets.setdefault(identifier, events)
        entry["events_ref"] = identifier
    document = dict(fixture="tests_u11.fixtures.circuit11(flat=False), parameterized through existing APIs",
                    step_1="accepted under A4; not rerun", compositions=composition_status(),
                    episode_semantics="single declared harness episode 0 includes preparation; events explicitly join operation actor/key",
                    event_sets=event_sets, histories=entries)
    text = json.dumps(document, sort_keys=True, separators=(",", ":")) + "\n"
    if len(text.encode()) >= 200000:
        raise ValueError("delivery manifest exceeds R3")
    (PROJECT / "HISTORIES_DELIVERY.json").write_text(text)
    (PROJECT / "REPORT_DELIVERY.md").write_text(report(histories))
    print("triad: not producible (fixed Bob/Eve SLI profiles)", flush=True)
    print("HISTORIES_DELIVERY.json: " + str(len(entries)) + " entries; " + str(len(text.encode())) + " bytes", flush=True)
    print("REPORT_DELIVERY.md: generated from the delivery observations", flush=True)


if __name__ == "__main__":
    main()
