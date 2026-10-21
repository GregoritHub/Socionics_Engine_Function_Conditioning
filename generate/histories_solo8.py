import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
json = __import__("json")
hashlib = __import__("hashlib")
replace = __import__("dataclasses").replace
u = __import__("tests_u11.fixtures", fromlist=["setup11"])
c = __import__("tests_c7_workflow.fixtures", fromlist=["setup_workflow"])
WorkflowEngine = __import__("hle_unified.workflow_execution", fromlist=["WorkflowEngine"]).WorkflowEngine
delivery = __import__("generate.histories_delivery", fromlist=["argument"])
tables = __import__("conditioning_v2.tables", fromlist=["load_histories"])
classes = __import__("conditioning_v2.classes", fromlist=["history"])
measures = tables.measures
PROJECT = pathlib.Path(__file__).resolve().parents[1]
SEEDS = delivery.SEEDS
COMPOSITION = "pair-solo8"
PRIMITIVES = ("repair", "transfer", "use", "care", "consume")

# Batch 9 §9.1.3 as amended by A9: the probe-uptake row is the Express
# expenditure default; the fixture's CARE stock holds two units, so exactly one
# further care-consuming row (row 2, the element-override witness) runs, and the
# Organize rows are withdrawn. Every element keeps both faces.
PROGRAM = (
    (2, "Express", "expenditure", ("ne", "ti")),
    (3, "Express", "accumulation", ()),
    (4, "Express", "accumulation", ("ne", "ti")),
    (5, "Embody", "expenditure", ()),
    (6, "Embody", "expenditure", ("ti", "ne")),
    (7, "Share", "expenditure", ()),
    (8, "Share", "expenditure", ("fe",)),
    (9, "Share", "accumulation", ()),
    (10, "Share", "accumulation", ("fe",)),
    (11, "Coordinate", "expenditure", ()),
    (12, "Coordinate", "expenditure", ("se",)),
    (13, "Coordinate", "accumulation", ()),
    (14, "Coordinate", "accumulation", ("se",)),
    (15, "Theorize", "expenditure", ()),
    (16, "Theorize", "expenditure", ("ne",)),
    (19, "Apply", "accumulation", ()),
    (20, "Apply", "accumulation", ("ti",)),
)
PREDICTION = ("internalisation > 0 for workshop:alice at seats 5 and 6 under the wide reading; "
              "every seat 1-8 has >= 1 content use for workshop:alice; "
              "workshop:bob's only uses after after-summary are exchange replies (A9)")


def argument(value):
    """delivery.argument, with frozen requests reduced to key, type and repr hash (R3)."""
    if hasattr(value, "key") and hasattr(value, "actor") and hasattr(value, "__dataclass_fields__"):
        return dict(request=type(value).__name__, key=value.key, actor=delivery.argument(value.actor),
                    repr_sha256=hashlib.sha256(repr(value).encode()).hexdigest())
    if isinstance(value, dict):
        return {str(k): argument(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [argument(v) for v in value]
    return delivery.argument(value)


def workshop_factory(world, law):
    """The setup11 record seeding on a WorkflowEngine (P-E), via the same helpers."""
    definitions = tuple(u.ObjectVersion(u.ref("u11-primitive-" + n), u.WRITER, "Primitive " + n, (u.Role.PROCEDURE,),
                                        (u.Procedure(u.SIGNATURES[n], (), (), (), "u4." + n + ".v1"),)) for n in PRIMITIVES)
    materials = [u.tool(u.SHARED, damaged=True, maximum=5), u.stock(u.BOB_CARE, "care", 8, u.BOB)]
    for actor in (u.ALICE, u.BOB, u.EVE):
        for name in PRIMITIVES:
            materials.append(u.tool(u.ref("u11-practice-" + actor.key + "-" + name), owner=actor,
                                    damaged=name == "repair", wear=int(name == "care"), maximum=20))
        materials.extend((u.tool(u.ref("u11-kit-" + actor.key), owner=actor, maximum=60),
                          u.stock(u.ref("u11-repair-" + actor.key), "repair", 20, actor),
                          u.stock(u.ref("u11-care-" + actor.key), "care", 20, actor),
                          u.stock(u.ref("u11-consume-" + actor.key), "consume", 20, actor)))
    world.create("u11-supplied-workshop", u.WRITER, (*definitions, *materials))
    return WorkflowEngine(world, law)


def build(seed):
    """One world: workshop + workflow equipment on WorkflowEngine; probe; pair; solo program.

    Seeds choose only the nonbinding budget, as in the pair composition.
    """
    if seed not in SEEDS:
        raise ValueError("undeclared seed")
    calls, refusals = [], []

    def invoke(module, name, *args, **kwargs):
        calls.append(dict(function=module.__name__ + "." + name, args=argument(args), kwargs=argument(kwargs)))
        return getattr(module, name)(*args, **kwargs)

    budget = 2000000 + 1000 * seed
    engine = invoke(c, "setup_workflow", "iee", engine_type=workshop_factory, budget=budget)
    calls[-1]["kwargs"]["engine_type"] = "generate.histories_solo8.workshop_factory"
    for actor in (u.ALICE, u.BOB, u.EVE):
        for obj in (u.ROOM, u.CUE5, u.ObjectRef(u.ALICE, 1), u.ObjectRef(u.BOB, 1), u.ObjectRef(u.EVE, 1)):
            invoke(u, "expose", engine, actor, obj)
        if actor is not u.EVE:
            invoke(u, "train", engine, actor, PRIMITIVES)
    e = engine

    def prepare(key):
        for obj in (c.DEVICE, c.CARE):
            invoke(c, "expose", e, u.ALICE, e.world.head(obj.identity).ref)
        if c.attrs(e.world.head(c.DEVICE.identity)).get("wear") == 0:
            invoke(c, "observe", e, key + "-wear", primitive="use")

    def row(number, name, face, elements):
        key = f"solo-{number:02d}-{name.lower()}-{face}-{''.join(elements) or 'default'}" if number else "probe-uptake"
        prepare(key)
        base = invoke(c, "cell", e, name, face, key=key, prepare_only=True)
        request = base["request"]
        if elements:
            request = replace(request, elements=elements)
            calls.append(dict(function="dataclasses.replace", args=[argument(base["request"])], kwargs=dict(elements=list(elements))))
        invoke(c, "work", e, request, allow_failure=True)
        status = e.job_status(u.ALICE, key)
        if status["status"] != "succeeded":
            refusals.append(dict(row=number, key=key, status=status["status"], failure=status.get("failure")))
        return status

    # 9.1.1 uptake prerequisite (P-F)
    probe = row(0, "Express", "expenditure", ())
    if probe["status"] != "succeeded":
        raise ValueError("uptake prerequisite refused: " + str(probe.get("failure")))
    phase_marks = dict(probe_end=len(e.world.journal()))

    # 9.1.2 collective phase: the committed pair sequence
    def current(ref):
        return e.world.head(ref.identity).ref
    kit, repair_stock = u.ref("u11-kit-alice"), u.ref("u11-repair-alice")
    repair_members = invoke(u, "group", e, "repair-group", members=(),
                            resources=tuple(current(r) for r in (u.SHARED, kit, repair_stock)))
    repair_step = invoke(u, "step", u.ALICE, "repair", target=u.SHARED, tool=kit, stock=repair_stock)
    repair_plan = invoke(u, "proposed", e, repair_members, (repair_step,), key="repair-program")
    repair_run = invoke(u, "instantiate", e, repair_plan, key="repair-run", mode="aggregate", accept=True)
    repair_run = invoke(u, "finish", e, repair_run, key="repair")
    retained_repair = invoke(u, "work", e, "retain-repair", "retain", focus=repair_run["ref"])[0]
    invoke(u, "expose", e, u.ALICE, current(u.SHARED))
    request = u.OperationRequest("renew-demand", u.ALICE, "damage", u.ROOM, target=current(u.SHARED),
                                 evidence=u.evidence(e, u.ALICE, current(u.SHARED)))
    event = invoke(u, "perform", e, request, limit=100)
    invoke(u, "receive", e, event, u.ALICE, "renew-demand")
    team = invoke(u, "group", e, "workshop-team", members=(repair_members["ref"],), resources=(current(u.SHARED), u.BOB_CARE))
    team = invoke(u, "join", e, team, actor=u.BOB, key="join")
    program = (("call", retained_repair["ref"]),
               invoke(u, "step", u.ALICE, "transfer", target=u.SHARED, recipient=u.BOB),
               invoke(u, "step", u.BOB, "use", target=u.SHARED),
               invoke(u, "step", u.BOB, "care", target=u.SHARED, stock=u.BOB_CARE))
    plan = invoke(u, "proposed", e, team, program, key="team-program")
    invoke(u, "work", e, "before-summary", "summarize", focus=team["ref"])
    run = invoke(u, "instantiate", e, plan, key="team-run", mode="aggregate", accept=True)
    run = invoke(u, "finish", e, run, key="team")
    invoke(u, "work", e, "retain-team", "retain", focus=run["ref"])
    invoke(u, "work", e, "after-summary", "summarize", focus=team["ref"])
    if run["status"] != "succeeded":
        raise ValueError("collective circuit did not succeed: " + run["status"])
    phase_marks["collective_end"] = len(e.world.journal())

    # 9.1.3 solo phase
    for number, name, face, elements in PROGRAM:
        row(number, name, face, elements)
    if len(refusals) > 4:
        raise ValueError("more than four program rows refused: " + json.dumps(refusals))
    phase_marks["solo_end"] = len(e.world.journal())
    if e.resource_model != "legacy-r4":
        raise ValueError("solo8 history must use legacy-r4")
    return e, calls, refusals, phase_marks


def main():
    out = PROJECT / "OUT"
    out.mkdir(exist_ok=True)
    histories, event_sets, call_sets = [], {}, {}
    for seed in SEEDS:
        engine, calls, refusals, marks = build(seed)
        name = COMPOSITION + "-seed-" + str(seed)
        text = engine.world.checkpoint()
        raw = text.encode()
        (out / (name + ".checkpoint")).write_bytes(raw)
        transactions = engine.world.journal()
        events = delivery.episode_events(transactions)
        events_ref = hashlib.sha256(json.dumps(events, sort_keys=True).encode()).hexdigest()
        event_sets[events_ref] = events
        calls_text = json.dumps(calls, indent=1, sort_keys=True) + "\n"
        calls_ref = hashlib.sha256(calls_text.encode()).hexdigest()
        calls_dir = PROJECT / "CALLS_SOLO8"
        calls_dir.mkdir(exist_ok=True)
        if len(calls_text.encode()) >= 200000:
            raise ValueError("call log exceeds R3")
        (calls_dir / (name + ".json")).write_text(calls_text, encoding="utf-8")
        call_sets[name] = calls_ref
        observation = measures.history(transactions, tuple(dict(actor=tables.ObjectId(*ev["actor"].split(":", 1)),
                                                                key=ev["key"], episode=ev["episode"]) for ev in events))
        actors = {measures.actor_name(a): t for a, t in observation["profiles"].items()}
        histories.append(dict(name=name, composition=COMPOSITION, model="legacy-r4", engine="hle_unified.workflow_execution.WorkflowEngine",
                              seeds=dict(fixture=seed, budget=2000000 + 1000 * seed), actors=actors,
                              transactions=len(transactions), checkpoint_sha256=hashlib.sha256(raw).hexdigest(),
                              checkpoint_codec="OperationStore", events_ref=events_ref, phase_marks=marks,
                              refused_rows=refusals, calls_ref=calls_ref))
        print(f"{name}: {len(transactions)} transactions; {len(observation['received'])} received wide; "
              f"refused rows {[r['row'] for r in refusals]}", flush=True)
    manifest = dict(composition=COMPOSITION, prediction=PREDICTION, program=[dict(row=n, recipe=r, face=f, elements=list(el)) for n, r, f, el in PROGRAM],
                    amendments=["A9"], histories=histories, event_sets=event_sets,
                    call_logs=dict(folder="CALLS_SOLO8", sha256=call_sets))
    text = json.dumps(manifest, indent=1, sort_keys=True) + "\n"
    if len(text.encode()) >= 200000:
        raise ValueError("manifest exceeds R3")
    (PROJECT / "HISTORIES_SOLO8.json").write_text(text, encoding="utf-8")
    print("HISTORIES_SOLO8.json: " + str(len(histories)) + " entries; " + str(len(text.encode())) + " bytes", flush=True)


if __name__ == "__main__":
    main()
