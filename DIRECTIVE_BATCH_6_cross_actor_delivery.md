# Directive Extension — Batch 6: Cross-actor delivery

Applies to: Batch Directive — Function Conditioning Ledger v2, v1.3 → v1.4
Issued: 20 October 2026, on reading `REPORT.md` §2 ("no cross-actor deliveries observed")
Authority: directive author. All standing rules R1–R10 apply unchanged. R10's scope sentence is extended by one clause: *and one additional fixture that routes one actor's completed output into another actor's paid use.*

## Why

Batches 0–5 built the instrument and ran it on histories in which no actor ever consumed another actor's output. Every `source` was `"self"` or `"world"`. The instrument therefore measured an empty set for the one thing it was built to measure. That is a property of the Batch 1 fixtures (`workflow_population` gives each actor its own independent demand), not of the instrument. Batch 6 supplies histories that contain fellowship.

## Inputs

`<read>/tests_u11/fixtures.py` (collective work: `group`, `join`, `proposed`, `instantiate`, `perform_step`, `finish` — U11 is where one actor's step output is consumed by another's), `<read>/tests_workflow_continuation/fixtures.py` (`chain`: generated-result chains), `<read>/tests_c6/fixtures.py` (`SelectionRequest(..., peer=BOB)`), `<read>/hle_unified/collective.py`, and the existing `conditioning_v2/` modules.

## May create

`generate/histories_delivery.py`, `HISTORIES_DELIVERY.json`, `tests/test_06_delivery.py`, `TABLES/*_delivery.md` (same three tables as Batch 4, on the new histories), `REPORT_DELIVERY.md`, `RECEIPTS/batch_6.md`.

## Steps

1. **Find the delivery path.** Read `tests_u11/fixtures.py::circuit11` and `tests_workflow_continuation/fixtures.py::chain` end to end. Identify, by running them once and inspecting the journal with `conditioning_v2.audit.uses`, which of the two produces at least one completed paid use whose exact consumed revision was committed by a transaction with a *different* non-null `actor`. Record in the receipt which fixture, which transaction, which actor pair. If neither does, stop under R9 with that finding — do not construct a delivery by hand.

2. **Generate three compositions** using that fixture, same seeds across compositions, ≥ 4 seeds, `legacy-r4` only (grade-v1 adds nothing to provenance):
   - **pair:** two actors, a dual pair (IEE + SLI as the fixtures already name them, or whatever pair the fixture supports);
   - **pair-sterile:** two actors in a relation the yield table lists as sterile both ways (e.g. the two in conflict or quasi-identity — pick one the fixture's `tim=` parameter allows; record which);
   - **triad:** the three actors of Batch 1 (IEE, SLI, LIE).
   Same episode count and quantum across all three. Record every parameter in `HISTORIES_DELIVERY.json`.

3. **Run the existing instrument unchanged.** Batches 2–4 code is not modified. `tests/test_06_delivery.py` asserts: I1–I5 pass on the new histories; at least one history in *pair* shows a use with `source` = an actor id (**the positive witness Batch 2 lacked**); the forged-provenance negative from Batch 2 still rejects.

4. **Tables and report.** The three Batch 4 tables, computed per composition. `REPORT_DELIVERY.md`, ≤ 300 words per section:
   1. Which fixture delivers, and the first delivery event (actor, seat, dim, relation).
   2. Conditioning index and hold index per actor, per composition.
   3. Coverage: pair vs. pair-sterile vs. triad. State the three numbers.
   4. Sterile pairs observed, with relation names, against the yield table's prediction.
   5. DCNH all-use vs. received-and-kept, per actor, per composition: agree or diverge.
   6. Limits.

## Proving command

`python generate/histories_delivery.py && python -m unittest tests.test_06_delivery -v && python -m conditioning_v2.tables --histories HISTORIES_DELIVERY.json`

**Pass line:** `OK`, and `REPORT_DELIVERY.md` §1 names a delivery event.
**Commit message:** `batch 6: cross-actor delivery compositions`

## After Batch 6

Stop. The question "does conditioning depend on who is present" is answered by §3 and §5 of `REPORT_DELIVERY.md` — coverage differing across compositions with the same seeds is the effect; identical coverage is its absence. Either is a result. No feedback rule is authorized by this batch.
