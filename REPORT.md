# Function Conditioning Ledger — population report

## 1. What was generated

Generated population histories contain Alice=IEE, Bob=SLI, and Eve=LIE. The
accepted manifests and original paid-use counts are unchanged under A5.

| Model | Fixture seeds | Actors | Transactions |
| --- | --- | --- | --- |
| legacy-r4 | 17, 29, 43, 61 | 3 | 216 |
| grade-v1 | 17, 29, 43, 61 | 3 | 216 |

Source: [accepted inputs](TABLES/per_population.md#accepted-inputs).

## 2. Cross-actor delivery and corrected conditioning

**No cross-actor delivery observed in generated histories under either reading.**
Wide uses every exact operation input; narrow uses only source.N/source_input.
Every source here is world. Both readings have zero received uses. The corrected
conditioning index is received weak uses / ALL weak uses; hold is kept received
/ received. A zero denominator is N/A. These rows hold in every listed history.
Bob's 0/9 means nine weak-seat uses and none received: a defined zero, not N/A.

| Actor | TIM | Status | Conditioning wide | Conditioning narrow | Hold wide | Hold narrow |
| --- | --- | --- | --- | --- | --- | --- |
| workshop:alice | iee | active | 0/1 = 0 | 0/1 = 0 | 0/0 (N/A) | 0/0 (N/A) |
| workshop:bob | sli | active | 0/9 = 0 | 0/9 = 0 | 0/0 (N/A) | 0/0 (N/A) |
| workshop:eve | lie | active | 0/4 = 0 | 0/4 = 0 | 0/0 (N/A) | 0/0 (N/A) |

Sources: [actor indices](TABLES/per_actor.md#actor-indices), [use trace](TABLES/per_actor.md#use-trace), [population summary](TABLES/per_population.md#population-summary).

## 3. DCNH all-use versus received-and-kept

Every row holds at every seed and model. Comparisons use complete observations; greatest-load cells retain all ties.

| Actor | TIM | All uses (both) | Received kept wide | Received kept narrow | Greatest all (both) | Greatest received kept wide | Greatest received kept narrow | Comparison wide | Comparison narrow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| workshop:alice | iee | 6 | 0 | 0 | H | C,N,H,D | C,N,H,D | diverge | diverge |
| workshop:bob | sli | 21 | 0 | 0 | H | H,D,C,N | H,D,C,N | diverge | diverge |
| workshop:eve | lie | 19 | 0 | 0 | H | D,H,N,C | D,H,N,C | diverge | diverge |

Source: [DCNH rows](TABLES/dcnh_two_ways.md). Empty received-and-kept observations do not assign a subtype.

## 4. Coverage per population and episode

| History | Final wide | Final narrow | Episode 0 wide | Episode 0 narrow | Episode 1 wide | Episode 1 narrow |
| --- | --- | --- | --- | --- | --- | --- |
| legacy-r4-seed-17 | 0/12 = 0 | 0/12 = 0 | 0/12 | 0/12 | 0/12 | 0/12 |
| legacy-r4-seed-29 | 0/12 = 0 | 0/12 = 0 | 0/12 | 0/12 | 0/12 | 0/12 |
| legacy-r4-seed-43 | 0/12 = 0 | 0/12 = 0 | 0/12 | 0/12 | 0/12 | 0/12 |
| legacy-r4-seed-61 | 0/12 = 0 | 0/12 = 0 | 0/12 | 0/12 | 0/12 | 0/12 |
| grade-v1-seed-17 | 0/12 = 0 | 0/12 = 0 | 0/12 | 0/12 | 0/12 | 0/12 |
| grade-v1-seed-29 | 0/12 = 0 | 0/12 = 0 | 0/12 | 0/12 | 0/12 | 0/12 |
| grade-v1-seed-43 | 0/12 = 0 | 0/12 = 0 | 0/12 | 0/12 | 0/12 | 0/12 |
| grade-v1-seed-61 | 0/12 = 0 | 0/12 = 0 | 0/12 | 0/12 | 0/12 | 0/12 |

Sources: [population summary](TABLES/per_population.md#population-summary) and [episode coverage](TABLES/per_population.md#coverage-by-episode-index). All committed actors' weak seats remain in the denominator. Episode indices pool actor-local episodes, not clock time.

## 5. Sterile ordered pairs

These rows hold in every history. Sterile requires zero received uses in both directions.

| Source | Receiver | Relation | Forward wide | Forward narrow | Reverse wide | Reverse narrow | Sterile wide | Sterile narrow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| workshop:alice | workshop:bob | duality | 0 | 0 | 0 | 0 | True | True |
| workshop:alice | workshop:eve | benefit | 0 | 0 | 0 | 0 | True | True |
| workshop:bob | workshop:alice | duality | 0 | 0 | 0 | 0 | True | True |
| workshop:bob | workshop:eve | supervision | 0 | 0 | 0 | 0 | True | True |
| workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | 0 | 0 | True | True |
| workshop:eve | workshop:bob | supervision_inverse | 0 | 0 | 0 | 0 | True | True |

Source: [ordered pairs](TABLES/per_population.md#ordered-pairs). Names annotate measured pairs.

## 6. Benefit pair versus triad

| Source | Receiver | Relation | Pair wide | Pair narrow | Triad wide | Triad narrow | Standalone pair |
| --- | --- | --- | --- | --- | --- | --- | --- |
| workshop:alice | workshop:eve | benefit | 0 | 0 | 0 | 0 | N/A: not generated |
| workshop:eve | workshop:alice | benefit_inverse | 0 | 0 | 0 | 0 | N/A: not generated |

Source: [benefit rows](TABLES/per_population.md#benefit-pairs-within-the-triad-versus-triad-total). Pair subsets are within this triad; independent pair experiments were not generated.

## 7. Limits

Generated workloads only; no historical archives, feedback, learning, subtype
assignment, or claims about people. Both readings preserve all-use counts and
DCNH. No actor-produced inputs were consumed in this fixture, so its zero
received counts do not test response to another actor's presence. Conditioning
is now defined when weak uses exist; hold and supplier concentration remain
N/A when no received uses exist. Wide is an operation-input upper bound on
semantic delivery. Narrow still assigns an operation's semantic-source tuple
to every paid block, not a verified lineage for each element. See [LIMITS.md](LIMITS.md).

## 8. Use classes and price of type

Wide reading; rows hold at every seed; N/A is a zero denominator. Cond. by class: received weak uses of the class / all weak uses of the class. Internalisation: received uses later followed by a self/world use at the same seat / received uses. Margin: greatest axis load minus runner-up. Energy is CT Table 13 block energy, not a legacy-r4 wallet debit.

| Actor | TIM | Hops | Content | Cond. content | Cond. hop | Internalisation | Greatest all (margin) | Greatest content (margin) | Greatest hop (margin) | Time | Energy |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| workshop:alice | iee | 2 | 4 | N/A | 0/1 | N/A | H (4) | H (4) | C,H (0) | 13 | 23 |
| workshop:bob | sli | 17 | 4 | 0/4 | 0/5 | N/A | H (1) | H (4) | C (3) | 47 | 67 |
| workshop:eve | lie | 15 | 4 | N/A | 0/4 | N/A | H (1) | H (4) | D (3) | 39 | 23 |

coverage: structural 0/12, observed 0/12. Narrow finds no received uses, so its class indices and internalisation are 0 or N/A. Sources: [classes](TABLES/classes.md), [price of type](TABLES/price_of_type.md), [DCNH five ways](TABLES/dcnh_five_ways.md).
