# Run 67: TOOLING-SPEC.md, toolchain contradictions, fifth run

- **Document**: TOOLING-SPEC.md
- **Pull request**: not yet opened at the time of the run; it is to be opened from branch
  `editor/toolchain-contradictions`. The readers read commit 645d811. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 65 in clause 4.2's heading and first paragraph, clause 8.1's first paragraph
  and clause 9.1's first paragraph.
- **Run within the pull request**: 5 (runs 57, 58, 62 and 65 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `efd52c615ca1e070ef6fc016a6d6eaeaac069cb9baf184ba36805631a0fabcf3`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at 645d811, each after one
  `===== FILE: <name> =====` line, one blank line between files; the marker rebuilt it from that
  commit and it matched byte for byte.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model.
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

Grades given, for the items the key accepts more than one: 5.1 Yes (1), Partial (2, 4, 5), No
(3); 6.1 Yes (1, 4, 5), Partial (2, 3), each Partial mentioning that no location is given for
calibrations or conventions; 6.2 No (all five), each mentioning that nothing rejects generic
text or a generic justification. Readers 1, 3, 4 and 5 note that the fixture does not say the
two undocumented rules are Blocking and grade 4.2 No on that assumption or inference, which the
key accepts with no condition.

Question 1: correct bullets per reader 5, 5, 4, 5 and 5 (reader 1: 4.1; 4.2; 4.3 with 4.5; 5.1
to 5.3; 6.1 to 6.3. Reader 2: 4.1; 4.2; 4.3; 4.4 with 4.5; 5.1 to 5.3 with 6.1 and 6.2. Reader
3: 4.1 with 4.2; 4.3 with 4.5; 5.1 to 5.3; 6.1 to 6.3. Reader 4: 4.1; 4.2; 4.3 with 4.5; 5.1 to
5.3; 6.1 to 6.3. Reader 5: 4.1; 4.2; 4.3 with 6.2; 4.4 with 4.5; 5.1 to 5.3 with 6.3 and 8.2).
Reader 5's fourth and sixth bullets name different clauses of one line of the key's list and
each count. No bullet asserts anything the key marks wrong. The first bullet of every reader
(the toolchain judged as one assembled whole, or one grade) states how conformance is measured,
and reader 3's sixth (a shipped artefact graded separately, section 7 SHOULDs, the declaration
optional) is of the kinds the key counts neither way.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through", which states element (2); for 2b all five quote section 9's "The project-level
verdict is a single grade; ..."; for 2c all five quote clause 9.1's "The two verdicts MUST be
graded and declared separately, and neither implies the other." No answer gives a grade per
part or a single grade for 2c. Reader 1's 2c says "two grades if it ships an artefact"; see the
points the rules did not settle.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says section 7 is not met or there is
no agent summary, and that the toolchain does not conform (all five); S8 says Zigpipe ships no
tooling (all five, readers 1, 2, 3 and 5 also placing zig-qa's grade on its own artefact); Decl
says the declaration is optional, not a condition, or that the verdict rests on the exercise
(all five).

### Misses

None. No answer matches a wrong reading the key names.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..645d811 adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                                                                                                                                             | Readers | Changed by the diff |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------- |
| 1   | Clause 4.2, first paragraph: "this one covers every [Identifier] the project can see, the project's own [Rules] included" and "covers the project's own [Rules] and every [Bundled defence]", set against the heading (1); "The mechanism is keyed on the [Identifier] exactly as printed", the mechanism not named first (3); "The [Toolchain] MUST resolve every [Identifier] its [Blocking] [Rules] print to [Remediation docs] on disk", the term not glossed in section 2 (5) | 1, 3, 5 | yes                 |
| 2   | Section 1, "How to read this document" paragraph: "self-contained for grading a [Toolchain], apart from clause 4.1", set against clause 4.4's citation of detector clauses 5.1 to 5.4 (4); described as where "the document says" the section 2 table "is how terms are defined for grading", set against clause 4.2 (5)                                                                                                                                                           | 4, 5    | yes                 |
| 3   | Clause 6.2 heading: "MUST carry a written justification that names the hazard and the scope" (3); "Clause 6.2's heading", "name the hazard and the scope" (4); each set against clause 6.2's fourth paragraph                                                                                                                                                                                                                                                                      | 3, 4    | no                  |
| 4   | Clause 6.2, fourth paragraph: "by a check it documents" (3); "by a check it documents: 'needed for now', 'legacy', 'TODO' and their like" and "cannot verify truth" (4); whether the check must test that hazard and scope are named                                                                                                                                                                                                                                               | 3, 4    | no                  |
| 5   | Clause 4.2 heading: "every [Identifier] a [Blocking] [Rule] it routes can print"; whether non-blocking rules are in scope                                                                                                                                                                                                                                                                                                                                                          | 1       | yes                 |
| 6   | Clause 6.2, first paragraph: "It MUST NOT supply a default", set against clause 6.4                                                                                                                                                                                                                                                                                                                                                                                                | 1       | no                  |
| 7   | Clause 6.4 heading: "The [Toolchain] SHOULD state its own defaults for anything the method leaves to the project"                                                                                                                                                                                                                                                                                                                                                                  | 1       | no                  |
| 8   | Clause 5.1, first paragraph: "MUST list every Defence active in the project" and "MUST provide the route to each one's full documentation"; whether an undocumented rule is listed                                                                                                                                                                                                                                                                                                 | 2       | no                  |
| 9   | Section 2 terminology table, [Defence] row: "A Rule with its documentation, in force and Blocking", set against clause 5.1                                                                                                                                                                                                                                                                                                                                                         | 2       | no                  |
| 10  | Clause 4.3, second paragraph: "This clause is where the project's decision is made and enforced, and the decision is no"                                                                                                                                                                                                                                                                                                                                                           | 2       | no                  |
| 11  | Clause 9.1, first paragraph: "MUST be graded and declared separately", set against clause 9.2                                                                                                                                                                                                                                                                                                                                                                                      | 3       | yes                 |
| 12  | Clause 9.2, third paragraph: "The declaration is optional."                                                                                                                                                                                                                                                                                                                                                                                                                        | 3       | yes                 |
| 13  | Clause 6.1, first paragraph: "define where the [Project record] lives"; whether one path holds all three kinds of judgement                                                                                                                                                                                                                                                                                                                                                        | 3       | no                  |
| 14  | Section 2 terminology, [Project record] entry: the record covering calibrations, exceptions and conventions, set against clause 6.1                                                                                                                                                                                                                                                                                                                                                | 3       | no                  |
| 15  | Clause 4.4, first paragraph: "clauses 5.1 to 5.4 of the [detector specification]", set against section 1's "How to read" paragraph                                                                                                                                                                                                                                                                                                                                                 | 4       | no                  |
| 16  | Clause 4.5, first paragraph: "in the order method section 5 states"; the method specification not supplied                                                                                                                                                                                                                                                                                                                                                                         | 4       | no                  |
| 17  | Clause 5.3, second paragraph: "Where such a [Defence] is not expressible in the [Toolchain]'s own [Detectors], its entry MAY be sourced from wherever it is enabled"; what "enabled" refers to                                                                                                                                                                                                                                                                                     | 5       | no                  |

Notes, not passages: readers 2, 3 and 4 remark under question 3 that the detector specification
was not supplied; none of those remarks is under question 4. Reader 5's reference to "the
section 2 table" as a whole names no row of it.

## Findings and where they lie

- **Finding A, passage 1, clause 4.2 first paragraph** (readers 1, 3 and 5): the diff rewrites
  this paragraph, adding the sentences on [Blocking] [Rules] and rewrapping the sentence reader 3
  quotes. Text the change wrote or altered. Blocks.
- **Finding B, passage 2, section 1 "How to read this document" paragraph** (readers 4 and 5,
  reader 5 counted by the open-point rule, point 1 below): the diff adds "apart from clause 4.1,
  which holds each [Detector] to the [detector specification](DETECTOR-SPEC.md) and summarises
  that document's MUSTs" to this paragraph. Text the change wrote or altered. Blocks.
- **Finding C, passage 3, clause 6.2 heading** (readers 3 and 4): unchanged by the diff, and each
  reader sets it only against clause 6.2's fourth paragraph, also unchanged. Elsewhere: to be
  recorded in `acceptance/ROUTED.md` and routed; does not block.
- **Finding D, passage 4, clause 6.2 fourth paragraph** (readers 3 and 4): unchanged by the diff,
  and set only against clause 6.2's heading. Elsewhere: to be recorded in `acceptance/ROUTED.md`
  and routed; does not block.

Passages 5 to 17 are each named by one reader: recorded, not findings.

## Points the rules did not settle

1. **Reader 5's description of section 1's "How to read" paragraph.** Reader 5 gives no clause
   number for it, describing it as where "the document says" the section 2 table "is how terms
   are defined for grading"; the nearest text is "The table in section 2 glosses every term it
   borrows" in that paragraph, with section 2's opening paragraph the other candidate. Whether
   that names the paragraph was marked by the open-point rule: counted. Finding B rests on it;
   finding A, and so the verdict, does not.
2. **Remarks on another document not supplied, given as passages.** Reader 4's remarks on clauses
   4.4 and 4.5 and reader 5's on clause 4.2 each quote a passage with its clause number, but turn
   in part on the detector or method specification not being supplied, which the Marking section
   calls a note. Marked by the open-point rule: counted as passages. Finding A stands on readers 1
   and 3 without reader 5; finding B rests on reader 4's clause 4.4 remark being counted.
3. **Reader 1's 2c answer, "two grades if it ships an artefact".** The Marking section gives a
   rule for a grade on a stated condition only under question 3. The question's company ships
   the package, so read for its sense the answer states two for the case asked about, and its
   quotation of clause 9.1 states element (2). Marked for the reader under the open-point rule:
   correct. No other mark turns on it.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 9907492, named before the readers started. The process files at
645d811 are identical to those at 9907492.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: two (findings A
  and B). Not met.
- Passages named by two or more readers elsewhere: two (findings C and D), for
  `acceptance/ROUTED.md`; they do not block.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on findings A and B; every keyed item passed.

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
