# Run 83: TOOLING-SPEC.md, toolchain contradictions, eleventh run

- **Document**: TOOLING-SPEC.md
- **Pull request**: [25](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25), opened later from branch
  `editor/toolchain-contradictions`. The readers read commit c770722. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 82: clause 5.1 says nothing of undocumented rules any more; the paragraph on
  a blocking rule whose documentation is missing now ends section 2, after the paragraph on the
  distinction between a bundled defence and a project's own, and opens "Throughout this
  document"; clause 4.1 and section 1 name the verdict a grader takes as one the detector already
  holds under the detector specification's section 8, and clause 4.1 says that without one the
  restated sentences are the test.
- **Run within the pull request**: 11 (runs 57, 58, 62, 65, 67, 68, 72, 76, 81 and 82 came
  before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `1f981586432ce938dba63935e5be59cd7e1b36b1569fedc019b576877b34c06d`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at c770722, each after one
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

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3  | 4.4 | 4.5 | 5.1 | 5.2 | 5.3 | 6.1 | 6.2 | 6.3 | S9  | AS  | S8  | Decl |
| ------ | ------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| 1      | correct | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 2      | correct | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 3      | correct | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 4      | correct | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |
| 5      | correct | ok  | ok  | ok  | ok  | ok  | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   |

Grades given, for the items the key accepts more than one: 5.1 Yes (readers 1, 3 and 4) and
Partial (readers 2 and 5); 6.1 Partial (readers 1, 3, 4 and 5, each mentioning that the fixture
names a place for exceptions and none for calibrations or conventions) and Yes (reader 2); 6.2
No (all five), each mentioning that nothing rejects a generic justification or generic text.
All five grade 4.1 No on the table's "Nothing for those two" row, and 4.2 No reading the two
undocumented rules as Blocking because `zig-qa run` stops when Lintomatic fails, which the key's
4.2 row reads as a No. Readers 3 and 4 give 5.1 Yes because section 2 says the two undocumented
rules are not yet Defences; readers 2 and 5 give Partial on the `(none)` routes. The key accepts
all three grades with no condition.

Question 1: correct clauses named per reader within the first six bullets. Reader 1: 4.1 with
4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3 with 6.3; 6.1 and 6.2. Reader 2: 4.1; 4.2 with 4.3; 4.4 and
4.5; 5.1 to 5.3 with 6.3; 6.1 and 6.2. Reader 3: 4.1 with 4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3
with 6.1 to 6.3; 8.1 and 8.2. Reader 4: 4.1; 4.2; 4.3; 4.5 with 5.1 to 5.3; 6.1 and 6.2.
Reader 5: 4.1 with 4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3 with 6.3; 6.1 and 6.2. No bullet asserts
anything the key marks wrong. Every reader's first bullet (the toolchain judged as one assembled
whole), reader 3's remark that agent-facing summaries are SHOULDs, and reader 5's remark that a
shipped artefact gets a separate grade with section 8 applying only to it are counted neither
way, as the key says.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through"; for 2b all five quote section 9's "The project-level verdict is a single grade; ...";
for 2c all five quote clause 9.1's "The two verdicts MUST be graded and declared separately, and
neither implies the other." No answer gives a grade per part or a single grade for 2c. Reader 2's
2b adds that a second grade arises only for a shipped artefact and Zigpipe ships none; it asserts
nothing the key marks wrong.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says the toolchain does not conform at
all and there is no agent summary (all five); S8 says Zigpipe ships no tooling to other projects
(all five); Decl says the declaration is optional and the verdict rests on the exercise or the
evidence (all five).

### Misses

- **Reader 5, clause 4.3: Partial** (key accepts Yes). Reasoning: the inline route is closed by
  `ignore_comments = false` and exceptions go to `quality-exceptions.toml`, but the fixture does
  not say whether Lintomatic has any other route, such as a silent baseline, so the reader cannot
  confirm the clause covers every route. The grade is stated outright, not on a condition. The
  reasoning quotes neither the document nor any sentence of clause 4.3; it is a reading of the
  fixture's silence. The key names no wrong reading for 4.3, so this is a single miss on the item,
  tolerated by the threshold (four of five correct).

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..c770722 (9e914fe
being the merge base with `next`) adds, rewords, moves or deletes a sentence in the paragraph,
changes a word, term or link in it, or parts it from what it refers to.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                   | Readers | Changed by the diff                                                       |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------- |
| 1   | Section 2, closing paragraph: "Throughout this document, a [Blocking] [Rule] whose documentation is missing is not yet a [Defence]. ..." (5 quotes it whole; 1 and 4 quote "a [Blocking] [Rule] whose documentation is missing is not yet a [Defence]"); each sets it against clause 5.1, whether undocumented blocking rules are listed | 1, 4, 5 | yes: added by the diff                                                    |
| 2   | Clause 5.1, first paragraph: "The [Toolchain] MUST list every [Defence] active in the project" (4, 5), and "every [Defence]" with clause number 5.1 and its listing requirement (1); set against passage 1                                                                                                                               | 1, 4, 5 | no in itself; each reader sets it against passage 1, which the diff added |
| 3   | Clause 6.2, first paragraph: "It MUST NOT supply a default, and MUST reject an [Exception] that omits one"; set against clause 6.4's defaults, whether a justification is a delegated judgement a default may fill                                                                                                                       | 2, 3    | no; nor is either 6.4 paragraph the readers set it against                |
| 4   | Clause 4.1, first paragraph: "Where it has not, the sentences that follow are the test" against "this clause holds the [Detector] to every one of them"; whether the restated sentences are the full test or a sample                                                                                                                    | 1       | yes: rewritten by the diff                                                |
| 5   | Clause 6.2, last paragraph: "could be pasted onto any [Exception] unchanged, by a check it documents: 'needed for now', 'legacy', 'TODO' and their like"; which test the check applies                                                                                                                                                   | 1       | no                                                                        |
| 6   | Clause 6.4, first paragraph: "Where the method specification delegates a judgement and the project has recorded nothing, a documented [Toolchain] default is what the [Practitioner] falls back to"                                                                                                                                      | 2       | no                                                                        |
| 7   | Clause 6.4 heading: "The [Toolchain] SHOULD state its own defaults for anything the method leaves to the project"                                                                                                                                                                                                                        | 3       | no                                                                        |
| 8   | Clause 9.1, first paragraph: "The two verdicts MUST be graded and declared separately", set against 9.2's optional declaration                                                                                                                                                                                                           | 3       | yes: the diff rewords sentences in the paragraph                          |
| 9   | Clause 9.2, third paragraph: "The declaration is optional", set against passage 8                                                                                                                                                                                                                                                        | 3       | yes: the diff extends the sentence quoted                                 |
| 10  | Section 2, the Consuming project entry: "A codebase that installs a [Detector] or a [Toolchain] shipped by somebody else", with the Bundled defence entry named by its term; whether the `zq.*` rules are bundled defences                                                                                                               | 4       | no                                                                        |
| 11  | Clause 6.1 heading: "MUST define a location for the project record", set against section 2's Project record entry; one location for all three kinds or not                                                                                                                                                                               | 4       | no                                                                        |

Passages 6 and 7 are different paragraphs: the Marking section makes a heading a paragraph of its
own, so readers 2 and 3 do not name the same 6.4 passage. Passages 3 and 5 are different
paragraphs of 6.2.

Notes, not passages: under question 3, readers 1, 3 and 5 remark that the detector specification
was not supplied and that they graded 4.1 (and, for reader 5, 4.4) on the restated sentences.

## Findings and where they lie

- **Finding A, passage 1, section 2 closing paragraph** (readers 1, 4 and 5): the diff adds the
  paragraph. Text the change wrote or altered. Blocks.
- **Finding B, passage 2, clause 5.1 first paragraph** (readers 1, 4 and 5): the paragraph is
  unchanged by the diff, but every reader naming it sets it against passage 1, which the diff
  added: whether a Blocking Rule that section 2 says is "not yet a [Defence]" falls within the
  duty to list "every [Defence] active in the project". A paragraph a reader naming the finding
  sets against a changed paragraph is the change's own text under the Marking section. Blocks.
- **Finding C, passage 3, clause 6.2 first paragraph** (readers 2 and 3): unchanged, and both
  readers set it against clause 6.4 (reader 2 its first paragraph, reader 3 its heading), also
  unchanged. Elsewhere: a finding against the document, to be recorded in `acceptance/ROUTED.md`,
  where no open row covers the default of 6.2 against the defaults of 6.4; routed to a change of
  its own, and does not block. The marker writes only this record; the ROUTED entry is for the
  editor.

Passages 4 to 11 are each named by one reader: recorded, not findings, applied at the editor's
discretion.

## Points the rules did not settle

1. **Whether reader 4 names the Bundled defence entry.** Reader 4 quotes the Consuming project
   entry and names "Bundled defence" only by its term in its item heading. Judgement: the term is
   a description that identifies the entry, so it is named; had it stayed open, the open-point
   rule counts the passage. No other reader names that entry, so it makes no finding either way.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit ae6faf2, named before the readers started. The process files at
c770722 (`ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md`, `tools/changes.py`, `spec-qa.py` and the CI workflows) are identical to those
at ae6faf2.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item but 4.3,
  where four of five are correct. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: two (findings A
  and B). Not met.
- Passages named by two or more readers elsewhere: finding C, routed to `acceptance/ROUTED.md`;
  does not block.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on findings A and B; every keyed item passed its threshold.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125970205); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125969785); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125970613).
