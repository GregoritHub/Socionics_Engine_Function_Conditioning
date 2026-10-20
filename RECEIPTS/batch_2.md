# Batch 2 receipt — provenance precondition blocked

Date: 20 October 2026. Status: NOT ACCEPTED.
Stopped under R9.

## Current source and scope

Starting published main: `a6e6869706d518a5f834dc7bc732f400edffb311`.
Read all current receipts (Batches 0 and 1), the operative directive retained in
README.md, FIELDS.md, the named engine audit/Model A/relation modules, and the
native record/checkpoint definitions. No earlier receipt contained an R9 stop.
The named standalone directive file remains absent; Batch 0 identifies README's
verbatim appendix as its durable source. No AGENTS.md is present in the write tree.
The original engine's separate continuous-build instructions do not authorize
writes to that repository under this companion directive.

This run attempts Batch 2 only. Batch 1 was already published, so it was not
repeated as a new batch. Its ignored checkpoints were regenerated using the
unchanged published generator. HISTORIES.json is byte-identical to the accepted
manifest. Both proving attempts independently restored all eight checkpoints,
verified every accepted SHA-256, and verified byte-exact re-checkpointing.

Read repository stays at `fdede6f16721f06422d0798a79d84170969b83f8`.
All 206 frozen files and the exact file set still match. The original working
tree is clean, and no source or checkpoint from it was copied or published.
Python: 3.12.14. Bytecode writes were disabled before engine imports.
Terminal read-only git fetch was unavailable due to the browser-proxy connection;
current GitHub contents were retrieved through the connected app instead.

## Concrete blocker

FIELDS.md resolves the structural exact-revision join:
consumed ObjectRef -> matching committed version.ref -> Transaction.actor.
It explicitly states that this actor is nullable and an actorless source is not
evidence of self-production. A resolved join does not supply a missing actor.

On every generated history the first consumed semantic seed revision joins to a
transaction whose actor is None. For example, legacy-r4-seed-17 consumes
workshop:history-17-alice-one revision 1, committed by
u4:seed:history-17-alice-one with actor=None. This is an actual semantic source,
not the physical content_target, context, cue, or broad evidence-input list.
The paid operation revisions themselves DO have committed actors; the first
positive test witnesses that the join works for those revisions.

The native fixture tests_u5/fixtures.py:45-60 declares the supplied Account and
then pays to bind it. seed() returns the originally declared revision. Declaring
that revision does not record its actor in Transaction.actor. An Account's owner,
the later paying actor, the writer label, and an actor inferred from a name are
not the producing Transaction.actor required by the declared provenance rule.
hle_unified/records.py:397-403 allows actor=None; compact.py:294-296,309-320,
372-376 preserves it through checkpoint roundtrips. Lineage inputs/evidence do
not populate a missing producer identity.

Batch 2 requires source to be either "self" or the recorded producing actor's
id and rejects forged provenance. Labeling these inputs "self", dropping their
uses, or adding an unknown-source category would change the directive's meaning
or break the exact completed_use totals. Changing the accepted Batch 1 generator
or the original engine is outside Batch 2's allowed files.

Missing for valid continuation: an explicit policy for actorless supplied input
revisions, or an authorized replacement of the generated histories with genuine
producer-bearing source revisions. No such policy is inferred here.

## Proving command and first failure

Command (combined stdout/stderr captured verbatim):

```sh
python -m unittest tests.test_02_fields -v
```

Attempt 1 used the declared primary semantic revision, source_input. The test
file is a prerequisite witness only: it does not claim an implementation of
uses() or I1-I5. The primary-source resolver was:

```python
def semantic_sources(d):
    return (d["source_input"],)
```

Full output, attempt 1:

```text
test_01_exact_revision_join_preserves_recorded_producer (tests.test_02_fields.ProvenancePreconditionTests.test_01_exact_revision_join_preserves_recorded_producer) ... ok
test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) ... 
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-17') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-29') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-43') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-61') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-17') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-29') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-43') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-61') ... FAIL

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-17')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 73, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: legacy-r4-seed-17; ObjectRef(identity=ObjectId(namespace='workshop', key='history-17-alice-one'), revision=1); producing transaction=u4:seed:history-17-alice-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-29')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 73, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: legacy-r4-seed-29; ObjectRef(identity=ObjectId(namespace='workshop', key='history-29-alice-one'), revision=1); producing transaction=u4:seed:history-29-alice-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-43')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 73, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: legacy-r4-seed-43; ObjectRef(identity=ObjectId(namespace='workshop', key='history-43-eve-one'), revision=1); producing transaction=u4:seed:history-43-eve-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-61')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 73, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: legacy-r4-seed-61; ObjectRef(identity=ObjectId(namespace='workshop', key='history-61-eve-one'), revision=1); producing transaction=u4:seed:history-61-eve-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-17')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 73, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: grade-v1-seed-17; ObjectRef(identity=ObjectId(namespace='workshop', key='history-17-alice-one'), revision=1); producing transaction=u4:seed:history-17-alice-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-29')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 73, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: grade-v1-seed-29; ObjectRef(identity=ObjectId(namespace='workshop', key='history-29-alice-one'), revision=1); producing transaction=u4:seed:history-29-alice-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-43')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 73, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: grade-v1-seed-43; ObjectRef(identity=ObjectId(namespace='workshop', key='history-43-eve-one'), revision=1); producing transaction=u4:seed:history-43-eve-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-61')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 73, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: grade-v1-seed-61; ObjectRef(identity=ObjectId(namespace='workshop', key='history-61-eve-one'), revision=1); producing transaction=u4:seed:history-61-eve-one; recorded actor=None

----------------------------------------------------------------------
Ran 2 tests in 33.756s

FAILED (failures=8)
```

Exit status: 1. One positive method passed; the prerequisite method failed in
eight history subtests.

## One repair attempt

Expanded semantic_sources to inspect every contiguous source.N revision, with
source_input checked against that set and used only when no indexed semantic
sources exist. This tests whether the primary-only lookup overlooked another
recorded semantic producer. Broad input.N context/evidence references were not
substituted, and no identity or revision was guessed. The final resolver and
prerequisite witnesses are retained in tests/test_02_fields.py.

Full output, attempt 2, same proving command:

```text
test_01_exact_revision_join_preserves_recorded_producer (tests.test_02_fields.ProvenancePreconditionTests.test_01_exact_revision_join_preserves_recorded_producer) ... ok
test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) ... 
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-17') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-29') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-43') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-61') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-17') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-29') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-43') ... FAIL
  test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-61') ... FAIL

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-17')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 86, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: legacy-r4-seed-17; ObjectRef(identity=ObjectId(namespace='workshop', key='history-17-alice-one'), revision=1); producing transaction=u4:seed:history-17-alice-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-29')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 86, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: legacy-r4-seed-29; ObjectRef(identity=ObjectId(namespace='workshop', key='history-29-alice-one'), revision=1); producing transaction=u4:seed:history-29-alice-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-43')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 86, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: legacy-r4-seed-43; ObjectRef(identity=ObjectId(namespace='workshop', key='history-43-eve-one'), revision=1); producing transaction=u4:seed:history-43-eve-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='legacy-r4-seed-61')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 86, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: legacy-r4-seed-61; ObjectRef(identity=ObjectId(namespace='workshop', key='history-61-eve-one'), revision=1); producing transaction=u4:seed:history-61-eve-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-17')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 86, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: grade-v1-seed-17; ObjectRef(identity=ObjectId(namespace='workshop', key='history-17-alice-one'), revision=1); producing transaction=u4:seed:history-17-alice-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-29')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 86, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: grade-v1-seed-29; ObjectRef(identity=ObjectId(namespace='workshop', key='history-29-alice-one'), revision=1); producing transaction=u4:seed:history-29-alice-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-43')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 86, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: grade-v1-seed-43; ObjectRef(identity=ObjectId(namespace='workshop', key='history-43-eve-one'), revision=1); producing transaction=u4:seed:history-43-eve-one; recorded actor=None

======================================================================
FAIL: test_02_consumed_semantic_revisions_have_recorded_producers (tests.test_02_fields.ProvenancePreconditionTests.test_02_consumed_semantic_revisions_have_recorded_producers) (history='grade-v1-seed-61')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/d5be342785cd/Socionics_Engine_Function_Conditioning/tests/test_02_fields.py", line 86, in test_02_consumed_semantic_revisions_have_recorded_producers
    self.assertIn(
AssertionError: None not found in {ObjectId(namespace='workshop', key='alice'): 'iee', ObjectId(namespace='workshop', key='bob'): 'sli', ObjectId(namespace='workshop', key='eve'): 'lie'} : unresolved_input_producer: grade-v1-seed-61; ObjectRef(identity=ObjectId(namespace='workshop', key='history-61-eve-one'), revision=1); producing transaction=u4:seed:history-61-eve-one; recorded actor=None

----------------------------------------------------------------------
Ran 2 tests in 33.866s

FAILED (failures=8)
```

Exit status: 1. Failed proving attempts: 2. Repair attempts: 1.
The expanded exact-input lookup still encounters the actorless semantic seed.
No third proving attempt, alternative attribution rule, audit implementation,
retention work, tables, or later batch was attempted.

## Invariance, commit, and stopping point

After generation and before the stop record:

```text
test_01_imports_resolve_to_read_clone ... ok
test_02_every_frozen_file_is_unchanged ... ok
test_03_no_reverse_import_reference ... ok
Ran 3 tests in 0.059s
OK
```

Only RECEIPTS/batch_2.md and tests/test_02_fields.py are committed. Both are small
UTF-8 text under 200,000 bytes. The failed prerequisite test is preserved as a
reproducer, not marked accepted. The R9 failure-record exception governs this
commit; the normal Batch 2 pass gate has NOT passed. No conditioning_v2 module
was created while the prerequisite was unsatisfied.

Commit message: `batch 2: stop under R9 — unresolved input producers`.
The connected GitHub app is used to save this new companion-only stop record
with the existing remote tree and an expected-head, non-forced ref update.
Publication is verified after saving; this receipt does not preclaim that outcome.
The continuation schedule was disabled because this blocker requires a directive
ruling rather than another unattended attempt. Wait for instruction.
