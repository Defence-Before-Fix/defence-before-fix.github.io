# Changes to the acceptance process

Changes to the process files that [ACCEPTANCE.md](../ACCEPTANCE.md) names, recorded here as it
describes. The process is not a specification and is not versioned, and a change to it is not
tested by a cohort. Changes to the three specifications are recorded in
[CHANGELOG.md](../CHANGELOG.md).

## Unreleased

- The cohort can be run and marked without judgement calls that the rules leave open. A cohort
  is an odd number of readers, at least five, and the editor may choose a larger one for a more
  load-bearing change. Each reader is a separate process with no tools, no settings files, no
  MCP servers and no context but its packet, started from an empty directory outside any
  repository, and the example command shows the flags that do this; a reader sharing the
  editor's context does not count, and a run left with fewer than five counting readers is void.
  The packet is the document, its question set and the fixture the questions name, with nothing
  added around them. A new marking section says what a delegated marker receives, that its
  verdict is final unless the editor shows a rule was misapplied, that the marker takes the
  stricter reading wherever it makes an open judgement, what counts as quoting, what a correct
  load-bearing answer needs, which misses are traceable to the text and how the key's statements
  bear on that, how unanswered items count, and when two confusing passages are the same.
  Thresholds read "every reader" and "all but one", the same as five of five and four of five for
  a cohort of five; every pass-criteria row must hold, and the last covers only what the others
  do not. The run record states how readers were isolated, the command they were started with
  and who marked, and links the answer sheets, which are posted unedited on the pull request
  rather than kept in the repository; the isolation rule and the posted sheets apply from run
  019, and runs 16 to 18 stand as recorded. Process changes are recorded
  in this file, not in the changelog. `CONTRIBUTING.md` requires a reviewer who did not draft the
  change, says which review findings mean a fresh run, adds the agent-facing rebuild after an
  Appendix A change, and points to how a change to the process files is made. Prompted by gaps in
  the text as it stood: `ACCEPTANCE.md` named no fixture in what a reader receives whilst
  `acceptance/README.md` did, the thresholds were written as five of five and four of five for a
  cohort of at least five, two pass-criteria rows both covered a single reader's traceable miss,
  and nothing settled an unanswered question or "the same passage". [Run
  16](runs/016-deferral-clause-run-1.md), [run 17](runs/017-deferral-clause-run-2.md) and
  [run 18](runs/018-deferral-clause-run-3.md) ruled on these case by case.
