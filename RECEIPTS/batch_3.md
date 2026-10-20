# Batch 3 receipt — retention (same-seat repeat)

Date: 20 October 2026 (America/New_York).
Status: ACCEPTED on the first proving attempt under Amendment A2.
Failed proving attempts under the fresh allowance: 0. Repair attempts: 0.

## Cleared by Amendment A2

The author explicitly authorized the restated I4 and a fresh two-failure
allowance in this session. The fixed definition of kept is unchanged. A kept
use remains True when a history grows; an existing False use may become True.
The last use at each (actor, seat, element) is False, including the ordinary
sequence ending [..., True, False]. The original cross-record monotonicity
requirement was contradictory and is superseded by A2.

Current GitHub main was read through both a fresh clone and the connected
GitHub app at `4ab98a1474ce1e2f5475bc84f16e2063a534691b`. Contrary to the
session's statement that A2 was already committed, that head contained only
v1.2, A1, and receipts 0–2. No Batch 3 receipt or implementation existed.
This session therefore preserves the supplied A2 file verbatim at the write
repository root and incorporates its exact ruling in README's v1.3 appendix.
A2 SHA-256: `b55143c30bd210bfe1771b5c11decd60d74ad15c2ae33ea854d41aaca349002f`.
No other directive rule is changed. This is execution of the author's ruling,
not a new theoretical interpretation or a repair counted against R9.

The historical Batch 2 R9 record is retained. Its later section headed
`Cleared by Amendment A1` records acceptance; no fresh Batch 2 stop exists.
All current receipts were consulted. Only Batch 3 is executed this session.

## Inputs and read-repository protection

The original engine remains at
`fdede6f16721f06422d0798a79d84170969b83f8`, clean and unchanged.
The existing read clone is imported by absolute path through the ignored
engine_path.txt; the sibling path points to that same read clone. No files are
copied out of it, and no engine commits, pushes, or behavior edits are made.
Bytecode writes are disabled before every engine import.

The eight surviving generated checkpoints match every SHA-256 in the accepted
HISTORIES.json. The accepted generator, manifest, and Batch 2 adapter bytes are
unchanged. Tests restore all eight with the native codec, verify byte-exact
re-checkpointing, and check the accepted transaction counts. OUT contains only
ignored local references to those checkpoints; none are committed. Neither
Batch 1 nor Batch 2 is rerun as a new batch.

## Implementation and R6 declaration

`conditioning_v2.retention.uses(transactions)` returns the existing Batch 2
records, in the same order, with one added Boolean field: `kept`. It calls the
unchanged Batch 2 adapter, which in turn validates completed paid work against
the engine auditor. It does not introduce another completion-counting rule.

After validating journal order, a reverse walk records whether a later use
exists for the exact (actor, seat, element). The operation is local to one
function call/history. No input transaction or engine state is changed. Paid
blocks within a transaction retain the canonical engine block sequence; an
earlier block can be kept by a later block at the same seat. The last block
at that actor/seat/element remains False. Becoming a capability or another
seat's use does not retain the earlier seat's use.

R6 required declaring an additional input before using it: Transaction.at.tick
and Transaction.at.order. Read the pinned Moment and Transaction definitions,
CompactStore.commit, and CompactStore.restore. The native store commits and
restores `Moment(journal_index, 0)`. Added that exact meaning and source lines
to FIELDS.md before implementing the checks. No new raw engine field is added.
The test suite exercises both valid values and forged tick/order values.

A replayed exact version reference raises DuplicateTransactionError. A history
whose transaction moments differ from the original zero-based committed order
raises TransactionOrderError. Reordered inputs are rejected, never sorted into
an apparently valid retention result. These checks accept a complete journal
or a prefix starting at its beginning.

## Witnesses

All six test methods exercise all eight accepted histories:

1. Compute kept on the first half of transactions and on the whole, matching
   every prefix occurrence to the same occurrence in the whole and asserting
   prefix True implies whole True. Because the inspected first-half prefix
   contains setup rather than paid work, also check the prefix ending at the
   first paid transaction. That additional prefix must contain at least one
   already-True use and an actual False-to-True extension witness in every history.
2. Preserve all Batch 2 fields and occurrence order exactly. Each repeated
   actor/seat/element group is True on every use except the final False. Check
   every use again against the independent forward-existential definition.
3. Construct an in-memory test prefix with paid completion cut after the first
   two distinct seats, adjusting the exact wallet debit for the active resource
   model. Both seats occur once and both are False. Removing payment evidence
   is rejected by the existing paid-work auditor. This synthetic witness does
   not replace or modify any accepted history, generator, or checkpoint.
4. Replay a paid transaction; require DuplicateTransactionError.
5. Find a same-actor, same-seat, same-element repeat in a later transaction and
   move that transaction before its earlier use; require TransactionOrderError.
6. Check the declared committed moments and reject forged tick and order values.

The earlier Batch 2 finding remains: **no cross-actor delivery observed in
generated histories**. Retention does not turn world sources into actor sources.
A cross-actor fixture replacement still needs the separate ruling named in A1.

## Required proving command

Run from the write repository:

```sh
python -m unittest tests.test_03_kept -v
```

Complete combined stdout/stderr of fresh attempt 1:

```text
test_01_i4_first_half_and_nonempty_paid_prefix_on_every_history (tests.test_03_kept.KeptTests.test_01_i4_first_half_and_nonempty_paid_prefix_on_every_history) ... ok
test_02_repeated_seats_are_true_except_last_and_preserve_batch2 (tests.test_03_kept.KeptTests.test_02_repeated_seats_are_true_except_last_and_preserve_batch2) ... ok
test_03_unique_seats_are_false_and_missing_payment_is_rejected (tests.test_03_kept.KeptTests.test_03_unique_seats_are_false_and_missing_payment_is_rejected) ... ok
test_04_forged_duplicate_transaction_is_rejected (tests.test_03_kept.KeptTests.test_04_forged_duplicate_transaction_is_rejected) ... ok
test_05_repeat_moved_before_earlier_use_is_rejected (tests.test_03_kept.KeptTests.test_05_repeat_moved_before_earlier_use_is_rejected) ... ok
test_06_declared_moment_fields_and_forged_moments (tests.test_03_kept.KeptTests.test_06_declared_moment_fields_and_forged_moments) ... ok

----------------------------------------------------------------------
Ran 6 tests in 34.344s

OK
```

Exit status: 0. Pass line: `OK`. Test count: 6.
No failed proving attempt and no repair attempt occurred.

## Final invariance command

```sh
python -m unittest tests.test_00_setup -v
```

Complete combined stdout/stderr after the Batch 3 proof:

```text
test_01_imports_resolve_to_read_clone (tests.test_00_setup.SetupTests.test_01_imports_resolve_to_read_clone) ... ok
test_02_every_frozen_file_is_unchanged (tests.test_00_setup.SetupTests.test_02_every_frozen_file_is_unchanged) ... ok
test_03_no_reverse_import_reference (tests.test_00_setup.SetupTests.test_03_no_reverse_import_reference) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.058s

OK
```

Exit status: 0. All 206 frozen files and the exact frozen file set still match;
engine imports resolve to the pinned read clone and reverse-import checks pass.
The engine's final git status is empty and its HEAD remains the pinned commit.

## Commit, publication, and next session

Commit message: `batch 3: retention (same-seat repeat)`.
Files: conditioning_v2/retention.py, tests/test_03_kept.py, this receipt,
FIELDS.md (R6), DIRECTIVE_AMENDMENT_A2_I4_monotone.md, and README.md (A2/v1.3).
All are allowed UTF-8 text files below 200,000 bytes. No engine source, journal,
checkpoint, workflow, archive, feedback, pricing, or behavioral change is staged.

A terminal commit is made after acceptance. Publication uses the previously
user-authorized connected GitHub route, with the observed main as parent and
an expected-head, non-forced ref update. The remote tree is checked against the
local committed tree. This pre-publication receipt does not preclaim that a
pending network operation succeeded; any refusal is recorded under R5 without
an alternate publication retry in this session.

Next eligible batch: **Batch 4**, in a separate session. It is not started here.
