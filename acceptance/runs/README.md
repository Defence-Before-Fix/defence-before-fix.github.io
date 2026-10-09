# Acceptance run records

One file per cohort run, `NNN-<slug>.md`, numbered in the one sequence the three documents
share. Runs 1 to 15 predate this directory and are summarised in the changelog entries for
1.0.0 and 1.0.1 of the method specification, 1.0.0 of the detector specification and 0.2.0 of
the toolchain specification; numbering here continues from 16.

A record states what `ACCEPTANCE.md` lists, in this order: the document; the pull request and
the commit the readers were given; the cohort size and model, with the model version each reader
reported; how the readers were isolated and the command they were started with; the run number
within that pull request; who marked and, for a delegated marker, how it was started; the marks
per reader per question against the key, with any judgement made in marking; the passages quoted
as confusing and by how many readers; the findings applied to the text as a result; and the
verdict against the criteria in `ACCEPTANCE.md`, with a link to the answer sheets. Earlier
records show the style only; where one differs from this order, this file wins. Answer sheets
are not kept in this repository, and the marks are the record; the sheets, unedited, and the
instruction a delegated marker was given are posted in one or more consecutive comments on the
pull request, each linked from the record.

The `Unreleased` changelog line for the change names the record, and `tools/changes.py` refuses a
specification change whose pull request adds no file here.
