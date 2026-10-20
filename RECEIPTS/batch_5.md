# Batch 5 receipt — final report

Date: 20 October 2026 (America/New_York).
Status: ACCEPTED. Directive complete; REPORT.md ready.

## Starting state

Current main was fetched and verified at
`39d61b8cc03d020c9165ee6d6f5b8f89b95f32f7`. The operative directive is the
v1.3 README appendix with Amendments A1 and A2. Receipts through Batch 4
establish acceptance. The historical Batch 2 R9 stop was explicitly cleared by
its later A1 section; no uncleared stop is present. No Batch 5 receipt existed.

This session performs only Batch 5. The report follows the seven required
sections in their prescribed order. It reads HISTORIES.json and the accepted
tables without regenerating or changing them. No implementation, experiment,
fixture replacement, or theory change is performed.

## Acceptance

Batch 5 specifies no proving command. Its documentary acceptance criterion is
that every number in REPORT.md appears in a table under TABLES/. The inline
verification below is an editorial traceability check, not a new batch proving
rule or an added test file. All measured values are checked against the exact
source columns and history/actor/pair row keys. Model names, seed identifiers,
and structural section numbering are not treated as new measured quantities.

Every report section is below 300 words. The report's generated-input values
also agree with HISTORIES.json. All source table hashes match Batch 4's receipt.
DCNH statements are limited to agree/diverge and the tabulated use counts.
Undefined ratios and unavailable standalone pair experiments remain distinct
from observed zeros. A1's literal conditioning-index scope is disclosed, not
redefined. The report makes no claim of theoretical closure.

Exact editorial verification command, run from the write repository:

```sh
python - <<'PY'
import pathlib, json, re, hashlib
root=pathlib.Path('.')
def rows(path, section=None):
    text=(root/path).read_text()
    if section:
        text=text.split('## '+section+'\n',1)[1].split('\n## ',1)[0]
    lines=[[x.strip() for x in line.strip().strip('|').split('|')]
           for line in text.splitlines() if line.startswith('| ')]
    return [dict(zip(lines[0], row)) for row in lines[2:]]
report=(root/'REPORT.md').read_text()
parts=re.split(r'^## \d+\. ',report,flags=re.M)[1:]
assert len(parts)==7
for i,part in enumerate(parts,1):
    count=len(part.split())
    assert count<=300,(i,count)
    print(f'Section {i}: {count} words; within 300-word limit.')
inputs=rows('TABLES/per_population.md','Accepted inputs')
manifest=json.loads((root/'HISTORIES.json').read_text())
assert {r['History'] for r in inputs}=={r['name'] for r in manifest}
for item in manifest:
    row=next(r for r in inputs if r['History']==item['name'])
    assert (row['Model'],int(row['Seed']),int(row['Actors']),int(row['Transactions']))==(
        item['model'],item['seeds']['fixture'],len(item['actors']),item['transactions'])
    assert row['Checkpoint SHA-256']==item['checkpoint_sha256']
for r in rows('REPORT.md','1. What was generated'):
    group=[s for s in inputs if s['Model']==r['Model']]
    assert ', '.join(s['Seed'] for s in group)==r['Fixture seeds']
    assert all(s['Actors']==r['Actors per history'] and s['Transactions']==r['Transactions per history'] for s in group)
pop=rows('TABLES/per_population.md','Population summary')
assert all(r['Received uses']=='0' and r['Supplier HHI']=='0/0 (N/A)' for r in pop)
assert all(r['Source']=='world' for r in rows('TABLES/per_actor.md','Use trace'))
dcnh=rows('TABLES/dcnh_two_ways.md')
for r in rows('REPORT.md','3. DCNH all-use versus received-and-kept'):
    matches=[s for s in dcnh if s['Actor']==r['Actor']]
    assert {s['History'] for s in matches}=={s['History'] for s in inputs}
    for s in matches:
        expected=r['All-use count'] if s['View']=='all uses' else r['Received-and-kept count']
        assert s['Uses']==expected and s['TIM']==r['TIM'] and s['Comparison']==r['DCNH comparison']
episodes=rows('TABLES/per_population.md','Coverage by episode index')
for r in rows('REPORT.md','4. Coverage per population and episode'):
    p=next(s for s in pop if s['History']==r['History'])
    assert p['Coverage'].split(' = ')[0]==r['Final coverage']
    for e in ('0','1'):
        s=next(s for s in episodes if s['History']==r['History'] and s['Through episode']==e)
        assert s['Coverage'].split(' = ')[0]==r['Through episode '+e]
pairs=rows('TABLES/per_population.md','Ordered pairs')
for r in rows('REPORT.md','5. Sterile ordered pairs'):
    matches=[s for s in pairs if (s['Source'],s['Receiver'])==(r['Source'],r['Receiver'])]
    assert {s['History'] for s in matches}=={s['History'] for s in inputs}
    assert all(s['Sterile']=='True' and all(s[k]==r[k] for k in r) for s in matches)
benefit=rows('TABLES/per_population.md','Benefit pairs within the triad versus triad total')
for r in rows('REPORT.md','6. Benefit pair versus triad'):
    matches=[s for s in benefit if (s['Source'],s['Receiver'])==(r['Source'],r['Receiver'])]
    assert {s['History'] for s in matches}=={s['History'] for s in inputs}
    for s in matches:
        assert s['Relation']==r['Relation']
        assert s['Pair-subset uses']==r['Pair-subset uses within triad']
        assert s['Triad benefit-family uses']==r['Triad benefit-family uses']
        assert s['Standalone pair uses']==r['Standalone pair uses']
assert all(r['Conditioning (A1 literal)']=='0/0 (N/A)' and r['Hold']=='0/0 (N/A)'
           for r in rows('TABLES/per_actor.md','Actor indices'))
prose='\n'.join(line for line in report.splitlines() if not line.startswith(('#','|')))
assert re.findall(r'(?<![\w])\d+(?:/\d+)?(?![\w])',prose)==['0','0/0','0/0']
for link in re.findall(r'\]\(([^)]+)\)',report):
    assert (root/link.split('#')[0]).is_file()
for name,digest in {
    'dcnh_two_ways.md':'1934a9d4ab9dcfdc382ff74d7c7a6e1491424c989097da1a98324c0037bb63ab',
    'per_actor.md':'a43741f2ebaaa1627c74a9077ca750247c6b81eb4983b0bf41208e0c192bda3b',
    'per_population.md':'26e68f49197c80c9934055061a07a9b986afd496815b99c88b7211a187035913'
}.items():
    assert hashlib.sha256((root/'TABLES'/name).read_bytes()).hexdigest()==digest
print('PASS: report table values match the named source rows across every history.')
print('PASS: numeric prose claims and N/A distinctions match source cells.')
print('PASS: manifest agrees with accepted-input rows; report links resolve.')
print('PASS: all accepted table hashes are unchanged.')
print('Batch 5 acceptance: every reported numeric finding is traced to TABLES/.')
PY
```

Complete combined stdout/stderr:

```text
Section 1: 103 words; within 300-word limit.
Section 2: 51 words; within 300-word limit.
Section 3: 120 words; within 300-word limit.
Section 4: 147 words; within 300-word limit.
Section 5: 137 words; within 300-word limit.
Section 6: 120 words; within 300-word limit.
Section 7: 131 words; within 300-word limit.
PASS: report table values match the named source rows across every history.
PASS: numeric prose claims and N/A distinctions match source cells.
PASS: manifest agrees with accepted-input rows; report links resolve.
PASS: all accepted table hashes are unchanged.
Batch 5 acceptance: every reported numeric finding is traced to TABLES/.
```

Exit status: 0. Documentary acceptance passed on its first check.
No failed proving command or repair occurred.

## Final invariance

Command:

```sh
python -m unittest tests.test_00_setup -v
```

Complete combined stdout/stderr:

```text
test_01_imports_resolve_to_read_clone (tests.test_00_setup.SetupTests.test_01_imports_resolve_to_read_clone) ... ok
test_02_every_frozen_file_is_unchanged (tests.test_00_setup.SetupTests.test_02_every_frozen_file_is_unchanged) ... ok
test_03_no_reverse_import_reference (tests.test_00_setup.SetupTests.test_03_no_reverse_import_reference) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.059s

OK
```

Exit status: 0. All 206 frozen files and the exact file set still match;
path imports resolve to the read clone and reverse-import absence passes.
The original engine's git status is empty and its HEAD remains
`fdede6f16721f06422d0798a79d84170969b83f8`.
No read-repository file was modified, copied, committed, or pushed.

## Commit, publication, and final stopping point

Commit message: `batch 5: report`.
Only REPORT.md and RECEIPTS/batch_5.md are committed, both UTF-8 Markdown under
200,000 bytes. No source table, code, checkpoint, raw journal, or earlier receipt
is changed. This receipt includes the exact verification command and output so
the acceptance record is self-contained.

After the accepted terminal commit, publication uses the previously authorized
connected GitHub route, a non-forced update against the observed parent, and
full tree verification. This pre-publication receipt does not preclaim success
of a pending network operation. Any refusal is recorded under R5, without an
alternate publication retry in this session.

**Directive complete; REPORT.md ready.**
There is no next eligible batch and no Batch 6. Future sessions encountering
this receipt report completion and stop. Energy regeneration, practice pricing,
feedback, fixture replacement, and any follow-on experiment require a separate
directive. None is started.
