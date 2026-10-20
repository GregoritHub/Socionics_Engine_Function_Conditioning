import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
conditioning = __import__("hle_unified.conditioning_audit", fromlist=["completed_use"])
energy = __import__("hle_unified.energy_audit", fromlist=["blocks", "data"])
model_a = __import__("hle.model_a", fromlist=["fields", "position_of"])
relations = __import__("hle.relations", fromlist=["relation", "landing_position"])


def _semantic_sources(d):
    """A3: every exact consumed revision on the operation, deduplicated.

    Keep the helper name for existing callers. Sources no longer correspond
    one-to-one with routes. Broad input.N evidence counts under this ruling.
    """
    refs = [ref for _, ref in sorted(
        (int(k[7:]), ref) for k, ref in d.items()
        if k.startswith("source.") and k[7:].isdigit())]
    if "source_input" in d:
        refs.append(d["source_input"])
    refs.extend(ref for _, ref in sorted(
        (int(k[6:]), ref) for k, ref in d.items()
        if k.startswith("input.") and k[6:].isdigit()))
    return tuple(dict.fromkeys(refs))


def _operation_source(refs, consumer, producers, profiles):
    """Resolve only exact revisions; other actors take priority over self."""
    others, has_self = set(), False
    for ref in refs:
        producer = producers.get(ref)
        if producer is None:
            raise ValueError("missing exact provenance revision")
        actor = producer.actor
        if actor is None:
            continue
        if actor not in profiles:
            raise ValueError("unknown provenance actor")
        if actor == consumer:
            has_self = True
        else:
            others.add(actor)
    return tuple(sorted(others)) if others else "self" if has_self else "world"


def _validate_record(record, profiles):
    """Validate all derived claims before returning an observation."""
    actor = record["actor"]
    if actor not in profiles or record["tim"] != profiles[actor]:
        raise ValueError("record actor/TIM mismatch")
    expected_seat = model_a.position_of(record["tim"], record["element"])
    if record["seat"] != expected_seat:
        raise ValueError("element-seat mismatch")
    expected_dim = model_a.fields(expected_seat)["dimensionality"]
    if record["dim"] != expected_dim:
        raise ValueError("seat-dimension mismatch")

    source = record["source"]
    if source in ("self", "world"):
        if record["source_seat"] is not None or record["relation"] is not None:
            raise ValueError("non-actor source has relation fields")
        return
    if (type(source) is not tuple or not source
            or any(s not in profiles or s == actor for s in source)
            or source != tuple(sorted(set(source)))):
        raise ValueError("invalid actor-id source")
    source_seats = tuple(model_a.position_of(profiles[s], record["element"])
                         for s in source)
    if record["source_seat"] != source_seats:
        raise ValueError("source element-seat mismatch")
    expected_relations = tuple(relations.relation(profiles[s], record["tim"])
                               for s in source)
    if record["relation"] != expected_relations:
        raise ValueError("source relation mismatch")
    for sender, source_seat in zip(source, source_seats):
        if relations.landing_position(profiles[sender], source_seat,
                                      record["tim"]) != expected_seat:
            raise ValueError("source landing-position mismatch")


def uses(transactions):
    """Derive paid uses with A3 operation-level, exact-revision provenance.

    source_seat and relation tuples align with the sorted source actor tuple.
    Completed-use counting remains the native audit's canonical block count.
    """
    transactions = tuple(transactions)
    profiles, expected = conditioning.completed_use(transactions)

    producers = {}
    for tx in transactions:
        for version in tx.versions:
            if version.ref in producers:
                raise ValueError("duplicate exact provenance revision")
            producers[version.ref] = tx

    heads, records = {}, []
    for tx in transactions:
        jobs = [v for v in tx.versions
                if energy.data(v).get("record_type") == "operation"]
        if jobs:
            version = jobs[0]
            d = energy.data(version)
            old = heads.get(version.ref.identity)
            previous = {} if old is None else energy.data(old)
            before, after = previous.get("completed", 0), d["completed"]
            if "route_count" in d:
                source_refs = _semantic_sources(d)
                if previous and set(_semantic_sources(previous)) != set(source_refs):
                    raise ValueError("changed semantic source revisions")
                source = None
                for start, end, _, element in energy.blocks(d):
                    if element is None or not before < end <= after:
                        continue
                    if source is None:
                        source = _operation_source(source_refs, d["actor"],
                                                   producers, profiles)

                    seat = model_a.position_of(d["tim"], element)
                    if source in ("self", "world"):
                        source_seat = relation = None
                    else:
                        source_seat = tuple(model_a.position_of(profiles[s], element)
                                            for s in source)
                        relation = tuple(relations.relation(profiles[s], d["tim"])
                                         for s in source)
                    record = dict(actor=d["actor"], tim=d["tim"], element=element,
                                  seat=seat,
                                  dim=model_a.fields(seat)["dimensionality"],
                                  source=source, source_seat=source_seat,
                                  relation=relation)
                    _validate_record(record, profiles)
                    records.append(record)
        for version in tx.versions:
            heads[version.ref.identity] = version

    observed = {actor: dict.fromkeys(conditioning.ELEMENTS, 0)
                for actor in profiles}
    for record in records:
        observed[record["actor"]][record["element"]] += 1
    if observed != expected:
        raise ValueError("completed-use attribution mismatch")
    return records
