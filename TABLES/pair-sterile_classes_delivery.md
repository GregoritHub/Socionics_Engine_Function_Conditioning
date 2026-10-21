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
| pair-sterile-seed-17 | workshop:alice | eie | active | hop | 20/39 = 20/39 | 0/39 = 0 | 53/55 = 53/55 | 0/0 (N/A) | u82, u86, u89, u93, u96, u100, u104, u108, u120, u124, u127, u131, u134, u138, u141, u145, u184, u188, u192, u196 | u80, u81, u82, u84, u85, u86, u88, u89, u91, u92, u93, u95, u96, u98, u99, u100, u102, u103, u104, u106, u107, u108, u118, u119, u120, u122, u123, u124, u126, u127, u129, u130, u131, u133, u134, u136, u137, u138, u140, u141, u143, u144, u145, u182, u183, u184, u186, u187, u188, u190, u191, u192, u196 |
| pair-sterile-seed-17 | workshop:alice | eie | active | content | 20/38 = 10/19 | 0/38 = 0 | 18/20 = 9/10 | 0/0 (N/A) | u83, u87, u90, u94, u97, u101, u105, u109, u121, u125, u128, u132, u135, u139, u142, u146, u185, u189, u193, u197 | u83, u87, u90, u94, u97, u101, u105, u109, u121, u125, u128, u132, u135, u139, u142, u146, u185, u189 |
| pair-sterile-seed-17 | workshop:alice | eie | active | internalisation | 0/75 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-sterile-seed-17 | workshop:bob | sli | active | hop | 12/12 = 1 | 0/12 = 0 | 38/40 = 19/20 | 0/0 (N/A) | u72, u77, u110, u115, u147, u152, u156, u161, u165, u170, u174, u179 | u71, u72, u73, u74, u76, u77, u78, u110, u111, u112, u114, u115, u116, u147, u148, u149, u151, u152, u153, u155, u156, u157, u158, u160, u161, u162, u164, u165, u166, u167, u169, u171, u173, u174, u175, u176, u178, u180 |
| pair-sterile-seed-17 | workshop:bob | sli | active | content | 0/0 (N/A) | 0/0 (N/A) | 10/12 = 5/6 | 0/0 (N/A) | none | u75, u79, u113, u117, u150, u154, u159, u163, u168, u172 |
| pair-sterile-seed-17 | workshop:bob | sli | active | internalisation | 0/52 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-sterile-seed-17 | workshop:eve | sli | inactive | hop | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-sterile-seed-17 | workshop:eve | sli | inactive | content | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-sterile-seed-17 | workshop:eve | sli | inactive | internalisation | 0/0 (N/A) | 0/0 (N/A) |  |  | none |  |
| pair-sterile-seed-29 | workshop:alice | eie | active | hop | 20/39 = 20/39 | 0/39 = 0 | 53/55 = 53/55 | 0/0 (N/A) | u82, u86, u89, u93, u96, u100, u104, u108, u120, u124, u127, u131, u134, u138, u141, u145, u184, u188, u192, u196 | u80, u81, u82, u84, u85, u86, u88, u89, u91, u92, u93, u95, u96, u98, u99, u100, u102, u103, u104, u106, u107, u108, u118, u119, u120, u122, u123, u124, u126, u127, u129, u130, u131, u133, u134, u136, u137, u138, u140, u141, u143, u144, u145, u182, u183, u184, u186, u187, u188, u190, u191, u192, u196 |
| pair-sterile-seed-29 | workshop:alice | eie | active | content | 20/38 = 10/19 | 0/38 = 0 | 18/20 = 9/10 | 0/0 (N/A) | u83, u87, u90, u94, u97, u101, u105, u109, u121, u125, u128, u132, u135, u139, u142, u146, u185, u189, u193, u197 | u83, u87, u90, u94, u97, u101, u105, u109, u121, u125, u128, u132, u135, u139, u142, u146, u185, u189 |
| pair-sterile-seed-29 | workshop:alice | eie | active | internalisation | 0/75 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-sterile-seed-29 | workshop:bob | sli | active | hop | 12/12 = 1 | 0/12 = 0 | 38/40 = 19/20 | 0/0 (N/A) | u72, u77, u110, u115, u147, u152, u156, u161, u165, u170, u174, u179 | u71, u72, u73, u74, u76, u77, u78, u110, u111, u112, u114, u115, u116, u147, u148, u149, u151, u152, u153, u155, u156, u157, u158, u160, u161, u162, u164, u165, u166, u167, u169, u171, u173, u174, u175, u176, u178, u180 |
| pair-sterile-seed-29 | workshop:bob | sli | active | content | 0/0 (N/A) | 0/0 (N/A) | 10/12 = 5/6 | 0/0 (N/A) | none | u75, u79, u113, u117, u150, u154, u159, u163, u168, u172 |
| pair-sterile-seed-29 | workshop:bob | sli | active | internalisation | 0/52 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-sterile-seed-29 | workshop:eve | sli | inactive | hop | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-sterile-seed-29 | workshop:eve | sli | inactive | content | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-sterile-seed-29 | workshop:eve | sli | inactive | internalisation | 0/0 (N/A) | 0/0 (N/A) |  |  | none |  |
| pair-sterile-seed-43 | workshop:alice | eie | active | hop | 20/39 = 20/39 | 0/39 = 0 | 53/55 = 53/55 | 0/0 (N/A) | u82, u86, u89, u93, u96, u100, u104, u108, u120, u124, u127, u131, u134, u138, u141, u145, u184, u188, u192, u196 | u80, u81, u82, u84, u85, u86, u88, u89, u91, u92, u93, u95, u96, u98, u99, u100, u102, u103, u104, u106, u107, u108, u118, u119, u120, u122, u123, u124, u126, u127, u129, u130, u131, u133, u134, u136, u137, u138, u140, u141, u143, u144, u145, u182, u183, u184, u186, u187, u188, u190, u191, u192, u196 |
| pair-sterile-seed-43 | workshop:alice | eie | active | content | 20/38 = 10/19 | 0/38 = 0 | 18/20 = 9/10 | 0/0 (N/A) | u83, u87, u90, u94, u97, u101, u105, u109, u121, u125, u128, u132, u135, u139, u142, u146, u185, u189, u193, u197 | u83, u87, u90, u94, u97, u101, u105, u109, u121, u125, u128, u132, u135, u139, u142, u146, u185, u189 |
| pair-sterile-seed-43 | workshop:alice | eie | active | internalisation | 0/75 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-sterile-seed-43 | workshop:bob | sli | active | hop | 12/12 = 1 | 0/12 = 0 | 38/40 = 19/20 | 0/0 (N/A) | u72, u77, u110, u115, u147, u152, u156, u161, u165, u170, u174, u179 | u71, u72, u73, u74, u76, u77, u78, u110, u111, u112, u114, u115, u116, u147, u148, u149, u151, u152, u153, u155, u156, u157, u158, u160, u161, u162, u164, u165, u166, u167, u169, u171, u173, u174, u175, u176, u178, u180 |
| pair-sterile-seed-43 | workshop:bob | sli | active | content | 0/0 (N/A) | 0/0 (N/A) | 10/12 = 5/6 | 0/0 (N/A) | none | u75, u79, u113, u117, u150, u154, u159, u163, u168, u172 |
| pair-sterile-seed-43 | workshop:bob | sli | active | internalisation | 0/52 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-sterile-seed-43 | workshop:eve | sli | inactive | hop | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-sterile-seed-43 | workshop:eve | sli | inactive | content | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-sterile-seed-43 | workshop:eve | sli | inactive | internalisation | 0/0 (N/A) | 0/0 (N/A) |  |  | none |  |
| pair-sterile-seed-61 | workshop:alice | eie | active | hop | 20/39 = 20/39 | 0/39 = 0 | 53/55 = 53/55 | 0/0 (N/A) | u82, u86, u89, u93, u96, u100, u104, u108, u120, u124, u127, u131, u134, u138, u141, u145, u184, u188, u192, u196 | u80, u81, u82, u84, u85, u86, u88, u89, u91, u92, u93, u95, u96, u98, u99, u100, u102, u103, u104, u106, u107, u108, u118, u119, u120, u122, u123, u124, u126, u127, u129, u130, u131, u133, u134, u136, u137, u138, u140, u141, u143, u144, u145, u182, u183, u184, u186, u187, u188, u190, u191, u192, u196 |
| pair-sterile-seed-61 | workshop:alice | eie | active | content | 20/38 = 10/19 | 0/38 = 0 | 18/20 = 9/10 | 0/0 (N/A) | u83, u87, u90, u94, u97, u101, u105, u109, u121, u125, u128, u132, u135, u139, u142, u146, u185, u189, u193, u197 | u83, u87, u90, u94, u97, u101, u105, u109, u121, u125, u128, u132, u135, u139, u142, u146, u185, u189 |
| pair-sterile-seed-61 | workshop:alice | eie | active | internalisation | 0/75 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-sterile-seed-61 | workshop:bob | sli | active | hop | 12/12 = 1 | 0/12 = 0 | 38/40 = 19/20 | 0/0 (N/A) | u72, u77, u110, u115, u147, u152, u156, u161, u165, u170, u174, u179 | u71, u72, u73, u74, u76, u77, u78, u110, u111, u112, u114, u115, u116, u147, u148, u149, u151, u152, u153, u155, u156, u157, u158, u160, u161, u162, u164, u165, u166, u167, u169, u171, u173, u174, u175, u176, u178, u180 |
| pair-sterile-seed-61 | workshop:bob | sli | active | content | 0/0 (N/A) | 0/0 (N/A) | 10/12 = 5/6 | 0/0 (N/A) | none | u75, u79, u113, u117, u150, u154, u159, u163, u168, u172 |
| pair-sterile-seed-61 | workshop:bob | sli | active | internalisation | 0/52 = 0 | 0/0 (N/A) |  |  | none |  |
| pair-sterile-seed-61 | workshop:eve | sli | inactive | hop | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-sterile-seed-61 | workshop:eve | sli | inactive | content | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | none | none |
| pair-sterile-seed-61 | workshop:eve | sli | inactive | internalisation | 0/0 (N/A) | 0/0 (N/A) |  |  | none |  |

## Internalisation and observed suppliers per weak seat

| History | Actor | Seat | Internalisation wide | Internalisation narrow | Observed suppliers (wide) |
| --- | --- | --- | --- | --- | --- |
| pair-sterile-seed-17 | workshop:alice | 3 | 0/20 = 0 | 0/0 (N/A) | workshop:bob x20 |
| pair-sterile-seed-17 | workshop:alice | 4 | 0/20 = 0 | 0/0 (N/A) | workshop:bob x20 |
| pair-sterile-seed-17 | workshop:alice | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-17 | workshop:alice | 6 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-17 | workshop:bob | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-17 | workshop:bob | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-17 | workshop:bob | 5 | 0/4 = 0 | 0/0 (N/A) | none |
| pair-sterile-seed-17 | workshop:bob | 6 | 0/8 = 0 | 0/0 (N/A) | none |
| pair-sterile-seed-17 | workshop:eve | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-17 | workshop:eve | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-17 | workshop:eve | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-17 | workshop:eve | 6 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-29 | workshop:alice | 3 | 0/20 = 0 | 0/0 (N/A) | workshop:bob x20 |
| pair-sterile-seed-29 | workshop:alice | 4 | 0/20 = 0 | 0/0 (N/A) | workshop:bob x20 |
| pair-sterile-seed-29 | workshop:alice | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-29 | workshop:alice | 6 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-29 | workshop:bob | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-29 | workshop:bob | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-29 | workshop:bob | 5 | 0/4 = 0 | 0/0 (N/A) | none |
| pair-sterile-seed-29 | workshop:bob | 6 | 0/8 = 0 | 0/0 (N/A) | none |
| pair-sterile-seed-29 | workshop:eve | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-29 | workshop:eve | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-29 | workshop:eve | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-29 | workshop:eve | 6 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-43 | workshop:alice | 3 | 0/20 = 0 | 0/0 (N/A) | workshop:bob x20 |
| pair-sterile-seed-43 | workshop:alice | 4 | 0/20 = 0 | 0/0 (N/A) | workshop:bob x20 |
| pair-sterile-seed-43 | workshop:alice | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-43 | workshop:alice | 6 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-43 | workshop:bob | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-43 | workshop:bob | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-43 | workshop:bob | 5 | 0/4 = 0 | 0/0 (N/A) | none |
| pair-sterile-seed-43 | workshop:bob | 6 | 0/8 = 0 | 0/0 (N/A) | none |
| pair-sterile-seed-43 | workshop:eve | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-43 | workshop:eve | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-43 | workshop:eve | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-43 | workshop:eve | 6 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-61 | workshop:alice | 3 | 0/20 = 0 | 0/0 (N/A) | workshop:bob x20 |
| pair-sterile-seed-61 | workshop:alice | 4 | 0/20 = 0 | 0/0 (N/A) | workshop:bob x20 |
| pair-sterile-seed-61 | workshop:alice | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-61 | workshop:alice | 6 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-61 | workshop:bob | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-61 | workshop:bob | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-61 | workshop:bob | 5 | 0/4 = 0 | 0/0 (N/A) | none |
| pair-sterile-seed-61 | workshop:bob | 6 | 0/8 = 0 | 0/0 (N/A) | none |
| pair-sterile-seed-61 | workshop:eve | 3 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-61 | workshop:eve | 4 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-61 | workshop:eve | 5 | 0/0 (N/A) | 0/0 (N/A) | none |
| pair-sterile-seed-61 | workshop:eve | 6 | 0/0 (N/A) | 0/0 (N/A) | none |

## Structural versus observed coverage

Structural coverage is the Batch 4 column (supplier holds the element at a strong seat). Observed coverage additionally requires an earlier content block by the supplier at that element.

| History | Structural wide | Observed wide | Structural narrow | Observed narrow | Observed use IDs |
| --- | --- | --- | --- | --- | --- |
| pair-sterile-seed-17 | 4/12 = 1/3 | 2/12 = 1/6 | 0/12 = 0 | 0/12 = 0 | u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u184, u185, u188, u189, u192, u193, u196, u197 |
| pair-sterile-seed-29 | 4/12 = 1/3 | 2/12 = 1/6 | 0/12 = 0 | 0/12 = 0 | u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u184, u185, u188, u189, u192, u193, u196, u197 |
| pair-sterile-seed-43 | 4/12 = 1/3 | 2/12 = 1/6 | 0/12 = 0 | 0/12 = 0 | u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u184, u185, u188, u189, u192, u193, u196, u197 |
| pair-sterile-seed-61 | 4/12 = 1/3 | 2/12 = 1/6 | 0/12 = 0 | 0/12 = 0 | u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u184, u185, u188, u189, u192, u193, u196, u197 |

## Use class trace

Aligned with per_actor's use trace. Energy is CT Table 13 block energy (the grade-v1 debit), not the legacy-r4 wallet debit.

| History | Use ID | Kind | Time | Energy | Ring | Support seat | Support at |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pair-sterile-seed-17 | u0 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u1 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-17 | u2 | hop | 1 | 2 | vital | 6 | 2 |
| pair-sterile-seed-17 | u3 | hop | 4 | 3 | mental | 6 | 2 |
| pair-sterile-seed-17 | u4 | content | 4 | 3 | mental | 6 | 2 |
| pair-sterile-seed-17 | u5 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u6 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u7 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u8 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u9 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-17 | u10 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-17 | u11 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u12 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u13 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u14 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u15 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u16 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u17 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-17 | u18 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-17 | u19 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u20 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u21 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u22 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u23 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u24 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u25 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-17 | u26 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-17 | u27 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u28 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u29 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u30 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u31 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u32 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u33 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-17 | u34 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-17 | u35 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u36 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u37 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u38 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u39 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u40 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u41 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-17 | u42 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u43 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u44 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-17 | u45 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-17 | u46 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u47 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u48 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-17 | u49 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-17 | u50 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-17 | u51 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-17 | u52 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-17 | u53 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-17 | u54 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u55 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u56 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u57 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u58 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u59 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u60 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u61 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u62 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u63 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-17 | u64 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-17 | u65 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u66 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u67 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u68 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u69 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u70 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u71 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u72 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-17 | u73 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u74 | hop | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u75 | content | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u76 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u77 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-17 | u78 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u79 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u80 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-17 | u81 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-17 | u82 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u83 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u84 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u85 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u86 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u87 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u88 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-17 | u89 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u90 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u91 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-17 | u92 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-17 | u93 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u94 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u95 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u96 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u97 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u98 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u99 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u100 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u101 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u102 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-17 | u103 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-17 | u104 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u105 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u106 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u107 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u108 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u109 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u110 | hop | 3 | 4 | vital | 6 | 1 |
| pair-sterile-seed-17 | u111 | hop | 2 | 1 | mental | 6 | 1 |
| pair-sterile-seed-17 | u112 | hop | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-17 | u113 | content | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-17 | u114 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u115 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-17 | u116 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u117 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u118 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-17 | u119 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-17 | u120 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u121 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-17 | u122 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u123 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u124 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u125 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u126 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-17 | u127 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u128 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u129 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-17 | u130 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-17 | u131 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u132 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u133 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u134 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u135 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u136 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-17 | u137 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-17 | u138 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u139 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-17 | u140 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-17 | u141 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u142 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u143 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-17 | u144 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-17 | u145 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u146 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u147 | hop | 3 | 4 | vital | 6 | 1 |
| pair-sterile-seed-17 | u148 | hop | 2 | 1 | mental | 6 | 1 |
| pair-sterile-seed-17 | u149 | hop | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-17 | u150 | content | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-17 | u151 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u152 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-17 | u153 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u154 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u155 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u156 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-17 | u157 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u158 | hop | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u159 | content | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u160 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u161 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-17 | u162 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u163 | content | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u164 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u165 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-17 | u166 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u167 | hop | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u168 | content | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u169 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u170 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-17 | u171 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u172 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-17 | u173 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u174 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-17 | u175 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u176 | hop | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u177 | content | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u178 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u179 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-17 | u180 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u181 | content | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-17 | u182 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-17 | u183 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-17 | u184 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-17 | u185 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-17 | u186 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-17 | u187 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-17 | u188 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u189 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u190 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-17 | u191 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-17 | u192 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-17 | u193 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-17 | u194 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-17 | u195 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-17 | u196 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-17 | u197 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u0 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u1 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-29 | u2 | hop | 1 | 2 | vital | 6 | 2 |
| pair-sterile-seed-29 | u3 | hop | 4 | 3 | mental | 6 | 2 |
| pair-sterile-seed-29 | u4 | content | 4 | 3 | mental | 6 | 2 |
| pair-sterile-seed-29 | u5 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u6 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u7 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u8 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u9 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-29 | u10 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-29 | u11 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u12 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u13 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u14 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u15 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u16 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u17 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-29 | u18 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-29 | u19 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u20 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u21 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u22 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u23 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u24 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u25 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-29 | u26 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-29 | u27 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u28 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u29 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u30 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u31 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u32 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u33 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-29 | u34 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-29 | u35 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u36 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u37 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u38 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u39 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u40 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u41 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-29 | u42 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u43 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u44 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-29 | u45 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-29 | u46 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u47 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u48 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-29 | u49 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-29 | u50 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-29 | u51 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-29 | u52 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-29 | u53 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-29 | u54 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u55 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u56 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u57 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u58 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u59 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u60 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u61 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u62 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u63 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-29 | u64 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-29 | u65 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u66 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u67 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u68 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u69 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u70 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u71 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u72 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-29 | u73 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u74 | hop | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u75 | content | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u76 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u77 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-29 | u78 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u79 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u80 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-29 | u81 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-29 | u82 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u83 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u84 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u85 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u86 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u87 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u88 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-29 | u89 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u90 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u91 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-29 | u92 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-29 | u93 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u94 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u95 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u96 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u97 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u98 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u99 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u100 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u101 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u102 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-29 | u103 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-29 | u104 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u105 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u106 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u107 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u108 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u109 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u110 | hop | 3 | 4 | vital | 6 | 1 |
| pair-sterile-seed-29 | u111 | hop | 2 | 1 | mental | 6 | 1 |
| pair-sterile-seed-29 | u112 | hop | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-29 | u113 | content | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-29 | u114 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u115 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-29 | u116 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u117 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u118 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-29 | u119 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-29 | u120 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u121 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-29 | u122 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u123 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u124 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u125 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u126 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-29 | u127 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u128 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u129 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-29 | u130 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-29 | u131 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u132 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u133 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u134 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u135 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u136 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-29 | u137 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-29 | u138 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u139 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-29 | u140 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-29 | u141 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u142 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u143 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-29 | u144 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-29 | u145 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u146 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u147 | hop | 3 | 4 | vital | 6 | 1 |
| pair-sterile-seed-29 | u148 | hop | 2 | 1 | mental | 6 | 1 |
| pair-sterile-seed-29 | u149 | hop | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-29 | u150 | content | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-29 | u151 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u152 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-29 | u153 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u154 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u155 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u156 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-29 | u157 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u158 | hop | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u159 | content | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u160 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u161 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-29 | u162 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u163 | content | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u164 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u165 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-29 | u166 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u167 | hop | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u168 | content | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u169 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u170 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-29 | u171 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u172 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-29 | u173 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u174 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-29 | u175 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u176 | hop | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u177 | content | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u178 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u179 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-29 | u180 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u181 | content | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-29 | u182 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-29 | u183 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-29 | u184 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-29 | u185 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-29 | u186 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-29 | u187 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-29 | u188 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u189 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u190 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-29 | u191 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-29 | u192 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-29 | u193 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-29 | u194 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-29 | u195 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-29 | u196 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-29 | u197 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u0 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u1 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-43 | u2 | hop | 1 | 2 | vital | 6 | 2 |
| pair-sterile-seed-43 | u3 | hop | 4 | 3 | mental | 6 | 2 |
| pair-sterile-seed-43 | u4 | content | 4 | 3 | mental | 6 | 2 |
| pair-sterile-seed-43 | u5 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u6 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u7 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u8 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u9 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-43 | u10 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-43 | u11 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u12 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u13 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u14 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u15 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u16 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u17 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-43 | u18 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-43 | u19 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u20 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u21 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u22 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u23 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u24 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u25 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-43 | u26 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-43 | u27 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u28 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u29 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u30 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u31 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u32 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u33 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-43 | u34 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-43 | u35 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u36 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u37 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u38 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u39 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u40 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u41 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-43 | u42 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u43 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u44 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-43 | u45 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-43 | u46 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u47 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u48 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-43 | u49 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-43 | u50 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-43 | u51 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-43 | u52 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-43 | u53 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-43 | u54 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u55 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u56 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u57 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u58 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u59 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u60 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u61 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u62 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u63 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-43 | u64 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-43 | u65 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u66 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u67 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u68 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u69 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u70 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u71 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u72 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-43 | u73 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u74 | hop | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u75 | content | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u76 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u77 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-43 | u78 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u79 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u80 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-43 | u81 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-43 | u82 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u83 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u84 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u85 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u86 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u87 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u88 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-43 | u89 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u90 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u91 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-43 | u92 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-43 | u93 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u94 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u95 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u96 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u97 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u98 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u99 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u100 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u101 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u102 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-43 | u103 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-43 | u104 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u105 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u106 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u107 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u108 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u109 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u110 | hop | 3 | 4 | vital | 6 | 1 |
| pair-sterile-seed-43 | u111 | hop | 2 | 1 | mental | 6 | 1 |
| pair-sterile-seed-43 | u112 | hop | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-43 | u113 | content | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-43 | u114 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u115 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-43 | u116 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u117 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u118 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-43 | u119 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-43 | u120 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u121 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-43 | u122 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u123 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u124 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u125 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u126 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-43 | u127 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u128 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u129 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-43 | u130 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-43 | u131 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u132 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u133 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u134 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u135 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u136 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-43 | u137 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-43 | u138 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u139 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-43 | u140 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-43 | u141 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u142 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u143 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-43 | u144 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-43 | u145 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u146 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u147 | hop | 3 | 4 | vital | 6 | 1 |
| pair-sterile-seed-43 | u148 | hop | 2 | 1 | mental | 6 | 1 |
| pair-sterile-seed-43 | u149 | hop | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-43 | u150 | content | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-43 | u151 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u152 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-43 | u153 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u154 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u155 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u156 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-43 | u157 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u158 | hop | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u159 | content | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u160 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u161 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-43 | u162 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u163 | content | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u164 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u165 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-43 | u166 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u167 | hop | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u168 | content | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u169 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u170 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-43 | u171 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u172 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-43 | u173 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u174 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-43 | u175 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u176 | hop | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u177 | content | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u178 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u179 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-43 | u180 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u181 | content | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-43 | u182 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-43 | u183 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-43 | u184 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-43 | u185 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-43 | u186 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-43 | u187 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-43 | u188 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u189 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u190 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-43 | u191 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-43 | u192 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-43 | u193 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-43 | u194 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-43 | u195 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-43 | u196 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-43 | u197 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u0 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u1 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-61 | u2 | hop | 1 | 2 | vital | 6 | 2 |
| pair-sterile-seed-61 | u3 | hop | 4 | 3 | mental | 6 | 2 |
| pair-sterile-seed-61 | u4 | content | 4 | 3 | mental | 6 | 2 |
| pair-sterile-seed-61 | u5 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u6 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u7 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u8 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u9 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-61 | u10 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-61 | u11 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u12 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u13 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u14 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u15 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u16 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u17 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-61 | u18 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-61 | u19 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u20 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u21 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u22 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u23 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u24 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u25 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-61 | u26 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-61 | u27 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u28 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u29 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u30 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u31 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u32 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u33 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-61 | u34 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-61 | u35 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u36 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u37 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u38 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u39 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u40 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u41 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-61 | u42 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u43 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u44 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-61 | u45 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-61 | u46 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u47 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u48 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-61 | u49 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-61 | u50 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-61 | u51 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-61 | u52 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-61 | u53 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-61 | u54 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u55 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u56 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u57 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u58 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u59 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u60 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u61 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u62 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u63 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-61 | u64 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-61 | u65 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u66 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u67 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u68 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u69 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u70 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u71 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u72 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-61 | u73 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u74 | hop | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u75 | content | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u76 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u77 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-61 | u78 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u79 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u80 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-61 | u81 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-61 | u82 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u83 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u84 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u85 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u86 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u87 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u88 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-61 | u89 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u90 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u91 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-61 | u92 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-61 | u93 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u94 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u95 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u96 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u97 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u98 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u99 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u100 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u101 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u102 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-61 | u103 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-61 | u104 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u105 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u106 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u107 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u108 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u109 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u110 | hop | 3 | 4 | vital | 6 | 1 |
| pair-sterile-seed-61 | u111 | hop | 2 | 1 | mental | 6 | 1 |
| pair-sterile-seed-61 | u112 | hop | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-61 | u113 | content | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-61 | u114 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u115 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-61 | u116 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u117 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u118 | hop | 2 | 4 | vital | 8 | 2 |
| pair-sterile-seed-61 | u119 | hop | 1 | 2 | vital | 8 | 2 |
| pair-sterile-seed-61 | u120 | hop | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u121 | content | 4 | 3 | mental | 8 | 2 |
| pair-sterile-seed-61 | u122 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u123 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u124 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u125 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u126 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-61 | u127 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u128 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u129 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-61 | u130 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-61 | u131 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u132 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u133 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u134 | hop | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u135 | content | 4 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u136 | hop | 1 | 2 | vital | 8 | 1 |
| pair-sterile-seed-61 | u137 | hop | 2 | 4 | vital | 8 | 1 |
| pair-sterile-seed-61 | u138 | hop | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u139 | content | 3 | 3 | mental | 8 | 1 |
| pair-sterile-seed-61 | u140 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-61 | u141 | hop | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u142 | content | 3 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u143 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-61 | u144 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-61 | u145 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u146 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u147 | hop | 3 | 4 | vital | 6 | 1 |
| pair-sterile-seed-61 | u148 | hop | 2 | 1 | mental | 6 | 1 |
| pair-sterile-seed-61 | u149 | hop | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-61 | u150 | content | 1 | 1 | mental | 6 | 1 |
| pair-sterile-seed-61 | u151 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u152 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-61 | u153 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u154 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u155 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u156 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-61 | u157 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u158 | hop | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u159 | content | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u160 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u161 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-61 | u162 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u163 | content | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u164 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u165 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-61 | u166 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u167 | hop | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u168 | content | 1 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u169 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u170 | hop | 3 | 4 | vital | 6 | 2 |
| pair-sterile-seed-61 | u171 | hop | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u172 | content | 2 | 1 | mental | 6 | 2 |
| pair-sterile-seed-61 | u173 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u174 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-61 | u175 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u176 | hop | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u177 | content | 2 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u178 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u179 | hop | 4 | 2 | vital | 5 | 2 |
| pair-sterile-seed-61 | u180 | hop | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u181 | content | 1 | 1 | mental | 5 | 2 |
| pair-sterile-seed-61 | u182 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-61 | u183 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-61 | u184 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-61 | u185 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-61 | u186 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-61 | u187 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-61 | u188 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u189 | content | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u190 | hop | 1 | 2 | vital | 7 | 2 |
| pair-sterile-seed-61 | u191 | hop | 2 | 4 | vital | 7 | 2 |
| pair-sterile-seed-61 | u192 | hop | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-61 | u193 | content | 3 | 3 | mental | 7 | 2 |
| pair-sterile-seed-61 | u194 | hop | 2 | 4 | vital | 7 | 1 |
| pair-sterile-seed-61 | u195 | hop | 1 | 2 | vital | 7 | 1 |
| pair-sterile-seed-61 | u196 | hop | 4 | 3 | mental | 7 | 1 |
| pair-sterile-seed-61 | u197 | content | 4 | 3 | mental | 7 | 1 |
