# Function Conditioning — delivery report

## 1. Fixture and first delivery

The accepted fixture is `tests_u11.fixtures.circuit11(flat=False)`; the original
Step 1 probe was not rerun. Existing parameterized setup/group/join calls
produce pair and pair-sterile compositions. All use legacy-r4, seeds 17, 29,
43, 61, and one harness episode including preparation. Seeds vary finite,
nonbinding budgets; they are not distinct stochastic workloads.

Wide includes source.N, source_input and input.N. Narrow excludes input.N.
The earliest observed deliveries in pair-seed-17 are:

| Reading | Use | Transaction | Operation | Receiver | Element | Seat | Dim | Sources | Producer transaction | Exact input |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| wide | u40 | 307 | join-accept | workshop:bob | te | 2 | 3 | workshop:alice | 302 | u11.invitation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@1 |
| narrow | none | none | none | none | none | none | none | none | none | none |

Sources: [manifest](HISTORIES_DELIVERY.json) for calls and wide witness; [pair trace](TABLES/pair_per_actor_delivery.md#use-trace) and exact-revision joins in the regenerated journal for both readings.

## 2. Actor indices

Received weak uses / all weak uses is the corrected conditioning index; kept received / received is hold. N/A denotes a zero denominator. Rows apply at every seed.

| Composition | Actor | TIM | Status | Conditioning wide | Conditioning narrow | Hold wide | Hold narrow |
| --- | --- | --- | --- | --- | --- | --- | --- |
| pair | workshop:alice | iee | active | 45/84 = 15/28 | 0/84 = 0 | 43/45 = 43/45 | 0/0 (N/A) |
| pair | workshop:bob | sli | active | 12/12 = 1 | 0/12 = 0 | 48/52 = 12/13 | 0/0 (N/A) |
| pair | workshop:eve | sli | inactive | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) |
| pair-sterile | workshop:alice | eie | active | 40/77 = 40/77 | 0/77 = 0 | 71/75 = 71/75 | 0/0 (N/A) |
| pair-sterile | workshop:bob | sli | active | 12/12 = 1 | 0/12 = 0 | 48/52 = 12/13 | 0/0 (N/A) |
| pair-sterile | workshop:eve | sli | inactive | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) | 0/0 (N/A) |

Sources: [pair indices](TABLES/pair_per_actor_delivery.md#actor-indices), [pair-sterile indices](TABLES/pair-sterile_per_actor_delivery.md#actor-indices).

## 3. Coverage across compositions

| Composition | Received wide | Received narrow | Coverage wide | Coverage narrow |
| --- | --- | --- | --- | --- |
| pair | 97 | 0 | 4/12 = 1/3 | 0/12 = 0 |
| pair-sterile | 127 | 0 | 4/12 = 1/3 | 0/12 = 0 |
| triad (IEE/SLI/LIE) | N/A | N/A | not producible | not producible |

These values hold at every seed and through episode 0. Compare each reading
separately: coverage is identical across the supported pair compositions.
The wide reading records U11 delivery for both duality and conflict; narrow records none; this does not establish
relation independence generally. Eve is an inactive SLI in both compositions
and remains in the denominator. No IEE/SLI/LIE triad or third-person presence
comparison was producible with the authorized calls.

Sources: [pair population](TABLES/pair_per_population_delivery.md),
[pair-sterile population](TABLES/pair-sterile_per_population_delivery.md).

## 4. Sterile pairs and prediction

| Composition | Source | Receiver | Relation | Forward wide | Forward narrow | Reverse wide | Reverse narrow | Sterile wide | Sterile narrow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair | workshop:alice | workshop:bob | duality | 52 | 0 | 45 | 0 | False | True |
| pair | workshop:alice | workshop:eve | duality | 0 | 0 | 0 | 0 | True | True |
| pair | workshop:bob | workshop:eve | identity | 0 | 0 | 0 | 0 | True | True |
| pair-sterile | workshop:alice | workshop:bob | conflict | 52 | 0 | 75 | 0 | False | True |
| pair-sterile | workshop:alice | workshop:eve | conflict | 0 | 0 | 0 | 0 | True | True |
| pair-sterile | workshop:bob | workshop:eve | identity | 0 | 0 | 0 | 0 | True | True |

Each row includes both directions and holds across seeds. The name pair-sterile records the directive's conflict prediction, not the result. No independent yield-table artifact was located. Eve's zeros do not show intrinsic sterility. Sources: ordered-pair rows in both population tables.

## 5. DCNH all-use versus received-and-kept

| Composition | Actor | TIM | All uses (both) | Received kept wide | Received kept narrow | Greatest all (both) | Greatest received kept wide | Greatest received kept narrow | Comparison wide | Comparison narrow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair | workshop:alice | iee | 85 | 43 | 0 | H,D | H | C,N,H,D | diverge | diverge |
| pair | workshop:bob | sli | 52 | 48 | 0 | D | D | H,D,C,N | diverge | diverge |
| pair | workshop:eve | sli | 0 | 0 | 0 | H,D,C,N | H,D,C,N | H,D,C,N | agree | agree |
| pair-sterile | workshop:alice | eie | 146 | 71 | 0 | H | D,H | D,H,N,C | diverge | diverge |
| pair-sterile | workshop:bob | sli | 52 | 48 | 0 | D | D | H,D,C,N | diverge | diverge |
| pair-sterile | workshop:eve | sli | 0 | 0 | 0 | H,D,C,N | H,D,C,N | H,D,C,N | agree | agree |

All-use rows equal native Phase 7 observations. Comparisons use complete observations; a shared greatest cell alone is not agreement. Eve's agreement is between empty observations. Sources: [pair DCNH](TABLES/pair_dcnh_two_ways_delivery.md), [pair-sterile DCNH](TABLES/pair-sterile_dcnh_two_ways_delivery.md).

## 6. Limits

Wide provenance is an upper bound: any exact operation input counts, including collective
evidence such as an invitation. Narrow removes generic input.N evidence, but
still assigns each operation's selected supplier tuple to every paid block.
Neither reading proves an element's semantic lineage, learning, or causation.

Only supplied generated workloads were measured. U11 emphasizes strong seats
and repeated work; retention is nearly saturated at this workload. Four seeds
vary only nonbinding budgets. Eve is always inactive. The requested triad was
not producible, so this is not a test of an added person's presence. No historical
archive was used. The circuit's existing paid damage renews supplied demand;
no new demand formation, feedback, regeneration, pricing, or Model G seats were
added. Read-engine hashes are unchanged. Undefined ratios remain N/A. See
[LIMITS.md](LIMITS.md) for consolidated bounds.

## 8. Use classes and price of type

Wide reading; rows hold at every seed; N/A is a zero denominator. Cond. by class: received weak uses of the class / all weak uses of the class. Internalisation: received uses later followed by a self/world use at the same seat / received uses. Margin: greatest axis load minus runner-up. Energy is CT Table 13 block energy, not a legacy-r4 wallet debit.

| Composition | Actor | TIM | Hops | Content | Cond. content | Cond. hop | Internalisation | Greatest all (margin) | Greatest content (margin) | Greatest hop (margin) | Time | Energy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pair | workshop:alice | iee | 47 | 38 | 20/38 | 25/46 | 0/45 | H,D (0) | H,D (0) | H,D (0) | 296 | 253 |
| pair | workshop:bob | sli | 40 | 12 | N/A | 12/12 | 0/52 | D (4) | H,D (0) | D (4) | 102 | 80 |
| pair-sterile | workshop:alice | eie | 108 | 38 | 20/38 | 20/39 | 0/75 | H (1) | D,H (0) | C (1) | 373 | 437 |
| pair-sterile | workshop:bob | sli | 40 | 12 | N/A | 12/12 | 0/52 | D (4) | H,D (0) | D (4) | 102 | 80 |

pair coverage: structural 4/12, observed 2/12; inactive (all N/A): workshop:eve. pair-sterile coverage: structural 4/12, observed 2/12; inactive (all N/A): workshop:eve. Narrow finds no received uses, so its class indices and internalisation are 0 or N/A. Sources: [classes](TABLES/pair_classes_delivery.md), [price of type](TABLES/pair_price_of_type_delivery.md), [DCNH five ways](TABLES/pair_dcnh_five_ways_delivery.md), and the pair-sterile files.
