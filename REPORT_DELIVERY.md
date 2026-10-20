# Function Conditioning — delivery report

## 1. Fixture and first delivery

The accepted Step 1 fixture is `tests_u11.fixtures.circuit11(flat=False)`;
Step 1 was not rerun. Its existing setup/group/join and circuit APIs generated
matched pair compositions on seeds 17, 29, 43 and 61, legacy-r4 only.
Each history is one harness episode including preparation. The same fixture
work limits apply in both compositions. Seeds choose finite, nonbinding budgets;
these are deterministic budget replicates, not distinct stochastic workloads.

In `pair-seed-17`, use u40 at transaction 307 (`join-accept`) is received by workshop:bob (sli), te at seat 2, dim 3. Supplier workshop:alice holds it at seat 6; relation: duality. Exact input `u11.invitation:f1fb117aa5db5f54af8a73fb4f93f9408498adeacc6441793e08e8e14f8b27de@1` was committed by that supplier at transaction 302.

Sources: [manifest](HISTORIES_DELIVERY.json), each history's exact calls, parameters and first-delivery join; [pair trace](TABLES/pair_per_actor_delivery.md#use-trace).

## 2. Actor indices

The following values hold at every seed. Conditioning retains the accepted
A1-literal ratio: received weak uses divided by received weak uses. It is
degenerate when defined. Hold is kept received / received.

| Composition | Actor | TIM | Status | Conditioning (A1 literal) | Hold |
| --- | --- | --- | --- | --- | --- |
| pair | workshop:alice | iee | active | 45/45 = 1 | 43/45 = 43/45 |
| pair | workshop:bob | sli | active | 12/12 = 1 | 48/52 = 12/13 |
| pair | workshop:eve | sli | inactive | 0/0 (N/A) | 0/0 (N/A) |
| pair-sterile | workshop:alice | eie | active | 40/40 = 1 | 71/75 = 71/75 |
| pair-sterile | workshop:bob | sli | active | 12/12 = 1 | 48/52 = 12/13 |
| pair-sterile | workshop:eve | sli | inactive | 0/0 (N/A) | 0/0 (N/A) |

Sources: Actor indices in the [pair](TABLES/pair_per_actor_delivery.md#actor-indices) and [pair-sterile](TABLES/pair-sterile_per_actor_delivery.md#actor-indices) tables.

## 3. Coverage across compositions

| Composition | Coverage at every seed and through episode 0 |
| --- | --- |
| pair | 4/12 = 1/3 |
| pair-sterile | 4/12 = 1/3 |
| triad (IEE/SLI/LIE) | N/A — not producible |

Coverage is identical across the supported pair compositions at matched seeds. This is the observed composition contrast; the requested pair-versus-triad presence comparison is unavailable.

Pair means Alice and Bob participate in the collective. The fixture also commits inactive Eve=SLI; her weak seats remain in the denominator. These are not worlds containing only two actor profiles. `setup11(tim=)` changes Alice only; group/join cannot make Eve a LIE.

Sources: Population summary and episode rows in the [pair](TABLES/pair_per_population_delivery.md) and [pair-sterile](TABLES/pair-sterile_per_population_delivery.md) tables; the manifest records the unavailable triad.

## 4. Sterile pairs and prediction

| Composition | Source | Receiver | Relation | Forward | Reverse | Sterile |
| --- | --- | --- | --- | --- | --- | --- |
| pair | workshop:alice | workshop:bob | duality | 52 | 45 | False |
| pair | workshop:alice | workshop:eve | duality | 0 | 0 | True |
| pair | workshop:bob | workshop:alice | duality | 45 | 52 | False |
| pair | workshop:bob | workshop:eve | identity | 0 | 0 | True |
| pair | workshop:eve | workshop:alice | duality | 0 | 0 | True |
| pair | workshop:eve | workshop:bob | identity | 0 | 0 | True |
| pair-sterile | workshop:alice | workshop:bob | conflict | 52 | 75 | False |
| pair-sterile | workshop:alice | workshop:eve | conflict | 0 | 0 | True |
| pair-sterile | workshop:bob | workshop:alice | conflict | 75 | 52 | False |
| pair-sterile | workshop:bob | workshop:eve | identity | 0 | 0 | True |
| pair-sterile | workshop:eve | workshop:alice | conflict | 0 | 0 | True |
| pair-sterile | workshop:eve | workshop:bob | identity | 0 | 0 | True |

Every row holds across seeds. The directive predicts conflict is sterile both ways; no separate yield-table artifact was located. `pair-sterile` names that prediction. These counts use A3/A4 provenance. Inactive Eve's zeros do not establish intrinsic relation sterility.

Sources: Ordered pairs in both composition population tables.

## 5. DCNH all-use versus received-and-kept

| Composition | Actor | TIM | All uses | Received and kept | Comparison |
| --- | --- | --- | --- | --- | --- |
| pair | workshop:alice | iee | 85 | 43 | diverge |
| pair | workshop:bob | sli | 52 | 48 | diverge |
| pair | workshop:eve | sli | 0 | 0 | agree |
| pair-sterile | workshop:alice | eie | 146 | 71 | diverge |
| pair-sterile | workshop:bob | sli | 52 | 48 | diverge |
| pair-sterile | workshop:eve | sli | 0 | 0 | agree |

These comparisons hold at every seed. Inactive Eve's agreement is between empty observations. All-use rows equal native Phase 7 observations exactly.

Sources: [pair DCNH](TABLES/pair_dcnh_two_ways_delivery.md) and [pair-sterile DCNH](TABLES/pair-sterile_dcnh_two_ways_delivery.md).

## 6. Limits

A3/A4 provenance counts **any exact operation input, including collective
evidence such as an invitation**. This is broader than delivery of one route's
semantic content. Every paid block of such an operation shares its producer
tuple. A listed producer need not have produced that block's information element;
its source seat is derived from its TIM. No causal learning claim follows.

These are generated, supplied circuit workloads, not historical observations.
The existing circuit includes paid damage to renew its supplied demand; no new
demand rule was added. The paired comparison changes Alice's TIM with Bob fixed;
it does not isolate a third member's presence. A true IEE/SLI/LIE triad was not
producible with the authorized fixture calls. Background Eve remains SLI and
inactive. Four matched seeds vary only nonbinding budgets, so they do not
establish workload robustness. The fixture has operation-specific work limits,
not a Population scheduler quantum; the manifest records the exact common limits.

The accepted conditioning-index denominator is still degenerate. Undefined
ratios remain N/A. No feedback, energy regeneration, practice pricing, Model G
seats, or new demand formation was added. The read repository is unchanged;
the accepted Batch 1 outputs regenerate byte-identically. Nothing is closed.
