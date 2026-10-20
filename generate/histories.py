import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
json = __import__("json")
hashlib = __import__("hashlib")
random = __import__("random")
f = __import__("tests_c7_workflow.fixtures", fromlist=["setup_workflow"])
sustained = __import__("tests_workflow_population.sustained_fixtures", fromlist=["owned_request"])
energy = __import__("tests_energy.fixtures", fromlist=["factory"])
cognition = __import__("hle_unified.cognition", fromlist=["profile"])
Population = __import__("hle_unified.population", fromlist=["Population"]).Population
audit = __import__("hle_unified.conditioning_audit", fromlist=["completed_use"])

PROJECT = pathlib.Path(__file__).resolve().parents[1]
SEEDS = (17, 29, 43, 61)
MODELS = ("legacy-r4", "grade-v1")
ACTORS = ((f.ALICE, "iee"), (f.BOB, "sli"), (f.EVE, "lie"))


def actor_name(actor):
    return actor.namespace + ":" + actor.key


def build(model, seed):
    """Prepared demands only; seed chooses task counts and request order."""
    if model not in MODELS or seed not in SEEDS:
        raise ValueError("undeclared model or seed")

    def factory(world, law):
        # Initial fixture profiles, before any paid work. No running-world edits.
        fresh = f.OperationStore()
        profiles = {cognition.profile(a, t).ref: cognition.profile(a, t)
                    for a, t in ACTORS}
        for tx in world.journal():
            versions = tuple(profiles.get(v.ref, v) for v in tx.versions)
            fresh.commit(tx.key, tx.writer, versions, tx.lineage, actor=tx.actor)
        return energy.factory(model)(fresh, law)

    engine = f.setup_workflow(engine_type=factory, budget=200000)
    rng = random.Random(seed)
    requests = []
    for i, (actor, _) in enumerate(ACTORS):
        for obj in (f.ROOM, f.CUE5, f.DEVICE, f.LOAN, f.DUE, f.CARE,
                    *(f.ObjectRef(a, 1) for a, _ in ACTORS)):
            f.expose(engine, actor, obj)
        requests.append(sustained.owned_request(
            engine, actor, "history-" + str(seed) + "-" + actor.key,
            count=rng.choice((2, 4, 8)), externalize=i == 1))
    rng.shuffle(requests)
    population = Population(engine, requests, episodes=3, quantum=128, repeat_limit=2)
    result = population.run(10000)
    if not result["done"]:
        raise RuntimeError("finite population did not stop within guard")
    return population


def summarize(population, model, seed, checkpoint):
    profiles, counts = audit.completed_use(population.engine.world.journal())
    active = {r.actor for r in population.requests}
    if active != set(profiles) or any(sum(counts[a].values()) < 1 for a in active):
        raise ValueError("every active actor must have a completed paid use")
    return dict(name=model + "-seed-" + str(seed), model=model,
                seeds={"fixture": seed},
                actors={actor_name(a): profiles[a] for a in sorted(profiles)},
                transactions=len(population.engine.world.journal()),
                checkpoint_sha256=hashlib.sha256(checkpoint.encode()).hexdigest(),
                completed_paid_uses={actor_name(a): sum(counts[a].values()) for a in sorted(active)},
                finite_stop=dict(done=population.done, turns=population.turn,
                    episodes=population.episodes,
                    counts={actor_name(r.actor): c for r, c in zip(population.requests, population.counts)},
                    reasons={actor_name(r.actor): s or "episode_limit" for r, s in zip(population.requests, population.stopped)}))


def main():
    out = PROJECT / "OUT"
    out.mkdir(exist_ok=True)
    manifest = []
    for model in MODELS:
        for seed in SEEDS:
            population = build(model, seed)
            checkpoint = population.checkpoint()
            row = summarize(population, model, seed, checkpoint)
            (out / (row["name"] + ".checkpoint")).write_text(checkpoint, encoding="utf-8")
            manifest.append(row)
            print(row["name"] + ": finite stop; " + str(row["transactions"]) + " transactions", flush=True)
    (PROJECT / "HISTORIES.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print("HISTORIES.json: " + str(len(manifest)) + " entries", flush=True)


if __name__ == "__main__":
    main()
