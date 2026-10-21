# Amendment A7 — publication transport

Issued by the repository owner on 20 October 2026 (client date).

R4 forbids automation that writes without you; it does not require terminal git
for the push. You are authorized to publish through the authenticated GitHub
connector, as Batches 0–6 were. The local terminal commit remains the record of
what was done; the connector commit is the publication of it. Where the hashes
differ, the receipt lists both: "local <hash> → published <hash>". Push as a
non-forced update on the expected remote head; verify the published tree matches
the local tree by file hash and record that in the receipt.

Order: publish the stopped receipt (local 2bb8e3a) now; run the corrected gate
(reproduce.py, unittest discover, path_check.py); on pass, commit locally,
publish, report "Ready for outside review" with both hashes, end. A6's allowance
stands. Read repository stays untouched.
