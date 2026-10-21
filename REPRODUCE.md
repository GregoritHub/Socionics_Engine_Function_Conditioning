# Reproduce the published results

Use Python 3.12, Git, and a POSIX shell with grep. No pip installation is needed.

## 1. Clone both repositories and pin the engine

```sh
git clone https://github.com/GregoritHub/Socionics_Engine.git && git -C Socionics_Engine checkout fdede6f
git clone https://github.com/GregoritHub/Socionics_Engine_Function_Conditioning.git
```

## 2. Set the engine path

```sh
cd Socionics_Engine_Function_Conditioning
printf '%s\n' '../Socionics_Engine' > engine_path.txt
```

The ignored file contains one line: `../Socionics_Engine`. Keep the clones as
siblings and run the following command from the companion repository root.

## 3. Run everything

```sh
python tools/reproduce.py
```

The runner verifies setup, regenerates all three history sets, runs every unittest,
regenerates all tables (Batch 4–7, the Batch 8 class tables, the Batch 9 solo8 tables) and all three reports, and compares their bytes with Git HEAD.
It runs with Python site-package loading disabled (`-S`) so ambient startup
hooks cannot become hidden dependencies. It never writes to the engine or uses a generated output as its own reference.
Per-step stdout/stderr is retained locally in ignored `OUT/reproduce_*.log`.

## 4. Success output, verbatim

```text
PASS: python -S -m unittest tests.test_00_setup -v
PASS: python -S generate/histories.py
PASS: python -S generate/histories_delivery.py
PASS: python -S generate/histories_solo8.py
PASS: python -S -m unittest discover -s tests -v
PASS: python -S -m conditioning_v2.tables
PASS: python -S -m conditioning_v2.tables --histories HISTORIES_DELIVERY.json
PASS: python -S -m conditioning_v2.classes
PASS: python -S -m conditioning_v2.classes --histories HISTORIES_DELIVERY.json
PASS: python -S -m conditioning_v2.solo8
REPRODUCED: 32 files identical
```

## 5. Expected time

Allow approximately 15–30 minutes on a laptop, depending on CPU speed. No
network is needed after cloning. The measured execution environment is in
[environment.txt](environment.txt); the acceptance timing is in the
[Batch 7 receipt](RECEIPTS/batch_7.md). The full publication gate runs the suite
once more after reproduction, so it takes longer than this reviewer command.

## 6. What is not reproducible from a bare clone

Nothing in the current measured results requires private data, downloaded
packages, or an unavailable archive. Checkpoints are generated locally and
verified against the committed manifest hashes. Historical stop receipts remain
records of earlier attempts; the runner does not recreate historical timings or
replay superseded failures. The unavailable triad is a documented limitation,
not a missing input that the reviewer must find.
