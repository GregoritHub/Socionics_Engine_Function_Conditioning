import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
unittest = __import__("unittest")
json = __import__("json")
hashlib = __import__("hashlib")
replace = __import__("dataclasses").replace
Population = __import__("hle_unified.population", fromlist=["Population"]).Population
conditioning = __import__("hle_unified.conditioning_audit", fromlist=["completed_use"])
energy = __import__("hle_unified.energy_audit", fromlist=["data", "TIME"])
material = __import__("hle_unified.material", fromlist=["attributes"])
model_a = __import__("hle.model_a", fromlist=["fields", "position_of"])
relations = __import__("hle.relations", fromlist=["relation", "landing_position"])
v2 = __import__("conditioning_v2.audit", fromlist=["uses"])

PROJECT = pathlib.Path(__file__).resolve().parents[1]
ELEMENTS = conditioning.ELEMENTS


class FieldTests(unittest.TestCase):
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
            cls.histories.append((row["name"], population.engine.world.journal()))

    @staticmethod
    def _first_source(txs):
        producers = {v.ref: (i, tx) for i, tx in enumerate(txs) for v in tx.versions}
        for tx in txs:
            for version in tx.versions:
                d = energy.data(version)
                if (d.get("record_type") == "operation" and "route_count" in d
                        and d.get("completed", 0) > 0):
                    ref = v2._semantic_sources(d)[0]
                    index, producer = producers[ref]
                    return index, producer, d["actor"]
        raise AssertionError("no completed routed source witness")

    @staticmethod
    def _with_producer_actor(txs, actor):
        index, producer, consumer = FieldTests._first_source(txs)
        altered = list(txs)
        altered[index] = replace(producer, actor=actor)
        return altered, consumer

    def test_01_i1_i2_i3_i5_on_every_history(self):
        for name, txs in self.histories:
            with self.subTest(history=name):
                profiles, expected = conditioning.completed_use(txs)
                rows = v2.uses(txs)
                observed = {actor: dict.fromkeys(ELEMENTS, 0) for actor in profiles}
                actor_sources = 0
                for row in rows:
                    self.assertEqual(row["seat"],
                                     model_a.position_of(row["tim"], row["element"]))
                    self.assertEqual(row["dim"],
                                     model_a.fields(row["seat"])["dimensionality"])
                    self.assertTrue(row["source"] in ("self", "world")
                                    or isinstance(row["source"], tuple))
                    if isinstance(row["source"], tuple):
                        actor_sources += 1
                        self.assertTrue(row["source"])
                        self.assertEqual(row["source"], tuple(sorted(set(row["source"]))))
                        self.assertEqual(len(row["source"]), len(row["source_seat"]))
                        self.assertEqual(len(row["source"]), len(row["relation"]))
                        for sender, seat, relation in zip(row["source"], row["source_seat"], row["relation"]):
                            source_tim = profiles[sender]
                            self.assertNotEqual(sender, row["actor"])
                            self.assertEqual(seat, model_a.position_of(source_tim, row["element"]))
                            self.assertEqual(relation, relations.relation(source_tim, row["tim"]))
                            self.assertEqual(relations.landing_position(source_tim, seat, row["tim"]), row["seat"])
                    else:
                        self.assertIsNone(row["source_seat"])
                        self.assertIsNone(row["relation"])
                    observed[row["actor"]][row["element"]] += 1
                self.assertEqual(observed, expected)
                self.assertEqual(actor_sources, 0)
                self.assertTrue(rows)
                self.assertTrue(all(row["source"] == "world" for row in rows))

    def test_02_self_actor_and_world_source_adapters(self):
        _, txs = self.histories[0]
        profiles, _ = conditioning.completed_use(txs)

        world_rows = v2.uses(txs)
        self.assertTrue(any(row["source"] == "world" for row in world_rows))

        _, _, consumer = self._first_source(txs)
        self_rows = v2.uses(self._with_producer_actor(txs, consumer)[0])
        self.assertTrue(any(row["source"] == "self" for row in self_rows))

        other = next(actor for actor in profiles if actor != consumer)
        other_rows = v2.uses(self._with_producer_actor(txs, other)[0])
        received = [row for row in other_rows if row["source"] == (other,)]
        self.assertTrue(received)
        self.assertTrue(all(row["source_seat"] is not None
                            and row["relation"] is not None for row in received))

    def test_03_unknown_provenance_actor_is_rejected(self):
        _, txs = self.histories[0]
        profiles, _ = conditioning.completed_use(txs)
        exemplar = next(iter(profiles))
        forged = type(exemplar)("forged", "actor")
        altered, _ = self._with_producer_actor(txs, forged)
        with self.assertRaisesRegex(ValueError, "unknown provenance actor"):
            v2.uses(altered)

    def test_04_element_seat_contract_forgery_is_rejected(self):
        _, txs = self.histories[0]
        identity = field = replacement = None
        for tx in txs:
            for version in tx.versions:
                d = energy.data(version)
                keys = sorted(k for k in d if k.startswith("route.0.path.")
                              and k != "route.0.path.0")
                if d.get("record_type") == "operation" and keys:
                    field = keys[0]
                    charge = d["route.0.charges." + str(int(field.rsplit(".", 1)[1]) - 1)]
                    replacement = next(
                        element for element in ELEMENTS
                        if energy.TIME[model_a.position_of(d["tim"], element) - 1] != charge)
                    identity = version.ref.identity
                    break
            if identity is not None:
                break
        self.assertIsNotNone(identity, "no routed seat-contract witness")

        altered = []
        for tx in txs:
            versions = []
            for version in tx.versions:
                if version.ref.identity == identity:
                    d = energy.data(version)
                    d[field] = replacement
                    version = replace(version, attributes=material.attributes(d))
                versions.append(version)
            altered.append(replace(tx, versions=tuple(versions)))
        with self.assertRaisesRegex(ValueError, "raw hop time differs from CT table"):
            v2.uses(altered)


if __name__ == "__main__":
    unittest.main()
