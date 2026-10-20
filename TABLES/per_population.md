# Per-population measures — Batch 4

Only actor-id sources count as received. Coverage counts distinct receiver/seat
pairs at dim <= 2 supplied by a producer holding that element at dim >= 3,
divided by every committed actor's dim <= 2 seats, including inactive actors.
Supplier concentration is HHI: sum of squared supplier received-use counts /
squared total received uses (all receiver seats). Empty supply is N/A.
Sterile ordered pairs require zero received uses in BOTH directions; both
ordered directions are listed, with the kernel's directional relation labels.
Relation names are read from the pinned kernel label file and their landing
permutations are checked against hle.relations. No labels are inferred.

## Accepted inputs

| History | Model | Seed | Actors | Transactions | Checkpoint SHA-256 |
| --- | --- | --- | --- | --- | --- |
| legacy-r4-seed-17 | legacy-r4 | 17 | 3 | 216 | 67b84259159b00fe1e5f2de33cca155b80290063a715de26c24d04771d1ef86b |
| legacy-r4-seed-29 | legacy-r4 | 29 | 3 | 216 | 9dcf83e973882a3be6c20be08e8ca1e167e8ecd1aa591bb8816410c531cce6df |
| legacy-r4-seed-43 | legacy-r4 | 43 | 3 | 216 | 79f7b78caf0a12523ec32664dc9c072da131ea583a0ad7d1b0ad1bfda8418bfc |
| legacy-r4-seed-61 | legacy-r4 | 61 | 3 | 216 | 6d33d982528bec531e3fe43dbea8176451bfbdc6d470ef6c4904a264774ea2a8 |
| grade-v1-seed-17 | grade-v1 | 17 | 3 | 216 | 28abae8a8a576f9189288f8a9f2df0ad201f4a466d725c8d1d1ee23ca335ef73 |
| grade-v1-seed-29 | grade-v1 | 29 | 3 | 216 | b49b8cebdbbefd0fed4905b22ae8d41d9fdcae8755febebc2ca1d5b523b003c7 |
| grade-v1-seed-43 | grade-v1 | 43 | 3 | 216 | 09a2d1411ad9eea8dc648558961d6ab9a3a9b9a10faaf552a34e5904427d9033 |
| grade-v1-seed-61 | grade-v1 | 61 | 3 | 216 | 764e91002767ece728b9a1ac1d2dee72ef1a83b6ed952159871380dcdba1eff9 |

## Population summary

| History | Actors | Inactive | Received uses | Coverage | Supplier HHI | Sterile ordered pairs | Benefit-family uses | Coverage use IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| legacy-r4-seed-17 | 3 | 0 | 0 | 0/12 = 0 | 0/0 (N/A) | 6 | 0 | none |
| legacy-r4-seed-29 | 3 | 0 | 0 | 0/12 = 0 | 0/0 (N/A) | 6 | 0 | none |
| legacy-r4-seed-43 | 3 | 0 | 0 | 0/12 = 0 | 0/0 (N/A) | 6 | 0 | none |
| legacy-r4-seed-61 | 3 | 0 | 0 | 0/12 = 0 | 0/0 (N/A) | 6 | 0 | none |
| grade-v1-seed-17 | 3 | 0 | 0 | 0/12 = 0 | 0/0 (N/A) | 6 | 0 | none |
| grade-v1-seed-29 | 3 | 0 | 0 | 0/12 = 0 | 0/0 (N/A) | 6 | 0 | none |
| grade-v1-seed-43 | 3 | 0 | 0 | 0/12 = 0 | 0/0 (N/A) | 6 | 0 | none |
| grade-v1-seed-61 | 3 | 0 | 0 | 0/12 = 0 | 0/0 (N/A) | 6 | 0 | none |

## Coverage by episode index

Cumulative through each actor-local episode index, pooled across actors; not a wall-clock snapshot. The denominator is fixed, including inactive actors.

| History | Through episode | Coverage | Qualifying use IDs |
| --- | --- | --- | --- |
| legacy-r4-seed-17 | 0 | 0/12 = 0 | none |
| legacy-r4-seed-17 | 1 | 0/12 = 0 | none |
| legacy-r4-seed-29 | 0 | 0/12 = 0 | none |
| legacy-r4-seed-29 | 1 | 0/12 = 0 | none |
| legacy-r4-seed-43 | 0 | 0/12 = 0 | none |
| legacy-r4-seed-43 | 1 | 0/12 = 0 | none |
| legacy-r4-seed-61 | 0 | 0/12 = 0 | none |
| legacy-r4-seed-61 | 1 | 0/12 = 0 | none |
| grade-v1-seed-17 | 0 | 0/12 = 0 | none |
| grade-v1-seed-17 | 1 | 0/12 = 0 | none |
| grade-v1-seed-29 | 0 | 0/12 = 0 | none |
| grade-v1-seed-29 | 1 | 0/12 = 0 | none |
| grade-v1-seed-43 | 0 | 0/12 = 0 | none |
| grade-v1-seed-43 | 1 | 0/12 = 0 | none |
| grade-v1-seed-61 | 0 | 0/12 = 0 | none |
| grade-v1-seed-61 | 1 | 0/12 = 0 | none |

## Ordered pairs

Forward means source -> receiver. An empty ID set is an observed zero.

| History | Source | Receiver | Relation | Forward uses | Reverse uses | Sterile | Forward IDs | Reverse IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| legacy-r4-seed-17 | workshop:alice | workshop:bob | duality | 0 | 0 | True | none | none |
| legacy-r4-seed-17 | workshop:alice | workshop:eve | benefit | 0 | 0 | True | none | none |
| legacy-r4-seed-17 | workshop:bob | workshop:alice | duality | 0 | 0 | True | none | none |
| legacy-r4-seed-17 | workshop:bob | workshop:eve | supervision | 0 | 0 | True | none | none |
| legacy-r4-seed-17 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | True | none | none |
| legacy-r4-seed-17 | workshop:eve | workshop:bob | supervision_inverse | 0 | 0 | True | none | none |
| legacy-r4-seed-29 | workshop:alice | workshop:bob | duality | 0 | 0 | True | none | none |
| legacy-r4-seed-29 | workshop:alice | workshop:eve | benefit | 0 | 0 | True | none | none |
| legacy-r4-seed-29 | workshop:bob | workshop:alice | duality | 0 | 0 | True | none | none |
| legacy-r4-seed-29 | workshop:bob | workshop:eve | supervision | 0 | 0 | True | none | none |
| legacy-r4-seed-29 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | True | none | none |
| legacy-r4-seed-29 | workshop:eve | workshop:bob | supervision_inverse | 0 | 0 | True | none | none |
| legacy-r4-seed-43 | workshop:alice | workshop:bob | duality | 0 | 0 | True | none | none |
| legacy-r4-seed-43 | workshop:alice | workshop:eve | benefit | 0 | 0 | True | none | none |
| legacy-r4-seed-43 | workshop:bob | workshop:alice | duality | 0 | 0 | True | none | none |
| legacy-r4-seed-43 | workshop:bob | workshop:eve | supervision | 0 | 0 | True | none | none |
| legacy-r4-seed-43 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | True | none | none |
| legacy-r4-seed-43 | workshop:eve | workshop:bob | supervision_inverse | 0 | 0 | True | none | none |
| legacy-r4-seed-61 | workshop:alice | workshop:bob | duality | 0 | 0 | True | none | none |
| legacy-r4-seed-61 | workshop:alice | workshop:eve | benefit | 0 | 0 | True | none | none |
| legacy-r4-seed-61 | workshop:bob | workshop:alice | duality | 0 | 0 | True | none | none |
| legacy-r4-seed-61 | workshop:bob | workshop:eve | supervision | 0 | 0 | True | none | none |
| legacy-r4-seed-61 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | True | none | none |
| legacy-r4-seed-61 | workshop:eve | workshop:bob | supervision_inverse | 0 | 0 | True | none | none |
| grade-v1-seed-17 | workshop:alice | workshop:bob | duality | 0 | 0 | True | none | none |
| grade-v1-seed-17 | workshop:alice | workshop:eve | benefit | 0 | 0 | True | none | none |
| grade-v1-seed-17 | workshop:bob | workshop:alice | duality | 0 | 0 | True | none | none |
| grade-v1-seed-17 | workshop:bob | workshop:eve | supervision | 0 | 0 | True | none | none |
| grade-v1-seed-17 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | True | none | none |
| grade-v1-seed-17 | workshop:eve | workshop:bob | supervision_inverse | 0 | 0 | True | none | none |
| grade-v1-seed-29 | workshop:alice | workshop:bob | duality | 0 | 0 | True | none | none |
| grade-v1-seed-29 | workshop:alice | workshop:eve | benefit | 0 | 0 | True | none | none |
| grade-v1-seed-29 | workshop:bob | workshop:alice | duality | 0 | 0 | True | none | none |
| grade-v1-seed-29 | workshop:bob | workshop:eve | supervision | 0 | 0 | True | none | none |
| grade-v1-seed-29 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | True | none | none |
| grade-v1-seed-29 | workshop:eve | workshop:bob | supervision_inverse | 0 | 0 | True | none | none |
| grade-v1-seed-43 | workshop:alice | workshop:bob | duality | 0 | 0 | True | none | none |
| grade-v1-seed-43 | workshop:alice | workshop:eve | benefit | 0 | 0 | True | none | none |
| grade-v1-seed-43 | workshop:bob | workshop:alice | duality | 0 | 0 | True | none | none |
| grade-v1-seed-43 | workshop:bob | workshop:eve | supervision | 0 | 0 | True | none | none |
| grade-v1-seed-43 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | True | none | none |
| grade-v1-seed-43 | workshop:eve | workshop:bob | supervision_inverse | 0 | 0 | True | none | none |
| grade-v1-seed-61 | workshop:alice | workshop:bob | duality | 0 | 0 | True | none | none |
| grade-v1-seed-61 | workshop:alice | workshop:eve | benefit | 0 | 0 | True | none | none |
| grade-v1-seed-61 | workshop:bob | workshop:alice | duality | 0 | 0 | True | none | none |
| grade-v1-seed-61 | workshop:bob | workshop:eve | supervision | 0 | 0 | True | none | none |
| grade-v1-seed-61 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | True | none | none |
| grade-v1-seed-61 | workshop:eve | workshop:bob | supervision_inverse | 0 | 0 | True | none | none |

## Benefit pairs within the triad versus triad total

Pair-subset counts are observations WITHIN the same triad, not independent two-actor experiments. Benefit-family totals include benefit and benefit_inverse directions. The accepted manifest has no standalone pair histories; their comparison is unavailable, not zero.

| History | Source | Receiver | Relation | Pair-subset uses | Triad benefit-family uses | Standalone pair uses | Pair-subset IDs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| legacy-r4-seed-17 | workshop:alice | workshop:eve | benefit | 0 | 0 | N/A: not generated | none |
| legacy-r4-seed-17 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | N/A: not generated | none |
| legacy-r4-seed-29 | workshop:alice | workshop:eve | benefit | 0 | 0 | N/A: not generated | none |
| legacy-r4-seed-29 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | N/A: not generated | none |
| legacy-r4-seed-43 | workshop:alice | workshop:eve | benefit | 0 | 0 | N/A: not generated | none |
| legacy-r4-seed-43 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | N/A: not generated | none |
| legacy-r4-seed-61 | workshop:alice | workshop:eve | benefit | 0 | 0 | N/A: not generated | none |
| legacy-r4-seed-61 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | N/A: not generated | none |
| grade-v1-seed-17 | workshop:alice | workshop:eve | benefit | 0 | 0 | N/A: not generated | none |
| grade-v1-seed-17 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | N/A: not generated | none |
| grade-v1-seed-29 | workshop:alice | workshop:eve | benefit | 0 | 0 | N/A: not generated | none |
| grade-v1-seed-29 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | N/A: not generated | none |
| grade-v1-seed-43 | workshop:alice | workshop:eve | benefit | 0 | 0 | N/A: not generated | none |
| grade-v1-seed-43 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | N/A: not generated | none |
| grade-v1-seed-61 | workshop:alice | workshop:eve | benefit | 0 | 0 | N/A: not generated | none |
| grade-v1-seed-61 | workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | N/A: not generated | none |
