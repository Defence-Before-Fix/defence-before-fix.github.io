# Run 65: TOOLING-SPEC.md, toolchain contradictions, fourth run

- **Document**: TOOLING-SPEC.md
- **Pull request**: [25](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25), opened later from branch
  `editor/toolchain-contradictions`. The readers read commit dfd4b4d. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 62 in clause 4.2's heading and first paragraph.
- **Run within the pull request**: 4 (runs 57, 58 and 62 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `1186cb6938da03e55dfbec783676bac2414b667e1005d7cf831a67424e0ed90e`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at dfd4b4d, each after one
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

Grades given, for the items the key accepts more than one: 5.1 Yes (all five); 6.1 Yes (1, 4,
5), Partial (2, 3), each Partial mentioning that no location is given for calibrations or
conventions; 6.2 No (all five), each mentioning that nothing rejects generic text or a generic
justification. Reader 1 grades 6.1 Yes and adds that it would be Partial if calibrations and
conventions have no location; the grade in its table is Yes, and Yes and Partial are both
accepted. Readers 2 and 3 note that the fixture does not say the two undocumented rules are
Blocking; both grade 4.2 No, which the key accepts with no condition.

Question 1: correct bullets per reader 6, 5, 4, 5 and 6 (reader 1: section 1's governing
principle; 4.1; 4.2; 4.3; 4.5 with 4.4; 5.1 to 5.3 with 6.1 to 6.3. Reader 2: 4.1; 4.2; 4.3;
4.4 and 4.5 with 5.1 to 5.3; 6.1 to 6.3. Reader 3: 4.1; 4.2; 4.3 with 4.5; 5.1 to 5.3 with 6.1
to 6.3. Reader 4: 4.1; 4.2; 4.3 with 6.2; 4.5; 5.1, 5.2, 6.1 and 6.3. Reader 5: 4.1; 4.2; 4.3;
4.4; 4.5; sections 5 and 6). Reader 5's fourth and fifth bullets name different clauses of one
line of the key's list and each count. No bullet asserts anything the key marks wrong. The
first bullet of readers 2, 3 and 4 (the toolchain judged as one assembled whole) and reader 3's
sixth (one project grade, a separate artefact grade, the agent summary a SHOULD) state how
conformance is measured or call section 7 a SHOULD, which the key counts neither way; so does
reader 4's sixth, in calling the agent summary and the self-audit "SHOULD or conditional". A
bullet on neither list is listed under the points the rules did not settle.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through", which states element (2); for 2b all five quote section 9's "The project-level
verdict is a single grade; ..."; for 2c all five quote clause 9.1's "The two verdicts MUST be
graded and declared separately, and neither implies the other." No answer gives a grade per
part or a single grade for 2c.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says section 7 is not met or there is no
agent summary, and that the toolchain does not conform (all five); S8 says Zigpipe ships no
tooling (all five, each also placing zig-qa's grade on its own artefact); Decl says the
declaration is optional and the verdict rests on the exercise (all five).

### Misses

None. No answer matches a wrong reading the key names.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..dfd4b4d adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                | Readers | Changed by the diff |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------- |
| 1   | Clause 4.2, first paragraph: "a [Blocking] [Rule] whose documentation is missing is not yet a [Defence]" (2, 4, 5); the clause covers Blocking rules that by the definition are not Defences (2); whether clause 5.1 then covers an undocumented blocking rule (4, 5) | 2, 4, 5 | yes                 |
| 2   | Section 2 terminology table, [Defence] row: "A [Rule] with its documentation, in force and [Blocking]", each set against clause 4.2's first paragraph                                                                                                                 | 2, 4, 5 | no                  |
| 3   | Clause 5.1, first paragraph: "every [Defence] active in the project" (5), "clause 5.1's listing obligation" (4), each set against clause 4.2's first paragraph                                                                                                        | 4, 5    | no                  |
| 4   | Clause 9.1, first paragraph: "graded against this document and section 7 of the method specification" (1, 3); which section 7 governs the project grade, set against section 1's "How to read" paragraph and section 9 (1) or section 9's first paragraph (3)         | 1, 3    | yes                 |
| 5   | Clause 4.2 heading: "[Blocking] [Rules] it routes" (2), given with the clause number inside its remark on the first paragraph                                                                                                                                         | 2       | yes                 |
| 6   | Section 1, "How to read this document" paragraph: self-contained "apart from 4.1", set against clause 9.1                                                                                                                                                             | 1       | yes                 |
| 7   | Section 9, agent-support paragraph: "section 7 of this document", set against clause 9.1                                                                                                                                                                              | 1       | yes                 |
| 8   | Section 9, first paragraph: "defines the project grade by sections 4 to 6 of this document", set against clause 9.1                                                                                                                                                   | 3       | yes                 |
| 9   | Clause 4.3, first paragraph: "A route bypasses the [Project record] when a finding can be silenced through it without an entry appearing in the [Project record]"; whether disabling an active rule in configuration is a route                                       | 1       | yes                 |
| 10  | Section 2 terminology, [Project record] entry: "[Calibrations], [Exceptions] and conventions", set against clause 6.1                                                                                                                                                 | 3       | no                  |
| 11  | Clause 6.1, first paragraph: "The [Toolchain] MUST define where the [Project record] lives and MUST load it"; whether the location covers all three kinds of judgement or only exceptions                                                                             | 3       | no                  |
| 12  | Clause 4.1, point 2, paragraph after the table: "exercised as its clause 8.1 describes"; the reader could not follow the reference to the detector specification                                                                                                      | 4       | yes                 |
| 13  | Clause 4.5, first paragraph: "MUST stop the levels below it from being treated as meaningful"; the direction of "below"                                                                                                                                               | 4       | no                  |

Notes, not passages: every reader remarks under question 3 that the detector specification, the
method specification or both were not supplied; none of those remarks is under question 4.

## Findings and where they lie

- **Finding A, passage 1, clause 4.2 first paragraph** (readers 2, 4 and 5): the sentence named
  was added by the change. Text the change wrote. Blocks.
- **Finding B, passage 2, section 2 [Defence] row** (readers 2, 4 and 5): the row is unchanged,
  but every reader naming it sets it against clause 4.2's first paragraph, which the change
  altered. Blocks.
- **Finding C, passage 3, clause 5.1 first paragraph** (readers 4 and 5): the paragraph is
  unchanged, but both readers set it against clause 4.2's first paragraph. Blocks.
- **Finding D, passage 4, clause 9.1 first paragraph** (readers 1 and 3): the sentence quoted is
  unchanged, but the change rewords and adds sentences in the same paragraph, and both readers
  set it against section 9 or section 1's "How to read" paragraph, which the change also altered.
  Text the change altered. Blocks.

Passages 5 to 13 are each named by one reader: recorded, not findings. Nothing is routed to
`acceptance/ROUTED.md` from this run.

## Points the rules did not settle

1. **A question 1 bullet on neither of the key's lists**: reader 3's sixth bullet says "default
   values are SHOULDs", which is clause 6.4 and on neither list. Marked by the rule for a bullet
   on neither list: not counted either way. Reader 3 has four correct bullets without it, so no
   mark turns on it. For the key to settle.
2. **Passages set against another and named by description**: reader 4 identifies clause 5.1 as
   "clause 5.1's listing obligation", and reader 3 identifies section 9's first paragraph by a
   description, each inside a remark on another passage. Whether that names the paragraph was
   marked by the open-point rule: counted. Finding C rests on reader 4's being counted; findings
   A, B and D, and so the verdict, do not.
3. **Reader 2's short quotation "[Blocking] [Rules] it routes"** matches no run of the body and
   is nearest the clause 4.2 heading. Whether it names the heading was marked by the open-point
   rule: counted, as passage 5. No other reader names the heading, so no finding turns on it.
4. **Reader 4's remark on "exercised as its clause 8.1 describes"** quotes a passage with its
   clause number, but its substance is that the detector specification was not supplied, which
   the Marking section calls a note. Marked by the open-point rule: counted as a passage. Named
   by reader 4 alone, so no finding turns on it.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 4081aa4, named before the readers started.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: four (findings A,
  B, C and D). Not met.
- Passages named by two or more readers elsewhere: none.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on findings A, B, C and D; every keyed item passed.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125961653); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125961175); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125962019).
