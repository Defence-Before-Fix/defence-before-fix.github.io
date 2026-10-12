# Run 58: TOOLING-SPEC.md, toolchain contradictions, second run

- **Document**: TOOLING-SPEC.md
- **Pull request**: not yet opened at the time of the run; it is to be opened from branch
  `editor/toolchain-contradictions`. The readers read commit 90a9936. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 57 in section 1 and clauses 4.1, 4.2, 4.3, 8.1, 9 and 9.1.
- **Run within the pull request**: 2 (run 57 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `43a220ebce6d3db005704ef829656671ecded332c3f3daf275b73db8abf0b825`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at 90a9936, each after one
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

Grades given, for the items the key accepts more than one: 5.1 Partial (1, 2, 4, 5), No (3);
6.1 Yes (all five); 6.2 No (all five), each mentioning that nothing rejects a generic
justification. Every reader graded 4.3 Yes; readers 1 to 5 each noted that the fixture names no
route beyond the ignore comment.

Question 1: correct bullets per reader 5, 5, 5, 5 and 5 (reader 1: 4.1; 4.2; 4.3; 5.1 to 5.3
with 4.5; 6.1 to 6.3). No bullet asserts anything the key marks wrong. Bullets on neither list
are listed under the points the rules did not settle.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through", which states element (2); for 2b all five quote section 9's "The project-level
verdict is a single grade; ..."; for 2c all five quote clause 9.1's "The two verdicts MUST be
graded and declared separately, and neither implies the other."

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says there is no agent summary (all
five); S8 says Zigpipe ships no tooling (all five; reader 5 answers "No, to Zigpipe's project
grade" and places section 8 on zig-qa's artefact grade); Decl says the declaration is optional
(all five).

### Misses

None. No answer matches a wrong reading the key names: reader 5's 4.1 reasoning says Lintomatic
"meets most of the detector specification" but grades No.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..90a9936 adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                 | Readers    | Changed by the diff |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------- |
| 1   | Clause 4.2, first paragraph: "Here [Defence] reaches every [Blocking] [Rule] the [Toolchain] runs, bundled or the project's own, whether or not its documentation exists"                                                                                              | 1, 3, 4, 5 | yes                 |
| 2   | Section 2 terminology table, [Defence] row: "A [Rule] with its documentation, in force and [Blocking]", set against clause 4.2's first paragraph                                                                                                                       | 1, 3, 4, 5 | no                  |
| 3   | Clause 4.1, first paragraph: "the six summarised here are the ones most often failed" (3, set against the Why paragraph's "six clauses of the method"); "That document's MUSTs are those of its sections 4 to 7, and every one of them applies; ... rests on them" (4) | 3, 4       | yes                 |
| 4   | Section 9, first paragraph: "The project-level verdict is a single grade" (1, set against the clause 9.1 heading); "every MUST in section 8 bears on its artefact grade under clause 9.1, not on this one", what "this one" refers to (2)                              | 1, 2       | yes                 |
| 5   | Clause 5.1, first paragraph: listing "every [Defence] active", set against clause 4.2 and the [Defence] row                                                                                                                                                            | 1          | no                  |
| 6   | Clause 9.1 heading: "has two levels of conformance", set against section 9's first paragraph                                                                                                                                                                           | 1          | no                  |
| 7   | Clause 4.1, point 2: "whether or not a clause below names the same gap again"                                                                                                                                                                                          | 1          | yes                 |
| 8   | Clause 8.2, last paragraph: "has no release and no [Consuming project], so this section does not bear on its [Conformance]"                                                                                                                                            | 2          | no                  |
| 9   | Clause 4.1, Why paragraph: "the six clauses of the method are carried out in a [Detector]"                                                                                                                                                                             | 3          | no                  |
| 10  | Clause 6.2, last paragraph: "The [Toolchain] MUST reject a justification that could be pasted onto any [Exception] unchanged, by a check it documents", against the requirement to name hazard and scope                                                               | 3          | no                  |
| 11  | Section 2 terminology, [Bundled defence] entry: "one with its documentation"                                                                                                                                                                                           | 4          | no                  |
| 12  | Clause 8.1 heading: "if a bundled defence lacks resolvable documentation"                                                                                                                                                                                              | 4          | no                  |
| 13  | Clause 5.3, second paragraph: "its entry MAY be sourced from wherever it is enabled", what "its entry" refers to                                                                                                                                                       | 4          | no                  |
| 14  | Section 9, second paragraph: "does each thing section 7 recommends", which document's section 7                                                                                                                                                                        | 5          | yes                 |
| 15  | Clause 9.1, first paragraph: "section 7 of the method specification", set against section 9's second paragraph                                                                                                                                                         | 5          | yes                 |
| 16  | Clause 6.4: a SHOULD, and whether an unmet 6.4 affects any grade                                                                                                                                                                                                       | 5          | no                  |

## Findings and where they lie

- **Finding A, passage 1, clause 4.2 first paragraph** (readers 1, 3, 4 and 5): the sentence
  named was added by the change. Text the change wrote. Blocks.
- **Finding B, passage 2, section 2 [Defence] row** (readers 1, 3, 4 and 5): the row is
  unchanged, but every reader naming it sets it against clause 4.2's first paragraph, which the
  change altered. Blocks.
- **Finding C, passage 3, clause 4.1 first paragraph** (readers 3 and 4): the change rewrote the
  sentences both readers quote. Text the change wrote. Blocks.
- **Finding D, passage 4, section 9 first paragraph** (readers 1 and 2): the change reworded the
  paragraph's first sentence, which reader 2 quotes; reader 1 quotes its unchanged second
  sentence, which lies in the same paragraph. Text the change altered. Blocks.

Passages 5 to 16 are each named by one reader: recorded, not findings. Nothing is routed to
`acceptance/ROUTED.md` from this run.

## Points the rules did not settle

1. **Question 1 bullets on neither of the key's lists**: reader 1's first and reader 3's first
   (the toolchain is judged as one assembled whole), reader 4's first ("must provide every
   mechanism the method needs", the governing principle of section 1), reader 2's sixth and
   reader 3's sixth (a shipped artefact graded separately, clause 9.1). Marked by the rule for a
   bullet on neither list: not counted either way. Every reader has five correct bullets
   without them, so no mark turns on it. For the key to settle.
2. **Reader 1's passage 5** gives clause 5.1 with the three-word quotation "every [Defence]
   active"; **reader 5's passage 16** gives clause 6.4 with a description ("It is a SHOULD")
   that identifies its heading rather than a quoted sentence. Whether each names a passage was
   marked by the open-point rule: counted. Each is named by one reader only, so neither makes a
   finding either way.
3. **Reader 1's passage 4** quotes section 9's second sentence, which the change did not reword,
   in a paragraph whose first sentence it did. The rule places a finding by paragraph, so the
   paragraph is the change's; had it been open, the open-point rule would have treated it as the
   change's own text in any case.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit c31d49a, named before the readers started.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: four (findings A to
  D). Not met.
- Passages named by two or more readers elsewhere: none.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on findings A to D alone; every keyed item passed.

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
