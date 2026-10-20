# Directive Amendment A4 — tuple-aware scope; guard restated

Applies to: Batch Directive — Function Conditioning Ledger v2, v1.5 → v1.6
Issued: 20 October 2026, on the A3-session Batch 6 receipt
Authority: directive author. Ruling, not repair.

## Finding accepted

Step 1 under A3 is accepted as run: `tests_u11.fixtures.circuit11(flat=False)` is the delivery fixture. 97 of 137 paid uses carry another actor as source; the first is Bob (SLI), Te at seat 2 (3D), from Alice (IEE) at seat 6, relation dual, invitation revision 1 committed by Alice at transaction 302. `chain` carries no cross-actor source. Recorded; no re-run of Step 1 is required.

## Ruling 1 — A3's guard was self-contradictory; restated

A3 required (a) tuple-valued `source` and (b) no change outside `audit.py` with all Batch 2–4 tests passing. (b) cannot hold under (a) because `tests/test_02_fields.py`, `tests/test_04_measures.py`, `conditioning_v2/measures.py` and `conditioning_v2/tables.py` were written for scalar sources. The receipt was right to stop rather than satisfy (b) by weakening tests.

The guard is now: **the accepted Batch 1 outputs are byte-identical.** Specifically, after any change:
- `TABLES/per_actor.md`, `TABLES/per_population.md`, `TABLES/dcnh_two_ways.md` and `REPORT.md` regenerate byte-identical from `HISTORIES.json`;
- every Batch 1 history still yields only `"self"`/`"world"` sources with unchanged per-element counts (I5);
- every negative witness in tests 02–04 still rejects (forged provenance, forged seat/element, forged duplicate, backward repeat, forged measure inputs, non-Boolean `kept`).

Within that guard, the following are **authorized**:
- `tests/test_02_fields.py` and `tests/test_04_measures.py`: filter and construct records with tuple sources; synthetic positive records use `(actor,)`.
- `conditioning_v2/measures.py`: "received" means `source` is a tuple; supplier map, source-seat, ordered-pair and sterile-pair logic iterate over each listed actor; a use with k listed actors counts once per actor in supplier/pair tables and once in the actor's own use profile.
- `conditioning_v2/tables.py`: accept `--histories <manifest>` and an output suffix; default remains `HISTORIES.json` with the existing filenames.
- `conditioning_v2/audit.py`: the A3 candidate (SHA-256 `b2ee1cbb…2442a8d`) is accepted for commit once the restated guard passes.

Nothing else. `retention.py`, `generate/histories.py`, `HISTORIES.json` and the read repository remain unchanged.

## Ruling 2 — proceed to Steps 2–4

With the guard passing, Batch 6 Steps 2–4 proceed as written, using `circuit11` as the fixture. Composition parameters that the fixture's signature does not expose (member TIMs, member count) are set through its `setup11(..., tim=)` and `group`/`join` calls; record exactly which calls and arguments produced each composition in `HISTORIES_DELIVERY.json`. If the fixture cannot produce a given composition without modifying the read repository, record that composition as "not producible" and run the ones that are.

`REPORT_DELIVERY.md` §6 states that A3/A4 provenance counts any exact operation input — including collective evidence such as an invitation — and is therefore broader than delivery of one route's semantic content.

## Ruling 3 — publication authority

Automatic review has twice refused publication on the ground that the user authorized local recording but not external disclosure. The directive author's files do not constitute that authorization. The user supplies it in their own prompt, naming the destination repository and the files. Until that sentence is present in the session prompt, R5 continues to apply: record the refusal, commit locally, continue.

## Ruling 4 — root files (repeated)

As of this receipt, `DIRECTIVE_AMENDMENT_A3_operation_provenance.md`, `DIRECTIVE_BATCH_6_cross_actor_delivery.md` and a README appendix beyond v1.3 are not on the write repository's default branch. The directive author commits A3, A4, Batch 6 and README v1.6 in one commit before the next session is started.
