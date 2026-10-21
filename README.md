# Function Conditioning Ledger v2

Start with [REPRODUCE.md](REPRODUCE.md) to regenerate every measured result.
The reports cover [population histories](REPORT.md), [delivery compositions](REPORT_DELIVERY.md)
and the [eight-element solo composition](REPORT_SOLO8.md).

## Engine commit

`fdede6f16721f06422d0798a79d84170969b83f8`

The read clone is the sibling directory `../Socionics_Engine`. Never edit or
commit there, copy its files here, or publish its files from this repository.
`ENGINE_FREEZE.sha256` records paths relative to that clone.

## Local setup and proof

Use Python 3.12. Clone and pin the engine as described in [REPRODUCE.md](REPRODUCE.md),
then create the ignored `engine_path.txt` with `../Socionics_Engine` on one line.
Run from this repository:

```sh
python tools/reproduce.py
```

For setup alone: `python -m unittest tests.test_00_setup -v`. Imports disable
bytecode writes before loading the engine. No pip packages are required.

## What this measures

**Seat** identifies the Model A position where an actor completes a paid use of
an information element. It connects the count to the actor's committed TIM;
it is not a Model G seat.

**Dim** is that seat's kernel-defined dimensionality. Weak seats have dim ≤ 2;
strong seats have dim ≥ 3. This categorization determines the conditioning-index
denominator and the receiver/supplier conditions for coverage.

**Source** identifies producers of exact input revisions: self, world, or a
sorted tuple of other committed actors. Wide includes every operation input;
narrow includes only declared semantic inputs. Both inherit the operation's
source tuple at every paid block, so neither proves individual element lineage.

**Kept** means the same actor later completes paid work at the same seat and
element within the history. It measures a repeat, not learning or acquisition;
the last use at a seat is not kept. See [GLOSSARY.md](GLOSSARY.md) for derived measures.

## What it does not do

This companion observes histories. It supplies no feedback, changes no prices
or execution choices, assigns no subtype, and makes no claim about people.
Relation names are attached after measurement and never drive numerical
aggregation or engine computation. The kernel transformations define the
benefit-family grouping; names label its presentation. Renaming labels leaves
all measured values unchanged. Ties remain ties. See [LIMITS.md](LIMITS.md).

## Findings

The population fixtures have **0 received uses under both readings**. The
corrected index is Alice **0/1**, Bob **0/9**, Eve **0/4** at every seed/model:
[actor rows](TABLES/per_actor.md#actor-indices). Bob completed nine weak-seat
uses, none received.

The first **wide** delivery is Bob's use u40 at transaction 307, consuming
Alice's invitation committed at transaction 302: [pair trace](TABLES/pair_per_actor_delivery.md#use-trace),
[exact join](REPORT_DELIVERY.md#1-fixture-and-first-delivery). Narrow finds **0**
deliveries; wide counts **97** for pair and **127** for pair-sterile:
[population rows](TABLES/pair_per_population_delivery.md#population-summary),
[comparison](REPORT_DELIVERY.md#3-coverage-across-compositions).

For pair Alice, greatest-load cells change from **H,D** on all uses to **H** on
wide received-and-kept uses. Narrow has an empty input and all cells tie:
[DCNH rows](TABLES/pair_dcnh_two_ways_delivery.md).

U11's wide delivery occurs for both duality and conflict; coverage is **4/12**
for either composition. Narrow coverage is **0/12** for either. This workload
does not show relation-specific coverage. Wide provenance is an upper bound,
and the requested triad was not producible; no third-person presence effect
was measured.

Batch 8 splits every use into a **hop** (transit along a route) or a **content**
block: Bob's 12 weak-seat uses are all hops, and the IEE and EIE complete the
same 38 content blocks for 47 versus 108 hops ([price of type](TABLES/pair_price_of_type_delivery.md),
[pair-sterile](TABLES/pair-sterile_price_of_type_delivery.md)). Observed coverage,
which requires the supplier to have done content work at the element, is **2/12**
against structural **4/12** ([classes](TABLES/pair_classes_delivery.md#structural-versus-observed-coverage)).
Internalisation, a received use later repeated self-sourced, is **0** in every
history, because each ends inside the collective ([five ways](TABLES/pair_dcnh_five_ways_delivery.md)).

## Full-field finding (Batch 9)

`pair-solo8` runs the pair sequence and then a 17-row program by Alice alone
that demands every element in both faces, on one journal
([report](REPORT_SOLO8.md)). Every one of Alice's eight seats completes
content work (**4,6,2,4,41,39,6,2** at seats 1–8). The prediction recorded
before generation held: internalisation is **23/67** at seat 5 and **62/62**
at seat 6 under the wide reading ([field](TABLES/pair-solo8_field.md),
[sequence](TABLES/pair-solo8_sequence.md)). Her greatest-load cell is **D**
on all uses but **H** on content alone, in every phase; the two readings of
the same history disagree by class, not by seed. Workflow operations declare
semantic inputs, so the narrow reading records received uses for the first
time (**28** for Alice, all from Bob's exchange replies). Share and Coordinate
rows need a peer by the fixture's construction, so Bob works in the solo phase
as a respondent (Amendment A9).

## How to read a table

Take Alice's `pair-seed-17` row in [actor indices](TABLES/pair_per_actor_delivery.md#actor-indices).
History identifies the run; Actor identifies Alice; TIM is IEE; Status is active.
Conditioning wide is **45/84 = 15/28**: received weak uses over all weak uses.
Hold wide is **43/45**. The next columns identify the conditioning numerator,
all received uses, and kept received uses: **45**, **45**, and **43** trace IDs.
Conditioning narrow is **0/84 = 0**; Hold narrow is **N/A** because no uses are
received; its three ID lists are empty. Each ID resolves to a transaction,
operation revision, block boundary, seat, dimension, source and kept value in
the shared use trace. Counts are occurrences, not distinct transactions.

## History of the build

- [Batch 0](RECEIPTS/batch_0.md): fields and engine freeze; publication refusal later resolved.
- [Batch 1](RECEIPTS/batch_1.md): generated population histories.
- [Batch 2](RECEIPTS/batch_2.md): provenance stop, then acceptance under A1.
- [Batch 3](RECEIPTS/batch_3.md): retention accepted after the A2 contradiction ruling.
- [Batch 4](RECEIPTS/batch_4.md): measures and traced tables; denominator caveat recorded.
- [Batch 5](RECEIPTS/batch_5.md): population report; no cross-actor delivery.
- [Batch 6](RECEIPTS/batch_6.md): stopped provenance/guard attempts, then A4 acceptance and delivery compositions.
- [Batch 7](RECEIPTS/batch_7.md): denominator correction, two readings, reproduction and review documentation.
- [A1](DIRECTIVE_AMENDMENT_A1_world_source.md): actorless producers become world; clears Batch 2.
- [A2](DIRECTIVE_AMENDMENT_A2_I4_monotone.md): defines I4 under history growth; clears retention contradiction.
- [A3](DIRECTIVE_AMENDMENT_A3_operation_provenance.md): operation-level provenance and receipt hygiene.
- [A4](DIRECTIVE_AMENDMENT_A4_tuple_scope.md): tuple-aware aggregation and accepted-output guard; clears Batch 6.
- [A5](DIRECTIVE_AMENDMENT_A5_review_guard.md): permits corrected indices; preserves other wide cells and historical receipts.
- [A6](DIRECTIVE_AMENDMENT_A6_path_gate_publication.md): replaces the grep gate with a scoped path checker; authorizes stopped-receipt publication.
- [A7](DIRECTIVE_AMENDMENT_A7_publication_transport.md): permits connector publication with local/published hashes and tree verification.
- [Batch 8](RECEIPTS/batch_8.md): use classes, observed supply, DCNH margins, price of type, internalisation; all additive.
- [A8](DIRECTIVE_AMENDMENT_A8_additive_tables.md): Batch 8 measures go in new tables; Batch 7 files byte-identical.
- [Batch 9](RECEIPTS/batch_9.md): the pair-solo8 composition on one journal; eight-seat field; internalisation observed.
- [A9](DIRECTIVE_AMENDMENT_A9_solo8_program.md): program trimmed to the fixture's two care units; wear preparation; Bob as respondent.

The [receipts index](RECEIPTS/README.md) retains the stops, refusals, repairs, and clearances.

## Relationship to the engine repository

The engine is read-only and pinned. The freeze verifies the complete file sets
and SHA-256 bytes under `hle_unified/` and `baseline/HLE_Rebuild_R21B/hle/`.
The setup check also detects references back to this companion. These checks
guarantee unchanged audited code relative to the recorded freeze; they do not
freeze every fixture/document in the engine, prove kernel correctness, establish
scientific validity, or demonstrate behavior outside the generated workloads.
The pinned Git commit identifies the remaining engine files.

## Directive appendix (v1.9)

The [original directive](BATCH_DIRECTIVE_Function_Conditioning_v1.md), linked
amendments, [Batch 6 extension](DIRECTIVE_BATCH_6_cross_actor_delivery.md),
[Batch 7 extension](DIRECTIVE_BATCH_7_review_prep.md) and
[Batches 8–9 extension](DIRECTIVE_BATCH_8_9_use_classes_observed_supply_solo_phase.md) form the audit trail.
A5 governs Batch 7's guard; A6 defines the path gate, A7 the publication transport,
A8 the additive placement of Batch 8 measures, A9 the solo8 program under the
fixture's material limits. No feedback rule is authorized. No LICENSE is included; licensing remains the owner's decision.
[CITATION.cff](CITATION.cff) records attribution and the pinned engine commit.
