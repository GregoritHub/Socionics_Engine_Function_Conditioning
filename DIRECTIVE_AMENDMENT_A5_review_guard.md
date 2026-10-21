# Amendment A5 — rulings on the Batch 7 contradictions

Issued by the repository owner in the Batch 7 continuation on 20 October 2026.
Both rulings are authorized. This text preserves the owner's ruling.

## Ruling 1 — the guard is restated for Batch 7 only

Correcting the conditioning-index denominator necessarily changes Batch 1 tables and REPORT.md; byte-identity of those outputs is replaced by these invariants: (a) HISTORIES.json and HISTORIES_DELIVERY.json byte-unchanged; (b) every per-element count, every all-use DCNH row, every source classification (self/world/tuple), every kept value, and every row of the existing TABLES except the conditioning-index column reproduce byte-identically — verify by diffing the regenerated tables against the committed ones and asserting that the only differing cells are in that column; (c) Batch 1 histories still show zero tuple sources under both readings. Record the full before/after of the changed column in the receipt (you already have it: Alice 0/1, Bob 0/9, Eve 0/4 — note that 0/9 for Bob is itself the first finding of the corrected index: nine weak-seat uses, none received). tools/reproduce.py compares against the newly committed Batch 7 tree, not the Batch 6 one.

## Ruling 2 — path hygiene exempts history and patterns

The grep in §D and the proving command excludes: RECEIPTS/batch_*.md that predate Batch 7 (they are the audit trail and stay byte-unchanged), and the directive and amendment files themselves (they quote the patterns). Implement as: grep --exclude-dir=RECEIPTS --exclude='DIRECTIVE_*' --exclude='BATCH_DIRECTIVE_*' ; then separately assert that RECEIPTS/batch_7.md and every file created in Batch 7 contain no absolute path. RECEIPTS/README.md may note that early receipts contain pre-hygiene paths.

Proceed with Batch 7 under A5. Fresh two-failure allowance. Read repository stays untouched.
