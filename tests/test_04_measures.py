import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
unittest = __import__("unittest")
tables = __import__("conditioning_v2.tables", fromlist=["load_histories"])
measures = __import__("conditioning_v2.measures", fromlist=["history"])
conditioning = __import__("hle_unified.conditioning_audit", fromlist=["observations"])
model = __import__("hle.model_a", fromlist=["fields", "position_of"])
relations = __import__("hle.relations", fromlist=["relation"])
ObjectId = __import__("hle_unified.records", fromlist=["ObjectId"]).ObjectId
PROJECT = pathlib.Path(__file__).resolve().parents[1]


def markdown_rows(name, section=None):
    text = (PROJECT / "TABLES" / name).read_text()
    if section:
        text = text.split("## " + section + "\n", 1)[1].split("\n## ", 1)[0]
    rows = [[cell.strip() for cell in line.strip().strip("|").split("|")]
            for line in text.splitlines() if line.startswith("| ")]
    return [dict(zip(rows[0], row)) for row in rows[2:]]


class MeasureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.histories = tables.load_histories()
        cls.by_name = {h["manifest"]["name"]: h for h in cls.histories}

    def test_01_i5_full_observation_equals_phase7_on_every_actor_history(self):
        for h in self.histories:
            expected = conditioning.observations(h["transactions"])
            data = h["observation"]
            for row in expected:
                with self.subTest(history=h["manifest"]["name"], actor=row["actor"]):
                    self.assertEqual(data["actors"][row["actor"]]["all_dcnh"], row)
                    self.assertEqual(data["actors"][row["actor"]]["received_kept_dcnh"]["counts"],
                                     dict.fromkeys(conditioning.ELEMENTS, 0))
            self.assertEqual(len(data["received"]), 0)
            self.assertEqual(data["coverage"]["ratio"], (0, 12))
            self.assertEqual(data["concentration"], (0, 0))
            self.assertEqual(sum(p["sterile"] for p in data["pairs"]), 6)
            self.assertIsNone(data["standalone_pair"])

    def test_02_twenty_saved_table_cells_recomputed_from_records(self):
        checked = 0
        profiles = markdown_rows("per_actor.md", "Use profile")
        for index in (round(i * (len(profiles) - 1) / 5) for i in range(6)):
            cell = profiles[index]
            records = self.by_name[cell["History"]]["observation"]["records"]
            selected = [r for r in records if measures.actor_name(r["actor"]) == cell["Actor"]
                        and r["seat"] == int(cell["Seat"])
                        and (r["source"] if r["source"] in ("self", "world") else "other") == cell["Source class"]
                        and str(r["kept"]) == cell["Kept"]]
            self.assertEqual(int(cell["Count"]), len(selected))
            checked += 1
        dcnh = markdown_rows("dcnh_two_ways.md")
        for cell in dcnh[::6]:
            records = self.by_name[cell["History"]]["observation"]["records"]
            counts = {p: sum(measures.actor_name(r["actor"]) == cell["Actor"] and r["seat"] == p
                             for r in records) for p in range(1, 9)}
            expected = tuple(counts[a] + counts[b] for a, b in ((1, 3), (2, 4), (5, 7), (6, 8)))
            self.assertEqual(tuple(map(int, cell["Loads"].split(","))), expected)
            checked += 1
        for cell in markdown_rows("per_population.md", "Population summary")[:6]:
            data = self.by_name[cell["History"]]["observation"]
            covered = {(r["actor"], r["seat"]) for r in data["records"]
                       if isinstance(r["source"], tuple) and r["dim"] <= 2
                       and any(model.fields(p)["dimensionality"] >= 3 for p in r["source_seat"])}
            denom = sum(model.fields(p)["dimensionality"] <= 2
                        for _ in data["profiles"] for p in range(1, 9))
            self.assertEqual(cell["Coverage"], tables.ratio((len(covered), denom)))
            checked += 1
        self.assertEqual(checked, 20)

    @staticmethod
    def positive_fixture():
        # Explicit test-only observations, not claimed generated deliveries.
        alice, bob, eve, inactive = [ObjectId("test", key) for key in ("alice", "bob", "eve", "inactive")]
        profiles = {alice: "iee", bob: "sli", eve: "lie", inactive: "ile"}
        def row(actor, element, source, kept):
            tim = profiles[actor]
            seat = model.position_of(tim, element)
            source = (source,) if source in profiles else source
            other = isinstance(source, tuple)
            return dict(actor=actor, tim=tim, element=element, seat=seat,
                        dim=model.fields(seat)["dimensionality"], source=source,
                        source_seat=tuple(model.position_of(profiles[s], element) for s in source) if other else None,
                        relation=tuple(relations.relation(profiles[s], tim) for s in source) if other else None, kept=kept)
        records = [row(alice, "si", bob, True), row(alice, "si", bob, False),
                   row(alice, "te", eve, True), row(alice, "te", eve, False),
                   row(bob, "ne", alice, False), row(alice, "se", eve, False),
                   row(alice, "ni", "world", False), row(alice, "ne", "self", False)]
        return profiles, records, (0, 1, 0, 1, 1, 1, 0, 0), (alice, bob, eve, inactive)

    def test_03_positive_supplier_coverage_hold_concentration_and_inactive(self):
        profiles, rows, episodes, (alice, bob, eve, inactive) = self.positive_fixture()
        data = measures.summarize(profiles, rows, episodes, (0, 1))
        self.assertEqual(data["actors"][alice]["conditioning"], (5, 5))
        self.assertEqual(data["actors"][alice]["hold"], (2, 5))
        self.assertEqual(data["actors"][alice]["suppliers"][5][bob], [0, 1])
        self.assertEqual(data["actors"][alice]["suppliers"][6][eve], [2, 3])
        self.assertEqual(data["coverage"]["ratio"], (3, 16))
        self.assertEqual(data["coverage"]["ids"], (0, 1, 2, 3, 4))
        self.assertEqual(data["episode_coverage"][0]["ratio"], (2, 16))
        self.assertEqual(data["episode_coverage"][0]["ids"], (0, 2))
        self.assertEqual(data["episode_coverage"][1]["ratio"], (3, 16))
        self.assertEqual(data["concentration"], (14, 36))
        self.assertEqual(data["benefit_ids"], (2, 3, 5))
        self.assertFalse(data["actors"][inactive]["active"])
        self.assertEqual(data["actors"][inactive]["hold"], (0, 0))
        self.assertEqual(sum(actor == inactive for actor, _ in data["coverage"]["denominator"]), 4)
        self.assertTrue(all(p["sterile"] for p in data["pairs"]
                            if inactive in (p["sender"], p["receiver"])))
        filtered = measures.summarize(profiles, rows[:6], episodes[:6], (0, 1))
        for field in ("received", "coverage", "concentration", "suppliers", "pairs", "benefit_ids"):
            self.assertEqual(data[field], filtered[field], field)
        self.assertNotEqual(data["actors"][alice]["all_dcnh"], filtered["actors"][alice]["all_dcnh"])
        self.assertEqual(data["actors"][alice]["received_kept_dcnh"]["counts"]["si"], 1)
        self.assertEqual(data["actors"][alice]["received_kept_dcnh"]["counts"]["te"], 1)

    def test_04_inactive_history_appears_in_rendered_denominators(self):
        h = self.histories[0]
        end = h["observation"]["locations"][0]["transaction"]
        inactive = measures.history(h["transactions"][:end], h["events"])
        self.assertEqual(inactive["records"], ())
        self.assertTrue(all(not row["active"] for row in inactive["actors"].values()))
        self.assertEqual(inactive["coverage"]["ratio"], (0, 12))
        rendered = tables.render([dict(h, observation=inactive)])
        self.assertIn("| inactive |", rendered["per_actor.md"])
        self.assertIn("0/12 = 0", rendered["per_population.md"])
        self.assertTrue(all(row["active"] for row in h["observation"]["actors"].values()))

    def test_05_missing_or_forged_measure_inputs_are_rejected(self):
        profiles, rows, episodes, _ = self.positive_fixture()
        for changed, message in ((dict(rows[0], source=(ObjectId("forged", "unknown"),)), "invalid actor-id source"),
                                 (dict(rows[0], dim=99), "seat-dimension mismatch"),
                                 (dict(rows[0], kept="True"), "kept must be Boolean")):
            with self.assertRaisesRegex(ValueError, message):
                measures.summarize(profiles, [changed, *rows[1:]], episodes, (0, 1))
        incomplete = dict(rows[0]); del incomplete["source"]
        with self.assertRaisesRegex(ValueError, "incomplete use record"):
            measures.summarize(profiles, [incomplete, *rows[1:]], episodes, (0, 1))
        with self.assertRaisesRegex(ValueError, "each use requires an episode"):
            measures.summarize(profiles, rows, episodes[:-1], (0, 1))

    def test_06_episode_join_has_positive_and_negative_witnesses(self):
        for h in self.histories:
            with self.subTest(history=h["manifest"]["name"]):
                data = h["observation"]
                self.assertEqual(set(data["episodes"]), {0, 1})
                self.assertEqual(len(data["locations"]), len(data["records"]))
                for i, location in enumerate(data["locations"]):
                    tx = h["transactions"][location["transaction"]]
                    version = next(v for v in tx.versions if v.ref == location["operation"])
                    attrs = measures.energy.data(version)
                    matching = {e["episode"] for e in h["events"] if e["actor"] == data["records"][i]["actor"]
                                and attrs["key"] == e["key"] + ":movement"}
                    self.assertEqual(matching, {location["episode"]})
                with self.assertRaisesRegex(ValueError, "paid use lacks recorded episode"):
                    measures.locate_uses(h["transactions"], (), data["records"], data["profiles"])
                forged = [*h["events"], dict(h["events"][0], episode=99)]
                with self.assertRaisesRegex(ValueError, "conflicting episode attribution"):
                    measures.locate_uses(h["transactions"], forged, data["records"], data["profiles"])

    def test_07_relation_labels_and_generated_table_artifacts(self):
        for key, entry in measures.LABELS.items():
            sender, receiver = key.split(":")
            self.assertEqual(tuple(entry["landing_permutation"]), relations.landing_permutation(sender, receiver))
            self.assertEqual(measures.relation_name(sender, receiver), entry["relation"])
        outputs = tables.render(self.histories)
        self.assertEqual(set(outputs), {"per_actor.md", "per_population.md", "dcnh_two_ways.md"})
        for name, expected in outputs.items():
            raw = (PROJECT / "TABLES" / name).read_bytes()
            self.assertLess(len(raw), 200000)
            self.assertEqual(raw.decode(), expected)
        self.assertIn("1 whenever defined, N/A when empty", outputs["per_actor.md"])
        self.assertIn("N/A: not generated", outputs["per_population.md"])


if __name__ == "__main__":
    unittest.main()
