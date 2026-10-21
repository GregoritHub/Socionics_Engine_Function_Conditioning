# Amendment A9 — pair-solo8 program under the fixture's material limits

Issued by the directive author on 20 October 2026, after the Batch 9 step 9.1.1
probes and before any solo8 history was generated.

Two facts of the pinned fixtures, found by probe, change the §9.1.3 program:

1. The workflow world's care stock (`CARE`, `tests_u4/fixtures.py` genesis) holds
   **two units**, and `tests_c7_workflow.fixtures.cell` names that stock for
   every care-consuming recipe (Express/expenditure, Organize's care observe).
   Only two such rows can ever complete in one world.
2. A care action needs a worn serviceable device, and each care leaves it at
   wear 0; the fixture's own `observe(…, primitive="use")` restores wear 1.

A9 rules, before generation:

- The uptake probe (Express/expenditure, recipe default) is the first care row.
  Row 1, its duplicate, is withdrawn. Row 2 (Express/expenditure with the
  `ne, ti` override, the P-D witness) is the second and last care row.
- Rows 17 and 18 (Organize) are withdrawn. Ti and Te expenditure remain
  covered by rows 5 and 6 (Embody); every element keeps both faces.
- Before each row, the generator re-exposes the current device and care-stock
  heads to Alice and, when device wear is 0, performs one plain `use` action
  by Alice (`observe(key + "-wear", primitive="use")`). A plain action has no
  route and counts no element use.
- The program is 17 rows (2–16, 19, 20). The manifest records it.
- The prediction's third clause is corrected before generation: Share and
  Coordinate rows require a peer by the fixture's construction, so Bob's uses
  after `after-summary` are expected and are exchange work, not program rows.
  The first two clauses stand unchanged.

Everything else in Batch 9 stands as written.
