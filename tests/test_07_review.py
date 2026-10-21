import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
unittest = __import__("unittest")
subprocess = __import__("subprocess")
json = __import__("json")
tables = __import__("conditioning_v2.tables", fromlist=["load_histories"])
PROJECT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "tests"))
BASE = "561028c4a1039a3dc71eac89cc5017dd0ab40980"


def committed(name):
    return subprocess.check_output(["git", "show", BASE + ":" + name], cwd=PROJECT)


def blocks(text):
    result, current = [], []
    for line in text.splitlines() + [""]:
        if line.startswith("| "):
            current.append([v.strip() for v in line.strip().strip("|").split("|")])
        elif current:
            result.append((current[0], current[2:]))
            current = []
    return result


def normalize(header):
    return [h.replace("Conditioning (A1 literal)", "Conditioning").replace(
        "Conditioning numerator and denominator IDs", "Conditioning numerator IDs") for h in header]


def verify_preserved():
    """A5: compare the regenerated wide projection against accepted table bytes."""
    for name in ("HISTORIES.json", "HISTORIES_DELIVERY.json"):
        if (PROJECT / name).read_bytes() != committed(name):
            raise AssertionError("manifest changed: " + name)
    checked, changes = 0, []
    for manifest in ("HISTORIES.json", "HISTORIES_DELIVERY.json"):
        histories = tables.load_histories(manifest)
        for composition in dict.fromkeys(h["manifest"].get("composition", "") for h in histories):
            subset = [h for h in histories if h["manifest"].get("composition", "") == composition]
            for name, text in tables.render(subset).items():
                path = "TABLES/" + (composition + "_" if composition else "") + pathlib.Path(name).stem + ("_delivery" if composition else "") + ".md"
                old, new = blocks(committed(path).decode()), blocks(text)
                if len(old) != len(new):
                    raise AssertionError("table section count changed: " + path)
                for (oh, orig), (nh, regen) in zip(old, new):
                    pairs = [(i, h.removesuffix(" wide").replace(" (both)", ""))
                             for i, h in enumerate(nh) if not h.endswith(" narrow") and h != "Reading"]
                    if normalize(oh) != [h for _, h in pairs]:
                        raise AssertionError("wide table headings differ: " + path)
                    if "Reading" in nh:
                        regen = [r for r in regen if r[nh.index("Reading")] == "wide"]
                    projected = [[r[i] for i, _ in pairs] for r in regen]
                    # Added narrow-only profile/supplier bins have exactly zero wide count.
                    extra = projected[len(orig):]
                    if extra:
                        if "Count" not in normalize(oh) or any(r[-2:] != ["0", "none"] for r in extra):
                            raise AssertionError("unexpected added wide row: " + path)
                    projected = projected[:len(orig)]
                    if len(projected) != len(orig):
                        raise AssertionError("missing wide row: " + path)
                    ci = normalize(oh).index("Conditioning") if "Conditioning" in normalize(oh) else None
                    for before, after in zip(orig, projected):
                        for i, (a, b) in enumerate(zip(before, after)):
                            checked += 1
                            if a != b:
                                if i != ci:
                                    raise AssertionError("non-conditioning cell changed: " + path + " " + str(before[:2]) + " " + oh[i])
                                changes.append((before[0], before[1], a, b))
        if manifest == "HISTORIES.json":
            for h in histories:
                for data in (h["observation"], h["narrow"]):
                    if data["received"] or any(type(r["source"]) is tuple for r in data["records"]):
                        raise AssertionError("Batch 1 tuple source introduced")
    for n in range(7):
        name = "RECEIPTS/batch_" + str(n) + ".md"
        if (PROJECT / name).read_bytes() != committed(name):
            raise AssertionError("historical receipt changed: " + name)
    return checked, changes


class ReviewTests(unittest.TestCase):
    def test_01_narrow_and_wide_inputs_positive_and_negative(self):
        audit = tables.measures.audit
        d = {"source.0": "semantic", "source_input": "single", "input.0": "generic"}
        self.assertEqual(audit._semantic_sources(d, "wide"), ("semantic", "single", "generic"))
        self.assertEqual(audit._semantic_sources(d, "narrow"), ("semantic", "single"))
        self.assertEqual(audit._semantic_sources({"input.0": "generic"}, "narrow"), ())
        self.assertEqual(audit._operation_source((), None, {}, {}), "world")
        with self.assertRaisesRegex(ValueError, "unknown provenance reading"):
            audit.uses((), "unknown")
        with self.assertRaisesRegex(ValueError, "unknown provenance reading"):
            audit._semantic_sources({}, "unknown")
        record = lambda actor: type("Producer", (), {"actor": actor})()
        profiles = {"a": "iee", "b": "sli"}
        producers = {"semantic": record("b"), "single": record("a"), "generic": record("ghost")}
        selected = audit._semantic_sources(d, "narrow")
        self.assertEqual(audit._operation_source(selected, "a", producers, profiles), ("b",))
        with self.assertRaisesRegex(ValueError, "unknown provenance actor"):
            audit._operation_source(audit._semantic_sources(d), "a", producers, profiles)
        with self.assertRaisesRegex(ValueError, "missing exact provenance revision"):
            audit._operation_source(("missing",), "a", producers, profiles)
        producers["semantic"] = record("ghost")
        with self.assertRaisesRegex(ValueError, "unknown provenance actor"):
            audit._operation_source(selected, "a", producers, profiles)
        self.assertEqual(audit._operation_source(("single",), "a", producers, profiles), "self")

    def test_02_conditioning_includes_world_and_self_weak_uses(self):
        fixture = __import__("test_04_measures", fromlist=["MeasureTests"]).MeasureTests
        profiles, records, episodes, (a, b, e, inactive) = fixture.positive_fixture()
        template = records[0]
        extra = [dict(template, source=s, source_seat=None, relation=None) for s in ("self", "world")]
        result = tables.measures.summarize(profiles, [*records, *extra], [*episodes, 0, 0], (0, 1))
        self.assertEqual(result["actors"][a]["conditioning"], (5, 7))
        self.assertEqual(result["actors"][inactive]["conditioning"], (0, 0))
        self.assertEqual(tables.ratio(result["actors"][inactive]["conditioning"]), "0/0 (N/A)")

    def test_03_readings_preserve_i1_i4_i5_and_narrow_is_subset(self):
        for manifest in ("HISTORIES.json", "HISTORIES_DELIVERY.json"):
            for h in tables.load_histories(manifest):
                w, n = h["observation"], h["narrow"]
                self.assertEqual(w["locations"], n["locations"])
                for rw, rn in zip(w["records"], n["records"]):
                    self.assertEqual({k:v for k,v in rw.items() if k not in ("source", "source_seat", "relation")},
                                     {k:v for k,v in rn.items() if k not in ("source", "source_seat", "relation")})
                    if type(rn["source"]) is tuple:
                        self.assertTrue(set(rn["source"]) <= set(rw["source"]))
                for actor in w["actors"]:
                    self.assertEqual(w["actors"][actor]["all_dcnh"], n["actors"][actor]["all_dcnh"])
                self.assertEqual(len(n["received"]), 0)

    def test_04_relation_display_names_do_not_drive_measures(self):
        fixture = __import__("test_04_measures", fromlist=["MeasureTests"]).MeasureTests
        profiles, records, episodes, _ = fixture.positive_fixture()
        m = tables.measures
        expected = m.summarize(profiles, records, episodes, (0, 1))
        original = m.LABELS
        try:
            m.LABELS = {k: dict(v, relation="display only") for k, v in original.items()}
            actual = m.summarize(profiles, records, episodes, (0, 1))
        finally:
            m.LABELS = original
        self.assertEqual(expected["benefit_ids"], actual["benefit_ids"])
        self.assertEqual(expected["actors"], actual["actors"])
        self.assertEqual(expected["coverage"], actual["coverage"])

    def test_05_review_hygiene_sizes_docs_and_historical_receipts(self):
        listed = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=PROJECT).decode().splitlines()
        base_names = set(subprocess.check_output(["git", "ls-tree", "-r", "--name-only", BASE], cwd=PROJECT).decode().splitlines())
        patterns = tuple("/" + part + "/" for part in ("home", "workspace", "Users")) + ("C:" + chr(92),)
        for name in listed:
            p = PROJECT / name
            raw = p.read_bytes()
            self.assertLess(len(raw), 200000, name)
            text = raw.decode("utf-8")
            self.assertNotIn(chr(0), text, name)
            historical = name.startswith("RECEIPTS/batch_") and name in base_names
            directive = p.name.startswith(("DIRECTIVE_", "BATCH_DIRECTIVE_"))
            if historical:
                self.assertEqual(raw, committed(name), name)
            elif not directive:
                self.assertFalse(any(pattern in text for pattern in patterns), name)
            if name not in base_names and not directive:
                self.assertFalse(any(pattern in text for pattern in patterns), name)
        self.assertFalse((PROJECT / "LICENSE").exists())
        ast = __import__("ast")
        for p in (PROJECT / "conditioning_v2").glob("*.py"):
            module = ast.parse(p.read_text())
            for node in module.body:
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and not node.name.startswith("_"):
                    doc = ast.get_docstring(node) or ""
                    self.assertTrue(any("I" + str(n) in doc for n in range(1,6)), (p.name, node.name))
                    self.assertIn("Batch", doc, (p.name, node.name))
        re = __import__("re")
        for part in re.split(r"^## ", (PROJECT / "README.md").read_text(), flags=re.M)[1:]:
            self.assertLessEqual(len(part.split()), 250, part.splitlines()[0])
        for name in ("REPORT.md", "REPORT_DELIVERY.md"):
            for part in re.split(r"^## ", (PROJECT / name).read_text(), flags=re.M)[1:]:
                self.assertLessEqual(len(part.split()), 300, (name, part.splitlines()[0]))


if __name__ == "__main__":
    unittest.main()
