# Function Conditioning Ledger v2

An observation-only companion to [Socionics_Engine](https://github.com/GregoritHub/Socionics_Engine).
Batch 0 declares the audit fields and freezes the unchanged engine sources.

## Engine commit

`fdede6f16721f06422d0798a79d84170969b83f8`

The read clone is the sibling directory `../Socionics_Engine`. Never edit or
commit in that clone, copy its files here, or publish its files from this repository.
`ENGINE_FREEZE.sha256` records every file under `hle_unified/` and
`baseline/HLE_Rebuild_R21B/hle/`, with paths relative to the read clone.

## Local setup and proof

Clone the read repository at the engine commit above, as the sibling directory.
Create the ignored `engine_path.txt` containing its absolute path and a newline.
Use Python 3.12 and run from this repository:

```sh
python -m unittest tests.test_00_setup -v
```

The test begins with the directive's exact R2 path preamble. It disables bytecode
writes before importing the engine, checks both import locations, verifies the
complete frozen file set and every digest, and runs the specified reverse-import
grep. No engine runtime behavior is changed.

## Receipts and directive source

Read `RECEIPTS/` and the applicable directive amendments before applying the stop
check. Run exactly one eligible batch and stop. An uncleared `Stopped under R9`
in any receipt requires reporting that batch and ending the session.
After Batch 5, report completion and stop; there is no Batch 6.

### Amendment A1 — next session

[Directive Amendment A1](DIRECTIVE_AMENDMENT_A1_world_source.md) is the author's
ruling for actorless input revisions. It clears only the original Batch 2 R9 stop
recorded on 20 October 2026. The next session must preserve that failure record,
append a section headed `Cleared by Amendment A1` to `RECEIPTS/batch_2.md`, and
re-attempt Batch 2 with a fresh allowance of two proving failures and one repair.
Any new R9 stop in that fresh attempt remains binding; A1 does not clear it.

Record the number of actor-id sources in every generated history. If all are
zero, record `no cross-actor delivery observed in generated histories`; Batch 2
still passes when its proving command passes, and Batch 3 proceeds. Replacing
the generator with a fixture that routes one actor's output into another actor's
paid use requires a separate author ruling after that finding. A1 does not
authorize that replacement.

### Amendment A2 — Batch 3

[Directive Amendment A2](DIRECTIVE_AMENDMENT_A2_I4_monotone.md) preserves the
fixed definition of `kept` and restates I4 as monotonicity under history growth.
An existing True use remains True when transactions are appended; False may
become True. The last use at a repeated seat remains False. The author clears
the Batch 3 contradiction and authorizes a fresh two-failure allowance. Its
first-half, repeated-seat, and forged-reordering witnesses govern Batch 3.

The destination was empty at the start of Batch 0, including the stated directive
path. Batch 0 preserved the supplied Markdown directive in this README's appendix
and recorded its original SHA-256 in `RECEIPTS/batch_0.md`. That original text is
retained in Git history. The operative appendix below is now version 1.3 with
Amendments A1 and A2 incorporated; the original digest does not describe this revision.

The user's session instruction permits a schedule that starts the assistant every
four hours. Each started session reads receipts and performs its own single batch;
GitHub Actions and other unattended repository writers remain prohibited.

`FIELDS.md` distinguishes raw attributes, revision metadata, derived block values,
and the exact input-revision-to-producing-transaction actor link. The named
`hle_unified/world_records.py` is absent at the pinned commit; the receipt records
the actual record definitions consulted.

## Directive appendix (v1.3)

The content between the following markers is the supplied directive as amended
by [Amendment A1](DIRECTIVE_AMENDMENT_A1_world_source.md) and
[Amendment A2](DIRECTIVE_AMENDMENT_A2_I4_monotone.md). A1 governs the original
Batch 2 stop clearance and the `world` source ruling. A2 governs the Batch 3
contradiction clearance and I4 under history growth.
The explicit user instruction permitting assistant-starting schedules governs R4.

<!-- BEGIN SUPPLIED DIRECTIVE -->
# Batch Directive — Function Conditioning Ledger v2

Version 1.3 — 20 October 2026 — incorporates Amendments A1 and A2
Read repository (never written): https://github.com/GregoritHub/Socionics_Engine
Write repository (the only place you commit): https://github.com/GregoritHub/Socionics_Engine_Function_Conditioning

This directive is written to be executed one batch at a time. Each batch names its exact inputs, the exact files it may create, the command that proves it, and the one condition under which it stops. Do not read ahead. Do not combine batches. Do not do anything a batch does not name.

---

## 0. Standing rules (apply to every batch)

These rules exist because of specific failures recorded in *Engine Socionics — Problems Encountered* (12 Oct 2026). Each rule names the failure it prevents.

**R1. Two clones, one of them read-only.**
Clone the read repository to `../Socionics_Engine` (sibling directory). Never modify, copy, or re-publish any file from it. Never run `git add`, `git commit`, or `git push` inside it. All work happens in the write repository. *(Prevents: scope-broader-than-authorization rejections; the 4,168-file transfer; the three blocked manifests.)*

**R2. Import by path, never by copy.**
Every script and test in the write repository begins with exactly this preamble and nothing else for imports:
```python
import sys, pathlib
ENGINE = pathlib.Path(__file__).resolve().parents[1] / "engine_path.txt"
ROOT = pathlib.Path(ENGINE.read_text().strip())
sys.path[:0] = [str(ROOT), str(ROOT / "baseline/HLE_Rebuild_R21B")]
```
`engine_path.txt` holds the absolute path of the read clone. It is created in Batch 0 and is listed in `.gitignore`. *(Prevents: `ModuleNotFoundError: No module named 'hle'`; test-discovery import failures.)*

**R3. Only small text files are ever committed.**
Allowed: `.py`, `.md`, `.json`, `.txt`, `.sha256`. Each file under 200 KB. No archives, no compressed payloads, no checkpoints, no binaries, no raw journals. If a result is larger than 200 KB, commit its SHA-256 and a summary, not the bytes. *(Prevents: opaque-payload rejections; fragmented 104-batch transfers.)*

**R4. No workflows, no schedules, no automation that writes.**
No GitHub Actions. No recurring runs. No cron. Every commit is made by you, in the batch that produced it, from the terminal. *(Prevents: write-access workflow rejection; scheduled runs that stall on a blocker.)*

**R5. Local acceptance is the gate; publication is a consequence.**
A batch is accepted when its named command prints its named pass line. Only then do you commit. If the commit or push is refused, write the refusal verbatim into `RECEIPTS/batch_N.md`, commit that file alone, and continue to the next batch. Development never waits on publication. *(Prevents: development stalled behind publication.)*

**R6. Field semantics are declared before any code reads them.**
Batch 0 produces `FIELDS.md`, a table of every transaction field this project reads, with its exact meaning as established by reading `hle_unified/energy_audit.py` and `hle_unified/conditioning_audit.py` in the read repository. Any later batch that needs a field not in `FIELDS.md` stops and adds it there first, with a test that exercises it. *(Prevents: the physical `target` / semantic `content_target` confusion that broke retention; the disclosure-subject mistake.)*

**R7. Every adapter path gets a positive and a negative witness.**
No panel "passes" on cases that do not traverse the code under test. Each batch's tests include at least one case where the new field is present and counted, and one where it is absent or forged and rejected. *(Prevents: 64 passing cases that never exercised the path.)*

**R8. Observation only.**
Nothing you write is imported by `hle_unified`. Nothing you write prices, selects, schedules, or alters Shell behavior. A test in Batch 0 asserts that no file under `hle_unified/` in the read repository has changed (by hash) and that no file in the write repository is imported by it. *(Preserves Release 1.0; matches Phase 7's own limit.)*

**R9. Stop rule.**
If a batch's proving command fails twice after one repair attempt, stop. Write `RECEIPTS/batch_N.md` with: the command, the full output of both failures, the repair you attempted, and the sentence "Stopped under R9." Commit that file. Do not proceed. Do not attempt a different approach. Wait for instruction. *(Prevents: repeated-failure loops.)*

**R10. One sentence of scope.**
This project adds four fields and five derived tables to the existing conditioning observation. It does not add energy regeneration, practice pricing, Model G seats, FT4 demand formation, or any feedback. If you find yourself writing any of those, stop under R9.

---

## Batch 0 — Setup, field declaration, invariance witness

**Inputs:** both clones.
**May create:** `engine_path.txt` (ignored), `.gitignore`, `README.md`, `FIELDS.md`, `ENGINE_FREEZE.sha256`, `tests/test_00_setup.py`, `RECEIPTS/batch_0.md`.

Steps:
1. Clone the read repository to a sibling directory. Record its `git rev-parse HEAD` in `README.md` under "Engine commit".
2. Write `engine_path.txt` and `.gitignore` (containing `engine_path.txt`, `__pycache__/`, `*.pyc`, `OUT/`).
3. Compute SHA-256 of every file under `<read>/hle_unified/` and `<read>/baseline/HLE_Rebuild_R21B/hle/`; write them to `ENGINE_FREEZE.sha256`.
4. Read `<read>/hle_unified/energy_audit.py` and `<read>/hle_unified/conditioning_audit.py`. Write `FIELDS.md` with one row per field those modules read from a transaction version: field name, which record type carries it, what it means, and the line number where the audit reads it. Include at minimum: `record_type`, `actor`, `tim`, `completed`, `required`, `spent`, `route_count`, and whatever `blocks(d)` yields per block (start, end, seat/position, element). Add a row for the **provenance** of an input revision (which field links a consumed revision to the actor that produced it) — find it by reading `hle_unified/world_records.py` and `hle_unified/compact.py`; if you cannot find it, write "UNRESOLVED" in that row and continue (Batch 2 will stop there if still unresolved).
5. Write `tests/test_00_setup.py` with three tests:
   - imports `hle.model_a` and `hle_unified.conditioning_audit` succeed via the R2 preamble;
   - every hash in `ENGINE_FREEZE.sha256` matches the read clone;
   - `grep -rl "Socionics_Engine_Function_Conditioning\|conditioning_v2" <read>/hle_unified` returns nothing.

**Proving command:** `python -m unittest tests.test_00_setup -v`
**Pass line:** `OK` with 3 tests.
**Commit message:** `batch 0: setup, FIELDS.md, engine freeze`

---

## Batch 1 — Generate histories

You do not have access to the historical raw archives (they are private; the read repository says so in `docs/research/Evidence_and_Reproduction.md`). You generate your own histories using the public engine.

**Inputs:** `<read>/docs/examples/first_run.py`, `<read>/tests_workflow_population/fixtures.py`, `<read>/tests_workflow_population/sustained_fixtures.py`.
**May create:** `generate/histories.py`, `OUT/` (ignored), `HISTORIES.json`, `tests/test_01_histories.py`, `RECEIPTS/batch_1.md`.

Steps:
1. Read `first_run.py` end to end. Do not modify it. Write `generate/histories.py` that uses the same fixtures and APIs to produce population worlds with **three actors of three distinct types** including at least one dual pair (e.g. IEE + SLI + a third), run each to its finite stop, and save each world's journal via the engine's own checkpoint codec to `OUT/<name>.checkpoint`.
2. Produce at least 8 histories: 4 under `legacy-r4`, the same 4 seeds under `grade-v1`.
3. Write `HISTORIES.json`: for each history, its name, model, seeds, actor→TIM map, number of transactions, and SHA-256 of the checkpoint. Checkpoints themselves are not committed (R3).
4. `tests/test_01_histories.py`: restoring each checkpoint reproduces its recorded hash; each history has ≥ 1 completed paid use per active actor (use `conditioning_audit.completed_use`).

**Proving command:** `python generate/histories.py && python -m unittest tests.test_01_histories -v`
**Pass line:** `OK` and `HISTORIES.json` lists ≥ 8 entries.
**Commit message:** `batch 1: generated histories manifest`

---

## Batch 2 — Seat, dimension, source, relation (no retention yet)

**Inputs:** `FIELDS.md`, `OUT/*.checkpoint`, `<read>/hle_unified/conditioning_audit.py`, `<read>/baseline/HLE_Rebuild_R21B/hle/{model_a,relations}.py`.
**May create:** `conditioning_v2/__init__.py`, `conditioning_v2/audit.py`, `tests/test_02_fields.py`, `RECEIPTS/batch_2.md`.

Precondition: the provenance row in `FIELDS.md` is resolved. If it says UNRESOLVED, resolve it now by reading the two named modules and adding a test that demonstrates the link on a generated history; if you cannot, stop under R9.

Steps:
1. `conditioning_v2/audit.py` exposes `uses(transactions)` returning a list of records, one per completed hop or seat-content block, each with: `actor`, `tim`, `element`, `seat` (via `hle.model_a.position_of`), `dim` (via `hle.model_a.fields`), `source` (the three values below), `source_seat` and `relation` (via `hle.relations.relation` / `landing_position` only when `source` is an actor id, else `None`).

   | `source` | When | Conditioning event? |
   |---|---|---|
   | `"self"` | The exact consumed revision was committed by a transaction whose `actor` is the consuming actor. | No |
   | `<actor id>` | The exact consumed revision was committed by a transaction whose `actor` is a different committed actor. | Yes, when the receiving seat has `dim ≤ 2` |
   | `"world"` | The exact consumed revision was committed by a transaction whose `actor` is `None` — a declared or supplied revision (fixture seeds, supplied prior associations, initial world material). | No |

   Resolve the exact consumed `ObjectRef` to the matching `version.ref` and its
   producing `Transaction.actor`, as declared in `FIELDS.md`. `None` maps to
   `"world"`. Do not infer a producer from `Account.owner`, the paying actor,
   the `writer` label, or the revision's name.

2. It must reuse `conditioning_audit.completed_use`'s counting logic, not reimplement it. The simplest correct form is: call the existing function for totals, then walk the same transactions to attach fields, and assert the two agree.
3. `tests/test_02_fields.py`:
   - **I1** every record's `seat`/`dim` is consistent with its actor's TIM;
   - **I2** every `source` is `"self"`, `"world"`, or a committed actor id;
   - **I3** only when `source` is an actor id, `relation` equals the kernel's `relation(source_tim, actor_tim)` and `landing_position(source, source_seat, actor) == seat`;
   - **I5** summing records by (actor, element), including `"world"` uses, reproduces `conditioning_audit.completed_use` counts exactly, on every history;
   - **negative:** a transaction with a forged `actor` on its provenance is rejected with a named error; a transaction whose element is not at the claimed seat for that TIM is rejected; a revision with `actor = None` must resolve to `"world"`, never to an actor id or `"self"`.

**Proving command:** `python -m unittest tests.test_02_fields -v`
**Pass line:** `OK`. Record the number of uses with `source` = an actor id for every history. If every history has zero such uses, that is a finding, not a failure: write "no cross-actor delivery observed in generated histories" in `RECEIPTS/batch_2.md` and continue to Batch 3 in the next session. `"world"` is not cross-actor delivery. Replacing the Batch 1 generator with a fixture that routes one actor's output into another actor's paid use requires a separate author ruling after this finding.
**Commit message:** `batch 2: v2 fields — seat, dim, source, relation`

---

## Batch 3 — Retention (`kept`)

**Inputs:** Batch 2 output.
**May create:** `conditioning_v2/retention.py`, `tests/test_03_kept.py`, `RECEIPTS/batch_3.md`.

Definition (fixed; do not reinterpret): a use is **kept** when the same actor later completes another paid use **at the same seat** of the same element within the same history. Reuse of the output by a different seat, or becoming an acquired capability, does **not** count. This is practice, not insight.

Steps:
1. `retention.py` adds `kept: bool` to each Batch 2 record.
2. `tests/test_03_kept.py`:
   - **I4 (Amendment A2):** `kept` is monotone under history growth: for any prefix of a history and the full history, every prefix use with kept=True remains kept=True in the full history. Appending transactions may change False to True, never True to False. Compute kept on the first half of each generated history's transactions and on the whole, and assert every prefix-True use is whole-True;
   - **positive:** a history where an actor repeats a seat shows kept=True on every use at that seat except the last, and False on the last. A sequence ending `[..., True, False]` is normal;
   - **negative:** a history where every (actor, seat) occurs once shows kept=False everywhere; a forged duplicate transaction is rejected; a forged reordering placing a repeat before the use it would mark is rejected (retention cannot point backward in transaction order).

**Proving command:** `python -m unittest tests.test_03_kept -v`
**Pass line:** `OK`.
**Commit message:** `batch 3: retention (same-seat repeat)`

---

## Batch 4 — Measures and tables

**Inputs:** Batches 2–3.
**May create:** `conditioning_v2/measures.py`, `conditioning_v2/tables.py`, `TABLES/per_actor.md`, `TABLES/per_population.md`, `TABLES/dcnh_two_ways.md`, `tests/test_04_measures.py`, `RECEIPTS/batch_4.md`.

Per actor: use profile by (seat, source∈{self,world,other}, kept); conditioning index = received uses at dim ≤ 2 ÷ all uses at dim ≤ 2; hold index = kept received ÷ received; supplier map for each seat with dim ≤ 2; and the existing Phase 7 axis loads/tilts/greatest-load cells computed **twice** — once on all uses (must match `conditioning_audit.observations` exactly), once on received-and-kept uses only.

Per population: coverage = fraction of (actor, seat) pairs with dim ≤ 2 that received ≥ 1 use from an actor holding that element at dim ≥ 3; coverage per episode index; supplier concentration; sterile ordered pairs (zero received uses either direction); benefit-relation received uses in pairs vs. in the triad.

**Amendment A1 source scope:** conditioning index, hold index, supplier map,
coverage and sterile pairs are computed over uses with `source` = an actor id
only. `"world"` uses appear in the use profile as their own column and in the
all-use DCNH, and nowhere else.

`tests/test_04_measures.py`: all-use DCNH equals Phase 7's `observations` row for every actor on every history (**I5 again, at the table level**); every table cell traces to a record (spot-check 20 cells by recomputation); inactive actors appear in denominators and are labeled.

**Proving command:** `python -m conditioning_v2.tables && python -m unittest tests.test_04_measures -v`
**Pass line:** `OK` and the three tables exist and are < 200 KB each.
**Commit message:** `batch 4: measures and tables`

---

## Batch 5 — Report

**Inputs:** Batches 1–4.
**May create:** `REPORT.md`, `RECEIPTS/batch_5.md`.

`REPORT.md`, in this order, each section ≤ 300 words, every number traceable to a table row:
1. What was generated (from `HISTORIES.json`).
2. Cross-actor delivery observed or not (Batch 2 finding).
3. DCNH all-use vs. received-and-kept: agree or diverge, per actor. State plainly which. Do not interpret beyond "agree"/"diverge."
4. Coverage per population and over episode index.
5. Sterile pairs listed with their relation names.
6. Benefit pair vs. triad.
7. Limits: generated histories only, no historical archive, no feedback, nothing closed.

No proving command. Acceptance is: every number in `REPORT.md` appears in a table under `TABLES/`.
**Commit message:** `batch 5: report`

---

## After Batch 5

Stop. Do not begin energy regeneration, practice pricing, or any feedback rule. Those are a separate directive that will be issued only after `REPORT.md` §3 has been read.

---

## Checklist you run before every commit

- [ ] Only allowed file types, each < 200 KB (R3)
- [ ] No file from the read repository is in the diff (R1)
- [ ] `ENGINE_FREEZE.sha256` still matches the read clone (R8)
- [ ] The batch's proving command printed its pass line in this session (R5)
- [ ] `RECEIPTS/batch_N.md` exists with the command and its output
<!-- END SUPPLIED DIRECTIVE -->
