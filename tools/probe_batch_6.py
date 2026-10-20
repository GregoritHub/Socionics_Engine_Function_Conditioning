import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
audit = __import__("conditioning_v2.audit", fromlist=["uses"])
conditioning = __import__("hle_unified.conditioning_audit", fromlist=["completed_use"])
energy = __import__("hle_unified.energy_audit", fromlist=["data"])
u11 = __import__("tests_u11.fixtures", fromlist=["circuit11"])
continuation = __import__("tests_workflow_continuation.fixtures", fromlist=["chain"])
traceback = __import__("traceback")
PROJECT = pathlib.Path(__file__).resolve().parents[1]


def actor_name(actor):
    return actor.namespace + ":" + actor.key


def first_delivery(transactions, records):
    """Locate the first tuple-source use without changing the journal."""
    producers = {v.ref: (i, tx) for i, tx in enumerate(transactions) for v in tx.versions}
    heads, occurrence = {}, 0
    for index, tx in enumerate(transactions):
        for version in tx.versions:
            d = energy.data(version)
            if d.get("record_type") == "operation" and "route_count" in d:
                previous = heads.get(version.ref.identity, {})
                for _, end, _, element in energy.blocks(d):
                    if element is None or not previous.get("completed", 0) < end <= d["completed"]:
                        continue
                    row = records[occurrence]
                    if type(row["source"]) is tuple:
                        exact = []
                        for ref in audit._semantic_sources(d):
                            producer_index, producer = producers[ref]
                            if producer.actor in row["source"]:
                                exact.append(dict(input=actor_name(ref.identity), revision=ref.revision,
                                                  producer_transaction=producer_index,
                                                  producer=actor_name(producer.actor)))
                        return dict(use=occurrence, transaction=index, operation=d["key"],
                                    operation_ref=actor_name(version.ref.identity),
                                    operation_revision=version.ref.revision,
                                    actor=actor_name(row["actor"]), tim=row["tim"],
                                    element=row["element"], seat=row["seat"], dim=row["dim"],
                                    sources=tuple(actor_name(s) for s in row["source"]),
                                    source_seat=row["source_seat"], relation=row["relation"],
                                    exact_inputs=exact)
                    occurrence += 1
            heads[version.ref.identity] = d
    return None


def inspect(name, engine):
    transactions = engine.world.journal()
    profiles, counts = conditioning.completed_use(transactions)
    print("Fixture:", name, flush=True)
    print("Transactions:", len(transactions), flush=True)
    print("Profiles:", {actor_name(a): t for a, t in profiles.items()}, flush=True)
    print("Completed paid uses:", {actor_name(a): sum(c.values()) for a, c in counts.items()}, flush=True)
    try:
        records = audit.uses(transactions)
    except ValueError as error:
        print("conditioning_v2.audit.uses:", type(error).__name__ + ":", error, flush=True)
        frames = [f for f in traceback.extract_tb(error.__traceback__)
                  if pathlib.Path(f.filename).is_relative_to(PROJECT)]
        if frames:
            frame = frames[-1]
            print('  File "<write>/' + str(pathlib.Path(frame.filename).relative_to(PROJECT))
                  + '", line ' + str(frame.lineno) + ', in ' + frame.name, flush=True)
            print("    " + frame.line, flush=True)
        print(type(error).__name__ + ": " + str(error), flush=True)
        return False
    sources = {"self": 0, "world": 0, "tuple": 0}
    for row in records:
        source = row["source"]
        sources["tuple" if type(source) is tuple else source] += 1
    print("conditioning_v2.audit.uses: accepted", flush=True)
    print("Source counts:", sources, flush=True)
    received = [row for row in records if type(row["source"]) is tuple]
    if received:
        print("First tuple-source delivery:", first_delivery(transactions, records), flush=True)
    else:
        print("Delivery transaction / actor pair: none observed under A3", flush=True)
    return bool(received)


print("Step 1 under A3: run each authorized fixture exactly once, with its defaults.", flush=True)
engine, result = u11.circuit11()
u11_delivers = inspect("tests_u11.fixtures.circuit11(flat=False)", engine)
population = continuation.chain()
print("chain.run(1000):", population.run(1000), flush=True)
chain_delivers = inspect("tests_workflow_continuation.fixtures.chain(budget=200000)", population.engine)
print("Qualifying delivery witness:", dict(circuit11=u11_delivers, chain=chain_delivers), flush=True)
if not (u11_delivers or chain_delivers):
    print("STEP 1 STOP: neither fixture supplies an accepted tuple-source delivery witness.", flush=True)
    sys.exit(1)
