# Run 87: TOOLING-SPEC.md, defined terms, ninth run

- **Document**: TOOLING-SPEC.md
- **Pull request**: [24](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24),
  branch `editor/defined-terms`. The readers read commit daa2512. Change: every use of a defined
  term in the three documents linked to its terminology entry, with the entries themselves
  unchanged in substance; in this document the section 2 table and clause 4.1 say Rule harness
  where they said Harness, the section 3 table's Correct construction row says the project
  supplies the Remediation docs content, and the uses of "remediation" in clause 4.5's **Why**
  paragraph and clause 9.1's first paragraph link to the method's term. The toolchain
  contradictions change (pull request 25), which passed its own cohort at run 86, is merged into
  this branch at its commit c1ad65b; this is a fresh run of this document after run 55.
- **Run within the pull request**: 9 for this document (runs 33, 37, 40, 43, 46, 49 and 52 under
  the earlier process and run 55 under this one came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `32c7ea2c954a34c0fff11518b39705d732d7014286118b53c959effe121f4c16`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at daa2512, each after one
  `===== FILE: <name> =====` line, one blank line between files; the marker rebuilt it from that
  commit and it matched byte for byte.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model, and each sheet is that output's `result`, which
  the marker confirmed byte for byte.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  marking instruction and its agent definition, having seen neither the drafting nor the review.

## Marks

Readers are numbered 1 to 5 as their sheets are. Question 3 columns: the eleven clauses, then
the four answers (S9 conformance under section 9, AS agent support, S8 whether section 8
applies, Decl whether the absence of a declaration affects the verdict).

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 4.4 | 4.5 | 5.1 | 5.2 | 5.3 | 6.1 | 6.2 | 6.3 | S9  | AS  | S8  | Decl |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| 1      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 2      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 3      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 4      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 5      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |

Grades given, for the items the key accepts more than one: 5.1 Yes (all five; readers 2, 4 and
5 add that the two `(none)` rules are not Defences under section 2 and so outside 5.1); 6.1 Yes
(readers 1, 2, 3 and 5) and Partial (reader 4, mentioning that the Project record also holds
calibrations and conventions and the fixture gives neither a location, which meets the key's
condition; it adds that it would be Yes if the exceptions file is the whole record, and the
Partial is the grade it gives for the case); 6.2 No (all five), each mentioning that nothing
rejects generic phrasing or generic text such as "TODO", which meets the key's condition. All
five grade 4.1 No on the two undocumented bundled rules with nothing supplied for them; each
says, in the table or above it, that only the restated points of the detector specification were
checked, and readers 1, 2, 4 and 5 that it was not supplied, which the key's 4.1 row accepts. All five grade 4.2 No;
reader 1 calls the two rules blocking, readers 2 and 4 say they read them as Blocking because
`zig-qa run` stops when Lintomatic fails or because they are enabled in the gating run, and
readers 3 and 5 say the No assumes they are Blocking (reader 5: "If they are not, this clause
would hold"); the key's 4.2 row reads a No given on that condition as a No.

Question 1: correct clauses named per reader within the first six bullets. Reader 1: 4.1 with
4.2; 4.3; 4.4 and 4.5; 5.1, 5.2 and 6.3 (four bullets; its sixth bullet's "self-audit MUSTs" for
a shipped toolchain is not needed for the count and is not decided). Reader 2: the governing
principle (section 1) with 4.1 point 1; 4.1; 4.2; 4.3; 4.5 and 4.4; 5.2, 5.3 and 6.1 to 6.3.
Reader 3: 4.1 and 4.2; 4.3 with 6.1; 6.2; 5.1 to 5.3 with 6.3; 4.5, 4.4, 8.1 and 8.2. Reader 4:
4.1; 4.2; 4.3 with 6.2; 4.4 and 4.5; 5.1 to 5.3; 6.1 and 6.3. Reader 5: 4.1; 4.2; 4.3 with 6.2;
4.5 and 4.4; 5.1 to 5.3 with 6.3. Four or more correct bullets each. No bullet asserts anything
the key marks wrong. The first bullets of readers 1 and 5 (the toolchain judged as one
assembled whole), reader 3's first bullet (each defence made governable, not just runnable) and
reader 1's remark that the agent-context summary and delivery are SHOULDs are counted neither
way, as the key says or as not needed for the count.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through"; for 2b all five quote section 9's "The project-level verdict is a single grade; ...";
for 2c all five quote clause 9.1's "The two verdicts MUST be graded and declared separately, and
neither implies the other." Readers 2 and 4 add under 2b that a shipped artefact has its own
grade under clause 9.1; that gives no grade per part. No answer gives a single grade for 2c.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says section 7 is not met or there is no
summary, and readers 1, 2, 3 and 5 add that the toolchain does not conform at all (all five);
S8 says Zigpipe ships no tooling to other projects (all five), readers 1 to 4 adding that
section 8 would bear on zig-qa's own artefact grade and reader 5 that zig-qa is the company's
package, not something Zigpipe ships; Decl says the declaration is optional, or that
the verdict rests on the exercise of the clauses (all five).

### Misses

None.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them. "This change" means the diff c1ad65b..daa2512 of
`TOOLING-SPEC.md`, this change's text over and above the merged toolchain contradictions change;
the diff 9e914fe..daa2512 (9e914fe being the merge base with `next`) shows both, and a paragraph
only the toolchain change altered is not this change's text. This change alters: the section 2
table's Rule harness row; the section 3 table's red proof and Correct construction rows; clause
4.1 point 1; clause 4.5's **Why** paragraph; clause 9.1's first paragraph; and the link
definitions. No passage below lies in any of them.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                    | Readers | Changed by this change                                 |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------ |
| 1   | Clause 6.2, heading: described as "the heading", which with the first body sentence requires the justification to name the hazard and scope (set against passage 2)                                                                                                                                       | 1       | no; nor by the toolchain change                        |
| 2   | Clause 6.2, fourth paragraph: "name the Hazard being accepted and the scope of the Exception", and the "documented check for pasteable generic phrases" (which check, if any, verifies that hazard and scope are named)                                                                                   | 1       | no; nor by the toolchain change                        |
| 3   | Section 2, the Bundled defence terminology entry: "one with its documentation, [Blocking], and routed through the [Toolchain]'s own entry point" (set against passages 4 and 5)                                                                                                                           | 2       | no; nor by the toolchain change                        |
| 4   | Clause 8.1, heading: "A shipped toolchain MUST fail its own release if a bundled defence lacks resolvable documentation" (set against passage 3)                                                                                                                                                          | 2       | no; nor by the toolchain change                        |
| 5   | Clause 8.1, first paragraph: "its body refers to 'a missing page'" (set against passage 3)                                                                                                                                                                                                                | 2       | no; the toolchain change wrote "a missing page" there  |
| 6   | Clause 4.1, point 2: "does the [Detector] meet every MUST of sections 4 to 7 of the [detector specification](DETECTOR-SPEC.md), exercised as its clause 8.1 describes?" (what exercising clause 8.1 involves)                                                                                             | 3       | no; the toolchain change reworded sentences in point 2 |
| 7   | Section 2, the Project record terminology entry: "[Calibrations], [Exceptions] and conventions" (set against passage 8: one location or a set of them)                                                                                                                                                    | 4       | no; nor by the toolchain change                        |
| 8   | Clause 6.1, first paragraph: "The [Toolchain] MUST define where the [Project record] lives" (set against passage 7)                                                                                                                                                                                       | 4       | no; nor by the toolchain change                        |
| 9   | Clause 4.1, first paragraph: "The sentences that follow restate the ones most often failed, so that a grader knows where to look first; they are not the whole test, and a grader without that document to hand can check only them, and says so in the verdict." (where in a verdict the caveat belongs) | 5       | no; the toolchain change wrote the sentence            |

Notes, not passages: reader 4's remark that "Calibrations" is linked to the method
specification, which it did not have, is a remark that a term is defined only in another
document, recorded as a note under the Marking section's question 4 rule; its passages 7 and 8
are counted on its remark that it is unclear whether the record is one location or a set.
Reader 3's item says it could not check clause 8.1 without the detector specification, but its
remark that the document does not say what exercising clause 8.1 involves is about the passage,
so passage 6 is counted. Under question 3, readers 1 to 5 remark that the detector
specification was not supplied; those are not question 4 answers.

## Findings and where they lie

None. Every passage is named by one reader only. The nearest pairs lie in different paragraphs:
passages 6 (reader 3) and 9 (reader 5) are in clause 4.1, the one in the list item of point 2
and the other in the clause's first paragraph; passages 2 (reader 1) and 8 (reader 4) are in
clauses 6.2 and 6.1; passages 3 (reader 2) and 7 (reader 4) are different terminology entries.
All nine are recorded, are not findings, and are applied at the editor's discretion. None lies
in text this change wrote or altered.

## Points the rules did not settle

1. **Whether reader 1 names clause 6.2's heading as well as its fourth paragraph.** Its
   quotation lies in the fourth paragraph, and it locates the words in "the heading and the
   first body sentence"; the heading of 6.2 does say the justification names the hazard and the
   scope, and a heading is a paragraph of its own. Marked in the direction the open-point rule
   gives: the heading is counted as named (passage 1). No other reader names either paragraph of
   clause 6.2, so the verdict does not turn on it.

Considered and settled by a rule, so not open: reader 3's item and reader 4's note on
"Calibrations", as above; reader 4's Partial on 6.1 and the conditional No on 4.2 of readers 3
and 5, by the key's rows for those clauses; reader 1's sixth question 1 bullet, not needed for
the count.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 568e323, named before the readers started. The process files at
daa2512 (`ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md`, `tools/changes.py`, `spec-qa.py` and the CI workflows and pull request
template under `.github/`) are identical to those at 568e323.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: none. Met.
- Passages named by two or more readers elsewhere: none.

## Findings applied

None at the time of marking.

## Verdict

PASS. Every keyed item met its threshold, every reader was correct on every keyed item, and no
passage was named by two or more readers.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6126059169); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6126058788); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6126059548).
