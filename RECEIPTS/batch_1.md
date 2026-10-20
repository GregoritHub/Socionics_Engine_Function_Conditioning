# Batch 1 receipt — generated histories

Date: 20 October 2026. Status: ACCEPTED locally on the first proving attempt.
Failed proving attempts: 0. Repair attempts: 0.

## Fresh preflight

Read the current README.md operative directive, every existing receipt (Batch 0),
FIELDS.md, the complete ENGINE_FREEZE.sha256, and the read repository AGENTS.md.
The explicit observation-only Batch 1 instruction governs this companion work;
the original engine's separate build instructions do not authorize writes there.
No applicable AGENTS.md exists in the write repository. No prior R9 stop exists.
Starting published head: `4a77b534c29f20130025262c5b45475b3db35cf2`.
The read clone is clean at `fdede6f16721f06422d0798a79d84170969b83f8`.
Runtime: Python 3.12.14. All 206 frozen files and the exact file set matched.
`python -m unittest tests.test_00_setup -v` passed all 3 tests before generation
(0.059s) and again after generation (0.069s), including reverse-import absence.

No other local batch worker was visible. Remote main remained at the starting
head on repeated checks. The read-only automation lookup exposed no automations
in this session; this is not a claim that the previously reported schedule was
removed. The supplied next start was 06:58 America/New_York, later than this run.
No schedule was created or changed. No concurrent work was observed.

## Generated histories

Read docs/examples/first_run.py end to end, and both named population fixtures.
Use their public fixture/engine APIs by path. The generator constructs prepared
workflow populations, with Alice=IEE, Bob=SLI, Eve=LIE; IEE/SLI is the dual pair.
The third actor already exists in the public fixture. Its initial profile is
supplied before engine creation and before paid work, following the public
population fixture's initial-profile pattern. No running engine or source is edited.
The energy fixture selects the resource model at initial engine creation.

Seeds 17, 29, 43, 61 each select task counts from 2/4/8 and shuffle owned requests;
the same seeds and initial budgets are used in legacy-r4 and grade-v1.
Each population uses the existing scheduler with 3 maximum episodes, quantum 128,
and repeat limit 2. The guard allows at most 10,000 turns and rejects an unfinished
world. All eight worlds stopped naturally at 18 turns, 2 episodes per actor,
with `unchanged_retained_result` for every actor. Each journal has 216 transactions.
Every history has completed paid-use totals Alice=6, Bob=21, Eve=19 as reconstructed
by conditioning_audit.completed_use. These are supplied scenarios, not historical
archives or evidence of spontaneous demand formation.

The engine's Population checkpoint codec preserves its engine journal and finite
scheduler state. All eight hashes are distinct. Checkpoints remain ignored in
OUT/; only hashes and summaries appear in HISTORIES.json. The tests restore every
checkpoint, compare its exact bytes and SHA-256, verify the manifest against the
restored journal, check terminal step stability, and regenerate all eight worlds
from scratch to identical bytes. Positive routed paid work is present. Negative
witnesses remove wallet evidence or forge its energy debit, and the unchanged
conditioning auditor rejects both under both models. The dual-pair witness checks
leading/creative to suggestive/mobilizing element correspondence in both directions.

## Required proving command

```sh
python generate/histories.py && python -m unittest tests.test_01_histories -v
```

Full combined output, attempt 1:

```text
legacy-r4-seed-17: finite stop; 216 transactions
legacy-r4-seed-29: finite stop; 216 transactions
legacy-r4-seed-43: finite stop; 216 transactions
legacy-r4-seed-61: finite stop; 216 transactions
grade-v1-seed-17: finite stop; 216 transactions
grade-v1-seed-29: finite stop; 216 transactions
grade-v1-seed-43: finite stop; 216 transactions
grade-v1-seed-61: finite stop; 216 transactions
HISTORIES.json: 8 entries
test_01_manifest_matched_seeds_types_and_dual_pair (tests.test_01_histories.HistoryTests.test_01_manifest_matched_seeds_types_and_dual_pair) ... ok
test_02_restore_hash_paid_use_finite_stop_and_regeneration (tests.test_01_histories.HistoryTests.test_02_restore_hash_paid_use_finite_stop_and_regeneration) ... ok
test_03_missing_and_forged_paid_evidence_rejected (tests.test_01_histories.HistoryTests.test_03_missing_and_forged_paid_evidence_rejected) ... ok

----------------------------------------------------------------------
Ran 3 tests in 72.928s

OK
```

Exit status: 0. Acceptance: OK and 8 manifest entries.

## Commit scope and stopping point

Only generate/histories.py, HISTORIES.json, tests/test_01_histories.py, and this
receipt are committed. Each is UTF-8 text under 200,000 bytes. No source copies,
raw journals, checkpoints, private execution data, or credential material are
published. The ignored engine_path.txt was recreated for local imports.
Bytecode writing is disabled before importing the engine.
Commit message: `batch 1: generated histories manifest`.

Publication uses the user-authorized connected GitHub route after the local
terminal commit, with the starting head as the expected parent and a non-forced
ref update. Its outcome and remote tree verification are reported to the user;
this pre-publication receipt does not claim that a pending network action succeeded.
No terminal credential setup or known-failing terminal push is attempted.
Stop after saving and verifying Batch 1. Batch 2 was not executed.
