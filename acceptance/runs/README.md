# Acceptance run records

One file per cohort run, `NNN-<slug>-run-<k>.md`, numbered in the one sequence the three
documents share, with `<k>` the run number within its pull request. Runs 1 to 15 predate this
directory and are summarised in the changelog entries for 1.0.0 and 1.0.1 of the method
specification, 1.0.0 of the detector specification and 0.2.0 of the toolchain specification;
numbering here continues from 16.

A record states what `ACCEPTANCE.md` lists under "The record", in this order: the document; the
pull request and the commit the readers were given; the cohort size and model, with the model
version each reader reported; how the readers were isolated and the command they were started
with; any reader set aside and why; who marked and, for a delegated marker, how it was started;
the marks per reader per keyed item, with each miss and the reader's reasoning in brief; every
passage named under question 4, with the words quoted or the description given, its clause and
the readers naming it; each finding and whether it lies in text the change wrote or altered; any
point the rules did not settle; whether the run was made under a process change before it merged
and, if so, at which commit; the findings applied afterwards; the verdict; and a link to the
answer sheets posted on the pull request. Earlier records show the style only; where one differs
from this order, this file wins. Answer sheets are not kept here; the marks are the record.

The `Unreleased` changelog line for the change names the record, and `tools/changes.py` refuses a
specification change whose pull request adds no file here.
