# Directive Amendment A2 — I4 restated

Applies to: Batch Directive — Function Conditioning Ledger v2, v1.2 → v1.3
Issued: 20 October 2026, on the Batch 3 contradiction reported by the executor
Authority: directive author. Ruling, not repair.

## Ruling

The executor's analysis is correct and the correction it recommends is **authorized**.

The fixed definition of `kept` stands unchanged: a use is kept when the same actor later completes another paid use at the same seat of the same element within the same history. Under that definition the *last* use at any (actor, seat) is always `kept = False`, so a sequence ending `[…, True, False]` is the normal case, not a violation. I4 as written forbade it. I4 was wrong.

**I4, restated:** `kept` is monotone under history growth. For any prefix of a history and the full history, every use present in the prefix with `kept = True` has `kept = True` in the full history. Appending transactions can change a use from False to True, never from True to False.

## Test for I4 (replaces the Batch 3 I4 test)

- **positive:** for each generated history, compute `kept` on the first half of its transactions and on the whole; assert every prefix-True use is whole-True.
- **positive:** a history where an actor repeats a seat shows `kept = True` on every use at that seat except the last, and `False` on the last.
- **negative:** a forged reordering that places a repeat *before* the use it would mark is rejected (retention cannot point backward in transaction order).

The remaining Batch 3 witnesses are unchanged.

## Procedure

1. Author commits this file to the write repository root and bumps the directive appendix to v1.3, substituting the restated I4 into Batch 3.
2. This clears the Batch 3 question. The next session proceeds with Batch 3 under the restated I4 with a fresh two-failure allowance.
3. No file in the read repository is touched.
