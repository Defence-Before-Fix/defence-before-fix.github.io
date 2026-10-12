# Run 82: TOOLING-SPEC.md, toolchain contradictions, tenth run

- **Document**: TOOLING-SPEC.md
- **Pull request**: not yet opened at the time of the run; it is to be opened from branch
  `editor/toolchain-contradictions`. The readers read commit de34774. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 81: clause 5.1 no longer says the listing covers every blocking rule,
  documented or not; it says a blocking rule whose route to documentation is missing is not yet
  a defence, that clause 4.2 fails it, and that the listing can show it with the gap showing; and
  section 2's closing paragraph names clauses 4.2 and 8.1 as the clauses that catch such a rule.
- **Run within the pull request**: 10 (runs 57, 58, 62, 65, 67, 68, 72, 76 and 81 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `1fa098d5a7901d8211c09387ca7bffd0bcabcd05caba5565a489557ae5761028`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at de34774, each after one
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

Grades given, for the items the key accepts more than one: 5.1 Yes (all five); 6.1 Partial
(readers 2, 3 and 5, each mentioning that the fixture names a place for exceptions and none for
calibrations or conventions) and Yes (readers 1 and 4); 6.2 No (all five), each mentioning that
nothing rejects a generic justification or generic text. All five grade 4.2 No reading the two
undocumented rules as Blocking because `zig-qa run` stops when Lintomatic fails, which the key's
4.2 row reads as a No. All five grade 4.3 Yes on the one route the fixture describes, which the
key's 4.3 row says is the case the fixture presents. Readers 1, 2 and 3 cite the 5.1 sentence
that the listing "can show it with that gap showing" for their 5.1 Yes; reader 5 says the two
`(none)` entries are the gap clause 4.2 reports.

Question 1: correct clauses named per reader within the first six bullets. Reader 1: 4.1 with
4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3 with 6.3; 6.1 and 6.2. Reader 2: 4.1; 4.2; 4.3 with 4.5;
5.1 to 5.3 with 6.2 and 6.3. Reader 3: 4.1 with 4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3; 6.1 to 6.3.
Reader 4 (seven bullets, the first six marked): 4.1; 4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3. Reader
5: 4.1; 4.2; 4.3; 5.1 to 5.3 with 6.2 and 6.3; 4.5. No bullet asserts anything the key marks
wrong. Every reader's first bullet (the toolchain judged as one assembled whole), the remarks of
readers 1, 2, 3 and 5 that a shipped artefact has a second grade, and the remarks of readers 2
and 3 that section 7 is SHOULDs, are counted neither way, as the key says. Reader 2's sixth
bullet also calls clause 6.4's defaults recommended; a bullet on a SHOULD asserts no obligation
and is not counted.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through"; for 2b all five quote section 9's "The project-level verdict is a single grade; ...";
for 2c all five quote clause 9.1's "The two verdicts MUST be graded and declared separately, and
neither implies the other." No answer gives a grade per part or a single grade for 2c. Reader 1's
2b adds that Zigpipe ships nothing and so has only the one grade, quoting section 9; it asserts
nothing the key marks wrong.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says there is no agent summary (all
five), each adding that the toolchain does not conform at all; S8 says Zigpipe ships no tooling
(all five), readers 1, 2, 4 and 5 adding that zig-qa would carry its own artefact grade, which
none grades; Decl says the declaration is optional and the verdict rests on the exercise (all
five).

### Misses

None. No answer matches a wrong reading the key names.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..de34774 (9e914fe
being the merge base with `next`) adds, rewords, moves or deletes a sentence in the paragraph,
changes a word, term or link in it, or parts it from what it refers to.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                                                                 | Readers | Changed by the diff                                                                              |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------------------------------------------------------------------------------------------------ |
| 1   | Clause 5.1, first paragraph: "It MUST provide the route to each one's full documentation" with "the listing can show it with that gap showing", whether an empty route meets the MUST (1); "MUST list every [Defence] active in the project" with "A [Blocking] [Rule] whose route to documentation is missing is not yet a [Defence] ... can show it", whether the undocumented rules must appear (3) | 1, 3    | yes: the second sentence each quotes is added by the diff                                        |
| 2   | Clause 4.1, first paragraph: "takes a verdict already given on the [Detector] under that document as settled" (1, 2), with "a [Detector] that document finds not to [Conform] fails this clause, whether or not the sentences that follow show why" (2); which verdict is meant, and what a grader does when none has been given                                                                       | 1, 2    | yes: rewritten by the diff                                                                       |
| 3   | Clause 6.2, last paragraph: "by a check it documents: 'needed for now', 'legacy', 'TODO' and their like" against "could be pasted onto any [Exception] unchanged", which test governs (1); "name the [Hazard] ... and the scope" and "cannot verify truth", with the heading's "MUST reject a generic one", whether the check must test that hazard and scope are named (4)                            | 1, 4    | no: neither the paragraph nor the 6.2 heading is touched by the diff                             |
| 4   | Clause 4.3, second paragraph: "This clause is where the project's decision is made and enforced, and the decision is no"; what the "no" answers                                                                                                                                                                                                                                                        | 2       | no: the diff adds sentences to the first paragraph only and inserts no paragraph between them    |
| 5   | Clause 4.4, first paragraph: "The [Toolchain]'s own entry point MUST meet clauses 5.1 to 5.4 of the [detector specification] for every [Defence] it routes"; the restatement covers three properties, so whether 5.4 is graded                                                                                                                                                                         | 2       | no                                                                                               |
| 6   | Clause 6.1, first paragraph: "The [Toolchain] MUST define where the [Project record] lives and MUST load it", set against section 2's Project record entry; one location for all three kinds or not                                                                                                                                                                                                    | 2       | no                                                                                               |
| 7   | Section 2: "These are additional."; what the terms are additional to                                                                                                                                                                                                                                                                                                                                   | 2       | no: the diff re-pads the table above it and adds a row; the sentence and its place are unchanged |
| 8   | Section 2, the paragraph "A [Blocking] [Rule] whose documentation is missing is not yet a [Defence]"; it sits under the Project record entry, so which term it governs                                                                                                                                                                                                                                 | 4       | yes: added by the diff                                                                           |
| 9   | Clause 5.3, second paragraph: "Where such a [Defence] is not expressible in the [Toolchain]'s own [Detectors], its entry MAY be sourced from wherever it is enabled ..."; whether that reaches configuration outside the toolchain's own files                                                                                                                                                         | 5       | no                                                                                               |

Notes, not passages: reader 4's remark on clause 9.1, "the project's remediations against
section 7 of the method specification", says it could not work out what that section requires
because the method specification was not in its materials; that is a remark that another document
was not supplied, and the Marking section records it as a note. Under question 3, readers 1, 2
and 3 remark that no verdict on Lintomatic under the detector specification was given, and
reader 2 that it did not have the detector specification, when grading 4.1 and 4.4.

## Findings and where they lie

- **Finding A, passage 1, clause 5.1 first paragraph** (readers 1 and 3): the diff adds the
  sentence "A [Blocking] [Rule] whose route to documentation is missing is not yet a \[Defence\]:
  clause 4.2 fails it, and the listing can show it with that gap showing." Reader 1 sets it
  against the paragraph's MUST on the route to documentation, reader 3 against its MUST to list
  every Defence. Text the change wrote or altered. Blocks.
- **Finding B, passage 2, clause 4.1 first paragraph** (readers 1 and 2): the diff rewrites the
  paragraph, adding the sentence each quotes, "A grader of this clause checks the sentences that
  follow ... and takes a verdict already given on the [Detector] under that document as settled:
  ...". Text the change wrote or altered. Blocks. Whether it is a passage rather than a note is
  recorded below.
- **Finding C, passage 3, clause 6.2 last paragraph** (readers 1 and 4): unchanged, and neither
  reader sets it against a changed paragraph; reader 4 sets it against the 6.2 heading, also
  unchanged. Elsewhere: a finding against the document, recorded in `acceptance/ROUTED.md`, where
  the open 6.2 row raised by runs 67 and 68 (whether the check must test that the hazard and the
  scope are named) covers it and gains run 82; routed to a change of its own, and does not block.
  The marker writes only this record; the ROUTED entry is for the editor.

Passages 4 to 9 are each named by one reader: recorded, not findings, applied at the editor's
discretion.

## Points the rules did not settle

1. **Whether passage 2 is a passage or a note.** Readers 1 and 2 tie their confusion to the
   fixture giving no verdict on Lintomatic under the detector specification, and the Marking
   section makes a remark that another document was not supplied a note. Judgement: each reader's
   confusion is what the sentence asks a grader to do, which verdict it means (1) and what to do
   when none has been given (2), and that is about the passage, not about a missing document; so
   it is a passage. Had it stayed open, the open-point rule counts the passage. Marked as named,
   which makes finding B.
2. **6.1 grades given with a remark on another case.** Readers 2, 3 and 5 grade Partial and say
   it would be Yes if the exceptions file is the whole project record (3 implicitly, 2 and 5 in
   terms). The Marking section reads a grade given on a stated condition as the grade for the
   case the fixture presents only where the key says which case that is, and the key's 6.1 row
   does not. Judgement: each reader states Partial outright and the remark names a different
   case, so Partial is the grade; it meets the key's condition. Had the remark made the grade
   conditional, the open-point rule marks it for the reader. Marked for the readers.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 0da928d, named before the readers started. The process files at
de34774 (`ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md`, `tools/changes.py`, `spec-qa.py` and the CI workflows) are identical to those
at 0da928d.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: two (findings A
  and B). Not met.
- Passages named by two or more readers elsewhere: finding C, routed to `acceptance/ROUTED.md`;
  does not block.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on findings A and B; every keyed item passed.

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
