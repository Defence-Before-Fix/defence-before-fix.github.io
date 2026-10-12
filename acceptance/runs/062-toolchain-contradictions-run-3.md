# Run 62: TOOLING-SPEC.md, toolchain contradictions, third run

- **Document**: TOOLING-SPEC.md
- **Pull request**: [25](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25), opened later from branch
  `editor/toolchain-contradictions`. The readers read commit 352cfcc. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 58 in clauses 4.1, 4.2, 8.1, 9 and 9.1.
- **Run within the pull request**: 3 (runs 57 and 58 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `7ceebd159dd90a77d1844c6f31d01d93fce2e3e6e38bf33e68f53044056c74aa`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at 352cfcc, each after one
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

Grades given, for the items the key accepts more than one: 5.1 Partial (1, 4), No (2), Yes
(3, 5); 6.1 Yes (1, 4, 5), Partial (2, 3), each Partial mentioning that no location is given for
calibrations or conventions; 6.2 No (all five), each mentioning that nothing rejects a generic
justification. Every reader graded 4.3 Yes, noting that the fixture names no route beyond the
ignore comment. Reader 2 states that it assumed the two undocumented rules are Blocking; the
key reads a 4.2 No on that condition as a No, and the reader's other grades do not turn on it.

Question 1: correct bullets per reader 6, 5, 4, 5 and 4 (reader 1: section 1's governing
principle; 4.1; 4.2; 4.3; 4.4 with 4.5; 5.1 to 5.2 with 6.2 and 6.3. Reader 3: 4.1; 4.2; 4.3 with
4.5; 5.1, 5.2, 6.2 and 6.3. Reader 5: 4.1; 4.2; 4.3 with 4.5; 5.1 to 5.3 with 6.1 and 6.2). No
bullet asserts anything the key marks wrong. The first bullet of readers 2 to 5 (the toolchain
judged as one assembled whole) states how conformance is measured, which the key counts neither
way. Bullets on neither list are listed under the points the rules did not settle.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through", which states element (2); for 2b all five quote section 9's "The project-level
verdict is a single grade; ..."; for 2c all five quote clause 9.1's "The two verdicts MUST be
graded and declared separately, and neither implies the other." Reader 1 states element (2) of
2c only in that quotation, which the Marking section counts as stated.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says section 7 is not met or there is no
agent summary (all five); S8 says Zigpipe ships no tooling (all five; readers 2, 3, 4 and 5 also
place section 8 on zig-qa's own artefact grade, reader 5 answering "No, not to Zigpipe's project
grade"); Decl says the declaration is optional, or that the verdict rests on the exercise (all
five).

### Misses

None. No answer matches a wrong reading the key names: reader 3's 4.1 reasoning says Lintomatic
"meets most of the detector specification" but grades No.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..352cfcc adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                                                    | Readers    | Changed by the diff |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------- |
| 1   | Clause 4.2, first paragraph: "a [Blocking] [Rule] the [Toolchain] runs whose documentation is missing is not yet a \[Defence\]: that [Rule] is the failure this clause names, not a [Rule] outside its reach" (2, 3, 4, 5; 5 adds "and the clause reaches every [Blocking] [Rule] the [Toolchain] runs"); whether the clause's scope is set by "its [Defences]" or by every Blocking rule | 2, 3, 4, 5 | yes                 |
| 2   | Section 2 terminology table, [Defence] row: "section 2 defines a defence as a rule with its documentation" (3), "section 2 defines a Defence as having documentation" (5), each set against clause 4.2's first paragraph                                                                                                                                                                  | 3, 5       | no                  |
| 3   | Clause 4.3, first paragraph: "Irreducible cases MUST be directed to the [Project record], where clause 6.2 requires a justification", "irreducible" not defined                                                                                                                                                                                                                           | 1          | yes                 |
| 4   | Section 2 terminology, [Project record] entry: "[Calibrations], [Exceptions] and conventions", set against clause 6.1                                                                                                                                                                                                                                                                     | 2          | no                  |
| 5   | Clause 6.1, first paragraph: "The [Toolchain] MUST define where the [Project record] lives and MUST load it", whether one location for all three kinds or only for exceptions                                                                                                                                                                                                             | 2          | no                  |
| 6   | Clause 5.1, first paragraph: "every [Defence]", set against clause 4.2's first paragraph                                                                                                                                                                                                                                                                                                  | 3          | no                  |
| 7   | Clause 6.2 heading: "reject a generic one"                                                                                                                                                                                                                                                                                                                                                | 4          | no                  |
| 8   | Clause 6.2, last paragraph: "name the [Hazard] being accepted and the scope", the documented check of phrases, "cannot verify truth"; whether the check is the phrase list, a check that hazard and scope are named, or both                                                                                                                                                              | 4          | no                  |
| 9   | Clause 4.4, first paragraph: "so that clause 4.3 of the [detector specification] holds through the wrapping", set against section 1's "How to read" paragraph                                                                                                                                                                                                                             | 5          | no                  |
| 10  | Section 1, "How to read this document" paragraph: "self-contained for grading a [Toolchain], apart from clause 4.1", set against clause 4.4                                                                                                                                                                                                                                               | 5          | yes                 |

Notes, not passages: reader 1 (question 3 preamble) and reader 4 (4.1 reasoning) remark that
the detector specification was not supplied; neither is under question 4.

## Findings and where they lie

- **Finding A, passage 1, clause 4.2 first paragraph** (readers 2, 3, 4 and 5): the sentences
  named were added by the change. Text the change wrote. Blocks.
- **Finding B, passage 2, section 2 [Defence] row** (readers 3 and 5): the row is unchanged, but
  both readers naming it set it against clause 4.2's first paragraph, which the change altered.
  Blocks.

Passages 3 to 10 are each named by one reader: recorded, not findings. Nothing is routed to
`acceptance/ROUTED.md` from this run.

## Points the rules did not settle

1. **Question 1 bullets on neither of the key's lists**: reader 3's sixth ("Agent-context
   summary and automatic delivery are recommended (SHOULD)", with "a shipped artefact has a
   separate grade with a self-audit") and reader 5's sixth ("partial conformance must not be
   called conformance", with the single grade and the separate artefact grade). The SHOULD half
   of reader 3's bullet and the section 9 partial-conformance MUST in reader 5's are on neither
   list; the rest of each states how conformance is measured, which the key counts neither way.
   Marked by the rule for a bullet on neither list: not counted either way. Readers 3 and 5 each
   have four correct bullets without them, so no mark turns on it. For the key to settle.
2. **Passage 2**: readers 3 and 5 identify the [Defence] row by a section number and a
   description, inside their remark on clause 4.2, not as a passage named on its own. Whether
   that names the row was marked by the open-point rule: counted. Finding B rests on it; finding
   A, and so the verdict, does not.
3. **Reader 4's 6.2 remark** names the heading and the last paragraph, each a paragraph of its
   own, and **reader 2's 6.1 remark** names clause 6.1 and the [Project record] entry; each is
   recorded as two passages. No other reader names any of them, so no finding turns on it.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit e6bdf40, named before the readers started.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: two (findings A
  and B). Not met.
- Passages named by two or more readers elsewhere: none.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on findings A and B alone; every keyed item passed.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125960137); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125959666); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125960585).
