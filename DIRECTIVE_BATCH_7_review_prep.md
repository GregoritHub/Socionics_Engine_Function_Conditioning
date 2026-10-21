# Directive Extension — Batch 7: Prepare for outside review

Applies to: Batch Directive — Function Conditioning Ledger v2, v1.6 → v1.7
Issued: 20 October 2026, after `REPORT_DELIVERY.md`
Authority: directive author. R1–R10 apply unchanged. R10's scope is extended by: *two instrument corrections named in §A, and documentation for a reader who has never seen this project.*

The goal: a stranger with Python 3.12 and two `git clone` commands reproduces every number in both reports in under an hour, and can tell at every step what was measured, what was found, and what was not.

---

## A. Two instrument corrections (do these first; they change numbers)

**A1. Conditioning index denominator.** The accepted Batch 4 ratio is degenerate (received weak uses ÷ received weak uses). The definition is restored to the Batch 4 directive text: **received uses at `dim ≤ 2` ÷ all uses at `dim ≤ 2`**, per actor. Where the denominator is zero the cell is `N/A`. The old column is removed, not kept beside the new one.

**A2. Two provenance readings, both reported.** A3/A4 provenance (any exact operation input, every block inheriting the tuple) is kept and relabelled **wide**. A second reading, **narrow**, resolves only `source.N` and `source_input` (the operation's declared semantic inputs), ignores `input.N`, and where an operation declares no semantic inputs yields `"self"` or `"world"` by the existing rule. Every table that reports received/kept/coverage/sterile/DCNH-received reports both readings as adjacent columns or adjacent tables, labelled. The guard stands: Batch 1 outputs byte-identical under both readings (every Batch 1 operation has no other-actor producer under either).

Regenerate all tables and both reports. Re-run the full test suite. Record the before/after of every changed number in `RECEIPTS/batch_7.md` as a table (history, actor, measure, old, new, reading).

---

## B. Reproduction

**B1. `REPRODUCE.md`** at the root — the only file a reviewer needs to read first. Exact contents, in order:
1. Two clone commands with the pinned engine commit (`git clone … && git -C Socionics_Engine checkout fdede6f`).
2. The `engine_path.txt` line.
3. One command that runs everything: `python tools/reproduce.py`.
4. What that prints on success, verbatim.
5. Expected wall-clock time on a laptop.
6. What is **not** reproducible from a bare clone (nothing in this project should be; say so).

**B2. `tools/reproduce.py`** — runs, in order, with no arguments: `test_00_setup`; `generate/histories.py`; `generate/histories_delivery.py`; the full unittest suite; `conditioning_v2.tables` for both manifests; then compares every file under `TABLES/` and both `REPORT*.md` byte-for-byte against the committed versions and prints `REPRODUCED: <n> files identical` or lists the differing files and exits 1. It must pass on the committed tree before Batch 7 is accepted.

**B3. `environment.txt`** — Python version, platform, and the fact that no package outside the standard library is used (assert this in `test_00_setup` with a check of `sys.modules` after all imports).

---

## C. Documentation for a reader who was not here

**C1. `README.md` rewritten** (keep the engine commit and setup sections; replace the rest) with these sections, each ≤ 250 words:
- *What this measures* — the four fields (seat, dim, source, kept) and why each exists, in one paragraph each. No theory beyond what a reader needs to understand the tables.
- *What it does not do* — observation only; no feedback; no subtype assignment; no claim about people; relation labels are applied after measurement and never read by any computation.
- *Findings* — the Batch 5 negative (no cross-actor delivery in the population fixtures), the Batch 6 positive (first delivery event), the DCNH cell change for Alice, the relation-indifference of U11 delivery at this workload, and the two caveats (wide provenance is an upper bound; the triad was not producible). Numbers cited with links to the table rows.
- *How to read a table* — one worked row from `TABLES/pair_per_actor_delivery.md`, column by column.
- *History of the build* — one line per batch with its receipt link; one line per amendment with what it changed and why. Do not hide the stops; they are the audit trail.
- *Relationship to the engine repository* — read-only, pinned, frozen, hash-verified; what `ENGINE_FREEZE.sha256` guarantees and what it does not.

**C2. `GLOSSARY.md`** — every term a reviewer meets in the tables, defined in one sentence with a pointer to the code that computes it: seat, dim, source (self/world/tuple), wide/narrow, kept, received, conditioning index, hold index, supplier map, coverage, sterile pair, DCNH two ways, all-use vs received-and-kept, inactive actor, world material, delivery event.

**C3. `LIMITS.md`** — one page, consolidated from both reports' §6 and the receipts, in order of how much each would change the findings if lifted. Include: generated workloads only; U11 drives uses to strong seats; retention near-saturated at this workload; four seeds vary only non-binding budgets; wide provenance over-counts; Eve inactive in every delivery history; triad not producible; no historical archives used.

**C4. Code docstrings.** Every public function in `conditioning_v2/` gets a docstring stating inputs, outputs, the invariant it enforces (by name, I1–I5), and which directive/amendment defines it. No behavior change.

**C5. Receipts index.** `RECEIPTS/README.md` — a table: batch, date, status (accepted / stopped / cleared by), one-line outcome, link. The stop receipts stay exactly as they are.

---

## D. Hygiene

- Every file under 200 KB; no absolute paths anywhere in the tree (grep for `/home/`, `/workspace/`, `/Users/`, `C:\`); no scratch identifiers.
- `tools/probe_batch_6.py` and `tools/guard_batch_6.py` get a two-line header saying what they were for and that `reproduce.py` supersedes them for review.
- A `LICENSE` file is **not** added by this batch; licensing is the owner's decision. Note its absence in `README.md`.
- `CITATION.cff` with the repository name, owner, and engine commit; no version number beyond the directive version.

---

## Proving command

`python tools/reproduce.py && python -m unittest discover -s tests -v && grep -rnE "/home/|/workspace/|/Users/|C:\\\\" --include=*.md --include=*.py --include=*.json . ; test $? -eq 1`

**Pass line:** `REPRODUCED: <n> files identical`, `OK` from the suite, and the grep finding nothing.
**Commit message:** `batch 7: instrument corrections and review preparation`

## After Batch 7

Stop. Report "Ready for outside review" with the commit hash. No feedback rule, no new fixture, no further batch under this directive.
