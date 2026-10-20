import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
unittest = __import__("unittest")
json = __import__("json")
hashlib = __import__("hashlib")
Population = __import__("hle_unified.population", fromlist=["Population"]).Population
audit = __import__("hle_unified.conditioning_audit", fromlist=["completed_use"])
data = __import__("hle_unified.energy_audit", fromlist=["data"]).data

PROJECT = pathlib.Path(__file__).resolve().parents[1]


def semantic_sources(d):
    """Inspect the full declared semantic input set, not context/evidence inputs.

    Repair attempt: the primary source alone might omit another recorded
    producer. Include every source.N and require the primary to agree.
    This cannot turn an actorless source into self-production.
    """
    numbered = sorted((int(k[7:]), ref) for k, ref in d.items()
                      if k.startswith("source.") and k[7:].isdigit())
    if [i for i, _ in numbered] != list(range(len(numbered))):
        raise ValueError("noncontiguous semantic source revisions")
    refs = tuple(ref for _, ref in numbered)
    primary = d.get("source_input")
    if refs and primary not in refs:
        raise ValueError("primary semantic revision differs from input set")
    return refs or ((primary,) if primary is not None else ())


class ProvenancePreconditionTests(unittest.TestCase):
    """Batch 2 must not invent a producer for supplied actorless seed revisions.

    These are prerequisite witnesses, not an implementation of uses() or I1-I5.
    A failed precondition prevents starting that implementation.
    """

    @classmethod
    def setUpClass(cls):
        cls.histories = []
        for row in json.loads((PROJECT / "HISTORIES.json").read_text()):
            raw = (PROJECT / "OUT" / (row["name"] + ".checkpoint")).read_bytes()
            if hashlib.sha256(raw).hexdigest() != row["checkpoint_sha256"]:
                raise AssertionError("checkpoint differs from accepted Batch 1")
            population = Population.restore(raw.decode())
            if population.checkpoint().encode() != raw:
                raise AssertionError("checkpoint restore changed bytes")
            txs = population.engine.world.journal()
            profiles, counts = audit.completed_use(txs)
            producers = {v.ref: tx for tx in txs for v in tx.versions}
            cls.histories.append((row["name"], txs, profiles, producers))

    def test_01_exact_revision_join_preserves_recorded_producer(self):
        # Positive witness: generated paid operation revisions have real actors.
        for name, txs, profiles, producers in self.histories:
            witnesses = [(v, tx) for tx in txs for v in tx.versions
                         if data(v).get("record_type") == "operation"
                         and data(v).get("completed", 0) > 0]
            self.assertTrue(witnesses, name)
            for v, tx in witnesses:
                self.assertIs(producers[v.ref], tx)
                self.assertIn(tx.actor, profiles)
                self.assertEqual(tx.actor, data(v)["actor"])

    def test_02_consumed_semantic_revisions_have_recorded_producers(self):
        # The required source domain is "self" or a committed producing actor.
        # A nullable Transaction.actor cannot be converted to either honestly.
        for name, txs, profiles, producers in self.histories:
            with self.subTest(history=name):
                checked = 0
                for tx in txs:
                    for v in tx.versions:
                        d = data(v)
                        if (d.get("record_type") != "operation"
                                or "route_count" not in d or v.ref.revision != 1):
                            continue
                        refs = semantic_sources(d)
                        self.assertTrue(refs, "missing semantic source revision")
                        for ref in refs:
                            self.assertIn(ref, producers, "missing exact input revision")
                            producer = producers[ref]
                            self.assertIn(
                                producer.actor, profiles,
                                "unresolved_input_producer: " + name + "; "
                                + str(ref) + "; producing transaction=" + producer.key
                                + "; recorded actor=" + repr(producer.actor))
                            checked += 1
                self.assertGreater(checked, 0, "no semantic source witness")


if __name__ == "__main__":
    unittest.main()
