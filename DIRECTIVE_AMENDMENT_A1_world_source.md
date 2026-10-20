# Directive Amendment A1 — `source = "world"`

Applies to: Batch Directive — Function Conditioning Ledger v2, v1.1 → v1.2
Issued: 20 October 2026, in response to `RECEIPTS/batch_2.md` (stop under R9, "unresolved input producers")
Authority: directive author. This is a ruling, not a repair attempt.

## Ruling

Batch 2's `source` field takes **three** values, not two:

| `source` | When | Conditioning event? |
|---|---|---|
| `"self"` | The exact consumed revision was committed by a transaction whose `actor` is the consuming actor. | No |
| `<actor id>` | The exact consumed revision was committed by a transaction whose `actor` is a different committed actor. | Yes, when the receiving seat has `dim ≤ 2` |
| `"world"` | The exact consumed revision was committed by a transaction whose `actor` is `None` — a declared or supplied revision (fixture seeds, supplied prior associations, initial world material). | No |

Resolution remains the exact-revision join already recorded in `FIELDS.md`: consumed `ObjectRef` → matching `version.ref` → producing `Transaction.actor`. `None` maps to `"world"`. No inference from `Account.owner`, the paying actor, the `writer` label, or the revision's name. The receipt was right to refuse all four.

The original tracking specification (19 Oct) defined `source` as `"self"` when the input was "the actor's own prior output **or world material**." The v1.1 directive dropped the second clause in transcription. `"world"` restores it as its own value rather than folding it into `"self"`, because an actorless source is not evidence of self-production — exactly as `FIELDS.md` states.

## Consequences for the invariants

- **I2** becomes: every `source` is `"self"`, `"world"`, or a committed actor id.
- **I3** is unchanged and applies only when `source` is an actor id.
- **I5** is unchanged: `"world"` uses are still completed uses and are counted in the per-element totals.
- **Negative witness** for Batch 2 gains one case: a revision with `actor = None` must resolve to `"world"`, never to any actor id, never to `"self"`.

## Consequences for Batch 4

Conditioning index, hold index, supplier map, coverage and sterile pairs are computed over uses with `source` = an actor id only. `"world"` uses appear in the use profile (as their own column) and in the all-use DCNH, and nowhere else.

## Procedure

1. The directive author commits this file to the write repository root and updates the version line of the directive in `README.md`'s appendix to v1.2 with the three-value table substituted into Batch 2 step 1.
2. The R9 stop in `RECEIPTS/batch_2.md` is **cleared by this amendment**. The next session appends to that receipt a section headed "Cleared by Amendment A1" and re-attempts Batch 2 under the ruling. This counts as a fresh batch attempt: two proving failures allowed.
3. The continuation schedule is re-enabled with the same prompt.
4. If, under the ruling, every generated history shows zero uses with `source` = an actor id, that is the Batch 2 finding ("no cross-actor delivery observed in generated histories") and the batch still passes. Record it; Batch 3 proceeds. Whether to replace the Batch 1 generator with one that routes one actor's output into another's paid use is a separate ruling the author will issue after reading that finding.
