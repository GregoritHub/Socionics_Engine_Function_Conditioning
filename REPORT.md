# Function Conditioning Ledger — final report

## 1. What was generated

The accepted `HISTORIES.json` contains matched fixture seeds under the following
resource models. Each history contains Alice (`workshop:alice`, IEE), Bob
(`workshop:bob`, SLI), and Eve (`workshop:eve`, LIE).

| Model | Fixture seeds | Actors per history | Transactions per history |
| --- | --- | --- | --- |
| legacy-r4 | 17, 29, 43, 61 | 3 | 216 |
| grade-v1 | 17, 29, 43, 61 | 3 | 216 |

Sources: [accepted input rows](TABLES/per_population.md#accepted-inputs), keyed
by model and seed; [DCNH rows](TABLES/dcnh_two_ways.md), keyed by history and actor,
for actor identities and TIMs. These are generated histories, not historical archives.

## 2. Cross-actor delivery

**No cross-actor delivery observed in generated histories.** Every history's
`Received uses` cell is **0**. The use-profile and trace rows identify the
observed sources as `world`, which does not count as actor-supplied delivery.
This retains the accepted provenance finding.

Sources: [population summary](TABLES/per_population.md#population-summary),
every history row; [use profile](TABLES/per_actor.md#use-profile) and
[use trace](TABLES/per_actor.md#use-trace).

## 3. DCNH all-use versus received-and-kept

The comparison is **diverge** for each actor in every generated history.
The following rows apply under every model and seed listed above.

| Actor | TIM | All-use count | Received-and-kept count | DCNH comparison |
| --- | --- | --- | --- | --- |
| workshop:alice | iee | 6 | 0 | diverge |
| workshop:bob | sli | 21 | 0 | diverge |
| workshop:eve | lie | 19 | 0 | diverge |

Source: [DCNH two ways](TABLES/dcnh_two_ways.md), each history's paired
`all uses` and `received and kept` rows for the named actor, including their
`Uses` and `Comparison` cells. The source table supplies the corresponding
axis loads, tilts, and greatest-load cells.

## 4. Coverage per population and episode

| History | Final coverage | Through episode 0 | Through episode 1 |
| --- | --- | --- | --- |
| legacy-r4-seed-17 | 0/12 | 0/12 | 0/12 |
| legacy-r4-seed-29 | 0/12 | 0/12 | 0/12 |
| legacy-r4-seed-43 | 0/12 | 0/12 | 0/12 |
| legacy-r4-seed-61 | 0/12 | 0/12 | 0/12 |
| grade-v1-seed-17 | 0/12 | 0/12 | 0/12 |
| grade-v1-seed-29 | 0/12 | 0/12 | 0/12 |
| grade-v1-seed-43 | 0/12 | 0/12 | 0/12 |
| grade-v1-seed-61 | 0/12 | 0/12 | 0/12 |

The denominator includes every committed actor's weak seats, including any
inactive actor. Episode coverage is cumulative through each actor-local
episode index, pooled across actors; it is not a wall-clock snapshot.

Sources: [population summary](TABLES/per_population.md#population-summary),
matching history's `Coverage` cell; [coverage by episode index](TABLES/per_population.md#coverage-by-episode-index),
matching history and `Through episode` row.

## 5. Sterile ordered pairs

These ordered pairs are sterile in every generated history. Forward means
source to receiver; sterility requires no received uses in either direction.

| Source | Receiver | Relation | Forward uses | Reverse uses |
| --- | --- | --- | --- | --- |
| workshop:alice | workshop:bob | duality | 0 | 0 |
| workshop:alice | workshop:eve | benefit | 0 | 0 |
| workshop:bob | workshop:alice | duality | 0 | 0 |
| workshop:bob | workshop:eve | supervision | 0 | 0 |
| workshop:eve | workshop:alice | benefit_inverse | 0 | 0 |
| workshop:eve | workshop:bob | supervision_inverse | 0 | 0 |

Source: [ordered pairs](TABLES/per_population.md#ordered-pairs), matching
source/receiver rows in every history. Their `Sterile` cells are `True`;
relation names retain the pinned kernel's direction convention.

## 6. Benefit pair versus triad

The following values apply in every generated history.

| Source | Receiver | Relation | Pair-subset uses within triad | Triad benefit-family uses | Standalone pair uses |
| --- | --- | --- | --- | --- | --- |
| workshop:alice | workshop:eve | benefit | 0 | 0 | N/A: not generated |
| workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | N/A: not generated |

Source: [benefit pairs within the triad versus triad total](TABLES/per_population.md#benefit-pairs-within-the-triad-versus-triad-total),
matching source/receiver rows in each history. The triad total includes both
benefit directions. Pair-subset counts describe the same triad; they are not
standalone pair experiments. A standalone pair-versus-triad comparison is
therefore unavailable, not an observed equality.

## 7. Limits

Generated histories only; no historical archive was used. Test-only positive
delivery examples are not findings from these histories. No feedback, energy
regeneration, practice pricing, demand formation, or executor change was added.
The read repository remains unchanged. Nothing about the theory is closed.

The [actor-index rows](TABLES/per_actor.md#actor-indices) report conditioning
and hold as **0/0 (N/A)** throughout. The [population-summary rows](TABLES/per_population.md#population-summary)
report supplier concentration as **0/0 (N/A)**. Undefined ratios are distinct
from measured zero delivery or coverage.

The reported conditioning index applies Amendment A1's literal actor-source
restriction to both numerator and denominator, making it degenerate whenever
defined. This report preserves the explicitly labeled calculation; it does
not resolve the source-scope question or silently restore the older denominator.
The missing standalone pair experiment remains unavailable. No generator
replacement or additional experiment is authorized by these findings.
