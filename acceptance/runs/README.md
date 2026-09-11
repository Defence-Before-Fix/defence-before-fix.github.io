# Acceptance run records

One file per cohort run, `NNN-<slug>.md`, numbered in the one sequence the three documents
share. Runs 1 to 15 predate this directory and are summarised in the changelog entries for
1.0.0 and 1.0.1 of the method specification, 1.0.0 of the detector specification and 0.2.0 of
the toolchain specification; numbering here continues from 16.

A record states, in this order: the document; the pull request and the commit the readers were
given; the cohort size and model; the run number within that pull request; the marks per reader
per question against the key; the passages quoted as confusing and by how many readers; the
findings applied to the text as a result; and the verdict against the criteria in
`ACCEPTANCE.md`. Answer sheets are not pasted in full; the marks are the record.

The `Unreleased` changelog line for the change names the record, and `tools/changes.py` refuses a
specification change whose pull request adds no file here.
