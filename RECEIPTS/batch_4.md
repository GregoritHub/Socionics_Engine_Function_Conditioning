# Batch 4 receipt — measures and tables

Date: 20 October 2026 (America/New_York).
Status: ACCEPTED on the first proving attempt.
Failed proving attempts: 0. Repair attempts: 0.

## Starting state and authority

Starting published main: `8f7c54d985def554868b58c9ed45191f3661d823`.
Fetched current main and checked the current receipts and operative v1.3
appendix. Batch 3 is accepted under A2. The original Batch 2 R9 failure record
is historical and explicitly cleared by its A1 acceptance section. There is
no uncleared R9 stop. No Batch 4 receipt existed. This session executes only
Batch 4; Batch 5 is not started.

The read clone remains clean at
`fdede6f16721f06422d0798a79d84170969b83f8`. Imports are by path with the exact
R2 preamble; bytecode writing is disabled before engine imports. No file from
the engine is modified, copied, committed, or published. Accepted checkpoints
are read from ignored OUT paths and verified against HISTORIES.json. Both the
table command and tests restore all eight through the native codec and verify
byte-exact re-checkpointing, transaction counts, and actor/TIM declarations.
The generator, manifest, Batch 2 adapter, and Batch 3 retention are unchanged.

## Implementation

Created conditioning_v2/measures.py, conditioning_v2/tables.py,
tests/test_04_measures.py, and the three named Markdown tables. Added R6 field
declarations in FIELDS.md before implementing the additional input reads.

The measures consume the unchanged Batch 3 use records. Use IDs are occurrence
indices, not deduplicated record values, and trace to the transaction index,
exact operation revision, and completed block boundary. All-use DCNH is
reconstructed from those records with the kernel's axis/formula functions and
checked for exact equality to the FULL Phase 7 observations row for every
actor. The second view includes only actor-sourced uses with kept=True.
No type assignment, executor hook, feedback, pricing, or selection is added.

Per-actor output includes source/seat/kept use bins, source-scoped conditioning
and hold ratios, every weak seat's supplier map, and the complete use trace.
Per-population output includes coverage, cumulative coverage by actor-local
episode index, supplier concentration (HHI), all ordered pairs with directional
relation labels and sterility, and benefit-family pair subsets within the triad.

R6 additions are the explicit Population.events actor/key/episode fields,
additional use of the already-declared operation key, stable actor display ID
fields, and the kernel label JSON relation/landing-permutation fields. Episode
joins use exact actor and declared request/job keys, never guessed name digits.
Every paid block must have an episode attribution. Missing or conflicting
joins are rejected. Cumulative episode coverage pools each actor's uses through
that actor-local index; it is not a chronological whole-world snapshot.

Relation labels are read by path from the pinned kernel relation_labels.json,
not copied into this project. All 256 entries' landing permutations are checked
against hle.relations. The source's direction convention is retained: benefit
on sender:receiver means sender is the benefactor. benefit_inverse is separate.

## Scope limitations and findings (not proving failures)

### A1-literal conditioning denominator

The original Batch 4 formula says received weak-seat uses / all weak-seat uses.
A1 subsequently restricts conditioning-index inputs to actor-id sources only
and says world uses appear only in the use profile and all-use DCNH. Applying
that restriction literally to BOTH index counts makes numerator and denominator
identical: the index is 1 whenever defined and N/A when empty. The implementation
and table label explicitly say `Conditioning (A1 literal)`; they do not silently
use the older all-source denominator. A source-scope ruling is needed if a
nondegenerate original-formula index is intended. No new amendment is invented.

Every actual actor/history row has 0/0 (N/A) for that scoped index and for hold.
Supplier HHI is likewise 0/0 (N/A). These are not reported as measured zeros.
Zero received uses remain an observed finding, not a reason to replace fixtures.

### No standalone pair experiment

HISTORIES.json contains only three-actor histories. The pair-subset counts shown
are delivered uses between two actors WITHIN their triad. Standalone two-actor
comparison is explicitly `N/A: not generated`. A zero in the within-triad pair
column is not treated as the result of an unrun pair experiment. Neither the
generator nor accepted population sizes are altered under this batch.

### Generated-history results

Each of eight histories has three active actors, zero actor-sourced received
uses, coverage 0/12, six sterile ordered pairs, and zero benefit-family received
uses. Cumulative coverage is 0/12 through both recorded episode indices 0 and 1.
All 24 actor/history comparisons are `diverge`: all-use DCNH is nonzero, while
received-and-kept DCNH is zero and ties all cells. This is a comparison of the
observed vectors, not evidence about subtypes or cross-actor conditioning.

The earlier finding remains: **no cross-actor delivery observed in generated
histories**. The all-use count per history is 46 (Alice 6, Bob 21, Eve 19), all
world-sourced, as traceable in per_actor.md and dcnh_two_ways.md. Synthetic test
witnesses below must never be reported as observed generated-history deliveries.

## Required proving command

```sh
python -m conditioning_v2.tables && python -m unittest tests.test_04_measures -v
```

Complete combined stdout/stderr of attempt 1:

```text
TABLES/per_actor.md: 80767 bytes
TABLES/per_population.md: 10549 bytes
TABLES/dcnh_two_ways.md: 9025 bytes
Histories: 8
All-use DCNH exactly matches Phase 7 for every actor.
A1-literal conditioning scope is degenerate; zero denominators are N/A.
Standalone pair comparison unavailable: no pair histories in accepted manifest.
test_01_i5_full_observation_equals_phase7_on_every_actor_history (tests.test_04_measures.MeasureTests.test_01_i5_full_observation_equals_phase7_on_every_actor_history) ... ok
test_02_twenty_saved_table_cells_recomputed_from_records (tests.test_04_measures.MeasureTests.test_02_twenty_saved_table_cells_recomputed_from_records) ... ok
test_03_positive_supplier_coverage_hold_concentration_and_inactive (tests.test_04_measures.MeasureTests.test_03_positive_supplier_coverage_hold_concentration_and_inactive) ... ok
test_04_inactive_history_appears_in_rendered_denominators (tests.test_04_measures.MeasureTests.test_04_inactive_history_appears_in_rendered_denominators) ... ok
test_05_missing_or_forged_measure_inputs_are_rejected (tests.test_04_measures.MeasureTests.test_05_missing_or_forged_measure_inputs_are_rejected) ... ok
test_06_episode_join_has_positive_and_negative_witnesses (tests.test_04_measures.MeasureTests.test_06_episode_join_has_positive_and_negative_witnesses) ... ok
test_07_relation_labels_and_generated_table_artifacts (tests.test_04_measures.MeasureTests.test_07_relation_labels_and_generated_table_artifacts) ... ok

----------------------------------------------------------------------
Ran 7 tests in 34.190s

OK
```

Exit status: 0. Pass line: `OK`. All three named tables exist below 200 KB.
No failed proving command and no repair attempt occurred.

The tests establish exact full-row Phase 7 agreement for every actor/history;
independently recompute 20 saved table cells (six use counts, eight DCNH load
cells, six coverage ratios); exercise nonzero suppliers, coverage, hold, HHI,
and benefit directions using explicit test-only observations; preserve inactive
actors in denominators; reject unknown sources, forged dimensions, non-Boolean
kept, missing fields, and missing/conflicting episodes; verify all relation
landing labels; and check that saved table bytes equal reproducible rendering.

An actual no-paid-use prefix witnesses all three committed actors as inactive,
still yielding the 12-seat denominator and visible inactive labels. A separate
nonzero four-profile test includes an inactive fourth actor in its 16-seat
coverage denominator. These are validation fixtures only, not replacement
published histories. Positive and negative source/episode paths are exercised
rather than relying on all-zero actual received-use data to pass tests.

## Artifact hashes

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `TABLES/dcnh_two_ways.md` | 9025 | `1934a9d4ab9dcfdc382ff74d7c7a6e1491424c989097da1a98324c0037bb63ab` |
| `TABLES/per_actor.md` | 80767 | `a43741f2ebaaa1627c74a9077ca750247c6b81eb4983b0bf41208e0c192bda3b` |
| `TABLES/per_population.md` | 10549 | `26e68f49197c80c9934055061a07a9b986afd496815b99c88b7211a187035913` |

## Final invariance command

```sh
python -m unittest tests.test_00_setup -v
```

Complete combined stdout/stderr after the Batch 4 proof:

```text
test_01_imports_resolve_to_read_clone (tests.test_00_setup.SetupTests.test_01_imports_resolve_to_read_clone) ... ok
test_02_every_frozen_file_is_unchanged (tests.test_00_setup.SetupTests.test_02_every_frozen_file_is_unchanged) ... ok
test_03_no_reverse_import_reference (tests.test_00_setup.SetupTests.test_03_no_reverse_import_reference) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.053s

OK
```

Exit status: 0. All 206 frozen files and the exact file set match; imports
resolve to the pinned engine and reverse-import absence passes. The original
engine's final git status is empty and its HEAD is unchanged.

## Commit and continuation

Commit message: `batch 4: measures and tables`.
Only the seven named Batch 4 files plus FIELDS.md's R6 declarations are staged.
All are permitted UTF-8 text under 200,000 bytes. No checkpoints, raw journals,
engine copies, workflow files, or behaviors are committed.

After the accepted terminal commit, publication uses the previously authorized
connected GitHub route, a non-forced expected-head ref update, and full tree
verification. This pre-publication receipt does not assert that a pending
network action has already succeeded. A refusal would be recorded verbatim under
R5 with no alternate publication retry in this session.

Next eligible batch: **Batch 5 (REPORT.md)**, in a separate session. It must
trace every reported number to these tables and preserve the N/A/zero/absent
experiment distinctions above. No Batch 5 work is performed here.
