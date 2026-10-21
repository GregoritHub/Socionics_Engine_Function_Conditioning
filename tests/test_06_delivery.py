import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
unittest = __import__("unittest")
json = __import__("json")
re = __import__("re")
hashlib = __import__("hashlib")
replace = __import__("dataclasses").replace
tables = __import__("conditioning_v2.tables", fromlist=["load_histories"])
measures = tables.measures
audit, retention = measures.audit, measures.retention
model, relations = measures.model, measures.relations
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
guard = __import__("test_07_review", fromlist=["verify_preserved"])
generator = __import__("generate.histories_delivery", fromlist=["report"])
field_tests = __import__("test_02_fields", fromlist=["FieldTests"])
measure_tests = __import__("test_04_measures", fromlist=["MeasureTests"])
PROJECT = pathlib.Path(__file__).resolve().parents[1]


class DeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.histories = tables.load_histories("HISTORIES_DELIVERY.json")
        cls.manifest = json.loads((PROJECT / "HISTORIES_DELIVERY.json").read_text())

    def test_00_a5_preserved_measurements_guard(self):
        guard.verify_preserved()

    def test_01_matched_compositions_codec_calls_and_limits(self):
        self.assertEqual(len(self.histories), 8)
        for composition in generator.COMPOSITIONS:
            subset = [h for h in self.histories if h["manifest"]["composition"] == composition]
            self.assertEqual({h["manifest"]["seeds"]["fixture"] for h in subset}, set(generator.SEEDS))
            for h in subset:
                m, obs = h["manifest"], h["observation"]
                self.assertEqual(m["model"], "legacy-r4")
                self.assertEqual(m["parameters"]["episodes"], 1)
                self.assertEqual(m["parameters"]["quantum"], generator.QUANTUM)
                self.assertEqual(m["parameters"]["budget"], 2000000 + 1000 * m["seeds"]["fixture"])
                self.assertEqual(m["finite_stop"]["status"], "succeeded")
                setup = m["calls"][0]
                self.assertEqual(setup["function"], "tests_u11.fixtures.setup11")
                self.assertEqual(setup["kwargs"], dict(tim=generator.COMPOSITIONS[composition],
                    budget=m["parameters"]["budget"], train_bob=True, train_eve=False))
                joins = [c for c in m["calls"] if c["function"] == "tests_u11.fixtures.join"]
                self.assertEqual(len(joins), 1)
                self.assertEqual(joins[0]["kwargs"], dict(actor="workshop:bob", key="join"))
                self.assertTrue(any(c["function"] == "tests_u11.fixtures.group" for c in m["calls"]))
                self.assertEqual(m["actors"]["workshop:eve"], "sli")
                eve = next(a for a in obs["profiles"] if a.key == "eve")
                self.assertFalse(obs["actors"][eve]["active"])
                self.assertEqual(len(obs["coverage"]["denominator"]), 12)
                self.assertEqual(set(obs["episodes"]), {0})
        unavailable = [c for c in self.manifest["compositions"] if c["status"] == "not producible"]
        self.assertEqual([c["name"] for c in unavailable], ["triad"])
        self.assertIn("fixed SLI", unavailable[0]["reason"])

    def test_02_i1_i2_i3_i5_and_real_pair_delivery(self):
        for h in self.histories:
            obs, txs = h["observation"], h["transactions"]
            profiles, expected = measures.conditioning.completed_use(txs)
            observed = {a: dict.fromkeys(measures.conditioning.ELEMENTS, 0) for a in profiles}
            for row in obs["records"]:
                self.assertEqual(row["seat"], model.position_of(row["tim"], row["element"]))
                self.assertEqual(row["dim"], model.fields(row["seat"])["dimensionality"])
                source = row["source"]
                self.assertTrue(source in ("self", "world") or type(source) is tuple)
                if type(source) is tuple:
                    self.assertTrue(source)
                    self.assertEqual(source, tuple(sorted(set(source))))
                    self.assertEqual(len(source), len(row["source_seat"]))
                    self.assertEqual(len(source), len(row["relation"]))
                    for actor, seat, relation in zip(source, row["source_seat"], row["relation"]):
                        self.assertIn(actor, profiles)
                        self.assertNotEqual(actor, row["actor"])
                        self.assertEqual(seat, model.position_of(profiles[actor], row["element"]))
                        self.assertEqual(relation, relations.relation(profiles[actor], row["tim"]))
                        self.assertEqual(relations.landing_position(profiles[actor], seat, row["tim"]), row["seat"])
                observed[row["actor"]][row["element"]] += 1
            self.assertEqual(observed, expected)
            self.assertEqual(obs["received"], tuple(i for i, r in enumerate(obs["records"]) if type(r["source"]) is tuple))
            for row in measures.conditioning.observations(txs):
                self.assertEqual(obs["actors"][row["actor"]]["all_dcnh"], row)
            if h["manifest"]["composition"] == "pair":
                self.assertTrue(obs["received"])
                self.assertIsNotNone(h["manifest"]["first_delivery"])
            witness = generator.first_delivery(txs, obs)
            self.assertEqual(witness, h["manifest"]["first_delivery"])
            self.assertTrue(witness["exact_inputs"])
            for exact in witness["exact_inputs"]:
                producer = txs[exact["transaction"]]
                self.assertEqual(measures.actor_name(producer.actor), exact["producer"])
                self.assertTrue(any(generator.argument(v.ref) == exact["ref"] for v in producer.versions))
                self.assertLess(exact["transaction"], witness["transaction"])

    def test_03_i4_prefix_monotonicity_repeat_duplicate_and_order(self):
        for h in self.histories:
            txs, whole = h["transactions"], h["observation"]["records"]
            paid_end = h["manifest"]["first_delivery"]["transaction"] + 1
            for end in (len(txs) // 2, paid_end):
                prefix = retention.uses(txs[:end])
                if end == paid_end:
                    self.assertTrue(any(r["kept"] for r in prefix))
                for i, row in enumerate(prefix):
                    self.assertEqual({k: v for k, v in row.items() if k != "kept"},
                                     {k: v for k, v in whole[i].items() if k != "kept"})
                    if row["kept"]:
                        self.assertIs(whole[i]["kept"], True)
            groups = {}
            for i, row in enumerate(whole):
                key = row["actor"], row["seat"], row["element"]
                groups.setdefault(key, []).append((i, row["kept"]))
            for group in groups.values():
                self.assertEqual([kept for _, kept in group], [True] * (len(group) - 1) + [False])
            with self.assertRaises(retention.DuplicateTransactionError):
                retention.uses((*txs, txs[-1]))
            first, repeat = next((a, b) for group in groups.values() for a, _ in group for b, _ in group
                                 if h["observation"]["locations"][a]["transaction"] < h["observation"]["locations"][b]["transaction"])
            a, b = (h["observation"]["locations"][i]["transaction"] for i in (first, repeat))
            reordered = list(txs)
            reordered.insert(a, reordered.pop(b))
            with self.assertRaises(retention.TransactionOrderError):
                retention.uses(reordered)

    def test_04_forged_provenance_and_seat_witnesses_still_reject(self):
        for h in self.histories:
            txs = h["transactions"]
            altered, _ = field_tests.FieldTests._with_producer_actor(txs, tables.ObjectId("forged", "actor"))
            with self.assertRaisesRegex(ValueError, "unknown provenance actor"):
                audit.uses(altered)
            # Exercise the original charged-hop forgery on each new history.
            fixture = field_tests.FieldTests("test_04_element_seat_contract_forgery_is_rejected")
            fixture.histories = [(h["manifest"]["name"], txs)]
            fixture.test_04_element_seat_contract_forgery_is_rejected()
            obs = h["observation"]
            delivery = h["manifest"]["first_delivery"]
            index = delivery["exact_inputs"][0]["transaction"]
            altered = list(txs)
            altered[index] = replace(txs[index], actor=tables.ObjectId("forged", "invitation_producer"))
            with self.assertRaisesRegex(ValueError, "unknown provenance actor"):
                audit.uses(altered)

    def test_05_multi_supplier_counting_and_tuple_negatives(self):
        profiles, rows, _, (alice, bob, eve, inactive) = measure_tests.MeasureTests.positive_fixture()
        source = tuple(sorted((bob, eve)))
        row = dict(rows[0], element="te", seat=6, dim=2, source=source,
                   source_seat=tuple(model.position_of(profiles[s], "te") for s in source),
                   relation=tuple(relations.relation(profiles[s], profiles[alice]) for s in source))
        data = measures.summarize(profiles, [row], [0], [0])
        self.assertEqual(data["received"], (0,))
        self.assertEqual(data["actors"][alice]["hold"], (1, 1))
        self.assertEqual(data["actors"][alice]["conditioning"], (1, 1))
        self.assertEqual(data["actors"][alice]["profile"][(6, "other", True)], [0])
        self.assertEqual(data["coverage"]["ratio"], (1, 16))
        self.assertEqual(data["concentration"], (2, 4))
        for sender in source:
            self.assertEqual(data["suppliers"][sender], [0])
            self.assertEqual(data["actors"][alice]["suppliers"][6][sender], [0])
            pair = next(p for p in data["pairs"] if p["sender"] == sender and p["receiver"] == alice)
            self.assertEqual(pair["forward"], (0,))
            self.assertFalse(pair["sterile"])
        for forged in ((), (bob, bob), tuple(reversed(source)), (alice,), (tables.ObjectId("forged", "unknown"),), bob):
            with self.assertRaisesRegex(ValueError, "invalid actor-id source"):
                measures.summarize(profiles, [dict(row, source=forged)], [0], [0])
        for changes, message in (({"source_seat": (1,)}, "source element-seat mismatch"),
                                 ({"relation": ()}, "source relation mismatch"),
                                 ({"kept": "True"}, "kept must be Boolean"),
                                 ({"dim": 99}, "seat-dimension mismatch")):
            with self.assertRaisesRegex(ValueError, message):
                measures.summarize(profiles, [dict(row, **changes)], [0], [0])

    def test_06_tables_report_traceability_and_size(self):
        text = (PROJECT / "REPORT_DELIVERY.md").read_text()
        self.assertEqual(text, generator.report(self.histories))
        sections = re.split(r"^## \d+\. ", text, flags=re.M)[1:]
        self.assertEqual(len(sections), 6)
        for i, section in enumerate(sections, 1):
            self.assertLessEqual(len(section.split()), 300, (i, len(section.split())))
        self.assertIn("join-accept", sections[0])
        self.assertIn("including collective", sections[5])
        self.assertIn("not producible", sections[2])
        self.assertLess((PROJECT / "HISTORIES_DELIVERY.json").stat().st_size, 200000)
        for composition in generator.COMPOSITIONS:
            histories = [h for h in self.histories if h["manifest"]["composition"] == composition]
            outputs = tables.render(histories)
            self.assertEqual(len(outputs), 3)
            for name, value in outputs.items():
                self.assertLess(len(value.encode()), 200000, (composition, name))
            for h in histories:
                obs = h["observation"]
                covered = {(r["actor"], r["seat"]) for r in obs["records"] if type(r["source"]) is tuple
                           and r["dim"] <= 2 and any(model.fields(p)["dimensionality"] >= 3 for p in r["source_seat"])}
                self.assertEqual(obs["coverage"]["ratio"], (len(covered), 4 * len(obs["profiles"])))
                for actor, r in obs["actors"].items():
                    incoming = [v for v in obs["records"] if v["actor"] == actor and type(v["source"]) is tuple]
                    self.assertEqual(r["hold"], (sum(v["kept"] for v in incoming), len(incoming)))
                    self.assertIn(tables.ratio(r["hold"]), text)
                self.assertIn(tables.ratio(obs["coverage"]["ratio"]), text)
        self.assertEqual(len({h["manifest"]["checkpoint_sha256"] for h in self.histories}), 8)


if __name__ == "__main__":
    unittest.main()
