# Per-actor measures — Batch 7

**Readings:** wide = source.N + source_input + input.N (A3/A4); narrow = source.N + source_input only (Batch 7). Shared columns, including kept, are identical under both readings. New zero bins show where only the other reading has observations.

Use IDs uN are zero-based occurrences in Batch 3's unchanged record sequence,
scoped to the History column. The use trace below links each to its committed
transaction, exact operation revision, and block completion boundary. Empty
ID lists mean zero observed uses, not missing histories. Inactive means zero
completed paid uses; such actors remain in population denominators.

**Batch 7 conditioning index:** received uses at dim <= 2 divided by ALL
uses at dim <= 2, per actor. The numerator IDs are listed; denominator IDs
are every row for that actor with Dim <= 2 in the use trace below.
Hold is kept received / received, across all seats. N/A denotes a zero denominator.
World and self are not received; they contribute to the weak-use denominator,
use profile/trace and all-use DCNH. No zero-denominator ratio is presented as zero.

## Actor indices

| History | Actor | TIM | Status | Conditioning wide | Hold wide | Conditioning numerator IDs wide | Received IDs wide | Kept received IDs wide | Conditioning narrow | Hold narrow | Conditioning numerator IDs narrow | Received IDs narrow | Kept received IDs narrow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| legacy-r4-seed-17 | workshop:alice | iee | active | 0/1 = 0 | 0/0 (N/A) | none | none | none | 0/1 = 0 | 0/0 (N/A) | none | none | none |
| legacy-r4-seed-17 | workshop:bob | sli | active | 0/9 = 0 | 0/0 (N/A) | none | none | none | 0/9 = 0 | 0/0 (N/A) | none | none | none |
| legacy-r4-seed-17 | workshop:eve | lie | active | 0/4 = 0 | 0/0 (N/A) | none | none | none | 0/4 = 0 | 0/0 (N/A) | none | none | none |
| legacy-r4-seed-29 | workshop:alice | iee | active | 0/1 = 0 | 0/0 (N/A) | none | none | none | 0/1 = 0 | 0/0 (N/A) | none | none | none |
| legacy-r4-seed-29 | workshop:bob | sli | active | 0/9 = 0 | 0/0 (N/A) | none | none | none | 0/9 = 0 | 0/0 (N/A) | none | none | none |
| legacy-r4-seed-29 | workshop:eve | lie | active | 0/4 = 0 | 0/0 (N/A) | none | none | none | 0/4 = 0 | 0/0 (N/A) | none | none | none |
| legacy-r4-seed-43 | workshop:alice | iee | active | 0/1 = 0 | 0/0 (N/A) | none | none | none | 0/1 = 0 | 0/0 (N/A) | none | none | none |
| legacy-r4-seed-43 | workshop:bob | sli | active | 0/9 = 0 | 0/0 (N/A) | none | none | none | 0/9 = 0 | 0/0 (N/A) | none | none | none |
| legacy-r4-seed-43 | workshop:eve | lie | active | 0/4 = 0 | 0/0 (N/A) | none | none | none | 0/4 = 0 | 0/0 (N/A) | none | none | none |
| legacy-r4-seed-61 | workshop:alice | iee | active | 0/1 = 0 | 0/0 (N/A) | none | none | none | 0/1 = 0 | 0/0 (N/A) | none | none | none |
| legacy-r4-seed-61 | workshop:bob | sli | active | 0/9 = 0 | 0/0 (N/A) | none | none | none | 0/9 = 0 | 0/0 (N/A) | none | none | none |
| legacy-r4-seed-61 | workshop:eve | lie | active | 0/4 = 0 | 0/0 (N/A) | none | none | none | 0/4 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-17 | workshop:alice | iee | active | 0/1 = 0 | 0/0 (N/A) | none | none | none | 0/1 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-17 | workshop:bob | sli | active | 0/9 = 0 | 0/0 (N/A) | none | none | none | 0/9 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-17 | workshop:eve | lie | active | 0/4 = 0 | 0/0 (N/A) | none | none | none | 0/4 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-29 | workshop:alice | iee | active | 0/1 = 0 | 0/0 (N/A) | none | none | none | 0/1 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-29 | workshop:bob | sli | active | 0/9 = 0 | 0/0 (N/A) | none | none | none | 0/9 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-29 | workshop:eve | lie | active | 0/4 = 0 | 0/0 (N/A) | none | none | none | 0/4 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-43 | workshop:alice | iee | active | 0/1 = 0 | 0/0 (N/A) | none | none | none | 0/1 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-43 | workshop:bob | sli | active | 0/9 = 0 | 0/0 (N/A) | none | none | none | 0/9 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-43 | workshop:eve | lie | active | 0/4 = 0 | 0/0 (N/A) | none | none | none | 0/4 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-61 | workshop:alice | iee | active | 0/1 = 0 | 0/0 (N/A) | none | none | none | 0/1 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-61 | workshop:bob | sli | active | 0/9 = 0 | 0/0 (N/A) | none | none | none | 0/9 = 0 | 0/0 (N/A) | none | none | none |
| grade-v1-seed-61 | workshop:eve | lie | active | 0/4 = 0 | 0/0 (N/A) | none | none | none | 0/4 = 0 | 0/0 (N/A) | none | none | none |

## Use profile

Bins present in either reading are printed; omitted (seat, source, kept) bins are zero in both.

| History | Actor | Seat | Source class | Kept (both) | Count wide | Use IDs wide | Count narrow | Use IDs narrow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| legacy-r4-seed-17 | workshop:alice | 3 | world | False | 1 | u0 | 1 | u0 |
| legacy-r4-seed-17 | workshop:alice | 7 | world | False | 1 | u25 | 1 | u25 |
| legacy-r4-seed-17 | workshop:alice | 7 | world | True | 4 | u1, u2, u3, u24 | 4 | u1, u2, u3, u24 |
| legacy-r4-seed-17 | workshop:bob | 3 | world | False | 1 | u45 | 1 | u45 |
| legacy-r4-seed-17 | workshop:bob | 3 | world | True | 8 | u13, u17, u18, u22, u23, u39, u40, u44 | 8 | u13, u17, u18, u22, u23, u39, u40, u44 |
| legacy-r4-seed-17 | workshop:bob | 7 | world | False | 1 | u43 | 1 | u43 |
| legacy-r4-seed-17 | workshop:bob | 7 | world | True | 7 | u14, u16, u19, u21, u36, u38, u41 | 7 | u14, u16, u19, u21, u36, u38, u41 |
| legacy-r4-seed-17 | workshop:bob | 8 | world | False | 1 | u42 | 1 | u42 |
| legacy-r4-seed-17 | workshop:bob | 8 | world | True | 3 | u15, u20, u37 | 3 | u15, u20, u37 |
| legacy-r4-seed-17 | workshop:eve | 1 | world | False | 1 | u33 | 1 | u33 |
| legacy-r4-seed-17 | workshop:eve | 1 | world | True | 6 | u5, u8, u10, u26, u28, u31 | 6 | u5, u8, u10, u26, u28, u31 |
| legacy-r4-seed-17 | workshop:eve | 2 | world | False | 1 | u35 | 1 | u35 |
| legacy-r4-seed-17 | workshop:eve | 2 | world | True | 7 | u6, u7, u11, u12, u29, u30, u34 | 7 | u6, u7, u11, u12, u29, u30, u34 |
| legacy-r4-seed-17 | workshop:eve | 5 | world | False | 1 | u32 | 1 | u32 |
| legacy-r4-seed-17 | workshop:eve | 5 | world | True | 3 | u4, u9, u27 | 3 | u4, u9, u27 |
| legacy-r4-seed-29 | workshop:alice | 3 | world | False | 1 | u0 | 1 | u0 |
| legacy-r4-seed-29 | workshop:alice | 7 | world | False | 1 | u25 | 1 | u25 |
| legacy-r4-seed-29 | workshop:alice | 7 | world | True | 4 | u1, u2, u3, u24 | 4 | u1, u2, u3, u24 |
| legacy-r4-seed-29 | workshop:bob | 3 | world | False | 1 | u35 | 1 | u35 |
| legacy-r4-seed-29 | workshop:bob | 3 | world | True | 8 | u4, u8, u9, u13, u14, u29, u30, u34 | 8 | u4, u8, u9, u13, u14, u29, u30, u34 |
| legacy-r4-seed-29 | workshop:bob | 7 | world | False | 1 | u33 | 1 | u33 |
| legacy-r4-seed-29 | workshop:bob | 7 | world | True | 7 | u5, u7, u10, u12, u26, u28, u31 | 7 | u5, u7, u10, u12, u26, u28, u31 |
| legacy-r4-seed-29 | workshop:bob | 8 | world | False | 1 | u32 | 1 | u32 |
| legacy-r4-seed-29 | workshop:bob | 8 | world | True | 3 | u6, u11, u27 | 3 | u6, u11, u27 |
| legacy-r4-seed-29 | workshop:eve | 1 | world | False | 1 | u43 | 1 | u43 |
| legacy-r4-seed-29 | workshop:eve | 1 | world | True | 6 | u16, u19, u21, u36, u38, u41 | 6 | u16, u19, u21, u36, u38, u41 |
| legacy-r4-seed-29 | workshop:eve | 2 | world | False | 1 | u45 | 1 | u45 |
| legacy-r4-seed-29 | workshop:eve | 2 | world | True | 7 | u17, u18, u22, u23, u39, u40, u44 | 7 | u17, u18, u22, u23, u39, u40, u44 |
| legacy-r4-seed-29 | workshop:eve | 5 | world | False | 1 | u42 | 1 | u42 |
| legacy-r4-seed-29 | workshop:eve | 5 | world | True | 3 | u15, u20, u37 | 3 | u15, u20, u37 |
| legacy-r4-seed-43 | workshop:alice | 3 | world | False | 1 | u20 | 1 | u20 |
| legacy-r4-seed-43 | workshop:alice | 7 | world | False | 1 | u45 | 1 | u45 |
| legacy-r4-seed-43 | workshop:alice | 7 | world | True | 4 | u21, u22, u23, u44 | 4 | u21, u22, u23, u44 |
| legacy-r4-seed-43 | workshop:bob | 3 | world | False | 1 | u43 | 1 | u43 |
| legacy-r4-seed-43 | workshop:bob | 3 | world | True | 8 | u9, u13, u14, u18, u19, u37, u38, u42 | 8 | u9, u13, u14, u18, u19, u37, u38, u42 |
| legacy-r4-seed-43 | workshop:bob | 7 | world | False | 1 | u41 | 1 | u41 |
| legacy-r4-seed-43 | workshop:bob | 7 | world | True | 7 | u10, u12, u15, u17, u34, u36, u39 | 7 | u10, u12, u15, u17, u34, u36, u39 |
| legacy-r4-seed-43 | workshop:bob | 8 | world | False | 1 | u40 | 1 | u40 |
| legacy-r4-seed-43 | workshop:bob | 8 | world | True | 3 | u11, u16, u35 | 3 | u11, u16, u35 |
| legacy-r4-seed-43 | workshop:eve | 1 | world | False | 1 | u31 | 1 | u31 |
| legacy-r4-seed-43 | workshop:eve | 1 | world | True | 6 | u1, u4, u6, u24, u26, u29 | 6 | u1, u4, u6, u24, u26, u29 |
| legacy-r4-seed-43 | workshop:eve | 2 | world | False | 1 | u33 | 1 | u33 |
| legacy-r4-seed-43 | workshop:eve | 2 | world | True | 7 | u2, u3, u7, u8, u27, u28, u32 | 7 | u2, u3, u7, u8, u27, u28, u32 |
| legacy-r4-seed-43 | workshop:eve | 5 | world | False | 1 | u30 | 1 | u30 |
| legacy-r4-seed-43 | workshop:eve | 5 | world | True | 3 | u0, u5, u25 | 3 | u0, u5, u25 |
| legacy-r4-seed-61 | workshop:alice | 3 | world | False | 1 | u20 | 1 | u20 |
| legacy-r4-seed-61 | workshop:alice | 7 | world | False | 1 | u45 | 1 | u45 |
| legacy-r4-seed-61 | workshop:alice | 7 | world | True | 4 | u21, u22, u23, u44 | 4 | u21, u22, u23, u44 |
| legacy-r4-seed-61 | workshop:bob | 3 | world | False | 1 | u43 | 1 | u43 |
| legacy-r4-seed-61 | workshop:bob | 3 | world | True | 8 | u9, u13, u14, u18, u19, u37, u38, u42 | 8 | u9, u13, u14, u18, u19, u37, u38, u42 |
| legacy-r4-seed-61 | workshop:bob | 7 | world | False | 1 | u41 | 1 | u41 |
| legacy-r4-seed-61 | workshop:bob | 7 | world | True | 7 | u10, u12, u15, u17, u34, u36, u39 | 7 | u10, u12, u15, u17, u34, u36, u39 |
| legacy-r4-seed-61 | workshop:bob | 8 | world | False | 1 | u40 | 1 | u40 |
| legacy-r4-seed-61 | workshop:bob | 8 | world | True | 3 | u11, u16, u35 | 3 | u11, u16, u35 |
| legacy-r4-seed-61 | workshop:eve | 1 | world | False | 1 | u31 | 1 | u31 |
| legacy-r4-seed-61 | workshop:eve | 1 | world | True | 6 | u1, u4, u6, u24, u26, u29 | 6 | u1, u4, u6, u24, u26, u29 |
| legacy-r4-seed-61 | workshop:eve | 2 | world | False | 1 | u33 | 1 | u33 |
| legacy-r4-seed-61 | workshop:eve | 2 | world | True | 7 | u2, u3, u7, u8, u27, u28, u32 | 7 | u2, u3, u7, u8, u27, u28, u32 |
| legacy-r4-seed-61 | workshop:eve | 5 | world | False | 1 | u30 | 1 | u30 |
| legacy-r4-seed-61 | workshop:eve | 5 | world | True | 3 | u0, u5, u25 | 3 | u0, u5, u25 |
| grade-v1-seed-17 | workshop:alice | 3 | world | False | 1 | u0 | 1 | u0 |
| grade-v1-seed-17 | workshop:alice | 7 | world | False | 1 | u25 | 1 | u25 |
| grade-v1-seed-17 | workshop:alice | 7 | world | True | 4 | u1, u2, u3, u24 | 4 | u1, u2, u3, u24 |
| grade-v1-seed-17 | workshop:bob | 3 | world | False | 1 | u45 | 1 | u45 |
| grade-v1-seed-17 | workshop:bob | 3 | world | True | 8 | u13, u17, u18, u22, u23, u39, u40, u44 | 8 | u13, u17, u18, u22, u23, u39, u40, u44 |
| grade-v1-seed-17 | workshop:bob | 7 | world | False | 1 | u43 | 1 | u43 |
| grade-v1-seed-17 | workshop:bob | 7 | world | True | 7 | u14, u16, u19, u21, u36, u38, u41 | 7 | u14, u16, u19, u21, u36, u38, u41 |
| grade-v1-seed-17 | workshop:bob | 8 | world | False | 1 | u42 | 1 | u42 |
| grade-v1-seed-17 | workshop:bob | 8 | world | True | 3 | u15, u20, u37 | 3 | u15, u20, u37 |
| grade-v1-seed-17 | workshop:eve | 1 | world | False | 1 | u33 | 1 | u33 |
| grade-v1-seed-17 | workshop:eve | 1 | world | True | 6 | u5, u8, u10, u26, u28, u31 | 6 | u5, u8, u10, u26, u28, u31 |
| grade-v1-seed-17 | workshop:eve | 2 | world | False | 1 | u35 | 1 | u35 |
| grade-v1-seed-17 | workshop:eve | 2 | world | True | 7 | u6, u7, u11, u12, u29, u30, u34 | 7 | u6, u7, u11, u12, u29, u30, u34 |
| grade-v1-seed-17 | workshop:eve | 5 | world | False | 1 | u32 | 1 | u32 |
| grade-v1-seed-17 | workshop:eve | 5 | world | True | 3 | u4, u9, u27 | 3 | u4, u9, u27 |
| grade-v1-seed-29 | workshop:alice | 3 | world | False | 1 | u0 | 1 | u0 |
| grade-v1-seed-29 | workshop:alice | 7 | world | False | 1 | u25 | 1 | u25 |
| grade-v1-seed-29 | workshop:alice | 7 | world | True | 4 | u1, u2, u3, u24 | 4 | u1, u2, u3, u24 |
| grade-v1-seed-29 | workshop:bob | 3 | world | False | 1 | u35 | 1 | u35 |
| grade-v1-seed-29 | workshop:bob | 3 | world | True | 8 | u4, u8, u9, u13, u14, u29, u30, u34 | 8 | u4, u8, u9, u13, u14, u29, u30, u34 |
| grade-v1-seed-29 | workshop:bob | 7 | world | False | 1 | u33 | 1 | u33 |
| grade-v1-seed-29 | workshop:bob | 7 | world | True | 7 | u5, u7, u10, u12, u26, u28, u31 | 7 | u5, u7, u10, u12, u26, u28, u31 |
| grade-v1-seed-29 | workshop:bob | 8 | world | False | 1 | u32 | 1 | u32 |
| grade-v1-seed-29 | workshop:bob | 8 | world | True | 3 | u6, u11, u27 | 3 | u6, u11, u27 |
| grade-v1-seed-29 | workshop:eve | 1 | world | False | 1 | u43 | 1 | u43 |
| grade-v1-seed-29 | workshop:eve | 1 | world | True | 6 | u16, u19, u21, u36, u38, u41 | 6 | u16, u19, u21, u36, u38, u41 |
| grade-v1-seed-29 | workshop:eve | 2 | world | False | 1 | u45 | 1 | u45 |
| grade-v1-seed-29 | workshop:eve | 2 | world | True | 7 | u17, u18, u22, u23, u39, u40, u44 | 7 | u17, u18, u22, u23, u39, u40, u44 |
| grade-v1-seed-29 | workshop:eve | 5 | world | False | 1 | u42 | 1 | u42 |
| grade-v1-seed-29 | workshop:eve | 5 | world | True | 3 | u15, u20, u37 | 3 | u15, u20, u37 |
| grade-v1-seed-43 | workshop:alice | 3 | world | False | 1 | u20 | 1 | u20 |
| grade-v1-seed-43 | workshop:alice | 7 | world | False | 1 | u45 | 1 | u45 |
| grade-v1-seed-43 | workshop:alice | 7 | world | True | 4 | u21, u22, u23, u44 | 4 | u21, u22, u23, u44 |
| grade-v1-seed-43 | workshop:bob | 3 | world | False | 1 | u43 | 1 | u43 |
| grade-v1-seed-43 | workshop:bob | 3 | world | True | 8 | u9, u13, u14, u18, u19, u37, u38, u42 | 8 | u9, u13, u14, u18, u19, u37, u38, u42 |
| grade-v1-seed-43 | workshop:bob | 7 | world | False | 1 | u41 | 1 | u41 |
| grade-v1-seed-43 | workshop:bob | 7 | world | True | 7 | u10, u12, u15, u17, u34, u36, u39 | 7 | u10, u12, u15, u17, u34, u36, u39 |
| grade-v1-seed-43 | workshop:bob | 8 | world | False | 1 | u40 | 1 | u40 |
| grade-v1-seed-43 | workshop:bob | 8 | world | True | 3 | u11, u16, u35 | 3 | u11, u16, u35 |
| grade-v1-seed-43 | workshop:eve | 1 | world | False | 1 | u31 | 1 | u31 |
| grade-v1-seed-43 | workshop:eve | 1 | world | True | 6 | u1, u4, u6, u24, u26, u29 | 6 | u1, u4, u6, u24, u26, u29 |
| grade-v1-seed-43 | workshop:eve | 2 | world | False | 1 | u33 | 1 | u33 |
| grade-v1-seed-43 | workshop:eve | 2 | world | True | 7 | u2, u3, u7, u8, u27, u28, u32 | 7 | u2, u3, u7, u8, u27, u28, u32 |
| grade-v1-seed-43 | workshop:eve | 5 | world | False | 1 | u30 | 1 | u30 |
| grade-v1-seed-43 | workshop:eve | 5 | world | True | 3 | u0, u5, u25 | 3 | u0, u5, u25 |
| grade-v1-seed-61 | workshop:alice | 3 | world | False | 1 | u20 | 1 | u20 |
| grade-v1-seed-61 | workshop:alice | 7 | world | False | 1 | u45 | 1 | u45 |
| grade-v1-seed-61 | workshop:alice | 7 | world | True | 4 | u21, u22, u23, u44 | 4 | u21, u22, u23, u44 |
| grade-v1-seed-61 | workshop:bob | 3 | world | False | 1 | u43 | 1 | u43 |
| grade-v1-seed-61 | workshop:bob | 3 | world | True | 8 | u9, u13, u14, u18, u19, u37, u38, u42 | 8 | u9, u13, u14, u18, u19, u37, u38, u42 |
| grade-v1-seed-61 | workshop:bob | 7 | world | False | 1 | u41 | 1 | u41 |
| grade-v1-seed-61 | workshop:bob | 7 | world | True | 7 | u10, u12, u15, u17, u34, u36, u39 | 7 | u10, u12, u15, u17, u34, u36, u39 |
| grade-v1-seed-61 | workshop:bob | 8 | world | False | 1 | u40 | 1 | u40 |
| grade-v1-seed-61 | workshop:bob | 8 | world | True | 3 | u11, u16, u35 | 3 | u11, u16, u35 |
| grade-v1-seed-61 | workshop:eve | 1 | world | False | 1 | u31 | 1 | u31 |
| grade-v1-seed-61 | workshop:eve | 1 | world | True | 6 | u1, u4, u6, u24, u26, u29 | 6 | u1, u4, u6, u24, u26, u29 |
| grade-v1-seed-61 | workshop:eve | 2 | world | False | 1 | u33 | 1 | u33 |
| grade-v1-seed-61 | workshop:eve | 2 | world | True | 7 | u2, u3, u7, u8, u27, u28, u32 | 7 | u2, u3, u7, u8, u27, u28, u32 |
| grade-v1-seed-61 | workshop:eve | 5 | world | False | 1 | u30 | 1 | u30 |
| grade-v1-seed-61 | workshop:eve | 5 | world | True | 3 | u0, u5, u25 | 3 | u0, u5, u25 |

## Weak-seat supplier map

Each dim <= 2 seat is listed, including empty supplier sets.

| History | Receiver | Seat | Supplier | Count wide | Use IDs wide | Count narrow | Use IDs narrow |
| --- | --- | --- | --- | --- | --- | --- | --- |
| legacy-r4-seed-17 | workshop:alice | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-17 | workshop:alice | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-17 | workshop:alice | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-17 | workshop:alice | 6 | none | 0 | none | 0 | none |
| legacy-r4-seed-17 | workshop:bob | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-17 | workshop:bob | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-17 | workshop:bob | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-17 | workshop:bob | 6 | none | 0 | none | 0 | none |
| legacy-r4-seed-17 | workshop:eve | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-17 | workshop:eve | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-17 | workshop:eve | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-17 | workshop:eve | 6 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:alice | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:alice | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:alice | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:alice | 6 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:bob | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:bob | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:bob | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:bob | 6 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:eve | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:eve | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:eve | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-29 | workshop:eve | 6 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:alice | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:alice | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:alice | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:alice | 6 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:bob | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:bob | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:bob | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:bob | 6 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:eve | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:eve | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:eve | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-43 | workshop:eve | 6 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:alice | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:alice | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:alice | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:alice | 6 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:bob | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:bob | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:bob | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:bob | 6 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:eve | 3 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:eve | 4 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:eve | 5 | none | 0 | none | 0 | none |
| legacy-r4-seed-61 | workshop:eve | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:alice | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:alice | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:alice | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:alice | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:bob | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:bob | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:bob | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:bob | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:eve | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:eve | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:eve | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-17 | workshop:eve | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:alice | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:alice | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:alice | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:alice | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:bob | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:bob | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:bob | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:bob | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:eve | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:eve | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:eve | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-29 | workshop:eve | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:alice | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:alice | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:alice | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:alice | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:bob | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:bob | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:bob | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:bob | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:eve | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:eve | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:eve | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-43 | workshop:eve | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:alice | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:alice | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:alice | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:alice | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:bob | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:bob | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:bob | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:bob | 6 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:eve | 3 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:eve | 4 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:eve | 5 | none | 0 | none | 0 | none |
| grade-v1-seed-61 | workshop:eve | 6 | none | 0 | none | 0 | none |

## Use trace

Transaction and episode indices are zero-based.

| History | Use ID | Transaction | Operation revision | Block end | Actor | Element | Seat | Dim | Source wide | Source narrow | Kept (both) | Episode |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| legacy-r4-seed-17 | u0 | 189 | u4.operation:b747d7c14f1e86239e7c65f21e006feace94434df175cc52c7c86cb47ee3cc7a@2 | 50 | workshop:alice | se | 3 | 2 | world | world | False | 0 |
| legacy-r4-seed-17 | u1 | 189 | u4.operation:b747d7c14f1e86239e7c65f21e006feace94434df175cc52c7c86cb47ee3cc7a@2 | 52 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-17 | u2 | 189 | u4.operation:b747d7c14f1e86239e7c65f21e006feace94434df175cc52c7c86cb47ee3cc7a@2 | 54 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-17 | u3 | 189 | u4.operation:b747d7c14f1e86239e7c65f21e006feace94434df175cc52c7c86cb47ee3cc7a@2 | 56 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-17 | u4 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 35 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| legacy-r4-seed-17 | u5 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 36 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-17 | u6 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 38 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-17 | u7 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 40 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-17 | u8 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 41 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-17 | u9 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 45 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| legacy-r4-seed-17 | u10 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 46 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-17 | u11 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 48 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-17 | u12 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 50 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-17 | u13 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-17 | u14 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-17 | u15 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 37 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| legacy-r4-seed-17 | u16 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 39 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-17 | u17 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-17 | u18 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-17 | u19 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 47 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-17 | u20 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 48 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| legacy-r4-seed-17 | u21 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 50 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-17 | u22 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 53 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-17 | u23 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 56 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-17 | u24 | 210 | u4.operation:04287b233b9a7e5c96df8b2961b706bb643b227f840f52e91e75da81f10a1ef8@2 | 49 | workshop:alice | ni | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-17 | u25 | 210 | u4.operation:04287b233b9a7e5c96df8b2961b706bb643b227f840f52e91e75da81f10a1ef8@2 | 51 | workshop:alice | ni | 7 | 3 | world | world | False | 1 |
| legacy-r4-seed-17 | u26 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 32 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-17 | u27 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 36 | workshop:eve | fi | 5 | 1 | world | world | True | 1 |
| legacy-r4-seed-17 | u28 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 37 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-17 | u29 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 39 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-17 | u30 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 41 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-17 | u31 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 42 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-17 | u32 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 46 | workshop:eve | fi | 5 | 1 | world | world | False | 1 |
| legacy-r4-seed-17 | u33 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 47 | workshop:eve | te | 1 | 4 | world | world | False | 1 |
| legacy-r4-seed-17 | u34 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 49 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-17 | u35 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 51 | workshop:eve | ni | 2 | 3 | world | world | False | 1 |
| legacy-r4-seed-17 | u36 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 33 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-17 | u37 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 34 | workshop:bob | ti | 8 | 4 | world | world | True | 1 |
| legacy-r4-seed-17 | u38 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-17 | u39 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 39 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-17 | u40 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-17 | u41 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 44 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-17 | u42 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 45 | workshop:bob | ti | 8 | 4 | world | world | False | 1 |
| legacy-r4-seed-17 | u43 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 47 | workshop:bob | se | 7 | 3 | world | world | False | 1 |
| legacy-r4-seed-17 | u44 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 50 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-17 | u45 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 53 | workshop:bob | ni | 3 | 2 | world | world | False | 1 |
| legacy-r4-seed-29 | u0 | 189 | u4.operation:26dede17d7af427fe64df6f75d43ce4eb0ee05251ff6e414c63a861c314a94d8@2 | 50 | workshop:alice | se | 3 | 2 | world | world | False | 0 |
| legacy-r4-seed-29 | u1 | 189 | u4.operation:26dede17d7af427fe64df6f75d43ce4eb0ee05251ff6e414c63a861c314a94d8@2 | 52 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-29 | u2 | 189 | u4.operation:26dede17d7af427fe64df6f75d43ce4eb0ee05251ff6e414c63a861c314a94d8@2 | 54 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-29 | u3 | 189 | u4.operation:26dede17d7af427fe64df6f75d43ce4eb0ee05251ff6e414c63a861c314a94d8@2 | 56 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-29 | u4 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 26 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-29 | u5 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 28 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-29 | u6 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 29 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| legacy-r4-seed-29 | u7 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 31 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-29 | u8 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-29 | u9 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 37 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-29 | u10 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 39 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-29 | u11 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 40 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| legacy-r4-seed-29 | u12 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 42 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-29 | u13 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-29 | u14 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 48 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-29 | u15 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 35 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| legacy-r4-seed-29 | u16 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 36 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-29 | u17 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 38 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-29 | u18 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 40 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-29 | u19 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 41 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-29 | u20 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 45 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| legacy-r4-seed-29 | u21 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 46 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-29 | u22 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 48 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-29 | u23 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 50 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-29 | u24 | 210 | u4.operation:bd3b4f88acdd62cf2f34127ec17f91af75e6d13abc89dfda90a01579aeda553b@2 | 49 | workshop:alice | ni | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-29 | u25 | 210 | u4.operation:bd3b4f88acdd62cf2f34127ec17f91af75e6d13abc89dfda90a01579aeda553b@2 | 51 | workshop:alice | ni | 7 | 3 | world | world | False | 1 |
| legacy-r4-seed-29 | u26 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 25 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-29 | u27 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 26 | workshop:bob | ti | 8 | 4 | world | world | True | 1 |
| legacy-r4-seed-29 | u28 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 28 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-29 | u29 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 31 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-29 | u30 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-29 | u31 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-29 | u32 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 37 | workshop:bob | ti | 8 | 4 | world | world | False | 1 |
| legacy-r4-seed-29 | u33 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 39 | workshop:bob | se | 7 | 3 | world | world | False | 1 |
| legacy-r4-seed-29 | u34 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-29 | u35 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | False | 1 |
| legacy-r4-seed-29 | u36 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 32 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-29 | u37 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 36 | workshop:eve | fi | 5 | 1 | world | world | True | 1 |
| legacy-r4-seed-29 | u38 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 37 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-29 | u39 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 39 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-29 | u40 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 41 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-29 | u41 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 42 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-29 | u42 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 46 | workshop:eve | fi | 5 | 1 | world | world | False | 1 |
| legacy-r4-seed-29 | u43 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 47 | workshop:eve | te | 1 | 4 | world | world | False | 1 |
| legacy-r4-seed-29 | u44 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 49 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-29 | u45 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 51 | workshop:eve | ni | 2 | 3 | world | world | False | 1 |
| legacy-r4-seed-43 | u0 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 49 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| legacy-r4-seed-43 | u1 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 50 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-43 | u2 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 52 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-43 | u3 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 54 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-43 | u4 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 55 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-43 | u5 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 59 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| legacy-r4-seed-43 | u6 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 60 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-43 | u7 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 62 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-43 | u8 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 64 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-43 | u9 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-43 | u10 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-43 | u11 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 37 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| legacy-r4-seed-43 | u12 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 39 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-43 | u13 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-43 | u14 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-43 | u15 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 47 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-43 | u16 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 48 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| legacy-r4-seed-43 | u17 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 50 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-43 | u18 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 53 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-43 | u19 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 56 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-43 | u20 | 193 | u4.operation:f1b63d59afd63daa4837580ca392405ccefc710f1d529a45f0c47d7a1f0ec08f@2 | 26 | workshop:alice | se | 3 | 2 | world | world | False | 0 |
| legacy-r4-seed-43 | u21 | 193 | u4.operation:f1b63d59afd63daa4837580ca392405ccefc710f1d529a45f0c47d7a1f0ec08f@2 | 28 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-43 | u22 | 193 | u4.operation:f1b63d59afd63daa4837580ca392405ccefc710f1d529a45f0c47d7a1f0ec08f@2 | 30 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-43 | u23 | 193 | u4.operation:f1b63d59afd63daa4837580ca392405ccefc710f1d529a45f0c47d7a1f0ec08f@2 | 32 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-43 | u24 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 46 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-43 | u25 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 50 | workshop:eve | fi | 5 | 1 | world | world | True | 1 |
| legacy-r4-seed-43 | u26 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 51 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-43 | u27 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 53 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-43 | u28 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 55 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-43 | u29 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 56 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-43 | u30 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 60 | workshop:eve | fi | 5 | 1 | world | world | False | 1 |
| legacy-r4-seed-43 | u31 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 61 | workshop:eve | te | 1 | 4 | world | world | False | 1 |
| legacy-r4-seed-43 | u32 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 63 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-43 | u33 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 65 | workshop:eve | ni | 2 | 3 | world | world | False | 1 |
| legacy-r4-seed-43 | u34 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 33 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-43 | u35 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 34 | workshop:bob | ti | 8 | 4 | world | world | True | 1 |
| legacy-r4-seed-43 | u36 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-43 | u37 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 39 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-43 | u38 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-43 | u39 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 44 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-43 | u40 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 45 | workshop:bob | ti | 8 | 4 | world | world | False | 1 |
| legacy-r4-seed-43 | u41 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 47 | workshop:bob | se | 7 | 3 | world | world | False | 1 |
| legacy-r4-seed-43 | u42 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 50 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-43 | u43 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 53 | workshop:bob | ni | 3 | 2 | world | world | False | 1 |
| legacy-r4-seed-43 | u44 | 214 | u4.operation:298fbc5b7e6abbc6996f16bbeaa7b37712eac5b0cb9edba5c696d5db318bf5f5@2 | 25 | workshop:alice | ni | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-43 | u45 | 214 | u4.operation:298fbc5b7e6abbc6996f16bbeaa7b37712eac5b0cb9edba5c696d5db318bf5f5@2 | 27 | workshop:alice | ni | 7 | 3 | world | world | False | 1 |
| legacy-r4-seed-61 | u0 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 49 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| legacy-r4-seed-61 | u1 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 50 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-61 | u2 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 52 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-61 | u3 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 54 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-61 | u4 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 55 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-61 | u5 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 59 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| legacy-r4-seed-61 | u6 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 60 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| legacy-r4-seed-61 | u7 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 62 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-61 | u8 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 64 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| legacy-r4-seed-61 | u9 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 26 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-61 | u10 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 28 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-61 | u11 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 29 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| legacy-r4-seed-61 | u12 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 31 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-61 | u13 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-61 | u14 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 37 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-61 | u15 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 39 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-61 | u16 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 40 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| legacy-r4-seed-61 | u17 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 42 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-61 | u18 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-61 | u19 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 48 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| legacy-r4-seed-61 | u20 | 193 | u4.operation:047dbf6d620d1784dbec9e7655691dd5985478ceb4fb50285270e5db3933d4c8@2 | 34 | workshop:alice | se | 3 | 2 | world | world | False | 0 |
| legacy-r4-seed-61 | u21 | 193 | u4.operation:047dbf6d620d1784dbec9e7655691dd5985478ceb4fb50285270e5db3933d4c8@2 | 36 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-61 | u22 | 193 | u4.operation:047dbf6d620d1784dbec9e7655691dd5985478ceb4fb50285270e5db3933d4c8@2 | 38 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-61 | u23 | 193 | u4.operation:047dbf6d620d1784dbec9e7655691dd5985478ceb4fb50285270e5db3933d4c8@2 | 40 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| legacy-r4-seed-61 | u24 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 46 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-61 | u25 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 50 | workshop:eve | fi | 5 | 1 | world | world | True | 1 |
| legacy-r4-seed-61 | u26 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 51 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-61 | u27 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 53 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-61 | u28 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 55 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-61 | u29 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 56 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| legacy-r4-seed-61 | u30 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 60 | workshop:eve | fi | 5 | 1 | world | world | False | 1 |
| legacy-r4-seed-61 | u31 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 61 | workshop:eve | te | 1 | 4 | world | world | False | 1 |
| legacy-r4-seed-61 | u32 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 63 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| legacy-r4-seed-61 | u33 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 65 | workshop:eve | ni | 2 | 3 | world | world | False | 1 |
| legacy-r4-seed-61 | u34 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 25 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-61 | u35 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 26 | workshop:bob | ti | 8 | 4 | world | world | True | 1 |
| legacy-r4-seed-61 | u36 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 28 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-61 | u37 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 31 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-61 | u38 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-61 | u39 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-61 | u40 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 37 | workshop:bob | ti | 8 | 4 | world | world | False | 1 |
| legacy-r4-seed-61 | u41 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 39 | workshop:bob | se | 7 | 3 | world | world | False | 1 |
| legacy-r4-seed-61 | u42 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| legacy-r4-seed-61 | u43 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | False | 1 |
| legacy-r4-seed-61 | u44 | 214 | u4.operation:df5aa119438b06e7568b46bbcfcbf633f32feb14ae8d32919aa355729ba10827@2 | 33 | workshop:alice | ni | 7 | 3 | world | world | True | 1 |
| legacy-r4-seed-61 | u45 | 214 | u4.operation:df5aa119438b06e7568b46bbcfcbf633f32feb14ae8d32919aa355729ba10827@2 | 35 | workshop:alice | ni | 7 | 3 | world | world | False | 1 |
| grade-v1-seed-17 | u0 | 189 | u4.operation:b747d7c14f1e86239e7c65f21e006feace94434df175cc52c7c86cb47ee3cc7a@2 | 50 | workshop:alice | se | 3 | 2 | world | world | False | 0 |
| grade-v1-seed-17 | u1 | 189 | u4.operation:b747d7c14f1e86239e7c65f21e006feace94434df175cc52c7c86cb47ee3cc7a@2 | 52 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-17 | u2 | 189 | u4.operation:b747d7c14f1e86239e7c65f21e006feace94434df175cc52c7c86cb47ee3cc7a@2 | 54 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-17 | u3 | 189 | u4.operation:b747d7c14f1e86239e7c65f21e006feace94434df175cc52c7c86cb47ee3cc7a@2 | 56 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-17 | u4 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 35 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| grade-v1-seed-17 | u5 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 36 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-17 | u6 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 38 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-17 | u7 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 40 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-17 | u8 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 41 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-17 | u9 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 45 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| grade-v1-seed-17 | u10 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 46 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-17 | u11 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 48 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-17 | u12 | 191 | u4.operation:7e25933621969476e1f728282c9d5cdcb7ce7ebf9da64c029c8e93f9f45b7720@2 | 50 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-17 | u13 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-17 | u14 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-17 | u15 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 37 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| grade-v1-seed-17 | u16 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 39 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-17 | u17 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-17 | u18 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-17 | u19 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 47 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-17 | u20 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 48 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| grade-v1-seed-17 | u21 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 50 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-17 | u22 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 53 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-17 | u23 | 193 | u4.operation:79d08fe66443b60609196cbc4f99ffada1db4596dea4a4446c1103a05f966132@2 | 56 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-17 | u24 | 210 | u4.operation:04287b233b9a7e5c96df8b2961b706bb643b227f840f52e91e75da81f10a1ef8@2 | 49 | workshop:alice | ni | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-17 | u25 | 210 | u4.operation:04287b233b9a7e5c96df8b2961b706bb643b227f840f52e91e75da81f10a1ef8@2 | 51 | workshop:alice | ni | 7 | 3 | world | world | False | 1 |
| grade-v1-seed-17 | u26 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 32 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-17 | u27 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 36 | workshop:eve | fi | 5 | 1 | world | world | True | 1 |
| grade-v1-seed-17 | u28 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 37 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-17 | u29 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 39 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-17 | u30 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 41 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-17 | u31 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 42 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-17 | u32 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 46 | workshop:eve | fi | 5 | 1 | world | world | False | 1 |
| grade-v1-seed-17 | u33 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 47 | workshop:eve | te | 1 | 4 | world | world | False | 1 |
| grade-v1-seed-17 | u34 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 49 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-17 | u35 | 212 | u4.operation:8b3d1ac3ee16ac17aa34aadbc7d6cee3c724b302caa0258e8ba121148a371a85@2 | 51 | workshop:eve | ni | 2 | 3 | world | world | False | 1 |
| grade-v1-seed-17 | u36 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 33 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-17 | u37 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 34 | workshop:bob | ti | 8 | 4 | world | world | True | 1 |
| grade-v1-seed-17 | u38 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-17 | u39 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 39 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-17 | u40 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-17 | u41 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 44 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-17 | u42 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 45 | workshop:bob | ti | 8 | 4 | world | world | False | 1 |
| grade-v1-seed-17 | u43 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 47 | workshop:bob | se | 7 | 3 | world | world | False | 1 |
| grade-v1-seed-17 | u44 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 50 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-17 | u45 | 214 | u4.operation:fd62f1354bcc049fcbbe6a2fad5624684cdc52706a176f67cdb5cad236363205@2 | 53 | workshop:bob | ni | 3 | 2 | world | world | False | 1 |
| grade-v1-seed-29 | u0 | 189 | u4.operation:26dede17d7af427fe64df6f75d43ce4eb0ee05251ff6e414c63a861c314a94d8@2 | 50 | workshop:alice | se | 3 | 2 | world | world | False | 0 |
| grade-v1-seed-29 | u1 | 189 | u4.operation:26dede17d7af427fe64df6f75d43ce4eb0ee05251ff6e414c63a861c314a94d8@2 | 52 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-29 | u2 | 189 | u4.operation:26dede17d7af427fe64df6f75d43ce4eb0ee05251ff6e414c63a861c314a94d8@2 | 54 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-29 | u3 | 189 | u4.operation:26dede17d7af427fe64df6f75d43ce4eb0ee05251ff6e414c63a861c314a94d8@2 | 56 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-29 | u4 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 26 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-29 | u5 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 28 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-29 | u6 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 29 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| grade-v1-seed-29 | u7 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 31 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-29 | u8 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-29 | u9 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 37 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-29 | u10 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 39 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-29 | u11 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 40 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| grade-v1-seed-29 | u12 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 42 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-29 | u13 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-29 | u14 | 191 | u4.operation:b158834b5307fa69fd8c92b38b315258b920e36483fa60b90d51d749db032d89@2 | 48 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-29 | u15 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 35 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| grade-v1-seed-29 | u16 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 36 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-29 | u17 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 38 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-29 | u18 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 40 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-29 | u19 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 41 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-29 | u20 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 45 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| grade-v1-seed-29 | u21 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 46 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-29 | u22 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 48 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-29 | u23 | 193 | u4.operation:e62fe641a8150650df582dc7e00221f2b669546090ce6d5540d6c9e81cd10362@2 | 50 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-29 | u24 | 210 | u4.operation:bd3b4f88acdd62cf2f34127ec17f91af75e6d13abc89dfda90a01579aeda553b@2 | 49 | workshop:alice | ni | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-29 | u25 | 210 | u4.operation:bd3b4f88acdd62cf2f34127ec17f91af75e6d13abc89dfda90a01579aeda553b@2 | 51 | workshop:alice | ni | 7 | 3 | world | world | False | 1 |
| grade-v1-seed-29 | u26 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 25 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-29 | u27 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 26 | workshop:bob | ti | 8 | 4 | world | world | True | 1 |
| grade-v1-seed-29 | u28 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 28 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-29 | u29 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 31 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-29 | u30 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-29 | u31 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-29 | u32 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 37 | workshop:bob | ti | 8 | 4 | world | world | False | 1 |
| grade-v1-seed-29 | u33 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 39 | workshop:bob | se | 7 | 3 | world | world | False | 1 |
| grade-v1-seed-29 | u34 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-29 | u35 | 212 | u4.operation:0d530258aac7fc6e8cf057001f3fe225d29b1b3a441e1a4d42026bbb9b70f750@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | False | 1 |
| grade-v1-seed-29 | u36 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 32 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-29 | u37 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 36 | workshop:eve | fi | 5 | 1 | world | world | True | 1 |
| grade-v1-seed-29 | u38 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 37 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-29 | u39 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 39 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-29 | u40 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 41 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-29 | u41 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 42 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-29 | u42 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 46 | workshop:eve | fi | 5 | 1 | world | world | False | 1 |
| grade-v1-seed-29 | u43 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 47 | workshop:eve | te | 1 | 4 | world | world | False | 1 |
| grade-v1-seed-29 | u44 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 49 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-29 | u45 | 214 | u4.operation:6f5971e63653a786c33f684cead286cf77005c11534d0563132bbf8e76ac7600@2 | 51 | workshop:eve | ni | 2 | 3 | world | world | False | 1 |
| grade-v1-seed-43 | u0 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 49 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| grade-v1-seed-43 | u1 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 50 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-43 | u2 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 52 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-43 | u3 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 54 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-43 | u4 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 55 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-43 | u5 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 59 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| grade-v1-seed-43 | u6 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 60 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-43 | u7 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 62 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-43 | u8 | 189 | u4.operation:6a772c52ceec33605cf2016912cf740b69851342ba4b5a20db330c58fde7182c@2 | 64 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-43 | u9 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-43 | u10 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-43 | u11 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 37 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| grade-v1-seed-43 | u12 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 39 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-43 | u13 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-43 | u14 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-43 | u15 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 47 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-43 | u16 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 48 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| grade-v1-seed-43 | u17 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 50 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-43 | u18 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 53 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-43 | u19 | 191 | u4.operation:4dea3c1f64cf440b6687a4db8ac07d2c7baede6495cd84989ae4cffd3106bbee@2 | 56 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-43 | u20 | 193 | u4.operation:f1b63d59afd63daa4837580ca392405ccefc710f1d529a45f0c47d7a1f0ec08f@2 | 26 | workshop:alice | se | 3 | 2 | world | world | False | 0 |
| grade-v1-seed-43 | u21 | 193 | u4.operation:f1b63d59afd63daa4837580ca392405ccefc710f1d529a45f0c47d7a1f0ec08f@2 | 28 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-43 | u22 | 193 | u4.operation:f1b63d59afd63daa4837580ca392405ccefc710f1d529a45f0c47d7a1f0ec08f@2 | 30 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-43 | u23 | 193 | u4.operation:f1b63d59afd63daa4837580ca392405ccefc710f1d529a45f0c47d7a1f0ec08f@2 | 32 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-43 | u24 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 46 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-43 | u25 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 50 | workshop:eve | fi | 5 | 1 | world | world | True | 1 |
| grade-v1-seed-43 | u26 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 51 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-43 | u27 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 53 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-43 | u28 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 55 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-43 | u29 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 56 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-43 | u30 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 60 | workshop:eve | fi | 5 | 1 | world | world | False | 1 |
| grade-v1-seed-43 | u31 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 61 | workshop:eve | te | 1 | 4 | world | world | False | 1 |
| grade-v1-seed-43 | u32 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 63 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-43 | u33 | 210 | u4.operation:98c02da843636a350d2266e5fe912aa8f0bc4b117e4dbcc34c60af1715bf197b@2 | 65 | workshop:eve | ni | 2 | 3 | world | world | False | 1 |
| grade-v1-seed-43 | u34 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 33 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-43 | u35 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 34 | workshop:bob | ti | 8 | 4 | world | world | True | 1 |
| grade-v1-seed-43 | u36 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-43 | u37 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 39 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-43 | u38 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-43 | u39 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 44 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-43 | u40 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 45 | workshop:bob | ti | 8 | 4 | world | world | False | 1 |
| grade-v1-seed-43 | u41 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 47 | workshop:bob | se | 7 | 3 | world | world | False | 1 |
| grade-v1-seed-43 | u42 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 50 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-43 | u43 | 212 | u4.operation:5f9450cd4167744050fb0d50d3b4af1c43219e8bda6c1645ac33e32b55590673@2 | 53 | workshop:bob | ni | 3 | 2 | world | world | False | 1 |
| grade-v1-seed-43 | u44 | 214 | u4.operation:298fbc5b7e6abbc6996f16bbeaa7b37712eac5b0cb9edba5c696d5db318bf5f5@2 | 25 | workshop:alice | ni | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-43 | u45 | 214 | u4.operation:298fbc5b7e6abbc6996f16bbeaa7b37712eac5b0cb9edba5c696d5db318bf5f5@2 | 27 | workshop:alice | ni | 7 | 3 | world | world | False | 1 |
| grade-v1-seed-61 | u0 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 49 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| grade-v1-seed-61 | u1 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 50 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-61 | u2 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 52 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-61 | u3 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 54 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-61 | u4 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 55 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-61 | u5 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 59 | workshop:eve | fi | 5 | 1 | world | world | True | 0 |
| grade-v1-seed-61 | u6 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 60 | workshop:eve | te | 1 | 4 | world | world | True | 0 |
| grade-v1-seed-61 | u7 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 62 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-61 | u8 | 189 | u4.operation:77bbbc0634e52b9ee8e5e9d15f52a8ba873eb367f926fbf80d4da14915c56aec@2 | 64 | workshop:eve | ni | 2 | 3 | world | world | True | 0 |
| grade-v1-seed-61 | u9 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 26 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-61 | u10 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 28 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-61 | u11 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 29 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| grade-v1-seed-61 | u12 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 31 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-61 | u13 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-61 | u14 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 37 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-61 | u15 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 39 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-61 | u16 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 40 | workshop:bob | ti | 8 | 4 | world | world | True | 0 |
| grade-v1-seed-61 | u17 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 42 | workshop:bob | se | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-61 | u18 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-61 | u19 | 191 | u4.operation:1cd7aaae87bcea868d68c017b3890fb9ead3eef0b3dc4e6cb88ed06a0004e2f9@2 | 48 | workshop:bob | ni | 3 | 2 | world | world | True | 0 |
| grade-v1-seed-61 | u20 | 193 | u4.operation:047dbf6d620d1784dbec9e7655691dd5985478ceb4fb50285270e5db3933d4c8@2 | 34 | workshop:alice | se | 3 | 2 | world | world | False | 0 |
| grade-v1-seed-61 | u21 | 193 | u4.operation:047dbf6d620d1784dbec9e7655691dd5985478ceb4fb50285270e5db3933d4c8@2 | 36 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-61 | u22 | 193 | u4.operation:047dbf6d620d1784dbec9e7655691dd5985478ceb4fb50285270e5db3933d4c8@2 | 38 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-61 | u23 | 193 | u4.operation:047dbf6d620d1784dbec9e7655691dd5985478ceb4fb50285270e5db3933d4c8@2 | 40 | workshop:alice | ni | 7 | 3 | world | world | True | 0 |
| grade-v1-seed-61 | u24 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 46 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-61 | u25 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 50 | workshop:eve | fi | 5 | 1 | world | world | True | 1 |
| grade-v1-seed-61 | u26 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 51 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-61 | u27 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 53 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-61 | u28 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 55 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-61 | u29 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 56 | workshop:eve | te | 1 | 4 | world | world | True | 1 |
| grade-v1-seed-61 | u30 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 60 | workshop:eve | fi | 5 | 1 | world | world | False | 1 |
| grade-v1-seed-61 | u31 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 61 | workshop:eve | te | 1 | 4 | world | world | False | 1 |
| grade-v1-seed-61 | u32 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 63 | workshop:eve | ni | 2 | 3 | world | world | True | 1 |
| grade-v1-seed-61 | u33 | 210 | u4.operation:6c320ad477390c0f13108c2a6ffbd0950bba30af68c88307b79d8acdd11db6f3@2 | 65 | workshop:eve | ni | 2 | 3 | world | world | False | 1 |
| grade-v1-seed-61 | u34 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 25 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-61 | u35 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 26 | workshop:bob | ti | 8 | 4 | world | world | True | 1 |
| grade-v1-seed-61 | u36 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 28 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-61 | u37 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 31 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-61 | u38 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 34 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-61 | u39 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 36 | workshop:bob | se | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-61 | u40 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 37 | workshop:bob | ti | 8 | 4 | world | world | False | 1 |
| grade-v1-seed-61 | u41 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 39 | workshop:bob | se | 7 | 3 | world | world | False | 1 |
| grade-v1-seed-61 | u42 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 42 | workshop:bob | ni | 3 | 2 | world | world | True | 1 |
| grade-v1-seed-61 | u43 | 212 | u4.operation:583b0c5980383b2c10e6513e9af62d4ea7af8a82b72583d73448464ce8bce0c5@2 | 45 | workshop:bob | ni | 3 | 2 | world | world | False | 1 |
| grade-v1-seed-61 | u44 | 214 | u4.operation:df5aa119438b06e7568b46bbcfcbf633f32feb14ae8d32919aa355729ba10827@2 | 33 | workshop:alice | ni | 7 | 3 | world | world | True | 1 |
| grade-v1-seed-61 | u45 | 214 | u4.operation:df5aa119438b06e7568b46bbcfcbf633f32feb14ae8d32919aa355729ba10827@2 | 35 | workshop:alice | ni | 7 | 3 | world | world | False | 1 |
