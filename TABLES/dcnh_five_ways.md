# DCNH five ways — Batch 8

The Batch 4 two views (all uses; received and kept, per reading) are repeated
unchanged, followed by content-only and hop-only views. Margin is the greatest
axis load minus the runner-up: 0 when the greatest cell is tied, N/A when every
load is zero. All ties are retained; no threshold is applied; no subtype is
assigned. Axis order is (1,3), (2,4), (5,7), (6,8); formula order is D,C,N,H.

| History | Actor | TIM | Status | View | Reading | Uses | Loads | Axis cells | Greatest-load cells | Margin | Formula sums | Use IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| legacy-r4-seed-17 | workshop:alice | iee | active | all | both | 6 | 1,0,5,0 | C,N,H,D | H | 4 | 1,1,0,5 | u0, u1, u2, u3, u24, u25 |
| legacy-r4-seed-17 | workshop:alice | iee | active | received-kept | wide | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| legacy-r4-seed-17 | workshop:alice | iee | active | received-kept | narrow | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| legacy-r4-seed-17 | workshop:alice | iee | active | content-only | both | 4 | 0,0,4,0 | C,N,H,D | H | 4 | 0,0,0,4 | u2, u3, u24, u25 |
| legacy-r4-seed-17 | workshop:alice | iee | active | hop-only | both | 2 | 1,0,1,0 | C,N,H,D | C,H | 0 | 1,1,0,1 | u0, u1 |
| legacy-r4-seed-17 | workshop:bob | sli | active | all | both | 21 | 9,0,8,4 | H,D,C,N | H | 1 | 8,8,4,9 | u13, u14, u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 |
| legacy-r4-seed-17 | workshop:bob | sli | active | received-kept | wide | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| legacy-r4-seed-17 | workshop:bob | sli | active | received-kept | narrow | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| legacy-r4-seed-17 | workshop:bob | sli | active | content-only | both | 4 | 4,0,0,0 | H,D,C,N | H | 4 | 0,0,0,4 | u18, u23, u40, u45 |
| legacy-r4-seed-17 | workshop:bob | sli | active | hop-only | both | 17 | 5,0,8,4 | H,D,C,N | C | 3 | 8,8,4,5 | u13, u14, u15, u16, u17, u19, u20, u21, u22, u36, u37, u38, u39, u41, u42, u43, u44 |
| legacy-r4-seed-17 | workshop:eve | lie | active | all | both | 19 | 7,8,4,0 | D,H,N,C | H | 1 | 7,0,4,12 | u4, u5, u6, u7, u8, u9, u10, u11, u12, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 |
| legacy-r4-seed-17 | workshop:eve | lie | active | received-kept | wide | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| legacy-r4-seed-17 | workshop:eve | lie | active | received-kept | narrow | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| legacy-r4-seed-17 | workshop:eve | lie | active | content-only | both | 4 | 0,4,0,0 | D,H,N,C | H | 4 | 0,0,0,4 | u7, u12, u30, u35 |
| legacy-r4-seed-17 | workshop:eve | lie | active | hop-only | both | 15 | 7,4,4,0 | D,H,N,C | D | 3 | 7,0,4,8 | u4, u5, u6, u8, u9, u10, u11, u26, u27, u28, u29, u31, u32, u33, u34 |
| legacy-r4-seed-29 | workshop:alice | iee | active | all | both | 6 | 1,0,5,0 | C,N,H,D | H | 4 | 1,1,0,5 | u0, u1, u2, u3, u24, u25 |
| legacy-r4-seed-29 | workshop:alice | iee | active | received-kept | wide | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| legacy-r4-seed-29 | workshop:alice | iee | active | received-kept | narrow | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| legacy-r4-seed-29 | workshop:alice | iee | active | content-only | both | 4 | 0,0,4,0 | C,N,H,D | H | 4 | 0,0,0,4 | u2, u3, u24, u25 |
| legacy-r4-seed-29 | workshop:alice | iee | active | hop-only | both | 2 | 1,0,1,0 | C,N,H,D | C,H | 0 | 1,1,0,1 | u0, u1 |
| legacy-r4-seed-29 | workshop:bob | sli | active | all | both | 21 | 9,0,8,4 | H,D,C,N | H | 1 | 8,8,4,9 | u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 |
| legacy-r4-seed-29 | workshop:bob | sli | active | received-kept | wide | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| legacy-r4-seed-29 | workshop:bob | sli | active | received-kept | narrow | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| legacy-r4-seed-29 | workshop:bob | sli | active | content-only | both | 4 | 4,0,0,0 | H,D,C,N | H | 4 | 0,0,0,4 | u9, u14, u30, u35 |
| legacy-r4-seed-29 | workshop:bob | sli | active | hop-only | both | 17 | 5,0,8,4 | H,D,C,N | C | 3 | 8,8,4,5 | u4, u5, u6, u7, u8, u10, u11, u12, u13, u26, u27, u28, u29, u31, u32, u33, u34 |
| legacy-r4-seed-29 | workshop:eve | lie | active | all | both | 19 | 7,8,4,0 | D,H,N,C | H | 1 | 7,0,4,12 | u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 |
| legacy-r4-seed-29 | workshop:eve | lie | active | received-kept | wide | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| legacy-r4-seed-29 | workshop:eve | lie | active | received-kept | narrow | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| legacy-r4-seed-29 | workshop:eve | lie | active | content-only | both | 4 | 0,4,0,0 | D,H,N,C | H | 4 | 0,0,0,4 | u18, u23, u40, u45 |
| legacy-r4-seed-29 | workshop:eve | lie | active | hop-only | both | 15 | 7,4,4,0 | D,H,N,C | D | 3 | 7,0,4,8 | u15, u16, u17, u19, u20, u21, u22, u36, u37, u38, u39, u41, u42, u43, u44 |
| legacy-r4-seed-43 | workshop:alice | iee | active | all | both | 6 | 1,0,5,0 | C,N,H,D | H | 4 | 1,1,0,5 | u20, u21, u22, u23, u44, u45 |
| legacy-r4-seed-43 | workshop:alice | iee | active | received-kept | wide | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| legacy-r4-seed-43 | workshop:alice | iee | active | received-kept | narrow | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| legacy-r4-seed-43 | workshop:alice | iee | active | content-only | both | 4 | 0,0,4,0 | C,N,H,D | H | 4 | 0,0,0,4 | u22, u23, u44, u45 |
| legacy-r4-seed-43 | workshop:alice | iee | active | hop-only | both | 2 | 1,0,1,0 | C,N,H,D | C,H | 0 | 1,1,0,1 | u20, u21 |
| legacy-r4-seed-43 | workshop:bob | sli | active | all | both | 21 | 9,0,8,4 | H,D,C,N | H | 1 | 8,8,4,9 | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 |
| legacy-r4-seed-43 | workshop:bob | sli | active | received-kept | wide | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| legacy-r4-seed-43 | workshop:bob | sli | active | received-kept | narrow | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| legacy-r4-seed-43 | workshop:bob | sli | active | content-only | both | 4 | 4,0,0,0 | H,D,C,N | H | 4 | 0,0,0,4 | u14, u19, u38, u43 |
| legacy-r4-seed-43 | workshop:bob | sli | active | hop-only | both | 17 | 5,0,8,4 | H,D,C,N | C | 3 | 8,8,4,5 | u9, u10, u11, u12, u13, u15, u16, u17, u18, u34, u35, u36, u37, u39, u40, u41, u42 |
| legacy-r4-seed-43 | workshop:eve | lie | active | all | both | 19 | 7,8,4,0 | D,H,N,C | H | 1 | 7,0,4,12 | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 |
| legacy-r4-seed-43 | workshop:eve | lie | active | received-kept | wide | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| legacy-r4-seed-43 | workshop:eve | lie | active | received-kept | narrow | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| legacy-r4-seed-43 | workshop:eve | lie | active | content-only | both | 4 | 0,4,0,0 | D,H,N,C | H | 4 | 0,0,0,4 | u3, u8, u28, u33 |
| legacy-r4-seed-43 | workshop:eve | lie | active | hop-only | both | 15 | 7,4,4,0 | D,H,N,C | D | 3 | 7,0,4,8 | u0, u1, u2, u4, u5, u6, u7, u24, u25, u26, u27, u29, u30, u31, u32 |
| legacy-r4-seed-61 | workshop:alice | iee | active | all | both | 6 | 1,0,5,0 | C,N,H,D | H | 4 | 1,1,0,5 | u20, u21, u22, u23, u44, u45 |
| legacy-r4-seed-61 | workshop:alice | iee | active | received-kept | wide | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| legacy-r4-seed-61 | workshop:alice | iee | active | received-kept | narrow | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| legacy-r4-seed-61 | workshop:alice | iee | active | content-only | both | 4 | 0,0,4,0 | C,N,H,D | H | 4 | 0,0,0,4 | u22, u23, u44, u45 |
| legacy-r4-seed-61 | workshop:alice | iee | active | hop-only | both | 2 | 1,0,1,0 | C,N,H,D | C,H | 0 | 1,1,0,1 | u20, u21 |
| legacy-r4-seed-61 | workshop:bob | sli | active | all | both | 21 | 9,0,8,4 | H,D,C,N | H | 1 | 8,8,4,9 | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 |
| legacy-r4-seed-61 | workshop:bob | sli | active | received-kept | wide | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| legacy-r4-seed-61 | workshop:bob | sli | active | received-kept | narrow | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| legacy-r4-seed-61 | workshop:bob | sli | active | content-only | both | 4 | 4,0,0,0 | H,D,C,N | H | 4 | 0,0,0,4 | u14, u19, u38, u43 |
| legacy-r4-seed-61 | workshop:bob | sli | active | hop-only | both | 17 | 5,0,8,4 | H,D,C,N | C | 3 | 8,8,4,5 | u9, u10, u11, u12, u13, u15, u16, u17, u18, u34, u35, u36, u37, u39, u40, u41, u42 |
| legacy-r4-seed-61 | workshop:eve | lie | active | all | both | 19 | 7,8,4,0 | D,H,N,C | H | 1 | 7,0,4,12 | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 |
| legacy-r4-seed-61 | workshop:eve | lie | active | received-kept | wide | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| legacy-r4-seed-61 | workshop:eve | lie | active | received-kept | narrow | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| legacy-r4-seed-61 | workshop:eve | lie | active | content-only | both | 4 | 0,4,0,0 | D,H,N,C | H | 4 | 0,0,0,4 | u3, u8, u28, u33 |
| legacy-r4-seed-61 | workshop:eve | lie | active | hop-only | both | 15 | 7,4,4,0 | D,H,N,C | D | 3 | 7,0,4,8 | u0, u1, u2, u4, u5, u6, u7, u24, u25, u26, u27, u29, u30, u31, u32 |
| grade-v1-seed-17 | workshop:alice | iee | active | all | both | 6 | 1,0,5,0 | C,N,H,D | H | 4 | 1,1,0,5 | u0, u1, u2, u3, u24, u25 |
| grade-v1-seed-17 | workshop:alice | iee | active | received-kept | wide | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| grade-v1-seed-17 | workshop:alice | iee | active | received-kept | narrow | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| grade-v1-seed-17 | workshop:alice | iee | active | content-only | both | 4 | 0,0,4,0 | C,N,H,D | H | 4 | 0,0,0,4 | u2, u3, u24, u25 |
| grade-v1-seed-17 | workshop:alice | iee | active | hop-only | both | 2 | 1,0,1,0 | C,N,H,D | C,H | 0 | 1,1,0,1 | u0, u1 |
| grade-v1-seed-17 | workshop:bob | sli | active | all | both | 21 | 9,0,8,4 | H,D,C,N | H | 1 | 8,8,4,9 | u13, u14, u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 |
| grade-v1-seed-17 | workshop:bob | sli | active | received-kept | wide | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| grade-v1-seed-17 | workshop:bob | sli | active | received-kept | narrow | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| grade-v1-seed-17 | workshop:bob | sli | active | content-only | both | 4 | 4,0,0,0 | H,D,C,N | H | 4 | 0,0,0,4 | u18, u23, u40, u45 |
| grade-v1-seed-17 | workshop:bob | sli | active | hop-only | both | 17 | 5,0,8,4 | H,D,C,N | C | 3 | 8,8,4,5 | u13, u14, u15, u16, u17, u19, u20, u21, u22, u36, u37, u38, u39, u41, u42, u43, u44 |
| grade-v1-seed-17 | workshop:eve | lie | active | all | both | 19 | 7,8,4,0 | D,H,N,C | H | 1 | 7,0,4,12 | u4, u5, u6, u7, u8, u9, u10, u11, u12, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 |
| grade-v1-seed-17 | workshop:eve | lie | active | received-kept | wide | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| grade-v1-seed-17 | workshop:eve | lie | active | received-kept | narrow | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| grade-v1-seed-17 | workshop:eve | lie | active | content-only | both | 4 | 0,4,0,0 | D,H,N,C | H | 4 | 0,0,0,4 | u7, u12, u30, u35 |
| grade-v1-seed-17 | workshop:eve | lie | active | hop-only | both | 15 | 7,4,4,0 | D,H,N,C | D | 3 | 7,0,4,8 | u4, u5, u6, u8, u9, u10, u11, u26, u27, u28, u29, u31, u32, u33, u34 |
| grade-v1-seed-29 | workshop:alice | iee | active | all | both | 6 | 1,0,5,0 | C,N,H,D | H | 4 | 1,1,0,5 | u0, u1, u2, u3, u24, u25 |
| grade-v1-seed-29 | workshop:alice | iee | active | received-kept | wide | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| grade-v1-seed-29 | workshop:alice | iee | active | received-kept | narrow | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| grade-v1-seed-29 | workshop:alice | iee | active | content-only | both | 4 | 0,0,4,0 | C,N,H,D | H | 4 | 0,0,0,4 | u2, u3, u24, u25 |
| grade-v1-seed-29 | workshop:alice | iee | active | hop-only | both | 2 | 1,0,1,0 | C,N,H,D | C,H | 0 | 1,1,0,1 | u0, u1 |
| grade-v1-seed-29 | workshop:bob | sli | active | all | both | 21 | 9,0,8,4 | H,D,C,N | H | 1 | 8,8,4,9 | u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u26, u27, u28, u29, u30, u31, u32, u33, u34, u35 |
| grade-v1-seed-29 | workshop:bob | sli | active | received-kept | wide | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| grade-v1-seed-29 | workshop:bob | sli | active | received-kept | narrow | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| grade-v1-seed-29 | workshop:bob | sli | active | content-only | both | 4 | 4,0,0,0 | H,D,C,N | H | 4 | 0,0,0,4 | u9, u14, u30, u35 |
| grade-v1-seed-29 | workshop:bob | sli | active | hop-only | both | 17 | 5,0,8,4 | H,D,C,N | C | 3 | 8,8,4,5 | u4, u5, u6, u7, u8, u10, u11, u12, u13, u26, u27, u28, u29, u31, u32, u33, u34 |
| grade-v1-seed-29 | workshop:eve | lie | active | all | both | 19 | 7,8,4,0 | D,H,N,C | H | 1 | 7,0,4,12 | u15, u16, u17, u18, u19, u20, u21, u22, u23, u36, u37, u38, u39, u40, u41, u42, u43, u44, u45 |
| grade-v1-seed-29 | workshop:eve | lie | active | received-kept | wide | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| grade-v1-seed-29 | workshop:eve | lie | active | received-kept | narrow | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| grade-v1-seed-29 | workshop:eve | lie | active | content-only | both | 4 | 0,4,0,0 | D,H,N,C | H | 4 | 0,0,0,4 | u18, u23, u40, u45 |
| grade-v1-seed-29 | workshop:eve | lie | active | hop-only | both | 15 | 7,4,4,0 | D,H,N,C | D | 3 | 7,0,4,8 | u15, u16, u17, u19, u20, u21, u22, u36, u37, u38, u39, u41, u42, u43, u44 |
| grade-v1-seed-43 | workshop:alice | iee | active | all | both | 6 | 1,0,5,0 | C,N,H,D | H | 4 | 1,1,0,5 | u20, u21, u22, u23, u44, u45 |
| grade-v1-seed-43 | workshop:alice | iee | active | received-kept | wide | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| grade-v1-seed-43 | workshop:alice | iee | active | received-kept | narrow | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| grade-v1-seed-43 | workshop:alice | iee | active | content-only | both | 4 | 0,0,4,0 | C,N,H,D | H | 4 | 0,0,0,4 | u22, u23, u44, u45 |
| grade-v1-seed-43 | workshop:alice | iee | active | hop-only | both | 2 | 1,0,1,0 | C,N,H,D | C,H | 0 | 1,1,0,1 | u20, u21 |
| grade-v1-seed-43 | workshop:bob | sli | active | all | both | 21 | 9,0,8,4 | H,D,C,N | H | 1 | 8,8,4,9 | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 |
| grade-v1-seed-43 | workshop:bob | sli | active | received-kept | wide | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| grade-v1-seed-43 | workshop:bob | sli | active | received-kept | narrow | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| grade-v1-seed-43 | workshop:bob | sli | active | content-only | both | 4 | 4,0,0,0 | H,D,C,N | H | 4 | 0,0,0,4 | u14, u19, u38, u43 |
| grade-v1-seed-43 | workshop:bob | sli | active | hop-only | both | 17 | 5,0,8,4 | H,D,C,N | C | 3 | 8,8,4,5 | u9, u10, u11, u12, u13, u15, u16, u17, u18, u34, u35, u36, u37, u39, u40, u41, u42 |
| grade-v1-seed-43 | workshop:eve | lie | active | all | both | 19 | 7,8,4,0 | D,H,N,C | H | 1 | 7,0,4,12 | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 |
| grade-v1-seed-43 | workshop:eve | lie | active | received-kept | wide | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| grade-v1-seed-43 | workshop:eve | lie | active | received-kept | narrow | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| grade-v1-seed-43 | workshop:eve | lie | active | content-only | both | 4 | 0,4,0,0 | D,H,N,C | H | 4 | 0,0,0,4 | u3, u8, u28, u33 |
| grade-v1-seed-43 | workshop:eve | lie | active | hop-only | both | 15 | 7,4,4,0 | D,H,N,C | D | 3 | 7,0,4,8 | u0, u1, u2, u4, u5, u6, u7, u24, u25, u26, u27, u29, u30, u31, u32 |
| grade-v1-seed-61 | workshop:alice | iee | active | all | both | 6 | 1,0,5,0 | C,N,H,D | H | 4 | 1,1,0,5 | u20, u21, u22, u23, u44, u45 |
| grade-v1-seed-61 | workshop:alice | iee | active | received-kept | wide | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| grade-v1-seed-61 | workshop:alice | iee | active | received-kept | narrow | 0 | 0,0,0,0 | C,N,H,D | C,N,H,D | N/A | 0,0,0,0 | none |
| grade-v1-seed-61 | workshop:alice | iee | active | content-only | both | 4 | 0,0,4,0 | C,N,H,D | H | 4 | 0,0,0,4 | u22, u23, u44, u45 |
| grade-v1-seed-61 | workshop:alice | iee | active | hop-only | both | 2 | 1,0,1,0 | C,N,H,D | C,H | 0 | 1,1,0,1 | u20, u21 |
| grade-v1-seed-61 | workshop:bob | sli | active | all | both | 21 | 9,0,8,4 | H,D,C,N | H | 1 | 8,8,4,9 | u9, u10, u11, u12, u13, u14, u15, u16, u17, u18, u19, u34, u35, u36, u37, u38, u39, u40, u41, u42, u43 |
| grade-v1-seed-61 | workshop:bob | sli | active | received-kept | wide | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| grade-v1-seed-61 | workshop:bob | sli | active | received-kept | narrow | 0 | 0,0,0,0 | H,D,C,N | H,D,C,N | N/A | 0,0,0,0 | none |
| grade-v1-seed-61 | workshop:bob | sli | active | content-only | both | 4 | 4,0,0,0 | H,D,C,N | H | 4 | 0,0,0,4 | u14, u19, u38, u43 |
| grade-v1-seed-61 | workshop:bob | sli | active | hop-only | both | 17 | 5,0,8,4 | H,D,C,N | C | 3 | 8,8,4,5 | u9, u10, u11, u12, u13, u15, u16, u17, u18, u34, u35, u36, u37, u39, u40, u41, u42 |
| grade-v1-seed-61 | workshop:eve | lie | active | all | both | 19 | 7,8,4,0 | D,H,N,C | H | 1 | 7,0,4,12 | u0, u1, u2, u3, u4, u5, u6, u7, u8, u24, u25, u26, u27, u28, u29, u30, u31, u32, u33 |
| grade-v1-seed-61 | workshop:eve | lie | active | received-kept | wide | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| grade-v1-seed-61 | workshop:eve | lie | active | received-kept | narrow | 0 | 0,0,0,0 | D,H,N,C | D,H,N,C | N/A | 0,0,0,0 | none |
| grade-v1-seed-61 | workshop:eve | lie | active | content-only | both | 4 | 0,4,0,0 | D,H,N,C | H | 4 | 0,0,0,4 | u3, u8, u28, u33 |
| grade-v1-seed-61 | workshop:eve | lie | active | hop-only | both | 15 | 7,4,4,0 | D,H,N,C | D | 3 | 7,0,4,8 | u0, u1, u2, u4, u5, u6, u7, u24, u25, u26, u27, u29, u30, u31, u32 |
