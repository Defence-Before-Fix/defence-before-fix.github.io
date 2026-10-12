# Passages routed out of a cohort

A finding is a passage two or more readers of one cohort named as confusing, under question 4,
that lies outside the text the change being tested wrote or altered. `ACCEPTANCE.md` routes such
a finding here rather than blocking the change whose cohort raised it, so that each change is
judged on what it changed and the document is still made clearer, one change at a time. The
editor reads this list before cutting a release.

A finding is open until a change that reworks its passage passes a cohort, when the line names
that run and moves below the rule, or until the editor closes it with a reason recorded here. A
finding raised again by a later run is noted on its line, not listed twice. The rows below were
raised by runs 31 to 52 under the earlier rules, on untouched text of the change those runs
tested, and are listed here so that they are not lost.

## Open

| Document           | Clause      | Passage                                                                                                                                                                              | Raised by               | Status                                 |
| ------------------ | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- | -------------------------------------- |
| `TOOLING-SPEC.md`  | 9 and 9.1   | Section 9 counts section 8 in a shipping project's project grade; clause 9.1 says section 8 bears on the artefact grade only                                                         | runs 43, 46             | `editor/toolchain-contradictions`      |
| `TOOLING-SPEC.md`  | 2, 4.2, 8.1 | The Defence row, "with its documentation, in force and Blocking", against clauses 4.2 and 8.1, which exist to catch a Blocking rule whose documentation is missing                   | runs 33, 40, 43, 46, 49 | `editor/toolchain-contradictions`      |
| `TOOLING-SPEC.md`  | 9.2         | "MUST record that gap alongside the version" against "The declaration is optional."                                                                                                  | runs 33, 52             | `editor/toolchain-contradictions`      |
| `TOOLING-SPEC.md`  | 4.3         | The heading, "through a defence of its own", against the body's "MUST disable ... or MUST run a Blocking Defence"                                                                    | run 33                  | `editor/toolchain-contradictions`      |
| `TOOLING-SPEC.md`  | 4.1         | "That document's MUSTs, in brief, are six", where the detector specification's sections 4 to 7 carry eleven                                                                          | runs 40, 46             | `editor/toolchain-contradictions`      |
| `TOOLING-SPEC.md`  | 5.3         | "Where such a Defence is not expressible in the Toolchain's own Detectors, its entry MAY be sourced from wherever it is enabled": what "such a Defence" and "its entry" refer to     | run 52                  | open                                   |
| `DETECTOR-SPEC.md` | 7.1         | "by a Rule the project can write in the Detector itself", read as the project editing the detector's own source, against clause 4.1's bespoke rules                                  | runs 36, 42, 45, 48, 51 | `editor/detector-route-rule`           |
| `DETECTOR-SPEC.md` | 8.1         | "MUST record that gap alongside the version it declares" against "The declaration is optional."                                                                                      | runs 39, 42             | `editor/detector-route-rule`           |
| `DETECTOR-SPEC.md` | 5.3         | "the location of the remainder": what the remainder is when the summary prints every finding                                                                                         | run 32                  | `editor/detector-route-rule`           |
| `SPEC.md`          | 1 (Owner)   | The default Owner sentences: whether whoever instructed the Practitioner may take section 4's decisions, and the bracketed verb "Suppress" among nouns                               | runs 41, 47, 50         | open                                   |
| `SPEC.md`          | 4           | "the Rule MAY merge at full width with that case recorded as a known Instance awaiting the Owner" against "provided the Rule does not become Blocking until every Instance is fixed" | run 50                  | open; a method question for the editor |

## Closed

None yet.
