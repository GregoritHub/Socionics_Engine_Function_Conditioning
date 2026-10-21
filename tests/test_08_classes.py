import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
unittest = __import__("unittest")
subprocess = __import__("subprocess")
copy = __import__("copy")
tables = __import__("conditioning_v2.tables", fromlist=["load_histories"])
classes = __import__("conditioning_v2.classes", fromlist=["classify"])
measures = tables.measures
conditioning = measures.conditioning
PROJECT = pathlib.Path(__file__).resolve().parents[1]
BATCH7 = "3fffd9b765ad040e88a6c9452117daef73fabe03"


def committed(name):
    return subprocess.check_output(["git", "show", BATCH7 + ":" + name], cwd=PROJECT)


def batch7_names():
    names = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", BATCH7], cwd=PROJECT).decode().splitlines()
    return [n for n in names if n.startswith("TABLES/") or n.startswith("RECEIPTS/batch_")]


class ClassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.population = tables.load_histories("HISTORIES.json")
        cls.delivery = tables.load_histories("HISTORIES_DELIVERY.json")
        cls.by_name = {h["manifest"]["name"]: h for h in (*cls.population, *cls.delivery)}
        for h in cls.by_name.values():
            classes.history(h, "wide")

    def test_01_alignment_and_i5_partition_on_every_history(self):
        for h in self.by_name.values():
            records, kinds = h["observation"]["records"], h["classes"]
            self.assertEqual(len(kinds), len(records))
            profiles, counts = conditioning.completed_use(h["transactions"])
            for actor in profiles:
                mine = [i for i, r in enumerate(records) if r["actor"] == actor]
                hops = sum(kinds[i]["kind"] == "hop" for i in mine)
                content = sum(kinds[i]["kind"] == "content" for i in mine)
                self.assertEqual(hops + content, sum(counts[actor].values()))
            for r, c in zip(records, kinds):
                self.assertEqual(c["ring"], measures.model.fields(r["seat"])["ring"])
                self.assertIn(c["support_seat"], (5, 6, 7, 8))
            # Reading independence: the narrow summary reuses the same classes.
            narrow = classes.history(h, "narrow")
            wide = classes.history(h, "wide")
            for a in wide["actors"]:
                self.assertEqual(wide["actors"][a]["price"], narrow["actors"][a]["price"])
                self.assertEqual(wide["actors"][a]["dcnh"]["all"], narrow["actors"][a]["dcnh"]["all"])

    def test_02_directive_probe_numbers_on_seed_17(self):
        pair = classes.history(self.by_name["pair-seed-17"], "wide")["actors"]
        sterile = classes.history(self.by_name["pair-sterile-seed-17"], "wide")["actors"]
        alice = next(r for a, r in pair.items() if a.key == "alice")
        bob = next(r for a, r in pair.items() if a.key == "bob")
        eie = next(r for a, r in sterile.items() if a.key == "alice")
        self.assertEqual((alice["price"]["hops"], alice["price"]["content"]), (47, 38))
        self.assertEqual(bob["per_kind"]["hop"]["conditioning"], (12, 12))
        self.assertEqual(bob["per_kind"]["content"]["conditioning"], (0, 0))
        self.assertEqual(eie["price"]["content"], alice["price"]["content"])
        self.assertGreater(eie["price"]["hops"], alice["price"]["hops"])
        self.assertEqual(eie["tim"], "eie")

    def test_03_observed_supply_bounded_and_bob_seats_unobserved(self):
        for h in self.by_name.values():
            for reading in ("wide", "narrow"):
                s = classes.history(h, reading)
                self.assertLessEqual(s["observed_coverage"]["ratio"][0], s["structural_coverage"]["ratio"][0])
                self.assertEqual(s["observed_coverage"]["ratio"][1], s["structural_coverage"]["ratio"][1])
        s = classes.history(self.by_name["pair-seed-17"], "wide")
        bob = next(r for a, r in s["actors"].items() if a.key == "bob")
        alice = next(r for a, r in s["actors"].items() if a.key == "alice")
        self.assertEqual(sum(len(v) for v in bob["observed_suppliers"][5].values()), 0)
        self.assertEqual(sum(len(v) for v in bob["observed_suppliers"][6].values()), 0)
        self.assertGreater(sum(len(v) for v in alice["observed_suppliers"][5].values()), 0)
        self.assertEqual(s["observed_coverage"]["ratio"], (2, 12))

    def test_04_internalisation_zero_everywhere_and_monotone(self):
        for h in self.by_name.values():
            for reading in ("wide", "narrow"):
                s = classes.history(h, reading)
                for r in s["actors"].values():
                    self.assertEqual(r["internalisation"][0], 0)
        # Positive and monotone witness on a synthetic record sequence.
        base = dict(actor="a", seat=5, element="si")
        seq = [dict(base, source=("b",)), dict(base, source=("b",)), dict(base, source="self")]
        self.assertEqual(classes.kept_self(seq), (True, True, False))
        self.assertEqual(classes.kept_self(seq[:2]), (False, False))
        other_seat = [dict(base, source=("b",)), dict(base, seat=6, element="te", source="self")]
        self.assertEqual(classes.kept_self(other_seat), (False, False))

    def test_05_margin_definition(self):
        for h in self.by_name.values():
            s = classes.history(h, "wide")
            for r in s["actors"].values():
                for view, d in r["dcnh"].items():
                    if d["margin"] == "N/A":
                        self.assertFalse(any(d["axis_loads"]))
                    else:
                        self.assertEqual(d["margin"] == 0, len(d["cells_with_greatest_load"]) > 1)
        self.assertEqual(classes.margin(dict(axis_loads=(3, 3, 0, 0))), 0)
        self.assertEqual(classes.margin(dict(axis_loads=(5, 1, 0, 0))), 4)
        self.assertEqual(classes.margin(dict(axis_loads=(0, 0, 0, 0))), "N/A")

    def test_06_negative_forged_kind_support_and_sequence(self):
        h = self.by_name["pair-seed-17"]
        records, kinds = h["observation"]["records"], h["classes"]
        forged = copy.deepcopy(list(kinds))
        forged[0]["kind"] = "transit"
        with self.assertRaisesRegex(ValueError, "forged use class"):
            classes.validate(forged, records)
        forged = copy.deepcopy(list(kinds))
        forged[0]["support_seat"] = 3
        with self.assertRaisesRegex(ValueError, "forged use class"):
            classes.validate(forged, records)
        forged = copy.deepcopy(list(kinds))
        forged[0]["energy"] += 1
        with self.assertRaisesRegex(ValueError, "energy differs"):
            classes.validate(forged, records)
        swapped = list(records)
        swapped[0] = dict(swapped[0], element="fe")
        with self.assertRaisesRegex(ValueError, "differs from Batch 3 sequence"):
            classes.classify(h["transactions"], swapped)
        with self.assertRaisesRegex(ValueError, "differs from Batch 3 sequence"):
            classes.classify(h["transactions"], records[:-1])
        with self.assertRaisesRegex(ValueError, "use class count"):
            classes.validate(kinds[:-1], records)

    def test_07_batch7_artifacts_byte_identical(self):
        for name in batch7_names():
            self.assertEqual((PROJECT / name).read_bytes(), committed(name), name)
        for name in ("REPORT.md", "REPORT_DELIVERY.md"):
            # The generators rewrite the reports without the Batch 8 section and
            # conditioning_v2.classes appends it afterwards (reproduce.py order), so
            # the Batch 7 text must be a prefix either way.
            text = (PROJECT / name).read_text(encoding="utf-8")
            marker = "\n## 8. "
            head = text[:text.index(marker) + 1] if marker in text else text
            self.assertEqual(head.rstrip("\n"), committed(name).decode().rstrip("\n"), name)
            if marker in text:
                self.assertLessEqual(len(text[text.index(marker):].split()), 300)
            else:
                section = classes.report_section(self.delivery if name.endswith("DELIVERY.md") else self.population,
                                                 name.endswith("DELIVERY.md"))
                self.assertLessEqual(len(section.split()), 300)
        for name in ("classes.md", "price_of_type.md", "dcnh_five_ways.md",
                     "pair_classes_delivery.md", "pair_price_of_type_delivery.md", "pair_dcnh_five_ways_delivery.md",
                     "pair-sterile_classes_delivery.md", "pair-sterile_price_of_type_delivery.md",
                     "pair-sterile_dcnh_five_ways_delivery.md"):
            self.assertTrue((PROJECT / "TABLES" / name).exists(), name)

    def test_08_rendered_cells_recomputed(self):
        subset = [self.by_name["pair-seed-17"]]
        rendered = classes.render(subset)["price_of_type.md"]
        s = classes.history(subset[0], "wide")
        alice = next(r for a, r in s["actors"].items() if a.key == "alice")
        row = next(l for l in rendered.splitlines() if l.startswith("| pair-seed-17 | workshop:alice | iee | active |"))
        cells = [c.strip() for c in row.strip("|").split("|")]
        self.assertEqual(cells[4:11], [str(alice["price"][k]) for k in
                         ("uses", "hops", "content", "time_total", "time_hop", "time_content", "energy_total")])
        self.assertEqual(int(cells[4]), 85)


if __name__ == "__main__":
    unittest.main()
