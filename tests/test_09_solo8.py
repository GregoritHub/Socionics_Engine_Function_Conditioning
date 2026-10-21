import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
unittest = __import__("unittest")
json = __import__("json")
replace = __import__("dataclasses").replace
tables = __import__("conditioning_v2.tables", fromlist=["load_histories"])
classes = __import__("conditioning_v2.classes", fromlist=["history"])
solo8 = __import__("conditioning_v2.solo8", fromlist=["sequences"])
measures = tables.measures
energy = measures.energy
PROJECT = pathlib.Path(__file__).resolve().parents[1]


def paid_sequence(h, lo, hi):
    """Uses between two transaction indices, grouped by (actor, operation key)."""
    obs = h["observation"]
    keys = {}
    for t, tx in enumerate(h["transactions"]):
        for v in tx.versions:
            d = energy.data(v)
            if d.get("record_type") == "operation":
                keys[(t, v.ref)] = (d["actor"].key, d["key"])
    out = {}
    for i in range(len(obs["records"])):
        loc = obs["locations"][i]
        if lo <= loc["transaction"] < hi:
            r = obs["records"][i]
            out.setdefault(keys[(loc["transaction"], loc["operation"])], []).append((r["element"], r["seat"], h["classes"][i]["kind"]))
    return out


def operation(h, actor_key, key):
    heads = {}
    for tx in h["transactions"]:
        for v in tx.versions:
            d = energy.data(v)
            if d.get("record_type") == "operation" and d["actor"].key == actor_key and d["key"] == key:
                heads[v.ref.identity] = d
    return list(heads.values())[-1]


class Solo8Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = json.loads((PROJECT / "HISTORIES_SOLO8.json").read_text())
        cls.histories = tables.load_histories("HISTORIES_SOLO8.json")
        cls.pair = {h["manifest"]["seeds"]["fixture"]: h for h in tables.load_histories("HISTORIES_DELIVERY.json")
                    if h["manifest"]["composition"] == "pair"}
        for h in (*cls.histories, *cls.pair.values()):
            classes.history(h, "wide")

    def test_01_manifest_prediction_program_and_engine(self):
        self.assertEqual({h["manifest"]["seeds"]["fixture"] for h in self.histories}, {17, 29, 43, 61})
        self.assertIn("internalisation > 0 for workshop:alice at seats 5 and 6", self.document["prediction"])
        self.assertEqual([r["row"] for r in self.document["program"]], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 19, 20])
        self.assertEqual(self.document["amendments"], ["A9"])
        for h in self.histories:
            m = h["manifest"]
            self.assertEqual(m["engine"], "hle_unified.workflow_execution.WorkflowEngine")
            self.assertEqual(m["model"], "legacy-r4")
            self.assertEqual(m["refused_rows"], [])
            self.assertLess(m["phase_marks"]["probe_end"], m["phase_marks"]["collective_end"])
            self.assertLess(m["phase_marks"]["collective_end"], m["phase_marks"]["solo_end"])
            self.assertEqual(m["phase_marks"]["solo_end"], m["transactions"])

    def test_02_collective_phase_reproduces_pair_paid_sequence(self):
        for h in self.histories:
            seed = h["manifest"]["seeds"]["fixture"]
            pair = self.pair[seed]
            marks = h["manifest"]["phase_marks"]
            mine = paid_sequence(h, marks["probe_end"], marks["collective_end"])
            theirs = paid_sequence(pair, 0, len(pair["transactions"]))
            self.assertEqual(set(mine), set(theirs), "collective phase operations differ from the pair history")
            for key in theirs:
                content = lambda rows: [r for r in rows if r[2] == "content"]
                self.assertEqual(content(mine[key]), content(theirs[key]), key)
                if key != ("alice", "repair-group"):
                    self.assertEqual(mine[key], theirs[key], key)
            # The first collective operation starts from a different active element
            # (Alice's cursor sits at the probe's last element), so only its hops differ.
            self.assertNotEqual(mine[("alice", "repair-group")], theirs[("alice", "repair-group")])
            # Batch 8 measures on the collective phase equal the pair values.
            s_pair = classes.history(pair, "wide")["actors"]
            for actor, r in s_pair.items():
                mine_ids = [i for i in range(len(h["observation"]["records"]))
                            if h["observation"]["records"][i]["actor"] == actor
                            and marks["probe_end"] <= h["observation"]["locations"][i]["transaction"] < marks["collective_end"]]
                self.assertEqual(sum(h["classes"][i]["kind"] == "content" for i in mine_ids), r["price"]["content"])
                if actor.key != "alice":
                    self.assertEqual(len(mine_ids), r["price"]["uses"])
                    self.assertEqual(sum(h["classes"][i]["time"] for i in mine_ids), r["price"]["time_total"])

    def test_03_solo_phase_reaches_every_seat_and_bob_only_exchanges(self):
        for h in self.histories:
            marks = h["manifest"]["phase_marks"]
            field = solo8.field_three_ways(h)
            alice = next(a for a in field if a.key == "alice")
            for p in range(1, 9):
                self.assertGreaterEqual(field[alice]["phases"]["solo"]["seats"][p]["content"], 1, (h["manifest"]["name"], p))
            keys = set()
            heads = {}
            for tx in h["transactions"][marks["collective_end"]:]:
                for v in tx.versions:
                    d = energy.data(v)
                    if d.get("record_type") == "operation" and d["actor"].key == "bob" and "route_count" in d:
                        keys.add(d["key"])
            self.assertTrue(keys, "Bob completes exchange work in the solo phase")
            self.assertTrue(all("-exchange" in k for k in keys), keys)
            eve = next(a for a in field if a.key == "eve")
            self.assertEqual(len(field[eve]["phases"]["whole"]["ids"]), 0)

    def test_04_internalisation_defined_and_monotone(self):
        for h in self.histories:
            marks = h["manifest"]["phase_marks"]
            for reading in ("wide", "narrow"):
                s = classes.history(h, reading)
                alice = next(a for a in s["actors"] if a.key == "alice")
                a = s["actors"][alice]
                self.assertGreater(a["internal_by_seat"][5][1], 0)
                self.assertGreater(a["internal_by_seat"][6][1], 0)
                if reading == "narrow":
                    # Workflow operations declare semantic inputs, so narrow is non-empty here.
                    self.assertGreater(a["internalisation"][1], 0)
            # A2 monotonicity: on the collective-phase prefix no self repeat exists yet.
            prefix = h["transactions"][:marks["collective_end"]]
            events = tuple(e for e in h["events"] if any(
                energy.data(v).get("record_type") == "operation" and energy.data(v)["actor"] == e["actor"] and energy.data(v)["key"] == e["key"]
                for tx in prefix for v in tx.versions))
            obs = measures.history(prefix, events, "wide")
            kept = classes.kept_self(obs["records"])
            received = [i for i in obs["received"] if obs["records"][i]["actor"].key == "alice"]
            self.assertTrue(received)
            self.assertFalse(any(kept[i] for i in received))
            full = classes.kept_self(h["observation"]["records"])
            self.assertTrue(any(full[i] for i in received))

    def test_05_element_override_witness(self):
        for h in self.histories:
            flipped = operation(h, "alice", "solo-02-express-expenditure-neti")
            self.assertEqual((flipped["route.0.element"], flipped["route.0.seat"], flipped["route.1.element"], flipped["route.1.seat"]),
                             ("ne", 1, "ti", 4))
            default = operation(h, "alice", "probe-uptake")
            self.assertEqual((default["route.0.seat"], default["route.1.seat"]), (7, 6))
            self.assertEqual(flipped["status"], "succeeded")

    def test_06_negatives_fold_family_and_forged_attribution(self):
        c = __import__("tests_c7_workflow.fixtures", fromlist=["setup_workflow"])
        e = c.setup_workflow("iee")
        base = c.cell(e, "Express", "expenditure", key="neg", prepare_only=True)["request"]
        with self.assertRaisesRegex(ValueError, "fixed Fold families"):
            replace(base, elements=("ni",))
        with self.assertRaisesRegex(ValueError, "fixed Fold families"):
            replace(base, elements=("si", "te"))
        self.assertEqual(replace(base, elements=("ne", "ti")).elements, ("ne", "ti"))
        h = self.histories[0]
        forged = []
        for ev in h["events"]:
            if ev["actor"].key == "alice" and ev["key"] == "solo-16-theorize-expenditure-ne":
                forged.append(dict(ev, actor=tables.ObjectId("workshop", "bob")))
            else:
                forged.append(ev)
        with self.assertRaisesRegex(ValueError, "paid use lacks recorded episode"):
            measures.history(h["transactions"], tuple(forged), "wide")

    def test_07_tables_and_report_present_and_sized(self):
        for name in ("per_actor_seed-17", "per_actor_seed-29", "per_actor_seed-43", "per_actor_seed-61", "per_population", "dcnh_two_ways", "classes", "price_of_type", "dcnh_five_ways", "sequence", "field"):
            path = PROJECT / "TABLES" / ("pair-solo8_" + name + ".md")
            self.assertTrue(path.exists(), name)
            self.assertLess(path.stat().st_size, 200000)
        text = (PROJECT / "REPORT_SOLO8.md").read_text(encoding="utf-8")
        self.assertLessEqual(len(text.split()), 500)
        self.assertIn(self.document["prediction"], text)


if __name__ == "__main__":
    unittest.main()
