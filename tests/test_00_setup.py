import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

# Imports must never create __pycache__ files in the read-only engine clone.
sys.dont_write_bytecode = True
# Keep the directive's four-line import preamble unchanged and the only import
# statement; load standard-library test helpers explicitly after path setup.
unittest = __import__("unittest")
hashlib = __import__("hashlib")
subprocess = __import__("subprocess")

PROJECT = pathlib.Path(__file__).resolve().parents[1]
FROZEN_DIRS = ("hle_unified", "baseline/HLE_Rebuild_R21B/hle")


class SetupTests(unittest.TestCase):
    def test_01_imports_resolve_to_read_clone(self):
        model = __import__("hle.model_a", fromlist=["position_of"])
        audit = __import__("hle_unified.conditioning_audit", fromlist=["completed_use"])
        self.assertEqual(
            pathlib.Path(model.__file__).resolve(),
            (ROOT / "baseline/HLE_Rebuild_R21B/hle/model_a.py").resolve(),
        )
        self.assertEqual(
            pathlib.Path(audit.__file__).resolve(),
            (ROOT / "hle_unified/conditioning_audit.py").resolve(),
        )
        self.assertTrue(callable(model.position_of))
        self.assertTrue(callable(audit.completed_use))

    def test_02_every_frozen_file_is_unchanged(self):
        expected = {}
        for row in (PROJECT / "ENGINE_FREEZE.sha256").read_text().splitlines():
            digest, relative = row.split("  ", 1)
            self.assertEqual(len(digest), 64, relative)
            self.assertTrue(all(c in "0123456789abcdef" for c in digest), relative)
            self.assertNotIn(relative, expected, "duplicate manifest path")
            self.assertTrue(any(relative.startswith(d + "/") for d in FROZEN_DIRS))
            self.assertTrue((ROOT / relative).resolve().is_relative_to(ROOT.resolve()))
            expected[relative] = digest
        self.assertTrue(expected, "empty freeze cannot establish invariance")
        actual_paths = {
            p.relative_to(ROOT).as_posix()
            for directory in FROZEN_DIRS
            for p in (ROOT / directory).rglob("*")
            if p.is_file()
        }
        self.assertEqual(set(expected), actual_paths, "frozen file set changed")
        for relative, digest in expected.items():
            with self.subTest(path=relative):
                self.assertEqual(hashlib.sha256((ROOT / relative).read_bytes()).hexdigest(), digest)

    def test_03_no_reverse_import_reference(self):
        result = subprocess.run(
            ["grep", "-rl", r"Socionics_Engine_Function_Conditioning\|conditioning_v2",
             str(ROOT / "hle_unified")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
