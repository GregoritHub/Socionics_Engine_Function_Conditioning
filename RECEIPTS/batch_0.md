# Batch 0 receipt

Date: 20 October 2026 (America/New_York).
Batch: 0 — setup, field declaration, invariance witness.
Status: ACCEPTED locally; first proving attempt passed with 3 tests and OK.

## Starting state and scope

- Read repository: https://github.com/GregoritHub/Socionics_Engine
- Read clone commit: `fdede6f16721f06422d0798a79d84170969b83f8`.
- Write repository: https://github.com/GregoritHub/Socionics_Engine_Function_Conditioning
- The write repository cloned successfully but was empty: no commits, no receipts,
  and no `BATCH_DIRECTIVE_Function_Conditioning_v1.md`. Git printed:
  `warning: You appear to have cloned an empty repository.`
- Used the user's attached `BATCH_DIRECTIVE_Function_Conditioning_v1.md`.
  SHA-256: `db1e275a137b10025e6079e8d7cb35e5cb4f07c698a3018715e0081179705199`.
  Its exact bytes are retained between the `BEGIN SUPPLIED DIRECTIVE` and
  `END SUPPLIED DIRECTIVE` HTML comment markers in README.md. Future sessions
  read that source appendix because the named root directive file was absent.
  This uses only the files Batch 0 permits.
- The user's explicit session instruction authorizes a recurring assistant session
  every four hours; each session executes exactly one batch. It does not authorize
  GitHub Actions or other independent repository writers. The schedule is created
  after the Batch 0 publication attempt, as requested.

## Deliverables and findings

- README.md records the pinned engine commit, setup and source directive.
- Ignored engine_path.txt points to the absolute sibling read-clone path.
  After a fresh clone, recreate this local path file; do not commit it.
- .gitignore contains engine_path.txt, __pycache__/, *.pyc, OUT/.
- ENGINE_FREEZE.sha256 lists all 206 files under hle_unified/ and
  baseline/HLE_Rebuild_R21B/hle/, including both source sets in full.
  File paths are relative to the read clone; manifest size is 21,771 bytes.
- FIELDS.md covers the raw fields read by both audits, the revision metadata,
  every blocks(d) value, and the input-revision provenance join.
- The third blocks(d) tuple entry is energy or None, not seat. The seat is derived
  from TIM and element. The source index uses zero-based seats for table lookup;
  Model A public positions are 1–8.
- The requested hle_unified/world_records.py is absent. Read the actual legacy
  baseline/HLE_Rebuild_R21B/hle/world_records.py, native hle_unified/records.py,
  and hle_unified/compact.py. The legacy message schema is not the native schema.
- Revision-level provenance is structurally resolved: an exact input ObjectRef
  joins to the matching committed version.ref and its enclosing Transaction.actor.
  FIELDS.md records exact source lines, nullable actors, semantic source.N versus
  broader input.N, and the distinction from writer and revision lineage. No
  generated-history delivery or per-block source attribution is claimed in Batch 0.
- tests/test_00_setup.py contains exactly three tests and the exact R2 preamble.
  Bytecode writes are disabled before engine imports so the read clone gains no
  cache files. The freeze check compares the complete file set as well as hashes.
- No read-repository files were copied into the write repository, no engine
  behavior was edited, and no engine code imports this project.

## Proving command

Run from the write repository:

```sh
python -m unittest tests.test_00_setup -v
```

Complete combined output of attempt 1:

```text
test_01_imports_resolve_to_read_clone (tests.test_00_setup.SetupTests.test_01_imports_resolve_to_read_clone) ... ok
test_02_every_frozen_file_is_unchanged (tests.test_00_setup.SetupTests.test_02_every_frozen_file_is_unchanged) ... ok
test_03_no_reverse_import_reference (tests.test_00_setup.SetupTests.test_03_no_reverse_import_reference) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.056s

OK
```

Exit status: 0.
Pass line recorded: `OK`; test count: 3.
Failed proving attempts: 0. Repair attempts: 0.

## Commit and continuation

Commit message: `batch 0: setup, FIELDS.md, engine freeze`.
Only the Batch 0 allowlist is staged; .gitignore is explicitly permitted by Batch 0.
All committed files are small UTF-8 text and below 200,000 bytes. Engine source
files remain only in the read clone; the freeze contains hashes and paths only.

This receipt and its deliverables are committed together after the successful
proof. The subsequent push result is reported to the user; a refusal will be
added verbatim to this receipt and committed alone, with no push retry this session.

Next eligible batch: 1. It has not been started. Batches 1–5 were not executed in
this session. At the next session, read all receipts before consulting the supplied
directive source in README.md. A prior R9 stop takes precedence over continuation.

## Publication refusal (R5)

Local accepted batch commit: `8b60aec44241ea28e9d558a04056494546da0690`.

Command:

```sh
git push -u origin main
```

Complete output (verbatim):

```text
fatal: could not read Username for 'https://github.com': No such device or address
```

Exit status: 128.

The terminal has no usable GitHub username/credential for this push. Local
acceptance is unchanged. No alternate publication route or push retry was attempted
this session. This refusal is added to the receipt and committed as a receipt-only
follow-up under R5. Remote publication is NOT complete; the GitHub repository has
no Batch 0 receipt from this session.

Local write clone: /workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning
Local read clone: /workspace/scratch/d5be342785cd/Socionics_Engine

If this local clone survives, its committed receipts establish Batch 0 acceptance.
If it does not survive and GitHub is still empty, do not assume its receipt or the
source directive can be recovered from GitHub. Report the actual missing source
state. The requested four-hour schedule is still to be created after this R5 record;
no later batch is executed now.

## Publication resolved — 20 October 2026

The user separately authorized fixing GitHub saving for the existing Batch 0
commits, verifying the upload, and stopping. This is publication repair only;
Batch 1 was not started and the original engine remains read-only.

Both existing snapshots were published through the connected GitHub app, with
their exact file bytes and original order preserved. Terminal Git authentication
was not installed or changed. The API publication has different commit IDs:

| Original local commit | Published commit | Identical Git tree |
| --- | --- | --- |
| `8b60aec44241ea28e9d558a04056494546da0690` | `8df3b74eddf70fb139e3c1916d298224f58441bc` | `e4d89252ed040c77a6a864e050b9594395ddc15c` |
| `73296a64c2e728539869cd91d33d1132fe8d5acc` | `361f2e6445b89bad0e2530bcb93f105249041547` | `7306d48bdf8c9e1d826a0f540d940d84d87699d1` |

The empty repository was initialized with the existing .gitignore only, at
`ac10116c322d93430814451a1e34ac707b4b119d`, before publishing those two commits.
The main ref update was a fast-forward with the expected previous head, never a
force push. The remote main ref and complete six-file tree were read back through
GitHub, and `git fetch origin main` downloaded the actual published objects.
For each snapshot, every path, mode, blob ID, and file byte matched its local
original. Both Git tree hashes above matched exactly. All 206 frozen engine files
were unchanged, and the read clone's working tree was clean.

The earlier refusal section is retained as historical evidence; its statement
that publication was incomplete is superseded by this resolution. This final
receipt-only note records the repair. The two accepted snapshots above retain
their original bytes. The four-hour schedule was created in the initial session
and was not modified during publication repair. Next eligible batch remains 1;
this repair session stops without executing it.
