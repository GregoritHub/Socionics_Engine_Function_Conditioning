import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
subprocess = __import__("subprocess")
os = __import__("os")
time = __import__("time")
# Exclude ambient .pth/site hooks; the reproduction has no installed dependencies.
if __name__ == "__main__" and not sys.flags.no_site:
    os.execv(sys.executable, [sys.executable, "-S", *sys.argv])
PROJECT = pathlib.Path(__file__).resolve().parents[1]


def artifact_paths(ref):
    """Enumerate every tracked table and top-level report in a Git tree."""
    names = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", ref], cwd=PROJECT).decode().splitlines()
    return sorted(n for n in names if n.startswith("TABLES/") or
                  ("/" not in n and n.startswith("REPORT") and n.endswith(".md")))


def verify_artifacts(expected):
    """Compare regenerated artifacts with the independently captured Git blobs."""
    actual = {p.relative_to(PROJECT).as_posix() for p in (PROJECT / "TABLES").rglob("*") if p.is_file()}
    actual.update(p.name for p in PROJECT.glob("REPORT*.md"))
    different = sorted(set(expected) ^ actual)
    different.extend(n for n in sorted(set(expected) & actual) if (PROJECT / n).read_bytes() != expected[n])
    return sorted(set(different))


def main():
    """Rebuild all measured outputs, then compare them with the committed tree.

    The no-argument reviewer path always uses HEAD. The maintainer-only
    REPRODUCE_BASE_TREE variable permits a prospective staged tree for the
    pre-commit gate; it is never written to a config file or used implicitly.
    A committed-tree run is still required before publication (Batch 7/A5).
    """
    if len(sys.argv) != 1:
        raise SystemExit("usage: python tools/reproduce.py")
    ref = os.environ.get("REPRODUCE_BASE_TREE", "HEAD")
    # Resolve once before any generator runs; never compare a file with itself.
    ref = subprocess.check_output(["git", "rev-parse", "--verify", ref + "^{tree}"], cwd=PROJECT).decode().strip()
    expected = {n: subprocess.check_output(["git", "show", ref + ":" + n], cwd=PROJECT) for n in artifact_paths(ref)}
    if not expected or not {"REPORT.md", "REPORT_DELIVERY.md"} <= set(expected):
        raise SystemExit("reproduction baseline lacks committed reports")
    commands = [
        ("-m", "unittest", "tests.test_00_setup", "-v"),
        ("generate/histories.py",),
        ("generate/histories_delivery.py",),
        ("-m", "unittest", "discover", "-s", "tests", "-v"),
        ("-m", "conditioning_v2.tables"),
        ("-m", "conditioning_v2.tables", "--histories", "HISTORIES_DELIVERY.json"),
    ]
    out = PROJECT / "OUT"
    out.mkdir(exist_ok=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    started = time.monotonic()
    for i, args in enumerate(commands):
        result = subprocess.run([sys.executable, "-S", *args], cwd=PROJECT, env=env,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        text = result.stdout.replace(str(PROJECT), "<write>").replace(str(ROOT.resolve()), "<read>")
        (out / ("reproduce_" + str(i) + ".log")).write_text(text, encoding="utf-8")
        label = "python -S " + " ".join(args)
        if result.returncode:
            print("FAILED: " + label, flush=True)
            print(text, end="" if text.endswith("\n") else "\n", flush=True)
            return result.returncode
        print("PASS: " + label, flush=True)
    different = verify_artifacts(expected)
    (out / "reproduce_seconds.txt").write_text(f"{time.monotonic() - started:.3f}\n")
    if different:
        for name in different:
            print("DIFF: " + name, flush=True)
        return 1
    print("REPRODUCED: " + str(len(expected)) + " files identical", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
