# Amendment A6 — grep gate and publication

Issued by the repository owner in the Batch 7 continuation on 21 October 2026.
This text preserves the owner's ruling.

## Ruling 1 — path-hygiene gate

Fresh R9 allowance for Batch 7, limited to correcting the path-hygiene gate.
Replace the shell grep with `tools/path_check.py`: walk the tree, skip `.git`,
`RECEIPTS/batch_[0-6].md`, and any file matching `DIRECTIVE_*` or
`BATCH_DIRECTIVE_*`; for every other `.md/.py/.json/.txt` file, fail if any line
contains `/home/`, `/workspace/`, `/Users/`, or `C:\` ; print `PATHS: clean` or
list offenders and exit 1.

The proving command becomes:

```sh
python tools/reproduce.py && python -m unittest discover -s tests -v && python tools/path_check.py
```

Pass line: `REPRODUCED`, `OK`, `PATHS: clean`. No other implementation change.

## Ruling 2 — publication

The repository owner explicitly authorizes publication to
https://github.com/GregoritHub/Socionics_Engine_Function_Conditioning of the
stopped Batch 7 receipt (local `c1da66b`) and, once the corrected gate passes,
of every Batch 7 file. Stop receipts are part of the audit trail and are
published whether or not the batch passed. Push the stopped receipt first,
then re-run the gate, then push the acceptance.

After the gate passes: commit, push, report "Ready for outside review" with
the commit hash, end. Read repository stays untouched.
