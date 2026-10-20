# Directive Amendment A3 — operation-level provenance; receipt hygiene

Applies to: Batch Directive — Function Conditioning Ledger v2, v1.4 → v1.5
Issued: 20 October 2026, on `RECEIPTS/batch_6.md` (stop under R9 at Step 1; publication refused)
Authority: directive author. Rulings, not repairs.

## Ruling 1 — the adapter, not the fixtures, is the blocker

The receipt establishes that both delivery-bearing fixtures (`circuit11`, `chain`) produce histories the native `conditioning_audit.completed_use` accepts and the v2 adapter rejects with `semantic source count differs from route count`. The v2 adapter's contract — exactly one `source.N` revision per route — was fitted to the Batch 1 workflow-selection operations and is narrower than the engine's operation formats. Collective operations carry zero `source.N`; continuation movements carry fewer `source.N` than routes. `FIELDS.md` already warned: the exact-revision join "does not select one source for a multi-input hop."

**Provenance is therefore resolved at the operation level, not per route.** For each completed use (hop or seat-content block) within an operation:

1. Collect the operation's exact consumed revisions: every `source.N`, `source_input`, and `input.N` reference present on the operation. No inferred heads; exact identity and revision only.
2. Resolve each through the existing join: consumed `ObjectRef` → matching `version.ref` → producing `Transaction.actor`.
3. Partition the resolved producers: `self` (equals the consuming actor), `world` (`None`), `others` (any other committed actor).
4. Set `source` for every use in that operation to:
   - the sorted tuple of distinct `others` ids, if non-empty;
   - `"self"` if `others` is empty and `self` is non-empty;
   - `"world"` otherwise.
5. `relation` and `source_seat` become per-listed-actor tuples when `source` is a tuple; `None` otherwise. `landing_position` is checked per listed actor.

Consequences: I1, I4, I5 unchanged. I2: `source` is `"self"`, `"world"`, or a non-empty sorted tuple of committed actor ids. I3 applies to each actor in the tuple. "Received" (for conditioning index, hold index, supplier map, coverage, sterile pairs) means `source` is a tuple. The Batch 1 histories must reproduce their accepted Batch 2–4 results exactly under the new adapter (every one of their operations has `others` empty); that identity is Batch 6's first test and replaces nothing.

This widens what counts as a delivery from "the one semantic input of a route" to "any exact revision the operation consumed." That is the broader reading and it is stated as such in `REPORT_DELIVERY.md` §6.

## Ruling 2 — the Batch 6 stop is cleared

The next session re-attempts Batch 6 under Ruling 1. Step 1 is re-run with the generalized adapter; a qualifying delivery witness is any use with `source` a tuple. If neither fixture yields one under the generalized adapter, stop under R9 and report — that would be a real finding about the engine. Fresh two-failure allowance.

The adapter change is made in `conditioning_v2/audit.py`, which is the one departure from Batch 6's "Batches 2–4 code is not modified." Every existing test in `tests/test_02..04` must still pass on the Batch 1 histories; that is the guard.

## Ruling 3 — receipt hygiene (R3 extended)

Publication of the Batch 6 receipt was refused by automatic review as containing "sensitive repository and filesystem details." The receipt included absolute scratch paths and a 70-line diagnostic script inline. From now on:

- Receipts replace every absolute local path with `<write>` or `<read>`. No `/workspace/...`, `/home/...`, or scratch identifiers.
- Diagnostic scripts are committed as files under `tools/` (R3 size limit applies) and referenced by path and SHA-256, not pasted into receipts.
- Tracebacks are trimmed to the final exception line plus the frame inside this repository.
- A receipt is a record of what was done and found. It does not need to prove the session's environment.

The unpublished Batch 6 receipt is rewritten to this standard and committed as `RECEIPTS/batch_6.md` (replacing the local stop record), with the original probe saved as `tools/probe_batch_6.py`.

## Ruling 4 — directive files at the root

The receipt correctly notes that `DIRECTIVE_BATCH_6_cross_actor_delivery.md` was not at the write-repository root and the README appendix was still v1.3. The directive author commits, in one commit: `DIRECTIVE_BATCH_6_cross_actor_delivery.md`, this amendment, and the README appendix bumped to v1.5. Sessions treat the committed files as authority; an attached file is authority only for the session it is attached to, and the receipt is right to say so.
