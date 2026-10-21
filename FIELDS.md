# Field declarations — pinned engine, Batch 0

Engine commit: `fdede6f16721f06422d0798a79d84170969b83f8`.
All paths and line numbers refer to this commit in the read clone.

`E` means `hle_unified/energy_audit.py`; `C` means
`hle_unified/conditioning_audit.py`. `data(version)` makes a dictionary from
`version.attributes` (`E:9–10`). Attributes below are dictionary entries, not
automatically fields on the `ObjectVersion` dataclass.

## Raw attributes read by the two audits

| Field or indexed field family | Record carrying it | Exact audit meaning | Read location |
| --- | --- | --- | --- |
| `record_type` | `ObjectVersion.attributes`; values used here are `operation` and `wallet` | Selects operation versions and wallet evidence. Profiles are selected by namespace, not this tag. | `E:70,89,115,119`; `C:20–21` |
| `actor` | Operation, wallet, and `u5.profile` version attributes | Committed actor identity: operation payer, wallet owner, or profile owner. It is not by itself the producer of an operation's semantic input. | `E:86–90,115,120`; `C:27,48,55–56` |
| `tim` | `u5.profile` and routed operation attributes | Profile's TIM and the routed operation's fixed TIM. The audit checks agreement and uses it to derive each element's Model A position. | `E:26,33,59–60,88,90`; `C:55` |
| `completed` | Operation attributes | Cumulative completed time/work units, not the number of completed element uses. A missing previous job supplies zero. Nondecreasing integer progress must not exceed `required`. | `E:56,62,96,102`; `C:30–34` |
| `required` | Operation attributes | Full operation extent in time/work units, including non-element work. Bounds completion and the final block end. Immutable within a job. | `E:16,39,41,59–60,96`; `C:32` |
| `spent` | Operation attributes | Cumulative paid work/time units; the conditioning audit requires equality with `completed`. It is not grade-v1 energy expenditure. | `C:33` |
| `route_count` | Routed operation attributes | Number of indexed routes. Presence selects routed accounting; absence produces one non-element block over the whole job. Immutable within a job. | `E:15,19,59–60,89`; `C:38` |
| `recall_units` | Routed operation attributes | Initial non-element work extent and initial route offset. Immutable within a job. | `E:17–18,59–60` |
| `route.{i}.path.{n}` | Routed operation attributes | Ordered route elements, with contiguous integer indices starting at zero. `path.0` is the starting position, so only `paths[1:]` produce paid hop blocks. | `E:20–26` |
| `route.{i}.charges.{j}` | Routed operation attributes | Time charge for the hop arriving at `path.{j+1}`. Must equal the literal CT `TIME` value at that arrival element's Model A seat. | `E:27–29` |
| `route.{i}.element` | Routed operation attributes | Element doing the route's seat-content work, following its hops. | `E:32–33` |
| `route.{i}.content_units` | Routed operation attributes | Seat-content duration in time units; an integer at least `TIME[seat-1]` and an exact multiple of it. One completed content block counts as one use even when the duration is a multiple. | `E:34–37`; `C:39–43` |
| All other `route.*` attributes | Routed operation attributes | Opaque route-contract values: `debit` compares every route-prefixed entry across revisions and rejects changes. No additional semantic interpretation is made here. | `E:58–61` |
| `resource_model` | Wallet attributes | Absent means `legacy-r4`; explicit presence must be `grade-v1`. Mixed/switched models are rejected. Determines whether wallet energy debit uses block energy or elapsed paid time. | `E:70–77`; `C:16,37` |
| `time` | Wallet attributes | Remaining time budget. Its decrease must equal the operation's newly completed time units; cannot be negative. Zero time prevents another paid unit. | `E:98`; `C:49–50` |
| `energy` | Wallet attributes | Remaining energy budget. Its decrease must match the selected model's debit; cannot be negative. Used to decide next-unit affordability. | `E:101–103`; `C:48,50` |
| `key` | Operation attributes | Job key used to locate an active operation, or its `:movement` job, in the grade-v1 agenda exhaustion check. | `E:114,118` |
| `status` | Operation attributes | A main job marked `succeeded` causes the exhaustion audit to inspect its corresponding movement job. Not the criterion for counting a completed block. | `E:117`; completion counting is `C:39–43` |

## Transaction and version metadata read by the audits

| Field | Record carrying it | Exact meaning | Read location |
| --- | --- | --- | --- |
| `versions` | `Transaction` | Ordered committed object versions inspected within each transaction. Wallet and work evidence must coincide as required by the audit. | `E:68,83,109`; `C:20–21,52` |
| `attributes` | `ObjectVersion` | Immutable named attribute records projected into the audit dictionary. | `E:10` |
| `name` | `Attribute` within a version | Dictionary key. | `E:10` |
| `value` | `Attribute` within a version | Dictionary value; may be an identity, exact revision reference, or scalar. | `E:10` |
| `ref.identity` | `ObjectVersion.ref` (`ObjectRef`) | Stable namespace/key identity used to retain the previous/head version while walking the journal. Identity alone is not an exact revision. | `E:109`; `C:28,47,57` |
| `ref.identity.namespace` | `ObjectVersion.ref.identity` (`ObjectId`) | `u5.profile` identifies committed actor type profiles. | `E:85`; `C:54` |
| `ref.revision` | `ObjectVersion.ref` | Exact positive revision number. Profiles must be revision 1 and unique by actor. | `E:86` |
| `previous` | `ObjectVersion` | Exact immediate predecessor reference or `None` on revision 1. Its presence selects wallet updates rather than wallet initialization. | `C:21`; schema `hle_unified/records.py:310,325–327` |
| `at.tick`, `at.order` (Batch 3 / R6) | `Transaction.at` (`hle.contracts.Moment`) | Committed logical journal position, not wall time or paid-work extent. The native store assigns `Moment(len(journal), 0)` on commit and requires the same sequence on restore. A complete history or its prefix therefore has `at.tick ==` its zero-based transaction index and `at.order == 0`. Retention rejects reordered or missing transactions instead of sorting them. Within a transaction, completed uses retain the existing audit's ordered block sequence. | `hle_unified/records.py:397–403`; `baseline/HLE_Rebuild_R21B/hle/contracts.py:84–92`; `hle_unified/compact.py:294–300,302–320,372–376`. Exercised by `tests/test_03_kept.py`'s timestamp, prefix, reordering, and forged-moment witnesses. |

## Derived values yielded by `blocks(d)`

The tuple is **`(start, end, energy_or_None, element)`**, as declared at `E:14`.
It does **not** contain a seat or position. These values are reconstructed from an
operation version, not stored as transaction attributes.

| Value | Record/source | Exact meaning | Construction/use |
| --- | --- | --- | --- |
| `start` | Derived operation block | Cumulative time offset at which the block starts. | `E:16–18,30,37,41`; `E:47–50`; `C:39` |
| `end` | Derived operation block | Cumulative time threshold at which the block completes. Count one use only when `before < end <= after` and the element is not `None`. | `E:16–18,30,37,41`; `C:39–43` |
| `energy_or_None` | Derived operation block | Third tuple value. Hop energy is `ENERGY[seat-1]`; content energy is that value times `content_units // TIME[seat-1]`. A non-element block has `None`, so energy follows elapsed time. Grade-v1 charges the entire element-block cost on the first unit that enters it. | `E:5–6,30,37,47–50`; `C:37` |
| `element` | Derived operation block | Hop arrival or seat-content element. `None` for recall, trailing work, and a non-routed job; these blocks never count as element uses. | `E:16–18,25,30,32,37,41`; `C:39–43` |
| `seat` / Model A position | Derived from operation `tim` and block `element` | Public position is `position_of(tim, element)` in 1–8. The audit's local variable `seat` subtracts one only for indexing `TIME` and `ENERGY`. It is not the block tuple's third item. | `E:26–28,33–37`; `C:67` uses positions 1–8 |

Completed hop/content blocks remain counted if the enclosing operation is later
cancelled. Partial blocks, proposals, preparation, and non-element blocks do not
count (`C:10–14,30–43`). A wallet revision must supply matching actor, time and
energy evidence (`C:44–51`).

## Input revision provenance

| Field/link | Record carrying it | Exact meaning and limits | Source location |
| --- | --- | --- | --- |
| **Provenance of an input revision: exact input `ObjectRef` → matching `version.ref` → producing `Transaction.actor`** | Operation input references, produced `ObjectVersion`, enclosing `Transaction` | **RESOLVED at revision level.** Find the transaction that committed the exact consumed reference, matching both identity and revision. Its `actor` is the actor recorded for that production transaction. It is nullable: an actorless source is not evidence of self-production. `writer` is a subsystem label, not an actor identity. This does not select one source for a multi-input hop or establish delivery/consumption by itself. | `hle_unified/records.py:304–305,397–403`; `hle_unified/compact.py:294–296,309–320,372–376`; actor attached by `hle_unified/operations.py:175–189` |
| `input.{n}` | Operation attributes | Indexed exact input revisions. Generic operations may include context and evidence inputs; this list is broader than semantic content. The source transaction is found through the exact-reference join above. | `hle_unified/operations.py:296–303,320–325`; not read by `E` or `C` |
| `source.{n}` | Workflow operation attributes | Indexed semantic input revisions from `r.inputs`, distinguished from the broader `input.{n}` list. No inferred latest-head substitution. | `hle_unified/workflow_execution.py:185–187,193`; not read by `E` or `C` |
| `source_input` | Workflow operation attributes | Primary semantic input `r.input`; a revision reference, not the producer's actor id. | `hle_unified/workflow_execution.py:173`; not read by `E` or `C` |
| `lineage` and each edge's `inputs`, `outputs`, `evidence` | `Transaction` and `Lineage` | Explicit causal revision links. In the common lifecycle, `inputs` contains the previous version on a revision; supplied input evidence is recorded separately in `evidence`. Do not conflate these two collections. | `hle_unified/records.py:380–387,403`; `hle_unified/operations.py:175–189,325`; `hle_unified/compact.py:294–296,320` |

The directive's path `hle_unified/world_records.py` does not exist at this commit.
The existing `baseline/HLE_Rebuild_R21B/hle/world_records.py` was read: its legacy
`Message.sender`, `Message.based_on`, and `Transaction` (`196–215`) are a different
schema and must not be substituted for native U2 transaction fields. Native
definitions are in `hle_unified/records.py`; `compact.py` preserves their exact
references and transaction actor. Batch 0 declares this structural link without
claiming a generated-history or cross-actor delivery witness.

## Other input to the energy audit

`validate_agenda_exhaustion` also reads the external state dictionary, not a
transaction version: `halted` (`E:107`), `active` (`110`), and that action's `actor`
and `key` (`113`) and `kind` (`117`). They select the actor/job being checked and
must not be presented as additional raw transaction fields.

## Batch 4 observation inputs (R6)

| Field/link | Record carrying it | Meaning and use | Pinned source |
| --- | --- | --- | --- |
| `events[].actor`, `events[].key`, `events[].episode` | Restored `Population.events` checkpoint state, not transaction attributes | Actor identity, exact episode request key, and zero-based actor-local episode count at that scheduler turn. Repeated turns at the same actor/key must agree on episode. Join operation `(actor, key)` using only the declared request key family: request key, `:movement`, `:feedback` (and `:admission` for legacy selection). Do not infer episodes from name digits. Cumulative coverage at index e pools uses whose actor-local episode is <= e; it is not a wall-clock snapshot. | `hle_unified/population.py:56–60,78–80,98,124,145,160,170–177,180–211`; workflow key construction `hle_unified/workflow_selection_execution.py:94`. Positive and forged/missing joins are tested in `tests/test_04_measures.py`. |
| Operation `key` (additional use) | Operation attributes | The already-declared job key joins the paid block's operation to the exact scheduler episode key family above. Every paid-use record must have exactly one episode attribution. | `hle_unified/workflow_execution.py:158–166`; `hle_unified/workflow_selection_execution.py:94`; existing `key` declaration above. |
| `ObjectId.namespace`, `ObjectId.key` | Actor identities | Stable display ID `namespace:key`; does not infer TIM, source, or provenance. | `hle_unified/records.py:19–26`. |
| `relation`, `landing_permutation` | Read-only kernel relation label JSON keyed by `sender_tim:receiver_tim` | Human relation label and eight-position sender-to-receiver landing permutation. Validate against `hle.relations.landing_permutation` before displaying a label. `benefit` means sender is receiver's benefactor; `benefit_inverse` is the reverse. | `baseline/HLE_Rebuild_R21B/baseline/crossing/sources/relation_labels.json`; `project_sources/HLE_Final_Build_Companion_Theory_v1_0.txt:564–565`; `hle/relations.py:29–34`. Read by path, never copied. |

Batch 4 trace IDs are zero-based occurrence indices in the unchanged Batch 3
record sequence, linked to transaction index, operation reference, and block end.
An empty trace is an observed zero only within the declared complete history.
Coverage denominators include all committed profile actors, including actors
with zero completed uses (labeled inactive). A ratio with a zero denominator is
displayed as N/A, never as a measured zero.

## Batch 8 observation inputs (A8)

| Field | Meaning and use | Pinned source |
| --- | --- | --- |
| block **kind** | `hop` if the block is an arrival along `route.{i}.path.{n}`, n ≥ 1; `content` if it is the route's seat-content block. Derived from the committed route structure in route order (the last element block of each route is content). Not stored as an attribute. | `hle_unified/energy_audit.py:12–41` |
| block **time** | `end − start` of the element block: `TIME[seat−1]` for a hop, `content_units` for content. | `hle_unified/energy_audit.py:5,26–37` |
| block **energy** | The third tuple value of `blocks(d)` for an element block: `ENERGY[seat−1]`, times `content_units // TIME[seat−1]` for content. Reported as CT Table 13 block energy under every resource model; it is the grade-v1 debit and is not the legacy-r4 wallet debit. | `hle_unified/energy_audit.py:6,30,37,47–50` |
| seat **ring** | `fields(seat)["ring"]`, `mental` (1–4) or `vital` (5–8). | `baseline/HLE_Rebuild_R21B/hle/model_a.py`, `fields` |
| `route.{i}.support_seat`, `route.{i}.support_at` | The vital-ring seat the route was built through (5 or 7 for accumulation, 6 or 8 for expenditure) and the hop index at which it is reached. Read for the support-traffic column only; never used to recompute a route (opaque route contract, Batch 0). | `hle_unified/cognitive_routes.py:20–36` |

Batch 8 class records are aligned index-for-index with the Batch 3 use records
and validated against the CT tables (`tests/test_08_classes.py`).

## Batch 9 manifest inputs (A9)

`HISTORIES_SOLO8.json` carries, per history, `phase_marks` (`probe_end`,
`collective_end`, `solo_end`: zero-based transaction indices ending each phase),
`refused_rows`, `engine`, and `calls_ref` (SHA-256 of the per-history call log in
`CALLS_SOLO8/`). These are generator records, not transaction attributes; the
tables read phase marks only to label phases. `WorkflowRequest.elements`
(`hle_unified/workflow_records.py:70,79`) is the element override used by the
program; it is a request field, consumed at route construction, and appears in
the journal only through the resulting `route.{i}.element` and `route.{i}.path.{n}`.
