# Batch 9 receipt — pair-solo8: the eight-element solo phase

Executed 20 October 2026 (client date) by the directive author, from `8505e4a`
(Batch 8 accepted). Engine read clone unchanged at `fdede6f`.

## Premises P-D to P-F, with the committed outcome

| Premise | Directive statement | Outcome | Holds |
| --- | --- | --- | --- |
| P-D | `WorkflowRequest.elements` flips the attitude within a Fold family; Express/expenditure with `ne, ti` lands an IEE on seats 1 and 4 | `solo-02-express-expenditure-neti`: `route.0 = (ne, 1)`, `route.1 = (ti, 4)`, status succeeded; `probe-uptake` default: seats 7, 6 (`tests/test_09_solo8.py::test_05`) | yes |
| P-E | The setup11 workshop runs its collective program on `WorkflowEngine`; one journal holds both phases | The pair sequence completes (`team` run succeeded) at transactions 312–533 of every solo8 history; the solo program follows on the same journal | yes |
| P-F | A direct request in the workshop world needs the uptake records `cell(…, prepare_only=True)` prepares | Seeding the c7 equipment (`DEVICE`, `LOAN`, `DUE`) into the workshop world before engine construction and performing `cell(e, 'Express', 'expenditure', key='probe-uptake', prepare_only=True)['request']` succeeds: spent 43, seats 7 and 6 | yes (resolved) |

Two further fixture facts were found by probe before generation and ruled in A9:
the workflow world's care stock holds two units, and each care action needs a
worn device. The program is 17 rows; the Organize rows and the probe's duplicate
are withdrawn; a plain `use` action restores wear before a care row.

## Prediction, as written to the manifest before generation

> internalisation > 0 for workshop:alice at seats 5 and 6 under the wide reading; every seat 1-8 has >= 1 content use for workshop:alice; workshop:bob's only uses after after-summary are exchange replies (A9)

## Outcome (identical at seeds 17, 29, 43, 61)

| Measure | Value |
| --- | --- |
| Transactions | 1060 (probe ends 312, collective ends 533, solo ends 1060) |
| Refused rows | none |
| Alice content per seat 1–8 | 4, 6, 2, 4, 41, 39, 6, 2 |
| Alice internalisation, wide | 107/164; seat 5 **23/67**; seat 6 **62/62** |
| Alice internalisation, narrow | 28/28; seat 5 4/4; seat 6 3/3 |
| Bob internalisation, wide / narrow | 0/142 / 21/32 |
| Alice price (whole) | 164 hops, 104 content, time 794, energy 755 |
| Alice greatest cell (margin) | all D (3); content-only H (6); hop-only D (9); collective-phase all D (2), content H,D (0); solo-phase all D (1), content H (6) |
| Coverage, wide | structural 5/12, observed 4/12 |
| Received, wide / narrow | 306 / 60 (first narrow deliveries in the project: workflow operations declare `source.N`/`source_input`) |

**The prediction held** in all three clauses, the third as amended: Bob's
solo-phase operations are all `*-exchange-*` keys (16: a join-accept and a reply per Share or Coordinate row) and
Eve has no uses.

What the sequence shows (seed 17, wide; `TABLES/pair-solo8_sequence.md`):

- seat 6 (Te): collective `S×19 O×23`, solo `S×6 O×44 S s` — the self return
  after the received regime at transaction 1048, after the last received use
  at 986;
- seat 5 (Si): collective `S×19 O×23`, solo `S O×44 o` — one self use after the
  collective phase, then received uses only, because Si content comes from
  Coordinate rows that need Bob as respondent; no self use after the last
  received one (1005).

## Files written

`generate/histories_solo8.py`; `HISTORIES_SOLO8.json` (prediction, program,
phase marks, call-log hashes); `CALLS_SOLO8/pair-solo8-seed-{17,29,43,61}.json`
(exact call logs, one per history, 52 KB each — the four together exceed R3's
200 KB in one file, so they are split); `conditioning_v2/solo8.py`;
`tests/test_09_solo8.py` (7 tests); `TABLES/pair-solo8_per_actor_seed-{17,29,43,61}.md`
(the per-actor table exceeds 200 KB for four histories and is split per seed),
`pair-solo8_per_population.md`, `pair-solo8_dcnh_two_ways.md`,
`pair-solo8_classes.md`, `pair-solo8_price_of_type.md`, `pair-solo8_dcnh_five_ways.md`,
`pair-solo8_sequence.md`, `pair-solo8_field.md`; `REPORT_SOLO8.md`;
`DIRECTIVE_AMENDMENT_A9_solo8_program.md`; `README.md`, `LIMITS.md`,
`GLOSSARY.md`, `FIELDS.md`, `REPRODUCE.md`, `tools/reproduce.py`, this index.

## Tests

`tests/test_09_solo8.py`: manifest, prediction, program and engine; the
collective phase reproduces the pair history's operations and content blocks
(only the first operation's hops differ, because Alice's cursor sits at the
probe's last element); every seat has solo content and Bob's solo operations
are exchange keys; internalisation defined under both readings, zero on the
collective-phase prefix and positive on the whole history (A2 monotonicity);
the element-override witness; negatives (Fold-family change rejected; a solo
operation forged to Bob rejected by the episode join); tables and report
present and sized.

## Proving command

```
python tools/reproduce.py && python -m unittest discover -s tests -v && python tools/path_check.py
```

Committed-tree run recorded below after the commit.
