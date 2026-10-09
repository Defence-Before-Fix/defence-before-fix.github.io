# Changes to the acceptance process

Changes to the process files that [ACCEPTANCE.md](../ACCEPTANCE.md) names, recorded here as it
describes: a line is added at the top for each change, naming its pull request. The process is
not a specification and is not versioned, and a change to it is not tested by a cohort. Changes
to the three specifications are recorded in [CHANGELOG.md](../CHANGELOG.md).

- Pull request #PR: the cohort can be run and marked without judgement calls that the rules
  leave open; this applies to runs made after it merges, and to run 19 if made under it, and
  runs 16 to 18 stand as recorded. A cohort is an odd
  number of readers started, at least five, larger at the editor's choice the more obligations
  the change touches, each a separate process with no tools and no project context, started from
  an empty directory outside any repository with no user, project or local settings files,
  `CLAUDE.md`, skills, plugins, hooks, MCP servers or saved session. A reader is set aside only
  if its answer text is empty or it shared the editor's context, and a run with a reader set
  aside is void, or fails if the readers who count already fail it or its own sheet has a miss
  traceable to the text; a void run has a number, a record and posted sheets. The packet is the question set, the document and the fixture, each
  after one `===== FILE: <name> =====` line. A new marking section says what a delegated marker
  receives and that its verdict is final unless a rule was misapplied, that open judgements take
  the stricter reading, and defines a keyed item, quoting (consecutive words of any length,
  verbatim apart from case, quotation-mark style and markup), a correct load-bearing answer,
  whose quotation must itself state part of the key's answer, a miss traceable to the text,
  including a question 1 bullet that quotes the document, which a key can add to but never
  remove, an unanswered item and the same passage. The thresholds apply to the readers whose answers count and block on a single
  reader for the first, third and fourth rows, and the fourth row says what a fresh cohort no
  longer naming a passage means. A fresh cohort runs after every change following a failure,
  every void run and every wording change, which is any change to the text after the readers
  read it except a version number or date the editor sets for a release. The record adds the
  model version each reader reported, the isolation, managed settings, readers set aside, void
  runs, re-marks and each confusing passage's words verbatim, and links each reader's whole
  output and the marker's instruction, posted on the pull request and never edited, hidden or
  deleted, or a run not already failed is void. The keys are marked at
  the commit the readers read and no longer limit which misses count against the document,
  removing such a limit is named as raising the bar, and the method key's "half right" is a miss.
  The process files include the checks that enforce them, and a process change goes through
  steps 1, 3 and 6 of `CONTRIBUTING.md`, applies to runs made after it merges, or earlier
  ones made under it at a named commit, and is recorded here, not in the changelog. `CONTRIBUTING.md` requires a reviewer who did not draft the change, points to
  the definition of a wording change, and adds the rebuild of the files `build-agent-surfaces.py`
  writes after an Appendix A change. Prompted by gaps in the text as it stood: `ACCEPTANCE.md`
  named no fixture in what a reader receives whilst `acceptance/README.md` did, the thresholds
  were written as five of five and four of five for a cohort of at least five, two pass-criteria
  rows both covered a single reader's traceable miss, and nothing settled an unanswered question
  or "the same passage". [Run
  16](runs/016-deferral-clause-run-1.md), [run 17](runs/017-deferral-clause-run-2.md) and
  [run 18](runs/018-deferral-clause-run-3.md) ruled on these case by case.
