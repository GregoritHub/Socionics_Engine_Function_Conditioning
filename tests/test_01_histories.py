import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
unittest = __import__("unittest")
json = __import__("json")
hashlib = __import__("hashlib")
replace = __import__("dataclasses").replace
histories = __import__("generate.histories", fromlist=["build"])
material = __import__("hle_unified.material", fromlist=["attrs", "attributes"])
model_a = __import__("hle.model_a", fromlist=["element_at"])


class HistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = json.loads((histories.PROJECT / "HISTORIES.json").read_text())

    def test_01_manifest_matched_seeds_types_and_dual_pair(self):
        self.assertGreaterEqual(len(self.rows), 8)
        self.assertEqual({(r["model"], r["seeds"]["fixture"]) for r in self.rows},
                         {(m, s) for m in histories.MODELS for s in histories.SEEDS})
        self.assertEqual(len({r["name"] for r in self.rows}), len(self.rows))
        for row in self.rows:
            self.assertEqual(set(row["actors"].values()), {"iee", "sli", "lie"})
            self.assertEqual(len(row["actors"]), 3)
        # Dual types exchange leading/creative with suggestive/mobilizing seats.
        for a, b in (("iee", "sli"), ("sli", "iee")):
            for source, target in ((1, 5), (2, 6)):
                self.assertEqual(model_a.element_at(a, source), model_a.element_at(b, target))

    def test_02_restore_hash_paid_use_finite_stop_and_regeneration(self):
        for row in self.rows:
            with self.subTest(history=row["name"]):
                raw = (histories.PROJECT / "OUT" / (row["name"] + ".checkpoint")).read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(), row["checkpoint_sha256"])
                restored = histories.Population.restore(raw.decode())
                self.assertEqual(restored.checkpoint().encode(), raw)
                self.assertTrue(restored.done)
                self.assertIsNone(restored.step())
                self.assertEqual(restored.checkpoint().encode(), raw)
                self.assertEqual(restored.engine.resource_model, row["model"])
                self.assertEqual(histories.summarize(restored, row["model"], row["seeds"]["fixture"], raw.decode()), row)
                self.assertTrue(all(n >= 1 for n in row["completed_paid_uses"].values()))
                regenerated = histories.build(row["model"], row["seeds"]["fixture"])
                self.assertEqual(regenerated.checkpoint().encode(), raw)

    def test_03_missing_and_forged_paid_evidence_rejected(self):
        for model in histories.MODELS:
            row = next(r for r in self.rows if r["model"] == model)
            raw = (histories.PROJECT / "OUT" / (row["name"] + ".checkpoint")).read_text()
            txs = list(histories.Population.restore(raw).engine.world.journal())
            # Find a routed paid transaction, ensuring the tested adapter is traversed.
            for index, tx in enumerate(txs):
                if (any("route_count" in material.attrs(v) and material.attrs(v).get("completed", 0) > 0
                        for v in tx.versions)
                    and any(material.attrs(v).get("record_type") == "wallet" and v.previous for v in tx.versions)):
                    break
            else:
                self.fail("no routed paid transaction witness")
            for mode in ("missing", "forged"):
                with self.subTest(model=model, mode=mode):
                    versions = []
                    for v in tx.versions:
                        d = material.attrs(v)
                        if d.get("record_type") == "wallet" and v.previous:
                            if mode == "missing":
                                continue
                            d["energy"] += 1
                            v = replace(v, attributes=material.attributes(d))
                        versions.append(v)
                    altered = txs[:]
                    altered[index] = replace(tx, versions=tuple(versions))
                    with self.assertRaisesRegex(ValueError, "wallet evidence|not paid by actor"):
                        histories.audit.completed_use(altered)


if __name__ == "__main__":
    unittest.main()
