# Changes to the acceptance process

Changes to the process files that [ACCEPTANCE.md](../ACCEPTANCE.md) names, recorded here as it
describes: a line is added at the top for each change, naming its pull request. The process is
not a specification and is not versioned, and a change to it is not tested by a cohort. Changes
to the three specifications are recorded in [CHANGELOG.md](../CHANGELOG.md).

- Pull request #PR: the cohort can be run and marked without judgement calls that the rules
  leave open. A cohort is an odd number of readers started, at least five, larger at the
  editor's choice the more obligations the change touches. Each reader is a separate process
  with no tools and no project context, started from an empty directory outside any repository
  with no settings files, `CLAUDE.md`, skills, plugins, hooks, MCP servers or saved session; the
  example command takes the packet on standard input. A reader is set aside only if its process
  failed or returned nothing or it shared the editor's context; a run left with fewer than five
  counting readers is void unless those readers already fail it, and a void run has a number, a
  record and posted sheets and counts towards the number of runs. The packet is the question
  set, the document and the fixture, each after one `===== FILE: <name> =====` line, with
  nothing else added. A new marking section says what a delegated marker receives, that it
  writes the record and its marks and PASS or FAIL are final unless the editor shows a rule was
  misapplied, that open judgements take the reading that records more misses or findings, what
  a keyed item is, that quoting is five or more consecutive verbatim words given as a quotation,
  what a correct load-bearing answer needs, that a miss is traceable to the text when its
  reasoning quotes or states what the document says or the key says it counts, and that a key
  can add such misses, never remove one, how unanswered items and truncated sheets count, and
  that two confusing passages are the same when they share a sentence or a paragraph. The
  thresholds apply to the readers whose answers count, read "every reader" and "all but one",
  and block on a single reader for the first, third and fourth rows; the fourth row's block lifts
  when a fresh cohort on the changed text passes it. A wording change is any change to the text
  after the readers read it, except the lines set for a version, and the cohort runs again after
  every failure, void run or wording change. The run record states the model version each reader
  reported, how readers were isolated, the command and who marked, and links the answer sheets,
  the exact prompt and the marker's instruction, posted unedited in comments on the pull request
  rather than kept in the repository, with the rest of the isolation attested by the editor; the
  isolation rule and the posted sheets apply from run 19, and runs 16 to 18 stand as recorded.
  The three keys no longer limit which misses count against the document, and removing such a
  limit is named as raising the bar. The process files include the checks that enforce them, and
  a process change goes through steps 1, 3 and 6 of `CONTRIBUTING.md`, applies on its merge into
  `next` and is recorded in this file, not in the changelog. `CONTRIBUTING.md` requires a
  reviewer who did not draft the change, named in the pull request with the review, points to
  the definition of a wording change, and adds the rebuild of the files
  `build-agent-surfaces.py` writes after an Appendix A change. Prompted by gaps in the text as it
  stood: `ACCEPTANCE.md` named no fixture in what a reader receives whilst
  `acceptance/README.md` did, the thresholds were written as five of five and four of five for a
  cohort of at least five, two pass-criteria rows both covered a single reader's traceable miss,
  and nothing settled an unanswered question or "the same passage". [Run
  16](runs/016-deferral-clause-run-1.md), [run 17](runs/017-deferral-clause-run-2.md) and
  [run 18](runs/018-deferral-clause-run-3.md) ruled on these case by case.
