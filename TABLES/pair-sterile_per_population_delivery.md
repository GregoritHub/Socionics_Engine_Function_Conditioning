# Per-population measures — Batch 6

Only non-empty actor tuples count as received. Coverage counts distinct receiver/seat
pairs at dim <= 2 supplied by a producer holding that element at dim >= 3,
divided by every committed actor's dim <= 2 seats, including inactive actors.
Supplier concentration is HHI: sum of squared supplier received-use counts /
squared total supplier incidences (all receiver seats). Empty supply is N/A.
Sterile ordered pairs require zero received uses in BOTH directions; both
ordered directions are listed, with the kernel's directional relation labels.
Relation names are read from the pinned kernel label file and their landing
permutations are checked against hle.relations. No labels are inferred.

## Accepted inputs

| History | Model | Seed | Actors | Transactions | Checkpoint SHA-256 |
| --- | --- | --- | --- | --- | --- |
| pair-sterile-seed-17 | legacy-r4 | 17 | 3 | 447 | dcbd46402a2643dd214e9a937a3681587ed64fa7367c7df2868c59b04cdd8929 |
| pair-sterile-seed-29 | legacy-r4 | 29 | 3 | 447 | 4698c51789fe2aba275fdb91e6c5276fd42aafabaac25fb0f76fd1327a802df9 |
| pair-sterile-seed-43 | legacy-r4 | 43 | 3 | 447 | 1e7653ab3783a906cf41e918c20abdec52a5b22aa6d1b3dc8ae3e1d57b7b0c38 |
| pair-sterile-seed-61 | legacy-r4 | 61 | 3 | 447 | 8edc5a9fcaa20e140cc5c59b73244cc26d2fdb5a713f3d2bf060c71ab16c04c1 |

## Population summary

| History | Actors | Inactive | Received uses | Coverage | Supplier HHI | Sterile ordered pairs | Benefit-family uses | Coverage use IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair-sterile-seed-17 | 3 | 1 | 127 | 4/12 = 1/3 | 8329/16129 = 8329/16129 | 4 | 0 | u72, u77, u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u110, u115, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u147, u152, u156, u161, u165, u170, u174, u179, u184, u185, u188, u189, u192, u193, u196, u197 |
| pair-sterile-seed-29 | 3 | 1 | 127 | 4/12 = 1/3 | 8329/16129 = 8329/16129 | 4 | 0 | u72, u77, u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u110, u115, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u147, u152, u156, u161, u165, u170, u174, u179, u184, u185, u188, u189, u192, u193, u196, u197 |
| pair-sterile-seed-43 | 3 | 1 | 127 | 4/12 = 1/3 | 8329/16129 = 8329/16129 | 4 | 0 | u72, u77, u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u110, u115, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u147, u152, u156, u161, u165, u170, u174, u179, u184, u185, u188, u189, u192, u193, u196, u197 |
| pair-sterile-seed-61 | 3 | 1 | 127 | 4/12 = 1/3 | 8329/16129 = 8329/16129 | 4 | 0 | u72, u77, u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u110, u115, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u147, u152, u156, u161, u165, u170, u174, u179, u184, u185, u188, u189, u192, u193, u196, u197 |

## Coverage by episode index

Cumulative through explicitly recorded harness episodes, including preparation; not scheduler episodes. The denominator is fixed, including inactive actors.

| History | Through episode | Coverage | Qualifying use IDs |
| --- | --- | --- | --- |
| pair-sterile-seed-17 | 0 | 4/12 = 1/3 | u72, u77, u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u110, u115, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u147, u152, u156, u161, u165, u170, u174, u179, u184, u185, u188, u189, u192, u193, u196, u197 |
| pair-sterile-seed-29 | 0 | 4/12 = 1/3 | u72, u77, u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u110, u115, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u147, u152, u156, u161, u165, u170, u174, u179, u184, u185, u188, u189, u192, u193, u196, u197 |
| pair-sterile-seed-43 | 0 | 4/12 = 1/3 | u72, u77, u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u110, u115, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u147, u152, u156, u161, u165, u170, u174, u179, u184, u185, u188, u189, u192, u193, u196, u197 |
| pair-sterile-seed-61 | 0 | 4/12 = 1/3 | u72, u77, u82, u83, u86, u87, u89, u90, u93, u94, u96, u97, u100, u101, u104, u105, u108, u109, u110, u115, u120, u121, u124, u125, u127, u128, u131, u132, u134, u135, u138, u139, u141, u142, u145, u146, u147, u152, u156, u161, u165, u170, u174, u179, u184, u185, u188, u189, u192, u193, u196, u197 |

## Ordered pairs

Forward means source -> receiver. An empty ID set is an observed zero.

| History | Source | Receiver | Relation | Forward uses | Reverse uses | Sterile | Forward IDs | Reverse IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair-sterile-seed-17 | workshop:alice | workshop:bob | conflict | 52 | 75 | False | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 |
| pair-sterile-seed-17 | workshop:alice | workshop:eve | conflict | 0 | 0 | True | none | none |
| pair-sterile-seed-17 | workshop:bob | workshop:alice | conflict | 75 | 52 | False | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 |
| pair-sterile-seed-17 | workshop:bob | workshop:eve | identity | 0 | 0 | True | none | none |
| pair-sterile-seed-17 | workshop:eve | workshop:alice | conflict | 0 | 0 | True | none | none |
| pair-sterile-seed-17 | workshop:eve | workshop:bob | identity | 0 | 0 | True | none | none |
| pair-sterile-seed-29 | workshop:alice | workshop:bob | conflict | 52 | 75 | False | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 |
| pair-sterile-seed-29 | workshop:alice | workshop:eve | conflict | 0 | 0 | True | none | none |
| pair-sterile-seed-29 | workshop:bob | workshop:alice | conflict | 75 | 52 | False | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 |
| pair-sterile-seed-29 | workshop:bob | workshop:eve | identity | 0 | 0 | True | none | none |
| pair-sterile-seed-29 | workshop:eve | workshop:alice | conflict | 0 | 0 | True | none | none |
| pair-sterile-seed-29 | workshop:eve | workshop:bob | identity | 0 | 0 | True | none | none |
| pair-sterile-seed-43 | workshop:alice | workshop:bob | conflict | 52 | 75 | False | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 |
| pair-sterile-seed-43 | workshop:alice | workshop:eve | conflict | 0 | 0 | True | none | none |
| pair-sterile-seed-43 | workshop:bob | workshop:alice | conflict | 75 | 52 | False | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 |
| pair-sterile-seed-43 | workshop:bob | workshop:eve | identity | 0 | 0 | True | none | none |
| pair-sterile-seed-43 | workshop:eve | workshop:alice | conflict | 0 | 0 | True | none | none |
| pair-sterile-seed-43 | workshop:eve | workshop:bob | identity | 0 | 0 | True | none | none |
| pair-sterile-seed-61 | workshop:alice | workshop:bob | conflict | 52 | 75 | False | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 |
| pair-sterile-seed-61 | workshop:alice | workshop:eve | conflict | 0 | 0 | True | none | none |
| pair-sterile-seed-61 | workshop:bob | workshop:alice | conflict | 75 | 52 | False | u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128, u129, u130, u131, u132, u133, u134, u135, u136, u137, u138, u139, u140, u141, u142, u143, u144, u145, u146, u182, u183, u184, u185, u186, u187, u188, u189, u190, u191, u192, u193, u194, u195, u196, u197 | u71, u72, u73, u74, u75, u76, u77, u78, u79, u110, u111, u112, u113, u114, u115, u116, u117, u147, u148, u149, u150, u151, u152, u153, u154, u155, u156, u157, u158, u159, u160, u161, u162, u163, u164, u165, u166, u167, u168, u169, u170, u171, u172, u173, u174, u175, u176, u177, u178, u179, u180, u181 |
| pair-sterile-seed-61 | workshop:bob | workshop:eve | identity | 0 | 0 | True | none | none |
| pair-sterile-seed-61 | workshop:eve | workshop:alice | conflict | 0 | 0 | True | none | none |
| pair-sterile-seed-61 | workshop:eve | workshop:bob | identity | 0 | 0 | True | none | none |

## Benefit-family pairs within the composition

Pair counts are within the recorded composition. The requested IEE/SLI/LIE triad is not producible; a standalone pair-versus-that-triad comparison is unavailable, not zero.

| History | Source | Receiver | Relation | Pair-subset uses | Composition benefit-family uses | Standalone pair uses | Pair-subset IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |

A3/A4: any exact operation input counts, including collective evidence. A use counts once in its receiver profile and once per listed supplier in supplier/pair counts.
