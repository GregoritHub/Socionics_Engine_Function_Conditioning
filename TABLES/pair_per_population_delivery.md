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
| pair-seed-17 | legacy-r4 | 17 | 3 | 447 | 430d4388ad49ce5ddfe3091d9669373fb1afa3ebaf1176075d18d85f86b06bda |
| pair-seed-29 | legacy-r4 | 29 | 3 | 447 | d68aaf7be5ef13e3ec5e23d94ef8d687c465cf86313f8561a8660c554a1c64ea |
| pair-seed-43 | legacy-r4 | 43 | 3 | 447 | bdbcf45af56356ba117c5891c38a8fc26be86ed2d05838afa61b05baccc0a535 |
| pair-seed-61 | legacy-r4 | 61 | 3 | 447 | 4c5152a654505168c6b1e32cf278c7498e6179bdb179d003d2cb04ccf1342884 |

## Population summary

| History | Actors | Inactive | Received uses | Coverage | Supplier HHI | Sterile ordered pairs | Benefit-family uses | Coverage use IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair-seed-17 | 3 | 1 | 97 | 4/12 = 1/3 | 4729/9409 = 4729/9409 | 4 | 0 | u41, u46, u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u72, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u99, u103, u108, u112, u117, u121, u126, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-29 | 3 | 1 | 97 | 4/12 = 1/3 | 4729/9409 = 4729/9409 | 4 | 0 | u41, u46, u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u72, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u99, u103, u108, u112, u117, u121, u126, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-43 | 3 | 1 | 97 | 4/12 = 1/3 | 4729/9409 = 4729/9409 | 4 | 0 | u41, u46, u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u72, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u99, u103, u108, u112, u117, u121, u126, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-61 | 3 | 1 | 97 | 4/12 = 1/3 | 4729/9409 = 4729/9409 | 4 | 0 | u41, u46, u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u72, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u99, u103, u108, u112, u117, u121, u126, u129, u130, u131, u132, u133, u134, u135, u136 |

## Coverage by episode index

Cumulative through explicitly recorded harness episodes, including preparation; not scheduler episodes. The denominator is fixed, including inactive actors.

| History | Through episode | Coverage | Qualifying use IDs |
| --- | --- | --- | --- |
| pair-seed-17 | 0 | 4/12 = 1/3 | u41, u46, u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u72, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u99, u103, u108, u112, u117, u121, u126, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-29 | 0 | 4/12 = 1/3 | u41, u46, u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u72, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u99, u103, u108, u112, u117, u121, u126, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-43 | 0 | 4/12 = 1/3 | u41, u46, u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u72, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u99, u103, u108, u112, u117, u121, u126, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-61 | 0 | 4/12 = 1/3 | u41, u46, u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u67, u72, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u94, u99, u103, u108, u112, u117, u121, u126, u129, u130, u131, u132, u133, u134, u135, u136 |

## Ordered pairs

Forward means source -> receiver. An empty ID set is an observed zero.

| History | Source | Receiver | Relation | Forward uses | Reverse uses | Sterile | Forward IDs | Reverse IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair-seed-17 | workshop:alice | workshop:bob | duality | 52 | 45 | False | u40, u41, u42, u43, u44, u45, u46, u47, u48, u67, u68, u69, u70, u71, u72, u73, u74, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u110, u111, u112, u113, u114, u115, u116, u117, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128 | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-17 | workshop:alice | workshop:eve | duality | 0 | 0 | True | none | none |
| pair-seed-17 | workshop:bob | workshop:alice | duality | 45 | 52 | False | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 | u40, u41, u42, u43, u44, u45, u46, u47, u48, u67, u68, u69, u70, u71, u72, u73, u74, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u110, u111, u112, u113, u114, u115, u116, u117, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128 |
| pair-seed-17 | workshop:bob | workshop:eve | identity | 0 | 0 | True | none | none |
| pair-seed-17 | workshop:eve | workshop:alice | duality | 0 | 0 | True | none | none |
| pair-seed-17 | workshop:eve | workshop:bob | identity | 0 | 0 | True | none | none |
| pair-seed-29 | workshop:alice | workshop:bob | duality | 52 | 45 | False | u40, u41, u42, u43, u44, u45, u46, u47, u48, u67, u68, u69, u70, u71, u72, u73, u74, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u110, u111, u112, u113, u114, u115, u116, u117, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128 | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-29 | workshop:alice | workshop:eve | duality | 0 | 0 | True | none | none |
| pair-seed-29 | workshop:bob | workshop:alice | duality | 45 | 52 | False | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 | u40, u41, u42, u43, u44, u45, u46, u47, u48, u67, u68, u69, u70, u71, u72, u73, u74, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u110, u111, u112, u113, u114, u115, u116, u117, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128 |
| pair-seed-29 | workshop:bob | workshop:eve | identity | 0 | 0 | True | none | none |
| pair-seed-29 | workshop:eve | workshop:alice | duality | 0 | 0 | True | none | none |
| pair-seed-29 | workshop:eve | workshop:bob | identity | 0 | 0 | True | none | none |
| pair-seed-43 | workshop:alice | workshop:bob | duality | 52 | 45 | False | u40, u41, u42, u43, u44, u45, u46, u47, u48, u67, u68, u69, u70, u71, u72, u73, u74, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u110, u111, u112, u113, u114, u115, u116, u117, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128 | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-43 | workshop:alice | workshop:eve | duality | 0 | 0 | True | none | none |
| pair-seed-43 | workshop:bob | workshop:alice | duality | 45 | 52 | False | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 | u40, u41, u42, u43, u44, u45, u46, u47, u48, u67, u68, u69, u70, u71, u72, u73, u74, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u110, u111, u112, u113, u114, u115, u116, u117, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128 |
| pair-seed-43 | workshop:bob | workshop:eve | identity | 0 | 0 | True | none | none |
| pair-seed-43 | workshop:eve | workshop:alice | duality | 0 | 0 | True | none | none |
| pair-seed-43 | workshop:eve | workshop:bob | identity | 0 | 0 | True | none | none |
| pair-seed-61 | workshop:alice | workshop:bob | duality | 52 | 45 | False | u40, u41, u42, u43, u44, u45, u46, u47, u48, u67, u68, u69, u70, u71, u72, u73, u74, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u110, u111, u112, u113, u114, u115, u116, u117, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128 | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 |
| pair-seed-61 | workshop:alice | workshop:eve | duality | 0 | 0 | True | none | none |
| pair-seed-61 | workshop:bob | workshop:alice | duality | 45 | 52 | False | u49, u50, u51, u52, u53, u54, u55, u56, u57, u58, u59, u60, u61, u62, u63, u64, u65, u66, u75, u76, u77, u78, u79, u80, u81, u82, u83, u84, u85, u86, u87, u88, u89, u90, u91, u92, u93, u129, u130, u131, u132, u133, u134, u135, u136 | u40, u41, u42, u43, u44, u45, u46, u47, u48, u67, u68, u69, u70, u71, u72, u73, u74, u94, u95, u96, u97, u98, u99, u100, u101, u102, u103, u104, u105, u106, u107, u108, u109, u110, u111, u112, u113, u114, u115, u116, u117, u118, u119, u120, u121, u122, u123, u124, u125, u126, u127, u128 |
| pair-seed-61 | workshop:bob | workshop:eve | identity | 0 | 0 | True | none | none |
| pair-seed-61 | workshop:eve | workshop:alice | duality | 0 | 0 | True | none | none |
| pair-seed-61 | workshop:eve | workshop:bob | identity | 0 | 0 | True | none | none |

## Benefit-family pairs within the composition

Pair counts are within the recorded composition. The requested IEE/SLI/LIE triad is not producible; a standalone pair-versus-that-triad comparison is unavailable, not zero.

| History | Source | Receiver | Relation | Pair-subset uses | Composition benefit-family uses | Standalone pair uses | Pair-subset IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |

A3/A4: any exact operation input counts, including collective evidence. A use counts once in its receiver profile and once per listed supplier in supplier/pair counts.
