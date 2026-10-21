# DCNH two ways — Batch 7

**Readings:** wide = source.N + source_input + input.N (A3/A4); narrow = source.N + source_input only (Batch 7). Shared columns, including kept, are identical under both readings. New zero bins show where only the other reading has observations.

All-use rows are reconstructed from Batch 3 records and checked for exact
equality to the full Phase 7 conditioning_audit.observations row per actor.
The other view includes actor-sourced AND kept uses only, across all seats.
Axis order is (1,3), (2,4), (5,7), (6,8); formula order is D,C,N,H. All ties
are retained. A zero received-and-kept vector ties every cell and is absence
of input, not evidence of a subtype. No subtype assignment is made.
Agreement compares the complete observation, not just the largest-load label.
Use IDs refer to per_actor.md's trace in the same history.

| History | Actor | TIM | Status | View | Uses | Loads | Tilts | Axis cells | Greatest-load cells | Formula sums | Comparison | Use IDs | Reading |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| legacy-r4-seed-17 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u0, u1, u2, u3, u24, u25 | wide |
| legacy-r4-seed-17 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u0, u1, u2, u3, u24, u25 | narrow |
| legacy-r4-seed-17 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-17 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | narrow |
| legacy-r4-seed-17 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u13, u14, u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 | wide |
| legacy-r4-seed-17 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u13, u14, u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 | narrow |
| legacy-r4-seed-17 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-17 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | narrow |
| legacy-r4-seed-17 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u4, u5, u6, u7, u8, u9, u10, u11, u12, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 | wide |
| legacy-r4-seed-17 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u4, u5, u6, u7, u8, u9, u10, u11, u12, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 | narrow |
| legacy-r4-seed-17 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-17 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | narrow |
| legacy-r4-seed-29 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u0, u1, u2, u3, u24, u25 | wide |
| legacy-r4-seed-29 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u0, u1, u2, u3, u24, u25 | narrow |
| legacy-r4-seed-29 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-29 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | narrow |
| legacy-r4-seed-29 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 | wide |
| legacy-r4-seed-29 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 | narrow |
| legacy-r4-seed-29 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-29 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | narrow |
| legacy-r4-seed-29 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 | wide |
| legacy-r4-seed-29 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 | narrow |
| legacy-r4-seed-29 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-29 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | narrow |
| legacy-r4-seed-43 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u20, u21, u22, u23, u44, u45 | wide |
| legacy-r4-seed-43 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u20, u21, u22, u23, u44, u45 | narrow |
| legacy-r4-seed-43 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-43 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | narrow |
| legacy-r4-seed-43 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 | wide |
| legacy-r4-seed-43 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 | narrow |
| legacy-r4-seed-43 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-43 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | narrow |
| legacy-r4-seed-43 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 | wide |
| legacy-r4-seed-43 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 | narrow |
| legacy-r4-seed-43 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-43 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | narrow |
| legacy-r4-seed-61 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u20, u21, u22, u23, u44, u45 | wide |
| legacy-r4-seed-61 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u20, u21, u22, u23, u44, u45 | narrow |
| legacy-r4-seed-61 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-61 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | narrow |
| legacy-r4-seed-61 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 | wide |
| legacy-r4-seed-61 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 | narrow |
| legacy-r4-seed-61 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-61 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | narrow |
| legacy-r4-seed-61 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 | wide |
| legacy-r4-seed-61 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 | narrow |
| legacy-r4-seed-61 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | wide |
| legacy-r4-seed-61 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-17 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u0, u1, u2, u3, u24, u25 | wide |
| grade-v1-seed-17 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u0, u1, u2, u3, u24, u25 | narrow |
| grade-v1-seed-17 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-17 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-17 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u13, u14, u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 | wide |
| grade-v1-seed-17 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u13, u14, u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 | narrow |
| grade-v1-seed-17 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-17 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-17 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u4, u5, u6, u7, u8, u9, u10, u11, u12, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 | wide |
| grade-v1-seed-17 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u4, u5, u6, u7, u8, u9, u10, u11, u12, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 | narrow |
| grade-v1-seed-17 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-17 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-29 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u0, u1, u2, u3, u24, u25 | wide |
| grade-v1-seed-29 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u0, u1, u2, u3, u24, u25 | narrow |
| grade-v1-seed-29 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-29 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-29 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 | wide |
| grade-v1-seed-29 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 | narrow |
| grade-v1-seed-29 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-29 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-29 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 | wide |
| grade-v1-seed-29 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 | narrow |
| grade-v1-seed-29 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-29 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-43 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u20, u21, u22, u23, u44, u45 | wide |
| grade-v1-seed-43 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u20, u21, u22, u23, u44, u45 | narrow |
| grade-v1-seed-43 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-43 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-43 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 | wide |
| grade-v1-seed-43 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 | narrow |
| grade-v1-seed-43 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-43 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-43 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 | wide |
| grade-v1-seed-43 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 | narrow |
| grade-v1-seed-43 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-43 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-61 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u20, u21, u22, u23, u44, u45 | wide |
| grade-v1-seed-61 | workshop:alice | iee | active | all uses | 6 | 1,0,5,0 | -1,0,-5,0 | C,N,H,D | H | 1,1,0,5 | diverge | u20, u21, u22, u23, u44, u45 | narrow |
| grade-v1-seed-61 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-61 | workshop:alice | iee | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | C,N,H,D | C,N,H,D | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-61 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 | wide |
| grade-v1-seed-61 | workshop:bob | sli | active | all uses | 21 | 9,0,8,4 | -9,0,-8,-4 | H,D,C,N | H | 8,8,4,9 | diverge | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 | narrow |
| grade-v1-seed-61 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-61 | workshop:bob | sli | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | H,D,C,N | H,D,C,N | 0,0,0,0 | diverge | none | narrow |
| grade-v1-seed-61 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 | wide |
| grade-v1-seed-61 | workshop:eve | lie | active | all uses | 19 | 7,8,4,0 | 7,8,4,0 | D,H,N,C | H | 7,0,4,12 | diverge | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 | narrow |
| grade-v1-seed-61 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | wide |
| grade-v1-seed-61 | workshop:eve | lie | active | received and kept | 0 | 0,0,0,0 | 0,0,0,0 | D,H,N,C | D,H,N,C | 0,0,0,0 | diverge | none | narrow |
