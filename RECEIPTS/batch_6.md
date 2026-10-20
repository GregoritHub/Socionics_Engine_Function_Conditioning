# Batch 6 receipt — accepted under A4

Date: 20 October 2026 (America/New_York).
Status: ACCEPTED. Batch 6 Steps 2–4 complete for supported compositions.
Step 1 was accepted by the author and was NOT rerun.
Fresh allowance: one failed proving command, one repair, then a passing command.
No R9 stop remains in this session. Stop after this batch; no feedback is authorized.

## Cleared by Amendment A4

A4 supersedes the A3 guard conflict and clears continuation with a fresh two-failure
allowance. The exact A3 audit candidate is now accepted within the restated guard.
Every earlier stopped/blocked instruction in this receipt's historical appendix
is superseded by this section and the successful proofs below.

The owner explicitly authorized external publication of all directive deliverables
to https://github.com/GregoritHub/Socionics_Engine_Function_Conditioning in this
session. This is the new publication authority requested by A4; no permission or
policy setting was changed. Previously refused receipt bytes/commits are not
replayed as ancestors.

## Starting state and durable authority

Published main was verified at `3ac82ebabfe313c93272978d063e37162b824755`, still
Batch 5. Contrary to the prompt's stated remote state, A3, A4, Batch 6 and README
v1.6 were absent there. The supplied attachments and explicit session rulings
authorize this work. Their exact files are preserved at the root, including the
original named directive that was formerly only in README. README now records
v1.6 and makes the linked rulings' precedence explicit over its historical text.

The earlier A3 local candidate and sanitized receipt/probe survived and were
recovered. The candidate SHA-256 is
`b2ee1cbb507ae7bfc5ed5f08dd6937dd64f962d56f9a17590d995e61d2442a8d`.
Eight surviving Batch 1 checkpoints matched every accepted manifest digest.
The ignored local engine_path.txt was recreated; no Batch 1 history generation
was repeated and no accepted history, generator or retention file was edited.

The read repository stayed at `fdede6f16721f06422d0798a79d84170969b83f8`.
No source from it was copied, edited, committed or pushed. All fixture and kernel
code is imported by path. Bytecode writing is disabled before engine imports.
The original engine's unrelated continuous-build instructions do not govern this
observation-only companion or authorize writes there.

## Accepted Step 1 — not rerun

The author accepted `tests_u11.fixtures.circuit11(flat=False)` as the delivery
fixture: 97 of 137 paid uses were tuple-sourced. Its first event was use u40,
transaction 307, Bob=SLI, Te at seat 2 (3D), supplied by Alice=IEE at seat 6,
relation duality. Exact invitation revision 1 was committed by Alice at transaction
302. `chain` had no tuple sources. These are the prior accepted observations, not
new probe executions. The saved probe remains reproducible but was never invoked
or imported in this session. Steps 2–4 use parameterized circuit API calls instead.

## Guard and tuple implementation

Changes outside the exact audit candidate are limited to the A4-authorized
measures, tables, tests 02/04 and the Batch 6 deliverables. Received means a
non-empty tuple. Supplier/pair logic counts once per listed actor; a receiver's
profile, conditioning, hold and coverage count a use once. Supplier HHI normalizes
by total supplier incidences, so multi-supplier shares sum to one. Tuple-aligned
source seats and relations retain per-source validation. The new multi-supplier
witness exercises both incidence counting and single-use receiver counting.

The original A1-literal conditioning denominator remains unchanged and degenerate.
A4 did not authorize redefining it. The report labels it explicitly. Default table
rendering remains byte-identical. The CLI accepts --histories and --suffix;
delivery histories produce the same three table kinds separately per composition
so every file stays below R3's 200,000-byte ceiling.

`tools/guard_batch_6.py` regenerates all original tables and REPORT.md from
HISTORIES.json and restored journals. Its report renderer retains the accepted
prose template, derives every numeric table row, verifies numeric prose and the
all-world/zero-delivery claims, then compares bytes and fixed SHA-256 digests.
It does not use REPORT.md as its generation template. The original negative
witnesses remain active, including provenance/seat forgeries, replay/reordering,
measure-input forgeries, non-Boolean kept, and missing/conflicting episodes.

Command from `<write>`:

```sh
set -o pipefail
PYTHONDONTWRITEBYTECODE=1 python tools/guard_batch_6.py 2>&1 | tee OUT/guard_a4_identity.log
```

Complete output:

```text
BYTE-IDENTICAL: TABLES/per_actor.md a43741f2ebaaa1627c74a9077ca750247c6b81eb4983b0bf41208e0c192bda3b
BYTE-IDENTICAL: TABLES/per_population.md 26e68f49197c80c9934055061a07a9b986afd496815b99c88b7211a187035913
BYTE-IDENTICAL: TABLES/dcnh_two_ways.md 1934a9d4ab9dcfdc382ff74d7c7a6e1491424c989097da1a98324c0037bb63ab
BYTE-IDENTICAL: REPORT.md 530f1bd6c16e800362f130d1020ef2ed7f50d779f2ea1524a6323b6c1e4bf55a
PASS: 8 accepted histories retain self/world-only sources and exact I5 counts.
PASS: accepted generator, manifest, retention, tables and report bytes unchanged.
```

Exit status: 0.

Command:

```sh
set -o pipefail
PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_02_fields tests.test_03_kept tests.test_04_measures -v 2>&1 | tee OUT/guard_a4_tests.log
```

Complete output:

```text
test_01_i1_i2_i3_i5_on_every_history (tests.test_02_fields.FieldTests.test_01_i1_i2_i3_i5_on_every_history) ... ok
test_02_self_actor_and_world_source_adapters (tests.test_02_fields.FieldTests.test_02_self_actor_and_world_source_adapters) ... ok
test_03_unknown_provenance_actor_is_rejected (tests.test_02_fields.FieldTests.test_03_unknown_provenance_actor_is_rejected) ... ok
test_04_element_seat_contract_forgery_is_rejected (tests.test_02_fields.FieldTests.test_04_element_seat_contract_forgery_is_rejected) ... ok
test_01_i4_first_half_and_nonempty_paid_prefix_on_every_history (tests.test_03_kept.KeptTests.test_01_i4_first_half_and_nonempty_paid_prefix_on_every_history) ... ok
test_02_repeated_seats_are_true_except_last_and_preserve_batch2 (tests.test_03_kept.KeptTests.test_02_repeated_seats_are_true_except_last_and_preserve_batch2) ... ok
test_03_unique_seats_are_false_and_missing_payment_is_rejected (tests.test_03_kept.KeptTests.test_03_unique_seats_are_false_and_missing_payment_is_rejected) ... ok
test_04_forged_duplicate_transaction_is_rejected (tests.test_03_kept.KeptTests.test_04_forged_duplicate_transaction_is_rejected) ... ok
test_05_repeat_moved_before_earlier_use_is_rejected (tests.test_03_kept.KeptTests.test_05_repeat_moved_before_earlier_use_is_rejected) ... ok
test_06_declared_moment_fields_and_forged_moments (tests.test_03_kept.KeptTests.test_06_declared_moment_fields_and_forged_moments) ... ok
test_01_i5_full_observation_equals_phase7_on_every_actor_history (tests.test_04_measures.MeasureTests.test_01_i5_full_observation_equals_phase7_on_every_actor_history) ... ok
test_02_twenty_saved_table_cells_recomputed_from_records (tests.test_04_measures.MeasureTests.test_02_twenty_saved_table_cells_recomputed_from_records) ... ok
test_03_positive_supplier_coverage_hold_concentration_and_inactive (tests.test_04_measures.MeasureTests.test_03_positive_supplier_coverage_hold_concentration_and_inactive) ... ok
test_04_inactive_history_appears_in_rendered_denominators (tests.test_04_measures.MeasureTests.test_04_inactive_history_appears_in_rendered_denominators) ... ok
test_05_missing_or_forged_measure_inputs_are_rejected (tests.test_04_measures.MeasureTests.test_05_missing_or_forged_measure_inputs_are_rejected) ... ok
test_06_episode_join_has_positive_and_negative_witnesses (tests.test_04_measures.MeasureTests.test_06_episode_join_has_positive_and_negative_witnesses) ... ok
test_07_relation_labels_and_generated_table_artifacts (tests.test_04_measures.MeasureTests.test_07_relation_labels_and_generated_table_artifacts) ... ok

----------------------------------------------------------------------
Ran 17 tests in 96.142s

OK
```

Exit status: 0. All 17 tests passed before composition generation. The identity
and exact I5 guard also ran again as Batch 6's first test after the repair.

## Composition calls, parameters and limitations

`generate/histories_delivery.py` follows the accepted circuit's existing APIs,
without calling circuit11() or chain() as a new Step 1 probe. Every history's
manifest records 21 exact fixture invocations: setup11, the child group/repair
program and run, retain, the circuit's existing paid damage action, root group,
Bob's join, the supplied team program, execution, retention and summaries.
Record handles are represented by exact identity@revision; OperationRequest's
complete repr retains all constructor arguments. Internal calls remain the
unchanged pinned fixture implementation.

| Composition | setup11 tim | Active collective people | Background profile | Outcome |
| --- | --- | --- | --- | --- |
| pair | iee | Alice=IEE, Bob=SLI | Eve=SLI, inactive | produced |
| pair-sterile | eie | Alice=EIE, Bob=SLI | Eve=SLI, inactive | produced |
| triad | requested IEE/SLI/LIE | not constructible with allowed calls | Bob/Eve fixed SLI | not producible |

Both produced compositions use seeds 17, 29, 43, 61, legacy-r4, one declared
harness episode including setup, and budgets `2000000 + 1000 * seed`. The fixture
has no seed input: only the nonbinding budget varies, not the deterministic work
program. It has no Population quantum parameter. Its common work limits are
ordinary fixture perform=100, collective work=10000000, physical-step advance=1000.
These exact limits are recorded rather than pretending a scheduler was used.
No runtime type/profile patch, actor removal, engine monkeypatch, new demand rule,
or synthetic delivery was used to make the requested compositions appear feasible.

Group/join set collective membership; they do not erase the fixture's inactive
Eve profile or alter TIMs. Therefore these are two-participant collectives within
three-profile worlds. Coverage retains Eve's weak seats. The requested IEE/SLI/LIE
triad cannot be produced because setup11 forwards tim to Alice only and setup5
hardcodes Bob and Eve as SLI. Its unavailability is explicit, not a zero result.
The conflict choice comes from Batch 6's supplied sterile example. No separately
identifiable yield-table artifact was located in the pinned engine, so no such
independent lookup is claimed.

The manifest's event records explicitly assign operation actor/key pairs to the
single harness episode 0. They are NOT Population scheduler events or episodes
inferred from key digits. Identical event sets are stored once in ordinary JSON,
referenced and SHA-256 verified by the loader. This adds no raw transaction field.
Checkpoints use the native OperationStore codec, remain ignored, and are restored
and re-encoded byte-exactly by the tests and tables.

## Full Batch 6 proving command — attempt 1

```sh
set -o pipefail
(PYTHONDONTWRITEBYTECODE=1 python generate/histories_delivery.py && PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_06_delivery -v && PYTHONDONTWRITEBYTECODE=1 python -m conditioning_v2.tables --histories HISTORIES_DELIVERY.json) 2>&1 | tee OUT/batch_6_a4_attempt_1.log
```

Complete output, paths normalized and traceback trimmed under A3:

```text
pair-seed-17: 447 transactions; 97 received; coverage 4/12 = 1/3
pair-seed-29: 447 transactions; 97 received; coverage 4/12 = 1/3
pair-seed-43: 447 transactions; 97 received; coverage 4/12 = 1/3
pair-seed-61: 447 transactions; 97 received; coverage 4/12 = 1/3
pair-sterile-seed-17: 447 transactions; 127 received; coverage 4/12 = 1/3
pair-sterile-seed-29: 447 transactions; 127 received; coverage 4/12 = 1/3
pair-sterile-seed-43: 447 transactions; 127 received; coverage 4/12 = 1/3
pair-sterile-seed-61: 447 transactions; 127 received; coverage 4/12 = 1/3
  File "<write>/generate/histories_delivery.py", line 286, in main
    raise ValueError("delivery manifest exceeds R3")
ValueError: delivery manifest exceeds R3
```

Exit status: 1. The generated worlds succeeded; the repeated manifest metadata
exceeded R3 before publication. No tests or table command ran in this failed
chain. This counts as the first failed proving command.

### One repair

Shared identical actor/key/episode records in one hash-addressed JSON event set
and serialized ordinary JSON without redundant whitespace. Exact calls, parameter
values, history identities and checkpoint hashes remain represented. Updated the
table loader to verify and resolve this event-set reference. This is lossless JSON
sharing, not an archive or compressed payload. No observation or fixture changed.
The resulting manifest is 61,824 bytes. No further repair was attempted.

## Full proving command — attempt 2

```sh
set -o pipefail
(PYTHONDONTWRITEBYTECODE=1 python generate/histories_delivery.py && PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_06_delivery -v && PYTHONDONTWRITEBYTECODE=1 python -m conditioning_v2.tables --histories HISTORIES_DELIVERY.json) 2>&1 | tee OUT/batch_6_a4_attempt_2.log
```

Complete output:

```text
pair-seed-17: 447 transactions; 97 received; coverage 4/12 = 1/3
pair-seed-29: 447 transactions; 97 received; coverage 4/12 = 1/3
pair-seed-43: 447 transactions; 97 received; coverage 4/12 = 1/3
pair-seed-61: 447 transactions; 97 received; coverage 4/12 = 1/3
pair-sterile-seed-17: 447 transactions; 127 received; coverage 4/12 = 1/3
pair-sterile-seed-29: 447 transactions; 127 received; coverage 4/12 = 1/3
pair-sterile-seed-43: 447 transactions; 127 received; coverage 4/12 = 1/3
pair-sterile-seed-61: 447 transactions; 127 received; coverage 4/12 = 1/3
triad: not producible (fixed Bob/Eve SLI profiles)
HISTORIES_DELIVERY.json: 8 entries; 61824 bytes
REPORT_DELIVERY.md: generated from the delivery observations
test_00_a4_byte_identity_guard (tests.test_06_delivery.DeliveryTests.test_00_a4_byte_identity_guard) ... BYTE-IDENTICAL: TABLES/per_actor.md a43741f2ebaaa1627c74a9077ca750247c6b81eb4983b0bf41208e0c192bda3b
BYTE-IDENTICAL: TABLES/per_population.md 26e68f49197c80c9934055061a07a9b986afd496815b99c88b7211a187035913
BYTE-IDENTICAL: TABLES/dcnh_two_ways.md 1934a9d4ab9dcfdc382ff74d7c7a6e1491424c989097da1a98324c0037bb63ab
BYTE-IDENTICAL: REPORT.md 530f1bd6c16e800362f130d1020ef2ed7f50d779f2ea1524a6323b6c1e4bf55a
PASS: 8 accepted histories retain self/world-only sources and exact I5 counts.
PASS: accepted generator, manifest, retention, tables and report bytes unchanged.
ok
test_01_matched_compositions_codec_calls_and_limits (tests.test_06_delivery.DeliveryTests.test_01_matched_compositions_codec_calls_and_limits) ... ok
test_02_i1_i2_i3_i5_and_real_pair_delivery (tests.test_06_delivery.DeliveryTests.test_02_i1_i2_i3_i5_and_real_pair_delivery) ... ok
test_03_i4_prefix_monotonicity_repeat_duplicate_and_order (tests.test_06_delivery.DeliveryTests.test_03_i4_prefix_monotonicity_repeat_duplicate_and_order) ... ok
test_04_forged_provenance_and_seat_witnesses_still_reject (tests.test_06_delivery.DeliveryTests.test_04_forged_provenance_and_seat_witnesses_still_reject) ... ok
test_05_multi_supplier_counting_and_tuple_negatives (tests.test_06_delivery.DeliveryTests.test_05_multi_supplier_counting_and_tuple_negatives) ... ok
test_06_tables_report_traceability_and_size (tests.test_06_delivery.DeliveryTests.test_06_tables_report_traceability_and_size) ... ok

----------------------------------------------------------------------
Ran 7 tests in 49.416s

OK
TABLES/pair_per_actor_delivery.md: 112930 bytes
TABLES/pair_per_population_delivery.md: 11684 bytes
TABLES/pair_dcnh_two_ways_delivery.md: 8980 bytes
TABLES/pair-sterile_per_actor_delivery.md: 166918 bytes
TABLES/pair-sterile_per_population_delivery.md: 13696 bytes
TABLES/pair-sterile_dcnh_two_ways_delivery.md: 11508 bytes
Histories: 8
All-use DCNH exactly matches Phase 7 for every actor.
A1-literal conditioning scope is degenerate; zero denominators are N/A.
Delivery tables are separated by composition; unavailable compositions remain in the manifest.
```

Exit status: 0. Pass line: `OK` (7 tests); six composition tables exist below
200 KB; REPORT_DELIVERY.md section 1 names and traces an actual delivery event.
The report has six sections, each below 300 words. Its bytes regenerate exactly
from the observed histories, and every reported ratio is recomputed from records.
The acceptance pass occurred in this session before the commit.

## Findings and bounds

At every matched seed, both worlds have 447 transactions. The dual pair has 137
paid uses (Alice 85, Bob 52), of which 97 are received; the conflict pair has 198
(Alice 146, Bob 52), of which 127 are received. Eve has zero paid uses throughout.
Coverage is 4/12 in BOTH compositions, including through episode 0. Thus there is
no coverage difference in this supported comparison. The requested triad contrast
is unavailable; no general third-person-presence conclusion is claimed.

The active conflict pair is not sterile under A3/A4: 52 uses Alice->Bob and 75
Bob->Alice. The dual pair has 52 and 45 respectively. This differs from the
directive's zero-delivery conflict example under the broadened observation rule.
All pairs involving inactive Eve are observed sterile, not intrinsically sterile.
All-use versus received-and-kept DCNH diverges for each active actor; it agrees
for inactive Eve's empty observations. Exact loads/tilts/cells are in the tables.

A3/A4 counts ANY exact operation input, including collective evidence such as an
invitation, and applies that provenance to every paid block in the operation.
It is broader than delivery of a route's semantic content. REPORT_DELIVERY.md
section 6 explicitly records this, budget-only replication, the background actor,
fixed types, degenerate index and lack of feedback or causal learning claims.

## Engine invariance

Command:

```sh
set -o pipefail
PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_00_setup -v 2>&1 | tee OUT/invariance_a4.log
```

Complete output:

```text
test_01_imports_resolve_to_read_clone (tests.test_00_setup.SetupTests.test_01_imports_resolve_to_read_clone) ... ok
test_02_every_frozen_file_is_unchanged (tests.test_00_setup.SetupTests.test_02_every_frozen_file_is_unchanged) ... ok
test_03_no_reverse_import_reference (tests.test_00_setup.SetupTests.test_03_no_reverse_import_reference) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.066s

OK
```

Exit status: 0. All 206 frozen files and the exact frozen file set match. Path
imports and reverse-import absence pass. The read clone's final git status is
empty and HEAD remains the pinned commit. `git diff --check` is clean.

## Artifact and diagnostic hashes

Diagnostics are stored under tools/ and referenced by path/digest, not pasted
inline. The accepted Step 1 probe is archived but unexecuted this session.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `tools/probe_batch_6.py` | 5281 | `049b4b9c1476964fa82bb2b4bfa7f530f76797513c22b3d510bd630aa64fe5cc` |
| `tools/guard_batch_6.py` | 10224 | `d321f41067c2516f6860736cff5e97f28c67e1d38f0341173100a4b3da30e103` |
| `generate/histories_delivery.py` | 18565 | `949b7af86ec980541b4dccda9ca15fa3061290a4187fe25c574e025eaf492f4c` |
| `tests/test_06_delivery.py` | 13027 | `a4489148537e494dcc5e6d9e8de990c1321661bf27ee04460d3b7363d988f26e` |
| `HISTORIES_DELIVERY.json` | 61824 | `537d700be9dc773fe463e9c05537b5df89cd22af7b4a4fd9f285e988aed9acfd` |
| `REPORT_DELIVERY.md` | 6319 | `9d6f4c7b230db41c50d50362d083f0718af7cfdbba288e4d3ab6da8d31f6b6e3` |
| `DIRECTIVE_BATCH_6_cross_actor_delivery.md` | 4274 | `3d900cac9668f022556df461e003423349390c010a60e4c852f7e1fc607085f3` |
| `DIRECTIVE_AMENDMENT_A3_operation_provenance.md` | 4712 | `3bf2ae38a0abf4aa5ce4f85263f02b114582f75f60126221aa0a8227c38360a4` |
| `DIRECTIVE_AMENDMENT_A4_tuple_scope.md` | 4084 | `393811549b63a597722ebc72bbc5910da52e31adba12cd837bd81fec4089ccd4` |
| `TABLES/pair-sterile_dcnh_two_ways_delivery.md` | 11508 | `afd3ce79f3ba892d5f450cd5425b253a88c9ae0650ed35659e22d1415bfe9271` |
| `TABLES/pair-sterile_per_actor_delivery.md` | 166918 | `d21628d41531525b43d399dc1900f8480c3939ba15fa31eba99a1aacff31715a` |
| `TABLES/pair-sterile_per_population_delivery.md` | 13696 | `2df5798c05f342a0f59a2a113eb5fb44853d94e288103ec3e89dc0dcd835645e` |
| `TABLES/pair_dcnh_two_ways_delivery.md` | 8980 | `426ccb93a718ef725413984432ce8ee869037011a1bd61951f6d6683c9deb445` |
| `TABLES/pair_per_actor_delivery.md` | 112930 | `40d360a7001639a628d61423d0f36705e64c76b4dd493d111cab0a191b837e4e` |
| `TABLES/pair_per_population_delivery.md` | 11684 | `7dace5795ef3e1a9fa3620eeb9d6e04f99696dae6af6a4136d4cff9611c870f6` |

## Commit and publication

Commit message: `batch 6: cross-actor delivery compositions`.
Only directive-authorized small UTF-8 text files are included. No raw journals,
checkpoints, archives, engine source copies, or independent writers are committed.
The accepted Batch 1 manifest/generator, retention, original tables and report
remain byte-unchanged. The A3 candidate's exact hash is preserved.

After the local terminal commit, use the previously established connected GitHub
publication route, with the observed remote head as parent and an expected-head,
non-forced main update. Verify the full remote tree against the local accepted
tree. This receipt records acceptance before that network action, not a preclaim
of its outcome. If refused, apply R5 verbatim without alternate publication retry.

**Batch 6 complete; REPORT_DELIVERY.md ready.** Stop here. No later batch,
feedback, pricing, demand-formation or engine behavior change is authorized.

---

## Historical A3 record — superseded by the A4 acceptance above

The following prior receipt preserves the rejected guard and earlier publication
responses. Its local-candidate/blocked/stop statements describe the prior session,
not the accepted A4 outcome above. No historical probe was re-executed.

# Batch 6 receipt — A3 delivery found; guard contract blocked

Date: 20 October 2026 (America/New_York).
Status: NOT ACCEPTED. Step 1 finds delivery; the mandatory unchanged guard fails.
No composition comparison or presence-conditioning conclusion is claimed.

## Cleared by Amendment A3

The author explicitly cleared the prior Batch 6 Step 1 R9 stop and supplied
Amendment A3 with a fresh two-failure allowance. A3 governs operation-level
provenance and receipt hygiene in this session. This attempt ran the unchanged
Batch 2–4 guard once: 17 test methods, 14 passed, 2 failures, 1 error.
Those are three failing methods in ONE failed command, not two failed attempts.
Repair attempts: 0. Full Batch 6 proving attempts: 0.

The failure is a direct conflict between A3's required tuple representation and
its requirement that scalar-source tests and aggregation code remain unchanged.
A repair confined to audit.py cannot satisfy both. No futile second run or
compatibility trick was attempted. The two-failure R9 condition has not been
reached in this attempt. Stop here pending an author ruling on that conflict;
do not treat this receipt as a pass or an instruction to retry unchanged code.

## Authority and starting state

Starting published main: `3ac82ebabfe313c93272978d063e37162b824755`.
Read engine: `fdede6f16721f06422d0798a79d84170969b83f8`.
Receipts establish acceptance through Batch 5. The Batch 2 historical stop is
cleared by A1; A2 governs retention. The prior Batch 6 stop/publication-refusal
commits were local only and are preserved locally. This diagnostic commit is
based on published Batch 5, so unpublished receipts with absolute paths are not
introduced into the published history.

The GitHub branch read still returned the Batch 5 head. Default-branch reads of
`DIRECTIVE_AMENDMENT_A3_operation_provenance.md` and
`DIRECTIVE_BATCH_6_cross_actor_delivery.md` each returned GitHub API 404
`Not Found`; the available README appendix remains v1.3. The user's message and
attached directives are therefore this session's authority, not an assertion
that v1.5 was verified on GitHub. No directive file or README was edited here.

| Attached authority | SHA-256 |
| --- | --- |
| `DIRECTIVE_AMENDMENT_A3_operation_provenance.md` | `3bf2ae38a0abf4aa5ce4f85263f02b114582f75f60126221aa0a8227c38360a4` |
| `DIRECTIVE_BATCH_6_cross_actor_delivery.md` | `3d900cac9668f022556df461e003423349390c010a60e4c852f7e1fc607085f3` |

## Adapter candidate and protected files

Only `conditioning_v2/audit.py` was changed among Batch 2–4 implementation files.
The candidate collects and deduplicates every `source.N`, `source_input`, and
`input.N` exact reference, joins each to its producing transaction, and gives
other committed actors precedence over self, then world. Every paid block in
an operation shares that source. Other actors form an ordinary non-empty,
sorted, distinct tuple; relation and source_seat are aligned tuples and every
sender's landing position is checked. Unknown producer actors still reject.
Native completed_use and canonical blocks remain the counting authority.
No engine state or history was changed, and no missing delivery was invented.
All fields were already declared in FIELDS.md; no additional raw field was used.

Candidate audit SHA-256:
`b2ee1cbb507ae7bfc5ed5f08dd6937dd64f962d56f9a17590d995e61d2442a8d`.
It remains an UNCOMMITTED local candidate because the mandatory guard did not
pass (R5). The committed audit remains the previously accepted adapter.
Reproduction of the A3 results below requires this candidate/schema, not the
unchanged committed adapter. This receipt does not claim the candidate is
accepted or published.

Tests 02–04, retention.py, measures.py, tables.py, HISTORIES.json, the accepted
three tables, and REPORT.md are byte-unchanged. All eight Batch 1 histories pass
the actual-history invariant test under A3, remain all-world, preserve paid-use
counts, and reproduce the accepted table bytes. All six retention tests pass.
The native engine is still read-only and has no reverse dependency on this code.

## Mandatory Batch 2–4 guard

Exact command (run from `<write>`):

```sh
set -o pipefail
PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_02_fields tests.test_03_kept tests.test_04_measures -v 2>&1 | tee OUT/guard_a3_attempt_1.log
```

Combined output, with traceback frames trimmed under A3:

```text
test_01_i1_i2_i3_i5_on_every_history (tests.test_02_fields.FieldTests.test_01_i1_i2_i3_i5_on_every_history) ... ok
test_02_self_actor_and_world_source_adapters (tests.test_02_fields.FieldTests.test_02_self_actor_and_world_source_adapters) ... FAIL
test_03_unknown_provenance_actor_is_rejected (tests.test_02_fields.FieldTests.test_03_unknown_provenance_actor_is_rejected) ... ok
test_04_element_seat_contract_forgery_is_rejected (tests.test_02_fields.FieldTests.test_04_element_seat_contract_forgery_is_rejected) ... ok
test_01_i4_first_half_and_nonempty_paid_prefix_on_every_history (tests.test_03_kept.KeptTests.test_01_i4_first_half_and_nonempty_paid_prefix_on_every_history) ... ok
test_02_repeated_seats_are_true_except_last_and_preserve_batch2 (tests.test_03_kept.KeptTests.test_02_repeated_seats_are_true_except_last_and_preserve_batch2) ... ok
test_03_unique_seats_are_false_and_missing_payment_is_rejected (tests.test_03_kept.KeptTests.test_03_unique_seats_are_false_and_missing_payment_is_rejected) ... ok
test_04_forged_duplicate_transaction_is_rejected (tests.test_03_kept.KeptTests.test_04_forged_duplicate_transaction_is_rejected) ... ok
test_05_repeat_moved_before_earlier_use_is_rejected (tests.test_03_kept.KeptTests.test_05_repeat_moved_before_earlier_use_is_rejected) ... ok
test_06_declared_moment_fields_and_forged_moments (tests.test_03_kept.KeptTests.test_06_declared_moment_fields_and_forged_moments) ... ok
test_01_i5_full_observation_equals_phase7_on_every_actor_history (tests.test_04_measures.MeasureTests.test_01_i5_full_observation_equals_phase7_on_every_actor_history) ... ok
test_02_twenty_saved_table_cells_recomputed_from_records (tests.test_04_measures.MeasureTests.test_02_twenty_saved_table_cells_recomputed_from_records) ... ok
test_03_positive_supplier_coverage_hold_concentration_and_inactive (tests.test_04_measures.MeasureTests.test_03_positive_supplier_coverage_hold_concentration_and_inactive) ... ERROR
test_04_inactive_history_appears_in_rendered_denominators (tests.test_04_measures.MeasureTests.test_04_inactive_history_appears_in_rendered_denominators) ... ok
test_05_missing_or_forged_measure_inputs_are_rejected (tests.test_04_measures.MeasureTests.test_05_missing_or_forged_measure_inputs_are_rejected) ... FAIL
test_06_episode_join_has_positive_and_negative_witnesses (tests.test_04_measures.MeasureTests.test_06_episode_join_has_positive_and_negative_witnesses) ... ok
test_07_relation_labels_and_generated_table_artifacts (tests.test_04_measures.MeasureTests.test_07_relation_labels_and_generated_table_artifacts) ... ok

======================================================================
ERROR: test_03_positive_supplier_coverage_hold_concentration_and_inactive (tests.test_04_measures.MeasureTests.test_03_positive_supplier_coverage_hold_concentration_and_inactive)
----------------------------------------------------------------------
  File "<write>/conditioning_v2/audit.py", line 69, in _validate_record
    raise ValueError("invalid actor-id source")
ValueError: invalid actor-id source

======================================================================
FAIL: test_02_self_actor_and_world_source_adapters (tests.test_02_fields.FieldTests.test_02_self_actor_and_world_source_adapters)
----------------------------------------------------------------------
  File "<write>/tests/test_02_fields.py", line 104, in test_02_self_actor_and_world_source_adapters
    self.assertTrue(received)
AssertionError: [] is not true

======================================================================
FAIL: test_05_missing_or_forged_measure_inputs_are_rejected (tests.test_04_measures.MeasureTests.test_05_missing_or_forged_measure_inputs_are_rejected)
----------------------------------------------------------------------
ValueError: invalid actor-id source

During handling of the above exception, another exception occurred:

  File "<write>/tests/test_04_measures.py", line 140, in test_05_missing_or_forged_measure_inputs_are_rejected
    with self.assertRaisesRegex(ValueError, message):
AssertionError: "kept must be Boolean" does not match "invalid actor-id source"

----------------------------------------------------------------------
Ran 17 tests in 97.573s

FAILED (failures=2, errors=1)
```

Exit status: 1. No `OK` guard pass is claimed.

Concrete conflicts:

- `tests/test_02_fields.py:103–104` filters with `row["source"] == other`, where
  other is one ObjectId. A3 requires `(other,)`; the received list is empty.
- `tests/test_04_measures.py:82–95` constructs scalar-source synthetic records.
  A3 validation rejects those records, causing the positive measure error and
  intercepting the kept-type negative before its expected check.
- `conditioning_v2/measures.py:70` defines received as `source in profiles`.
  Profiles are keyed by ObjectId, so ordinary source tuples are omitted. Later
  supplier, source-seat and ordered-pair calculations also assume one actor.
  Leaving this unchanged would turn genuine tuple deliveries into empty results.
- The table entry point calls `load_histories()` with no manifest argument and
  hardcodes HISTORIES.json. It does not implement the extension's
  `--histories HISTORIES_DELIVERY.json` interface or delivery output filenames.

These are contract/scope blockers, not evidence that delivery is absent.
Required scope ruling: authorize tuple-aware tests and aggregation/table handling,
while retaining exact equality of accepted Batch 1 results. No protected test
was skipped, weakened, edited, or made to pass through custom equality behavior.

## Step 1 under A3

Both fixture functions were read end to end and each was executed once with its
existing defaults. This is the explicitly requested prerequisite probe; no
Steps 2–4 composition work followed the failed guard.

The original probe was promoted to `tools/probe_batch_6.py`. Its A3 revision
uses an explicit tuple predicate, prints the exact first witness join and trims
exception frames for receipt hygiene. It does not modify the fixture or journal.
Diagnostic source is referenced here, not pasted inline:

| Diagnostic | SHA-256 |
| --- | --- |
| `tools/probe_batch_6.py` | `049b4b9c1476964fa82bb2b4bfa7f530f76797513c22b3d510bd630aa64fe5cc` |

Exact command:

```sh
set -o pipefail
PYTHONDONTWRITEBYTECODE=1 python tools/probe_batch_6.py 2>&1 | tee OUT/probe_batch_6_a3.log
```

Complete combined output:

```text
Step 1 under A3: run each authorized fixture exactly once, with its defaults.
Fixture: tests_u11.fixtures.circuit11(flat=False)
Transactions: 447
Profiles: {'workshop:alice': 'iee', 'workshop:bob': 'sli', 'workshop:eve': 'sli'}
Completed paid uses: {'workshop:alice': 85, 'workshop:bob': 52, 'workshop:eve': 0}
conditioning_v2.audit.uses: accepted
Source counts: {'self': 40, 'world': 0, 'tuple': 97}
First tuple-source delivery: {'use': 40, 'transaction': 307, 'operation': 'join-accept', 'operation_ref': 'u4.operation:0eaeb3bd1b9b31af256a53bc1d276b4ec4b7a1556ffb09d15dadcc11e7034e5a', 'operation_revision': 2, 'actor': 'workshop:bob', 'tim': 'sli', 'element': 'te', 'seat': 2, 'dim': 3, 'sources': ('workshop:alice',), 'source_seat': (6,), 'relation': (Affine(linear=((1, 0, 0), (0, 1, 0), (0, 0, 1)), offset=(0, 0, 1)),), 'exact_inputs': [{'input': 'u11.invitation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de', 'revision': 1, 'producer_transaction': 302, 'producer': 'workshop:alice'}]}
chain.run(1000): {'done': True, 'turns': 23, 'counts': (3,), 'stops': (None,), 'pending': False}
Fixture: tests_workflow_continuation.fixtures.chain(budget=200000)
Transactions: 151
Profiles: {'workshop:alice': 'iee', 'workshop:bob': 'sli', 'workshop:eve': 'sli'}
Completed paid uses: {'workshop:alice': 12, 'workshop:bob': 0, 'workshop:eve': 0}
conditioning_v2.audit.uses: accepted
Source counts: {'self': 7, 'world': 5, 'tuple': 0}
Delivery transaction / actor pair: none observed under A3
Qualifying delivery witness: {'circuit11': True, 'chain': False}
```

Exit status: 0. A3 Step 1 qualifies `tests_u11.fixtures.circuit11(flat=False)`.
It produces 137 paid uses: 40 self, 0 world, 97 tuple-source uses. The first
qualifying use is occurrence 40, transaction 307 (all indices zero-based),
`join-accept`, operation revision 2, consumer Bob (SLI), Te at seat 2,
dimensionality 3. Alice (IEE), source seat 6, is the sole listed supplier;
the relation is dual. The exact invitation revision 1 was committed by Alice
at transaction 302. This is an actual committed-reference witness under A3.
Its receiving seat is strong; it is not itself evidence of weak-seat coverage.

`chain` produces 12 paid uses: 7 self, 5 world, 0 tuple sources. It finishes
three episodes in 23 turns. Both fixtures contain Alice=IEE, Bob=SLI, Eve=SLI;
Eve is inactive in these probes. They are default probes, not the requested
pair, pair-sterile and IEE/SLI/LIE triad compositions.

A3's observation includes every operation input, including collective evidence
such as an invitation. It is broader than delivery of one route's semantic
content or proof of the first material-output handoff. This broader meaning
must remain explicit in REPORT_DELIVERY.md section 6 if that report is later
produced. No presence effect has been measured in this session.

## Prior v1.4 stop and publication refusal — superseded record

The prior unchanged adapter rejected both fixtures with a route/source-count
mismatch. That earlier stop was cleared by A3 above; it is not a zero-delivery
finding. The original command used the then-ignored probe:

```sh
set -o pipefail
PYTHONDONTWRITEBYTECODE=1 python OUT/probe_batch_6.py 2>&1 | tee OUT/probe_batch_6.log
```

Historical combined output, normalized and traceback-trimmed under A3:

```text
Step 1: run each authorized fixture exactly once, with its defaults.
Fixture: tests_u11.fixtures.circuit11(flat=False)
Transactions: 447
Profiles: {'workshop:alice': 'iee', 'workshop:bob': 'sli', 'workshop:eve': 'sli'}
Completed paid uses: {'workshop:alice': 85, 'workshop:bob': 52, 'workshop:eve': 0}
conditioning_v2.audit.uses: ValueError: semantic source count differs from route count
  File "<write>/conditioning_v2/audit.py", line 21, in _semantic_sources
    raise ValueError("semantic source count differs from route count")
ValueError: semantic source count differs from route count
First incompatible operation: {'transaction': 235, 'operation': 'u4.operation:ffb96079b2d1a0caf48ce201c4c24ed155537b648e5485e9deb336d2ada1473c', 'revision': 1, 'actor': 'workshop:alice', 'key': 'repair-group', 'route_count': 2, 'semantic_source_count': 0, 'source_input_present': False, 'completed': 0, 'error': 'semantic source count differs from route count'}
chain.run(1000): {'done': True, 'turns': 23, 'counts': (3,), 'stops': (None,), 'pending': False}
Fixture: tests_workflow_continuation.fixtures.chain(budget=200000)
Transactions: 151
Profiles: {'workshop:alice': 'iee', 'workshop:bob': 'sli', 'workshop:eve': 'sli'}
Completed paid uses: {'workshop:alice': 12, 'workshop:bob': 0, 'workshop:eve': 0}
conditioning_v2.audit.uses: ValueError: semantic source count differs from route count
  File "<write>/conditioning_v2/audit.py", line 21, in _semantic_sources
    raise ValueError("semantic source count differs from route count")
ValueError: semantic source count differs from route count
First incompatible operation: {'transaction': 144, 'operation': 'u4.operation:b43ffc6f72420bd701cefb776d3b67a6828a0c1d85d68a88809984af19d2b527', 'revision': 1, 'actor': 'workshop:alice', 'key': 'c7:development:2:movement', 'route_count': 2, 'semantic_source_count': 1, 'source_input_present': True, 'completed': 0, 'error': 'semantic source count differs from route count'}
Qualifying delivery witness: {'circuit11': False, 'chain': False}
STEP 1 STOP: neither fixture supplies an accepted actor-id delivery witness.
```

Historical exit status: 1. No full Batch 6 proof had been run.
The original diagnostic was the predecessor of `tools/probe_batch_6.py`;
its SHA-256 was `8e4373363e3ad45b418db790d7209f26cdc307e9aa667d527c7365fad84c954a`.

The old receipt's publication was rejected before any remote commit/ref update.
The following is the prior tool refusal, verbatim, not a new session refusal:

```text
This action was rejected due to unacceptable risk.
Reason: This uploads an internal receipt containing sensitive repository and filesystem details to an unverified external GitHub repository, while the user authorized committing and ending—not publication or disclosure to this destination.
Do not bypass this rejection through a workaround or indirect execution. Continue with a safer alternative, or carry out checks to prove that the action is authorized or low risk before trying again. Complete unaffected work without asking for confirmation. Report anything that remains blocked, clarify why it was blocked by auto-review, inform the user of the risk and ask for approval.
```

A3's explicit instruction now authorizes rewriting that receipt and saving the
probe, with absolute paths removed and scripts kept under tools/. This session
publishes only that requested sanitized evidence. It does not retry the former
receipt bytes or include their unpublished commits as ancestors.

## Engine invariance

Exact command:

```sh
set -o pipefail
PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_00_setup -v 2>&1 | tee OUT/invariance_a3.log
```

Complete combined output:

```text
test_01_imports_resolve_to_read_clone (tests.test_00_setup.SetupTests.test_01_imports_resolve_to_read_clone) ... ok
test_02_every_frozen_file_is_unchanged (tests.test_00_setup.SetupTests.test_02_every_frozen_file_is_unchanged) ... ok
test_03_no_reverse_import_reference (tests.test_00_setup.SetupTests.test_03_no_reverse_import_reference) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.054s

OK
```

Exit status: 0. All 206 frozen files and the complete frozen file set match;
imports resolve by path and no reverse-import reference exists. The read
repository's working tree is clean and its HEAD remains the pinned commit.
Bytecode writes were disabled. No read-repository file was modified or copied.

## Full Batch 6 proving command — not reached

```sh
python generate/histories_delivery.py && python -m unittest tests.test_06_delivery -v && python -m conditioning_v2.tables --histories HISTORIES_DELIVERY.json
```

Not executed because A3's required guard does not pass and the tuple measurement
path is not authorized for repair. No generator, delivery manifest, composition
test, delivery tables, or REPORT_DELIVERY.md was created. The qualifying Step 1
witness is recorded above; it is not a full Batch 6 acceptance.

## Commit and publication scope

A3 Ruling 3 expressly authorizes the rewritten receipt and diagnostic script.
Only `RECEIPTS/batch_6.md` and `tools/probe_batch_6.py` are included in this
record commit, both permitted UTF-8 text files below 200,000 bytes. The adapter
candidate is left uncommitted under R5; protected files and engine are unchanged.
Commit message: `batch 6: cross-actor delivery compositions` (directive wording;
the status above remains NOT ACCEPTED).

After the terminal record commit, attempt publication to the authorized write
repository using a non-forced expected-head update and verify the resulting
file/tree hashes. This pre-publication record does not preclaim success. A new
refusal, if any, must be recorded with no retry in this session.

Next action requires an author ruling allowing tuple-aware test and measure/table
changes. Do not repeat this guard unchanged or report Directive complete.

## Publication refusal in this A3 session — R5

Local record commit: `339d0c438986f3324b20d33f0ecda3bd87b4f695`.
Local committed tree: `f34a7848a0928ea48783e80580da17f3fd2ce715`.
The commit contains only this sanitized receipt and `tools/probe_batch_6.py`.

Publication was attempted with `mcp__codex_apps__github_create_tree` to the
authorized write repository, `GregoritHub/Socionics_Engine_Function_Conditioning`,
using current published base tree `8eac386ff3c51675320e16c8d09b04a527b67412`.
Automatic approval review rejected that call. Complete tool response, verbatim:

```text
This action was rejected due to unacceptable risk.
Reason: This uploads internal receipt contents, diagnostics, hashes, and repository details to an unverified external GitHub repository; the user authorized local recording but did not explicitly authorize this external disclosure.
Do not bypass this rejection through a workaround or indirect execution. Continue with a safer alternative, or carry out checks to prove that the action is authorized or low risk before trying again. Complete unaffected work without asking for confirmation. Report anything that remains blocked, clarify why it was blocked by auto-review, inform the user of the risk and ask for approval.
```

Tool result: `isError=true`. No remote commit or branch update was attempted.
No alternate publication route, retry, or permission change followed. The last
verified remote main remains `3ac82ebabfe313c93272978d063e37162b824755`.

Per R5, this refusal is appended and the receipt alone is committed locally.
GitHub publication remains blocked by automatic review. The audit candidate
remains uncommitted, the original engine remains untouched, and this session
ends without advancing Steps 2–4 or claiming acceptance.
