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


def first_delivery(transactions, observation, reading="wide"):
    producers = {v.ref: (i, tx.actor) for i, tx in enumerate(transactions) for v in tx.versions}
    for i in observation["received"]:
        row, loc = observation["records"][i], observation["locations"][i]
        version = next(v for v in transactions[loc["transaction"]].versions if v.ref == loc["operation"])
        d = measures.energy.data(version)
        exact = []
        for ref in audit._semantic_sources(d, reading):
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
    """Batch 7 report renderer; history generation and manifests are unchanged."""
    reports = __import__("conditioning_v2.reports", fromlist=["delivery"])
    return reports.delivery(histories)


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
                  + " received wide; coverage wide " + tables.ratio(obs["coverage"]["ratio"]), flush=True)
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
