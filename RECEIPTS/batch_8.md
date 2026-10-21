# Batch 8 receipt — use classes, observed supply, DCNH margin, price of type

Executed 20 October 2026 (client date) by the directive author, from the Batch 7
tree `3fffd9b` with the directive extension committed as `7ff7c53`. Engine read
clone unchanged at `fdede6f`; `ENGINE_FREEZE.sha256` verified by `test_00_setup`.

## Amendment before work

A8 (`DIRECTIVE_AMENDMENT_A8_additive_tables.md`) was issued before any code was
written: the Batch 7 preservation guard rejects added headings on existing
tables, so Batch 8 measures go in new tables (`classes`, `price_of_type`,
`dcnh_five_ways`, per composition and manifest) and in one trailing report
section. No Batch 7 file under `TABLES/` changes; both reports' Batch 7 text is
byte-identical; receipts 0–7 are byte-identical. `tests/test_08_classes.py`
checks all of this against `3fffd9b`.

## Premises P-A to P-C, restated with committed numbers

| Premise | Directive statement | Committed (pair-seed-17, wide) | Holds |
| --- | --- | --- | --- |
| P-A | Alice-IEE 47 hops / 38 content; Bob 12 weak hops / 0 weak content | Alice hops 47, content 38; Bob conditioning hop 12/12, content 0/0 (N/A) | yes |
| P-B | EIE content = IEE content; EIE hops > IEE hops | content 38 = 38; hops 108 > 47 (`pair-sterile-seed-17`); history totals 148 vs 87 hops | yes |
| P-C | structural coverage satisfied without supplier content; no self use after received | structural 4/12, observed 2/12 (Bob's seats 5, 6 unobserved: Alice has no Ne/Fi content); internalisation 0/45 (Alice), 0/52 (Bob) | yes |

The directive's "87 hops" in P-A was the whole-history count (Alice 47 + Bob 40);
§8.5 names the per-actor numbers, which are the ones tested.

## Findings (seed 17; rows hold at every seed and model)

| History | Actor | Hops | Content | Cond. hop | Cond. content | Hold hop | Hold content | Internalisation | Time | Energy | Greatest all (margin) | Content-only | Hop-only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair | alice (iee) | 47 | 38 | 25/46 | 20/38 | 25/25 | 18/20 | 0/45 | 296 | 253 | H,D (0) | H,D (0) | H,D (0) |
| pair | bob (sli) | 40 | 12 | 12/12 | N/A | 38/40 | 10/12 | 0/52 | 102 | 80 | D (4) | H,D (0) | D (4) |
| pair-sterile | alice (eie) | 108 | 38 | 20/39 | 20/38 | 53/55 | 18/20 | 0/75 | 373 | 437 | H (1) | D,H (0) | C (1) |
| pair-sterile | bob (sli) | 40 | 12 | 12/12 | N/A | 38/40 | 10/12 | 0/52 | 102 | 80 | D (4) | H,D (0) | D (4) |
| legacy-r4 / grade-v1 | alice (iee) | 2 | 4 | 0/1 | N/A | N/A | N/A | N/A | 13 | 23 | H (4) | H (4) | C,H (0) |
| legacy-r4 / grade-v1 | bob (sli) | 17 | 4 | 0/5 | 0/4 | N/A | N/A | N/A | 47 | 67 | H (1) | H (4) | C (3) |
| legacy-r4 / grade-v1 | eve (lie) | 15 | 4 | 0/4 | N/A | N/A | N/A | N/A | 39 | 23 | H (1) | H (4) | D (3) |

Internalisation is **0 in every history under both readings**: a finding, not a
failure. Every delivery history ends inside the collective; no received seat is
revisited self-sourced. Narrow has no received uses, so its class indices are 0
and its hold and internalisation N/A.

Ring and support traffic (pair-seed-17): Alice-IEE 1 mental / 84 vital uses,
support traffic at seats 5 (11) and 6 (16); Bob 40 mental / 12 vital, support
at 5 (4) and 6 (8); Alice-EIE 77 mental / 69 vital, support at 6 (1), 7 (14), 8 (23).

## Tables written

`TABLES/classes.md`, `price_of_type.md`, `dcnh_five_ways.md`;
`TABLES/pair_classes_delivery.md`, `pair_price_of_type_delivery.md`, `pair_dcnh_five_ways_delivery.md`;
`TABLES/pair-sterile_classes_delivery.md`, `pair-sterile_price_of_type_delivery.md`, `pair-sterile_dcnh_five_ways_delivery.md`.
`REPORT.md` and `REPORT_DELIVERY.md` each gain `## 8. Use classes and price of type` (≤ 300 words).
`FIELDS.md` gains the Batch 8 rows; `GLOSSARY.md` ten entries; `LIMITS.md` items 8–10;
`README.md` Findings and appendix; `REPRODUCE.md` and `tools/reproduce.py` run the two class commands.

## Tests

`tests/test_08_classes.py`, 8 tests: alignment and I5 partition on every history;
the directive's probe numbers; observed ≤ structural coverage with Bob's seats
unobserved; internalisation zero everywhere plus a positive and monotone
synthetic witness; margin definition; negatives (forged kind, support seat
outside 5–8, forged energy, swapped element, truncated sequence, count
mismatch); Batch 7 artifacts byte-identical; rendered cells recomputed.

## Proving command

```
python tools/reproduce.py && python -m unittest discover -s tests -v && python tools/path_check.py
```

Staged-tree gate (`REPRODUCE_BASE_TREE` = staged tree, A5/Batch 7 practice): the
first run failed in `test_08_classes.test_07` because the generators rewrite the
reports before the suite runs and the Batch 8 section is appended only afterwards;
the test was corrected to require the Batch 7 text as a prefix either way. The
second staged run passed every Batch ≤ 8 test (44); its only error was the Batch 9
test module, written into the working tree during the run, failing on a manifest
that did not yet exist. The acceptance run was therefore repeated on the committed
tree in a clean worktree.

## Committed-tree reproduction (accepted)

Commit `7ab5338` ("batch 8: use classes, observed supply, DCNH margin, price of type"),
checked out alone in a fresh worktree with only `engine_path.txt` added:

```
PASS: python -S -m unittest tests.test_00_setup -v
PASS: python -S generate/histories.py
PASS: python -S generate/histories_delivery.py
PASS: python -S -m unittest discover -s tests -v
PASS: python -S -m conditioning_v2.tables
PASS: python -S -m conditioning_v2.tables --histories HISTORIES_DELIVERY.json
PASS: python -S -m conditioning_v2.classes
PASS: python -S -m conditioning_v2.classes --histories HISTORIES_DELIVERY.json
REPRODUCED: 20 files identical
PATHS: clean
```

44 tests, OK; 756.5 s on the recorded environment (Python 3.13.16 here; the
runner and tests are version-independent within 3.12–3.13). Batch 8 accepted.

