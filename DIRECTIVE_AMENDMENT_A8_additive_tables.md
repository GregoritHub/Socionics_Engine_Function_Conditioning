# Amendment A8 — Batch 8 columns live in new tables

Issued by the directive author on 20 October 2026, before Batch 8 began.

Batch 8 §8.4 says new columns are appended to the existing per-actor tables.
The Batch 7 preservation guard (`tests/test_07_review.py`, `verify_preserved`)
compares regenerated headings and wide cells with the accepted tables and
rejects any added heading. Rather than weaken that guard, A8 rules:

1. No existing file under `TABLES/` changes by one byte. Every Batch 8 measure
   is written to new files: `classes`, `price_of_type`, `dcnh_five_ways`, with
   the existing composition prefix and `_delivery` suffix conventions.
2. `REPORT.md` and `REPORT_DELIVERY.md` gain one trailing section, `## 8.`;
   the text above that heading is byte-identical to Batch 7.
3. `verify_preserved` keeps its Batch 7 base. A second guard in
   `tests/test_08_classes.py` compares every Batch 7 table, both reports'
   Batch 7 text, and receipts 0–7 with commit `3fffd9b`.
4. The use trace is not extended; the class trace is a separate table aligned
   by use ID.

Everything else in Batch 8 stands as written.
