import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]

sys.dont_write_bytecode = True
os = __import__("os")
fnmatch = __import__("fnmatch")
PROJECT = pathlib.Path(__file__).resolve().parents[1]
SUFFIXES = {".md", ".py", ".json", ".txt"}
PATTERNS = tuple("/" + name + "/" for name in ("home", "workspace", "Users")) + ("C:" + chr(92),)
HISTORICAL_RECEIPTS = {"RECEIPTS/batch_" + str(i) + ".md" for i in range(7)}


def offenders(root):
    """Return relative file/line diagnostics under the exact Batch 7 A6 scope."""
    root = pathlib.Path(root)
    found = []

    def walk_error(error):
        relative = pathlib.Path(error.filename).relative_to(root).as_posix()
        found.append(relative + ": unreadable directory")

    for directory, directories, filenames in os.walk(root, onerror=walk_error):
        directories[:] = sorted(name for name in directories if name != ".git")
        for name in sorted(filenames):
            path = pathlib.Path(directory) / name
            relative = path.relative_to(root).as_posix()
            if path.suffix not in SUFFIXES or relative in HISTORICAL_RECEIPTS:
                continue
            if any(fnmatch.fnmatchcase(name, pattern) for pattern in ("DIRECTIVE_*", "BATCH_DIRECTIVE_*")):
                continue
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except (OSError, UnicodeError):
                found.append(relative + ": unreadable text")
                continue
            for number, line in enumerate(lines, 1):
                if any(pattern in line for pattern in PATTERNS):
                    found.append(relative + ":" + str(number))
    return sorted(found)


def main():
    """Print PATHS: clean or relative offenders; return the A6 gate exit code."""
    found = offenders(PROJECT)
    if found:
        print("PATHS: offenders")
        print("\n".join(found))
        return 1
    print("PATHS: clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
