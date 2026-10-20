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
    """Return one exact semantic source revision per declared route."""
    indexed = sorted((int(k[7:]), ref) for k, ref in d.items()
                     if k.startswith("source.") and k[7:].isdigit())
    if [i for i, _ in indexed] != list(range(len(indexed))):
        raise ValueError("noncontiguous semantic source revisions")
    refs = tuple(ref for _, ref in indexed)
    if len(refs) != d["route_count"]:
        raise ValueError("semantic source count differs from route count")
    if refs and d.get("source_input") != refs[0]:
        raise ValueError("primary semantic source differs from route source")
    return refs


def _block_routes(d):
    """Attach route indexes to the engine audit's canonical block sequence."""
    indexes = [None]
    for route in range(d["route_count"]):
        prefix = "route." + str(route) + ".path."
        paths = sorted(int(k[len(prefix):]) for k in d if k.startswith(prefix))
        if paths != list(range(len(paths))) or not paths:
            raise ValueError("noncontiguous raw path")
        indexes.extend([route] * len(paths))  # arrivals plus one content block
    indexes.append(None)
    result = energy.blocks(d)
    if len(indexes) != len(result):
        raise ValueError("route/block attribution mismatch")
    return tuple(zip(result, indexes))


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
    if source not in profiles or source == actor:
        raise ValueError("invalid actor-id source")
    source_tim = profiles[source]
    source_seat = model_a.position_of(source_tim, record["element"])
    if record["source_seat"] != source_seat:
        raise ValueError("source element-seat mismatch")
    expected_relation = relations.relation(source_tim, record["tim"])
    if record["relation"] != expected_relation:
        raise ValueError("source relation mismatch")
    if relations.landing_position(source_tim, source_seat, record["tim"]) != expected_seat:
        raise ValueError("source landing-position mismatch")


def uses(transactions):
    """Derive one observation per completed routed hop or content block."""
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
                if previous and _semantic_sources(previous) != source_refs:
                    raise ValueError("changed semantic source revisions")
                for (start, end, _, element), route in _block_routes(d):
                    if route is None or element is None or not before < end <= after:
                        continue
                    source_ref = source_refs[route]
                    producer = producers.get(source_ref)
                    if producer is None:
                        raise ValueError("missing exact provenance revision")
                    if producer.actor is None:
                        source = "world"
                    elif producer.actor == d["actor"]:
                        source = "self"
                    elif producer.actor in profiles:
                        source = producer.actor
                    else:
                        raise ValueError("unknown provenance actor")

                    seat = model_a.position_of(d["tim"], element)
                    if source in ("self", "world"):
                        source_seat = relation = None
                    else:
                        source_tim = profiles[source]
                        source_seat = model_a.position_of(source_tim, element)
                        relation = relations.relation(source_tim, d["tim"])
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
