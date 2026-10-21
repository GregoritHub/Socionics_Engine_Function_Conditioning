# Use classes — Batch 8

A paid use is a hop (an arrival along route.{i}.path.{n}, n >= 1) or a content
block (the route's seat-content work). Conditioning by class is received weak
uses of that class / all weak uses of that class; hold by class is kept received
/ received of that class. Internalisation is received uses later followed by a
self- or world-sourced use at the same seat and element / received uses; it is
reported per weak seat below. Observed suppliers are listed only where the
supplier completed a content block at that element earlier in the history.
Use IDs refer to per_actor's trace in the same history. N/A is a zero denominator.

## Conditioning, hold and internalisation by class

| History | Actor | TIM | Status | Class | Conditioning wide | Conditioning narrow | Hold wide | Hold narrow | Conditioning numerator IDs | Kept received IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair-seed-17 | workshop:alice | iee | active | hop | 25/46 = 25/46 | 0/46 = 0 | 25/25 = 1 | 0/0 (N/A) | u49, u51, u53, u54, u56, u58, u59, u61, u63, u65, u75, u77, u79, u80, u82, u84, u85, u87, u89, u90, u92, u129, u131, u133, u135 | u49, u51, u53, u54, u56, u58, u59, u61, u63, u65, u75, u77, u79, u80, u82, u84, u85, u87, u89, u90, u92, u129, u131, u133, u135 |
| pair-seed-17 | workshop:alice | iee | active | content | 20/38 = 10/19 | 0/38 = 0 | 18/20 = 9/10 | 0/0 (N/A) | u50, u52, u55, u57, u60, u62, u64, u66, u76, u78, u81, u83, u86, u88, u91, u93, u130, u132, u134, u136 | u50, u52, u55, u57, u60, u62, u64, u66, u76, u78, u81, u83, u86, u88, u91, u93, u130, u132 |
| pair-seed-17 | workshop:alice | iee | active | internalisation | 0/45 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-seed-17 | workshop:bob | sli | active | hop | 12/12 = 1 | 0/12 = 0 | 38/40 = 19/20 | 0/0 (N/A) | u41, u46, u67, u72, u94, u99, u103, u108, u112, u117, u121, u126 | u40, u41, u42, u43, u45, u46, u47, u67, u68, u69, u71, u72, u73, u94, u95, u96, u98, u99, u100, u102, u103, u104, u105, u107, u108, u109, u111, u112, u113, u114, u116, u118, u120, u121, u122, u123, u125, u127 |
| pair-seed-17 | workshop:bob | sli | active | content | 0/0 (N/A) | 0/0 (N/A) | 10/12 = 5/6 | 0/0 (N/A) | none | u44, u48, u70, u74, u97, u101, u106, u110, u115, u119 |
| pair-seed-17 | workshop:bob | sli | active | internalisation | 0/52 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-seed-17 | workshop:eve | sli | inactive | hop | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-seed-17 | workshop:eve | sli | inactive | content | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-seed-17 | workshop:eve | sli | inactive | internalisation | 0/0 (N/A) | 0/0 (N/A) |  |  | none |  |
| pair-seed-29 | workshop:alice | iee | active | hop | 25/46 = 25/46 | 0/46 = 0 | 25/25 = 1 | 0/0 (N/A) | u49, u51, u53, u54, u56, u58, u59, u61, u63, u65, u75, u77, u79, u80, u82, u84, u85, u87, u89, u90, u92, u129, u131, u133, u135 | u49, u51, u53, u54, u56, u58, u59, u61, u63, u65, u75, u77, u79, u80, u82, u84, u85, u87, u89, u90, u92, u129, u131, u133, u135 |
| pair-seed-29 | workshop:alice | iee | active | content | 20/38 = 10/19 | 0/38 = 0 | 18/20 = 9/10 | 0/0 (N/A) | u50, u52, u55, u57, u60, u62, u64, u66, u76, u78, u81, u83, u86, u88, u91, u93, u130, u132, u134, u136 | u50, u52, u55, u57, u60, u62, u64, u66, u76, u78, u81, u83, u86, u88, u91, u93, u130, u132 |
| pair-seed-29 | workshop:alice | iee | active | internalisation | 0/45 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-seed-29 | workshop:bob | sli | active | hop | 12/12 = 1 | 0/12 = 0 | 38/40 = 19/20 | 0/0 (N/A) | u41, u46, u67, u72, u94, u99, u103, u108, u112, u117, u121, u126 | u40, u41, u42, u43, u45, u46, u47, u67, u68, u69, u71, u72, u73, u94, u95, u96, u98, u99, u100, u102, u103, u104, u105, u107, u108, u109, u111, u112, u113, u114, u116, u118, u120, u121, u122, u123, u125, u127 |
| pair-seed-29 | workshop:bob | sli | active | content | 0/0 (N/A) | 0/0 (N/A) | 10/12 = 5/6 | 0/0 (N/A) | none | u44, u48, u70, u74, u97, u101, u106, u110, u115, u119 |
| pair-seed-29 | workshop:bob | sli | active | internalisation | 0/52 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-seed-29 | workshop:eve | sli | inactive | hop | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-seed-29 | workshop:eve | sli | inactive | content | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-seed-29 | workshop:eve | sli | inactive | internalisation | 0/0 (N/A) | 0/0 (N/A) |  |  | none |  |
| pair-seed-43 | workshop:alice | iee | active | hop | 25/46 = 25/46 | 0/46 = 0 | 25/25 = 1 | 0/0 (N/A) | u49, u51, u53, u54, u56, u58, u59, u61, u63, u65, u75, u77, u79, u80, u82, u84, u85, u87, u89, u90, u92, u129, u131, u133, u135 | u49, u51, u53, u54, u56, u58, u59, u61, u63, u65, u75, u77, u79, u80, u82, u84, u85, u87, u89, u90, u92, u129, u131, u133, u135 |
| pair-seed-43 | workshop:alice | iee | active | content | 20/38 = 10/19 | 0/38 = 0 | 18/20 = 9/10 | 0/0 (N/A) | u50, u52, u55, u57, u60, u62, u64, u66, u76, u78, u81, u83, u86, u88, u91, u93, u130, u132, u134, u136 | u50, u52, u55, u57, u60, u62, u64, u66, u76, u78, u81, u83, u86, u88, u91, u93, u130, u132 |
| pair-seed-43 | workshop:alice | iee | active | internalisation | 0/45 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-seed-43 | workshop:bob | sli | active | hop | 12/12 = 1 | 0/12 = 0 | 38/40 = 19/20 | 0/0 (N/A) | u41, u46, u67, u72, u94, u99, u103, u108, u112, u117, u121, u126 | u40, u41, u42, u43, u45, u46, u47, u67, u68, u69, u71, u72, u73, u94, u95, u96, u98, u99, u100, u102, u103, u104, u105, u107, u108, u109, u111, u112, u113, u114, u116, u118, u120, u121, u122, u123, u125, u127 |
| pair-seed-43 | workshop:bob | sli | active | content | 0/0 (N/A) | 0/0 (N/A) | 10/12 = 5/6 | 0/0 (N/A) | none | u44, u48, u70, u74, u97, u101, u106, u110, u115, u119 |
| pair-seed-43 | workshop:bob | sli | active | internalisation | 0/52 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-seed-43 | workshop:eve | sli | inactive | hop | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-seed-43 | workshop:eve | sli | inactive | content | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-seed-43 | workshop:eve | sli | inactive | internalisation | 0/0 (N/A) | 0/0 (N/A) |  |  | none |  |
| pair-seed-61 | workshop:alice | iee | active | hop | 25/46 = 25/46 | 0/46 = 0 | 25/25 = 1 | 0/0 (N/A) | u49, u51, u53, u54, u56, u58, u59, u61, u63, u65, u75, u77, u79, u80, u82, u84, u85, u87, u89, u90, u92, u129, u131, u133, u135 | u49, u51, u53, u54, u56, u58, u59, u61, u63, u65, u75, u77, u79, u80, u82, u84, u85, u87, u89, u90, u92, u129, u131, u133, u135 |
| pair-seed-61 | workshop:alice | iee | active | content | 20/38 = 10/19 | 0/38 = 0 | 18/20 = 9/10 | 0/0 (N/A) | u50, u52, u55, u57, u60, u62, u64, u66, u76, u78, u81, u83, u86, u88, u91, u93, u130, u132, u134, u136 | u50, u52, u55, u57, u60, u62, u64, u66, u76, u78, u81, u83, u86, u88, u91, u93, u130, u132 |
| pair-seed-61 | workshop:alice | iee | active | internalisation | 0/45 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-seed-61 | workshop:bob | sli | active | hop | 12/12 = 1 | 0/12 = 0 | 38/40 = 19/20 | 0/0 (N/A) | u41, u46, u67, u72, u94, u99, u103, u108, u112, u117, u121, u126 | u40, u41, u42, u43, u45, u46, u47, u67, u68, u69, u71, u72, u73, u94, u95, u96, u98, u99, u100, u102, u103, u104, u105, u107, u108, u109, u111, u112, u113, u114, u116, u118, u120, u121, u122, u123, u125, u127 |
| pair-seed-61 | workshop:bob | sli | active | content | 0/0 (N/A) | 0/0 (N/A) | 10/12 = 5/6 | 0/0 (N/A) | none | u44, u48, u70, u74, u97, u101, u106, u110, u115, u119 |
| pair-seed-61 | workshop:bob | sli | active | internalisation | 0/52 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-seed-61 | workshop:eve | sli | inactive | hop | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-seed-61 | workshop:eve | sli | inactive | content | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-seed-61 | workshop:eve | sli | inactive | internalisation | 0/0 (N/A) | 0/0 (N/A) |  |  | none |  |

## Internalisation and observed suppliers per weak seat

| History | Actor | Seat | Internalisation wide | Internalisation narrow | Observed suppliers (wide) |
| --- | --- | --- | --- | --- | --- |
| pair-seed-17 | workshop:alice | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-17 | workshop:alice | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-17 | workshop:alice | 5 | 0/23 = 0 | 0/0 (N/A) | workshop:bob x23 |
| pair-seed-17 | workshop:alice | 6 | 0/22 = 0 | 0/0 (N/A) | workshop:bob x22 |
| pair-seed-17 | workshop:bob | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-17 | workshop:bob | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-17 | workshop:bob | 5 | 0/4 = 0 | 0/0 (N/A) | none |
| pair-seed-17 | workshop:bob | 6 | 0/8 = 0 | 0/0 (N/A) | none |
| pair-seed-17 | workshop:eve | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-17 | workshop:eve | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-17 | workshop:eve | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-17 | workshop:eve | 6 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-29 | workshop:alice | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-29 | workshop:alice | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-29 | workshop:alice | 5 | 0/23 = 0 | 0/0 (N/A) | workshop:bob x23 |
| pair-seed-29 | workshop:alice | 6 | 0/22 = 0 | 0/0 (N/A) | workshop:bob x22 |
| pair-seed-29 | workshop:bob | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-29 | workshop:bob | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-29 | workshop:bob | 5 | 0/4 = 0 | 0/0 (N/A) | none |
| pair-seed-29 | workshop:bob | 6 | 0/8 = 0 | 0/0 (N/A) | none |
| pair-seed-29 | workshop:eve | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-29 | workshop:eve | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-29 | workshop:eve | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-29 | workshop:eve | 6 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-43 | workshop:alice | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-43 | workshop:alice | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-43 | workshop:alice | 5 | 0/23 = 0 | 0/0 (N/A) | workshop:bob x23 |
| pair-seed-43 | workshop:alice | 6 | 0/22 = 0 | 0/0 (N/A) | workshop:bob x22 |
| pair-seed-43 | workshop:bob | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-43 | workshop:bob | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-43 | workshop:bob | 5 | 0/4 = 0 | 0/0 (N/A) | none |
| pair-seed-43 | workshop:bob | 6 | 0/8 = 0 | 0/0 (N/A) | none |
| pair-seed-43 | workshop:eve | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-43 | workshop:eve | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-43 | workshop:eve | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-43 | workshop:eve | 6 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-61 | workshop:alice | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-61 | workshop:alice | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-61 | workshop:alice | 5 | 0/23 = 0 | 0/0 (N/A) | workshop:bob x23 |
| pair-seed-61 | workshop:alice | 6 | 0/22 = 0 | 0/0 (N/A) | workshop:bob x22 |
| pair-seed-61 | workshop:bob | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-61 | workshop:bob | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-61 | workshop:bob | 5 | 0/4 = 0 | 0/0 (N/A) | none |
| pair-seed-61 | workshop:bob | 6 | 0/8 = 0 | 0/0 (N/A) | none |
| pair-seed-61 | workshop:eve | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-61 | workshop:eve | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-61 | workshop:eve | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-seed-61 | workshop:eve | 6 | 0/0 (N/A) | 0/0 (N/A) | none |

## Structural versus observed coverage

Structural coverage is the Batch 4 column (supplier holds the element at a strong seat). Observed coverage additionally requires an earlier content block by the supplier at that element.

| History | Structural wide | Observed wide | Structural narrow | Observed narrow | Observed use IDs |
| --- | --- | --- | --- | --- | --- |
| pair-seed-17 | 4/12 = 1/3 | 2/12 = 1/6 | 0/12 = 0 | 0/12 = 0 | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-29 | 4/12 = 1/3 | 2/12 = 1/6 | 0/12 = 0 | 0/12 = 0 | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-43 | 4/12 = 1/3 | 2/12 = 1/6 | 0/12 = 0 | 0/12 = 0 | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-61 | 4/12 = 1/3 | 2/12 = 1/6 | 0/12 = 0 | 0/12 = 0 | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 |

## Use class trace

Aligned with per_actor's use trace. Energy is CT Table 13 block energy (the grade-v1 debit), not the legacy-r4 wallet debit.

| History | Use ID | Kind | Time | Energy | Ring | Support seat | Support at |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pair-seed-17 | u0 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u1 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-17 | u2 | hop | 4 | 2 | vital | 6 | 2 |
| pair-seed-17 | u3 | content | 4 | 2 | vital | 6 | 2 |
| pair-seed-17 | u4 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u5 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u6 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u7 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u8 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u9 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u10 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u11 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u12 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u13 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u14 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u15 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u16 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u17 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u18 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u19 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u20 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u21 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u22 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u23 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-17 | u24 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-17 | u25 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u26 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u27 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-17 | u28 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-17 | u29 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u30 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u31 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u32 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-17 | u33 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-17 | u34 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u35 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u36 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u37 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u38 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u39 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u40 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u41 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-17 | u42 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u43 | hop | 1 | 1 | mental | 6 | 2 |
| pair-seed-17 | u44 | content | 1 | 1 | mental | 6 | 2 |
| pair-seed-17 | u45 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u46 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-17 | u47 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u48 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u49 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u50 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u51 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u52 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u53 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u54 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-17 | u55 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-17 | u56 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u57 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u58 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u59 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-17 | u60 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-17 | u61 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u62 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u63 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u64 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u65 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u66 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u67 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u68 | hop | 2 | 1 | mental | 6 | 1 |
| pair-seed-17 | u69 | hop | 1 | 1 | mental | 6 | 1 |
| pair-seed-17 | u70 | content | 1 | 1 | mental | 6 | 1 |
| pair-seed-17 | u71 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u72 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-17 | u73 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u74 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u75 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u76 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-17 | u77 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u78 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u79 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u80 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-17 | u81 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-17 | u82 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u83 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u84 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u85 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-17 | u86 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-17 | u87 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u88 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u89 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u90 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-17 | u91 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-17 | u92 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u93 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u94 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-17 | u95 | hop | 2 | 1 | mental | 6 | 1 |
| pair-seed-17 | u96 | hop | 1 | 1 | mental | 6 | 1 |
| pair-seed-17 | u97 | content | 1 | 1 | mental | 6 | 1 |
| pair-seed-17 | u98 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u99 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-17 | u100 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u101 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u102 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-17 | u103 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-17 | u104 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-17 | u105 | hop | 2 | 1 | mental | 5 | 2 |
| pair-seed-17 | u106 | content | 2 | 1 | mental | 5 | 2 |
| pair-seed-17 | u107 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-17 | u108 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-17 | u109 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-17 | u110 | content | 1 | 1 | mental | 5 | 2 |
| pair-seed-17 | u111 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u112 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-17 | u113 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u114 | hop | 1 | 1 | mental | 6 | 2 |
| pair-seed-17 | u115 | content | 1 | 1 | mental | 6 | 2 |
| pair-seed-17 | u116 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u117 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-17 | u118 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u119 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-17 | u120 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-17 | u121 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-17 | u122 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-17 | u123 | hop | 2 | 1 | mental | 5 | 2 |
| pair-seed-17 | u124 | content | 2 | 1 | mental | 5 | 2 |
| pair-seed-17 | u125 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-17 | u126 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-17 | u127 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-17 | u128 | content | 1 | 1 | mental | 5 | 2 |
| pair-seed-17 | u129 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-17 | u130 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-17 | u131 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u132 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u133 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-17 | u134 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-17 | u135 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-17 | u136 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u0 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u1 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-29 | u2 | hop | 4 | 2 | vital | 6 | 2 |
| pair-seed-29 | u3 | content | 4 | 2 | vital | 6 | 2 |
| pair-seed-29 | u4 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u5 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u6 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u7 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u8 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u9 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u10 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u11 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u12 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u13 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u14 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u15 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u16 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u17 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u18 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u19 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u20 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u21 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u22 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u23 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-29 | u24 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-29 | u25 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u26 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u27 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-29 | u28 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-29 | u29 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u30 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u31 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u32 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-29 | u33 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-29 | u34 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u35 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u36 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u37 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u38 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u39 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u40 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u41 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-29 | u42 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u43 | hop | 1 | 1 | mental | 6 | 2 |
| pair-seed-29 | u44 | content | 1 | 1 | mental | 6 | 2 |
| pair-seed-29 | u45 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u46 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-29 | u47 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u48 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u49 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u50 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u51 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u52 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u53 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u54 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-29 | u55 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-29 | u56 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u57 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u58 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u59 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-29 | u60 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-29 | u61 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u62 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u63 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u64 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u65 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u66 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u67 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u68 | hop | 2 | 1 | mental | 6 | 1 |
| pair-seed-29 | u69 | hop | 1 | 1 | mental | 6 | 1 |
| pair-seed-29 | u70 | content | 1 | 1 | mental | 6 | 1 |
| pair-seed-29 | u71 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u72 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-29 | u73 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u74 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u75 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u76 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-29 | u77 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u78 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u79 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u80 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-29 | u81 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-29 | u82 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u83 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u84 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u85 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-29 | u86 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-29 | u87 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u88 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u89 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u90 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-29 | u91 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-29 | u92 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u93 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u94 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-29 | u95 | hop | 2 | 1 | mental | 6 | 1 |
| pair-seed-29 | u96 | hop | 1 | 1 | mental | 6 | 1 |
| pair-seed-29 | u97 | content | 1 | 1 | mental | 6 | 1 |
| pair-seed-29 | u98 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u99 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-29 | u100 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u101 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u102 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-29 | u103 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-29 | u104 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-29 | u105 | hop | 2 | 1 | mental | 5 | 2 |
| pair-seed-29 | u106 | content | 2 | 1 | mental | 5 | 2 |
| pair-seed-29 | u107 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-29 | u108 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-29 | u109 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-29 | u110 | content | 1 | 1 | mental | 5 | 2 |
| pair-seed-29 | u111 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u112 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-29 | u113 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u114 | hop | 1 | 1 | mental | 6 | 2 |
| pair-seed-29 | u115 | content | 1 | 1 | mental | 6 | 2 |
| pair-seed-29 | u116 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u117 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-29 | u118 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u119 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-29 | u120 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-29 | u121 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-29 | u122 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-29 | u123 | hop | 2 | 1 | mental | 5 | 2 |
| pair-seed-29 | u124 | content | 2 | 1 | mental | 5 | 2 |
| pair-seed-29 | u125 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-29 | u126 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-29 | u127 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-29 | u128 | content | 1 | 1 | mental | 5 | 2 |
| pair-seed-29 | u129 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-29 | u130 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-29 | u131 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u132 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u133 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-29 | u134 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-29 | u135 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-29 | u136 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u0 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u1 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-43 | u2 | hop | 4 | 2 | vital | 6 | 2 |
| pair-seed-43 | u3 | content | 4 | 2 | vital | 6 | 2 |
| pair-seed-43 | u4 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u5 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u6 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u7 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u8 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u9 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u10 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u11 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u12 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u13 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u14 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u15 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u16 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u17 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u18 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u19 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u20 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u21 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u22 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u23 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-43 | u24 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-43 | u25 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u26 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u27 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-43 | u28 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-43 | u29 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u30 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u31 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u32 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-43 | u33 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-43 | u34 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u35 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u36 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u37 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u38 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u39 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u40 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u41 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-43 | u42 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u43 | hop | 1 | 1 | mental | 6 | 2 |
| pair-seed-43 | u44 | content | 1 | 1 | mental | 6 | 2 |
| pair-seed-43 | u45 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u46 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-43 | u47 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u48 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u49 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u50 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u51 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u52 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u53 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u54 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-43 | u55 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-43 | u56 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u57 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u58 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u59 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-43 | u60 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-43 | u61 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u62 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u63 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u64 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u65 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u66 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u67 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u68 | hop | 2 | 1 | mental | 6 | 1 |
| pair-seed-43 | u69 | hop | 1 | 1 | mental | 6 | 1 |
| pair-seed-43 | u70 | content | 1 | 1 | mental | 6 | 1 |
| pair-seed-43 | u71 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u72 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-43 | u73 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u74 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u75 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u76 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-43 | u77 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u78 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u79 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u80 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-43 | u81 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-43 | u82 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u83 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u84 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u85 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-43 | u86 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-43 | u87 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u88 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u89 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u90 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-43 | u91 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-43 | u92 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u93 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u94 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-43 | u95 | hop | 2 | 1 | mental | 6 | 1 |
| pair-seed-43 | u96 | hop | 1 | 1 | mental | 6 | 1 |
| pair-seed-43 | u97 | content | 1 | 1 | mental | 6 | 1 |
| pair-seed-43 | u98 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u99 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-43 | u100 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u101 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u102 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-43 | u103 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-43 | u104 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-43 | u105 | hop | 2 | 1 | mental | 5 | 2 |
| pair-seed-43 | u106 | content | 2 | 1 | mental | 5 | 2 |
| pair-seed-43 | u107 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-43 | u108 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-43 | u109 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-43 | u110 | content | 1 | 1 | mental | 5 | 2 |
| pair-seed-43 | u111 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u112 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-43 | u113 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u114 | hop | 1 | 1 | mental | 6 | 2 |
| pair-seed-43 | u115 | content | 1 | 1 | mental | 6 | 2 |
| pair-seed-43 | u116 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u117 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-43 | u118 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u119 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-43 | u120 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-43 | u121 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-43 | u122 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-43 | u123 | hop | 2 | 1 | mental | 5 | 2 |
| pair-seed-43 | u124 | content | 2 | 1 | mental | 5 | 2 |
| pair-seed-43 | u125 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-43 | u126 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-43 | u127 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-43 | u128 | content | 1 | 1 | mental | 5 | 2 |
| pair-seed-43 | u129 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-43 | u130 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-43 | u131 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u132 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u133 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-43 | u134 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-43 | u135 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-43 | u136 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u0 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u1 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-61 | u2 | hop | 4 | 2 | vital | 6 | 2 |
| pair-seed-61 | u3 | content | 4 | 2 | vital | 6 | 2 |
| pair-seed-61 | u4 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u5 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u6 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u7 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u8 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u9 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u10 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u11 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u12 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u13 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u14 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u15 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u16 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u17 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u18 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u19 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u20 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u21 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u22 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u23 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-61 | u24 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-61 | u25 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u26 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u27 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-61 | u28 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-61 | u29 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u30 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u31 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u32 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-61 | u33 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-61 | u34 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u35 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u36 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u37 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u38 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u39 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u40 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u41 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-61 | u42 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u43 | hop | 1 | 1 | mental | 6 | 2 |
| pair-seed-61 | u44 | content | 1 | 1 | mental | 6 | 2 |
| pair-seed-61 | u45 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u46 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-61 | u47 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u48 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u49 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u50 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u51 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u52 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u53 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u54 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-61 | u55 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-61 | u56 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u57 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u58 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u59 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-61 | u60 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-61 | u61 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u62 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u63 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u64 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u65 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u66 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u67 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u68 | hop | 2 | 1 | mental | 6 | 1 |
| pair-seed-61 | u69 | hop | 1 | 1 | mental | 6 | 1 |
| pair-seed-61 | u70 | content | 1 | 1 | mental | 6 | 1 |
| pair-seed-61 | u71 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u72 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-61 | u73 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u74 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u75 | hop | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u76 | content | 4 | 2 | vital | 6 | 0 |
| pair-seed-61 | u77 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u78 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u79 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u80 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-61 | u81 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-61 | u82 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u83 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u84 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u85 | hop | 4 | 2 | vital | 6 | 1 |
| pair-seed-61 | u86 | content | 4 | 2 | vital | 6 | 1 |
| pair-seed-61 | u87 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u88 | content | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u89 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u90 | hop | 3 | 4 | vital | 5 | 1 |
| pair-seed-61 | u91 | content | 3 | 4 | vital | 5 | 1 |
| pair-seed-61 | u92 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u93 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u94 | hop | 3 | 4 | vital | 6 | 1 |
| pair-seed-61 | u95 | hop | 2 | 1 | mental | 6 | 1 |
| pair-seed-61 | u96 | hop | 1 | 1 | mental | 6 | 1 |
| pair-seed-61 | u97 | content | 1 | 1 | mental | 6 | 1 |
| pair-seed-61 | u98 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u99 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-61 | u100 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u101 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u102 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-61 | u103 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-61 | u104 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-61 | u105 | hop | 2 | 1 | mental | 5 | 2 |
| pair-seed-61 | u106 | content | 2 | 1 | mental | 5 | 2 |
| pair-seed-61 | u107 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-61 | u108 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-61 | u109 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-61 | u110 | content | 1 | 1 | mental | 5 | 2 |
| pair-seed-61 | u111 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u112 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-61 | u113 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u114 | hop | 1 | 1 | mental | 6 | 2 |
| pair-seed-61 | u115 | content | 1 | 1 | mental | 6 | 2 |
| pair-seed-61 | u116 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u117 | hop | 3 | 4 | vital | 6 | 2 |
| pair-seed-61 | u118 | hop | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u119 | content | 2 | 1 | mental | 6 | 2 |
| pair-seed-61 | u120 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-61 | u121 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-61 | u122 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-61 | u123 | hop | 2 | 1 | mental | 5 | 2 |
| pair-seed-61 | u124 | content | 2 | 1 | mental | 5 | 2 |
| pair-seed-61 | u125 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-61 | u126 | hop | 4 | 2 | vital | 5 | 2 |
| pair-seed-61 | u127 | hop | 1 | 1 | mental | 5 | 2 |
| pair-seed-61 | u128 | content | 1 | 1 | mental | 5 | 2 |
| pair-seed-61 | u129 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-61 | u130 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-61 | u131 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u132 | content | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u133 | hop | 3 | 4 | vital | 5 | 0 |
| pair-seed-61 | u134 | content | 3 | 4 | vital | 5 | 0 |
| pair-seed-61 | u135 | hop | 4 | 2 | vital | 5 | 1 |
| pair-seed-61 | u136 | content | 4 | 2 | vital | 5 | 1 |
