# Run 68: TOOLING-SPEC.md, toolchain contradictions, sixth run

- **Document**: TOOLING-SPEC.md
- **Pull request**: not yet opened at the time of the run; it is to be opened from branch
  `editor/toolchain-contradictions`. The readers read commit 0080b8e. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 67 in clause 4.2 (rewritten in three paragraphs), section 2's table (a
  Remediation docs row) and section 1's "How to read this document".
- **Run within the pull request**: 6 (runs 57, 58, 62, 65 and 67 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `dbce8540d4259779cdced1129c5fa71306bbe31597700618177c4a5f48662919`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at 0080b8e, each after one
  `===== FILE: <name> =====` line, one blank line between files; the marker rebuilt it from that
  commit and it matched byte for byte.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model, and each sheet is that output's `result`.
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

Grades given, for the items the key accepts more than one: 5.1 Partial (1), Yes (2, 3, 4, 5);
6.1 Yes (1, 2, 4, 5), Partial (3), the Partial mentioning that no location is given for
calibrations or conventions; 6.2 No (all five), each mentioning that nothing rejects generic
text or a generic justification. Readers 1, 2, 4 and 5 note that the fixture does not say the
two undocumented rules are Blocking and grade 4.2 No on that assumption or inference, which the
key accepts with no condition.

Question 1: correct bullets per reader 6, 5, 6, 5 and 4 (reader 1: the governing principle;
4.1; 4.2; 4.3; 4.4 with 4.5; 5.1 to 5.3 with 6.1 to 6.3. Reader 2: 4.1; 4.2; 4.3; 4.4 with 4.5;
5.1 to 5.3 with 6.1 to 6.3. Reader 3: 4.1; 4.2; 4.3; 4.4 with 4.5; 5.1 to 5.3; 6.1 to 6.3.
Reader 4: 4.1 with 4.3; 4.2; 4.5; 5.1 to 5.3 with 6.3; 6.1 and 6.2. Reader 5: 4.1 with 4.2; 4.3;
4.4 with 4.5; 5.1 to 5.3 with 6.1 to 6.3). Reader 4's fourth and fifth bullets name different
clauses of one line of the key's list and each count. No bullet asserts anything the key marks
wrong. The first bullets of readers 2 and 5 (the toolchain judged as one assembled whole) state
how conformance is measured; reader 2's sixth calls the agent summary recommended; reader 4's
sixth (a declaration permitted, a project grade and a separate artefact grade) and reader 5's
sixth (one project grade, a shipped artefact graded separately, section 7 and the declaration
SHOULD or MAY, not conditions) are of the kinds the key counts neither way.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through", which states element (2); for 2b all five quote section 9's "The project-level
verdict is a single grade; ..."; for 2c all five quote clause 9.1's "The two verdicts MUST be
graded and declared separately, and neither implies the other." No answer gives a grade per
part or a single grade for 2c. Reader 1's 2c says "Two grades, if the company's project actually
ships the package"; see the points the rules did not settle.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says the toolchain does not conform
and that there is no agent summary (all five); S8 says Zigpipe ships no tooling (all five,
readers 1, 2 and 3 also placing zig-qa's grade on its own artefact); Decl says the declaration
is optional and the verdict rests on the exercise (all five).

### Misses

None. No answer matches a wrong reading the key names.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..0080b8e adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                                                     | Readers | Changed by the diff |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------------------- |
| 1   | Clause 4.2, second paragraph: "The [Toolchain] resolves an [Identifier] by a mechanism of its own, a command, an index file or a URL scheme, keyed on the [Identifier] exactly as printed" and "MUST ship with the project or with the [Toolchain]", a URL scheme set against the heading (1, 5); "MUST ship with the project or with the [Toolchain]" set against the third paragraph (2) | 1, 2, 5 | yes                 |
| 2   | Clause 4.2 heading: "from the installed copy, without network access", set against the second paragraph's URL scheme                                                                                                                                                                                                                                                                       | 1, 5    | yes                 |
| 3   | Clause 4.2, first paragraph: "names [Blocking] [Rules] rather than [Defences] because the failure it catches is a [Rule] that blocks without the documentation that would make it a [Defence]", set against the section 2 Defence row and clause 5.1                                                                                                                                       | 3, 5    | yes                 |
| 4   | Section 2 terminology table, [Defence] row: "A [Rule] with its documentation, in force and [Blocking]", set against clause 4.2's first paragraph (3, 5) and clause 5.1 (3, 4, 5)                                                                                                                                                                                                           | 3, 4, 5 | no                  |
| 5   | Clause 5.1, first paragraph: "every [Defence] active in the project"; whether the two undocumented rules, which `zig-qa list` shows, are within it; set against the Defence row (3, 4, 5) and clause 4.2's first paragraph (3, 5)                                                                                                                                                          | 3, 4, 5 | no                  |
| 6   | Clause 4.1, first paragraph: "That document's MUSTs are those of its sections 4 to 7, and this clause holds the [Detector] to every one of them. ... they are a summary, not the test" (3); described as the clause taking its MUSTs from sections 4 to 7 of a document not supplied, graded from the summary (2)                                                                          | 2, 3    | yes                 |
| 7   | Clause 6.2, fourth paragraph: "'needed for now', 'legacy', 'TODO' and their like", where the open phrase stops (2); "could be pasted onto any Exception unchanged, by a check it documents", set against the heading (5)                                                                                                                                                                   | 2, 5    | no                  |
| 8   | Clause 4.2, third paragraph: "is not re-shipped here", set against the second paragraph                                                                                                                                                                                                                                                                                                    | 2       | yes                 |
| 9   | Clause 6.1, first paragraph: "The [Toolchain] MUST define where the [Project record] lives and MUST load it", set against the Project record entry                                                                                                                                                                                                                                         | 3       | no                  |
| 10  | Section 2 terminology, [Project record] entry: "[Calibrations], [Exceptions] and conventions", set against clause 6.1                                                                                                                                                                                                                                                                      | 3       | no                  |
| 11  | Clause 6.2 heading: "names the hazard and the scope", set against the fourth paragraph                                                                                                                                                                                                                                                                                                     | 5       | no                  |
| 12  | Clause 4.3, second paragraph: "This clause is where the project's decision is made and enforced, and the decision is no", set against the Why paragraph                                                                                                                                                                                                                                    | 5       | no                  |
| 13  | Clause 4.3, Why paragraph: suppression "an Owner decision", set against the second paragraph                                                                                                                                                                                                                                                                                               | 5       | no                  |
| 14  | Clause 4.1, point 2, "Behind the table" paragraph: its reference to the detector specification's "clause 8.1", that document not supplied                                                                                                                                                                                                                                                  | 5       | yes                 |

Notes, not passages: readers 2, 3, 4 and 5 remark under question 3 that the detector
specification was not supplied; none of those remarks is under question 4. The section 2 table
was realigned by the diff for the new Remediation docs row; the Defence row's words, terms and
links are unchanged, so passage 4 is marked unchanged.

## Findings and where they lie

- **Finding A, passage 1, clause 4.2 second paragraph** (readers 1, 2 and 5): the diff writes
  this paragraph's first sentence and rewraps the "MUST ship" sentence into it. Text the change
  wrote or altered. Blocks.
- **Finding B, passage 2, clause 4.2 heading** (readers 1 and 5): the diff changes "a defence"
  to "a blocking rule" in it. Text the change wrote or altered. Blocks.
- **Finding C, passage 3, clause 4.2 first paragraph** (readers 3 and 5): written by the diff.
  Text the change wrote or altered. Blocks.
- **Finding D, passage 4, section 2 Defence row** (readers 3, 4 and 5): unchanged, but readers
  3 and 5 set it against clause 4.2's first paragraph, which the diff wrote. Text the change
  wrote or altered, under the Marking section's rule on a paragraph a reader sets against one.
  Blocks.
- **Finding E, passage 5, clause 5.1 first paragraph** (readers 3, 4 and 5): unchanged, but
  readers 3 and 5 set it against clause 4.2's first paragraph. Text the change wrote or altered,
  as for finding D. Blocks.
- **Finding F, passage 6, clause 4.1 first paragraph** (readers 2 and 3, counted by the
  open-point rule, point 1 below): the diff rewrites the paragraph, adding "That document's
  MUSTs are those of its sections 4 to 7" and "they are a summary, not the test". Text the
  change wrote or altered. Blocks.
- **Finding G, passage 7, clause 6.2 fourth paragraph** (readers 2 and 5): unchanged by the
  diff, and set only against clause 6.2's heading, also unchanged. Elsewhere: to be recorded in
  `acceptance/ROUTED.md`, on the open clause 6.2 line run 67 raised, and routed; does not block.

Passages 8 to 14 are each named by one reader: recorded, not findings.

## Points the rules did not settle

1. **Remarks on another document not supplied, given as passages.** Readers 2 and 3 name clause
   4.1's first paragraph under question 4, reader 3 by quotation and reader 2 by clause number
   and a description identifying its "sections 4 to 7" sentence, but each turns in part on the
   detector specification not being supplied, which the Marking section calls a note. Reader 5's
   item on clause 4.1 point 2 is of the same kind. Marked by the open-point rule: counted as
   passages. Finding F rests on readers 2 and 3 both being counted; findings A to E, and so the
   verdict, do not.
2. **Reader 1's 2c answer, "Two grades, if the company's project actually ships the package".**
   The Marking section gives a rule for a grade on a stated condition only under question 3. The
   question's company publishes the package, so read for its sense the answer states two for the
   case asked about, and its quotation of clause 9.1 states element (2). Marked for the reader
   under the open-point rule: correct. No other mark turns on it.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit f3ec69e, named before the readers started. The process files at
0080b8e are identical to those at f3ec69e.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: six (findings A
  to F). Not met.
- Passages named by two or more readers elsewhere: one (finding G), for `acceptance/ROUTED.md`;
  it does not block.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on findings A to F; every keyed item passed.

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
