# Run 84: TOOLING-SPEC.md, toolchain contradictions, twelfth run

- **Document**: TOOLING-SPEC.md
- **Pull request**: [25](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25), opened later from branch
  `editor/toolchain-contradictions`. The readers read commit c2e3249. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 83 in section 2's closing paragraph alone: it now says that nothing this
  document asks of defences, clause 5.1's listing included, is asked of a blocking rule whose
  documentation is missing, and that a toolchain running one has failed clause 4.2 whether or
  not its listing shows it.
- **Run within the pull request**: 12 (runs 57, 58, 62, 65, 67, 68, 72, 76, 81, 82 and 83 came
  before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `eb3d2cc18c08b54960dd96080fcac5066e04ef556aaa983194c13e79bef930dc`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at c2e3249, each after one
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

Grades given, for the items the key accepts more than one: 5.1 Yes (all five), each saying the
two `(none)` rules are not Defences under section 2 and so outside 5.1 (readers 3, 4 and 5 add
that clause 4.2 catches them); 6.1 Yes (readers 1, 2, 3 and 5) and Partial (reader 4, mentioning
that section 2's Project record also holds calibrations and conventions and the fixture does not
say where those are, which meets the key's condition); 6.2 No (all five), each mentioning that
nothing rejects a generic justification or generic text. All five grade 4.1 No on the two
undocumented bundled rules with nothing supplied for them, and 4.2 No; readers 2, 3, 4 and 5
read the two rules as Blocking because `zig-qa run` stops when Lintomatic fails, which the key's
4.2 row reads as a No, and reader 1 grades No outright.

Question 1: correct clauses named per reader within the first six bullets. Reader 1: 4.1 with
4.2; 4.3 with 4.5; 4.4; 5.1 to 5.3; 6.1 to 6.3. Reader 2: 4.1; 4.2; 4.3 with 6.2; 4.4 and 4.5;
5.1 to 5.3 with 6.3. Reader 3: 4.1 with 4.2; 4.3; 4.5; 5.1 to 5.3; 6.1 to 6.3. Reader 4: 4.1
with 4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3 with 6.3; 6.2. Reader 5: 4.1 with 4.2; 4.3 with 4.5; 4.4;
5.1 to 5.3 with 6.1 and 6.2; 6.3. Five correct bullets each. No bullet asserts anything the key
marks wrong. Every reader's first bullet (the toolchain judged as one assembled whole), reader
2's and reader 4's remarks that the agent summary is a SHOULD, reader 4's that a declaration is
optional, and readers 4's and 5's that a shipped artefact gets its own grade are counted neither
way, as the key says.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through"; for 2b all five quote section 9's "The project-level verdict is a single grade; ...";
for 2c all five quote clause 9.1's "The two verdicts MUST be graded and declared separately, and
neither implies the other." No answer gives a grade per part or a single grade for 2c.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says the toolchain does not conform at
all, or that there is no summary, or both (all five); S8 says Zigpipe ships no tooling to other
projects (all five); Decl says the declaration is optional, or that the verdict rests on the
exercise of the clauses (all five).

### Misses

None.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..c2e3249 (9e914fe
being the merge base with `next`) adds, rewords, moves or deletes a sentence in the paragraph,
changes a word, term or link in it, or parts it from what it refers to.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                               | Readers | Changed by the diff                                       |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | --------------------------------------------------------- |
| 1   | Clause 4.1, first paragraph: "Where it has not, the sentences that follow are the test" (2, 3), "A grader of this clause checks the sentences that follow" (3, 5), "this clause holds the [Detector] to every one of them" (3; 5 quotes "every one of them"); whether the restated sentences or every MUST of the detector specification is the test | 2, 3, 5 | yes: rewritten by the diff                                |
| 2   | Clause 4.1, point 2: "Does the [Detector] meet every MUST of sections 4 to 7 of the [detector specification](DETECTOR-SPEC.md), exercised as its clause 8.1 describes?" (2), "every MUST of sections 4 to 7 … exercised as its clause 8.1 describes" (5); set against passage 1                                                                      | 2, 5    | yes: the diff rewords sentences in the item               |
| 3   | Section 2, closing paragraph: "not yet a [Defence]" and "clause 5.1's listing included", with the paragraph identified by its opening words, set against clause 5.1 (3); "where they reach a [Toolchain]'s [Rules] they reach every [Blocking] [Rule] it runs, documented or not", which clauses "they" refers to (5)                                | 3, 5    | yes: added by the diff, and the revision after run 83     |
| 4   | Section 2, the Project record entry: described as listing the project-record judgements, exceptions among them, set against clauses 6.2 and 6.4 (1); "[Calibrations], [Exceptions] and conventions", set against clause 6.1 (4)                                                                                                                      | 1, 4    | no                                                        |
| 5   | Clause 6.2, first paragraph: "MUST NOT supply a default", set against clause 6.4                                                                                                                                                                                                                                                                     | 1       | no                                                        |
| 6   | Clause 6.4 heading: "SHOULD state its own defaults for anything the method leaves to the project"                                                                                                                                                                                                                                                    | 1       | no                                                        |
| 7   | Clause 5.1, first paragraph: "MUST list every [Defence] active", set against passage 3                                                                                                                                                                                                                                                               | 3       | no in itself; set against passage 3, which the diff added |
| 8   | Clause 4.3, first paragraph: "A route bypasses the [Project record] when a finding can be silenced through it without an entry appearing in the [Project record]"; whether disabling a whole rule in configuration is a suppression route                                                                                                            | 4       | yes: the diff adds a sentence to the paragraph            |
| 9   | Section 2, the Exception row of the table: "a recorded, justified decision to leave an [Instance] unfixed or a [Rule] unapplied", set against passage 8                                                                                                                                                                                              | 4       | no                                                        |
| 10  | Clause 6.1, first paragraph: "The [Toolchain] MUST define where the [Project record] lives and MUST load it"; one location for all three kinds or not                                                                                                                                                                                                | 4       | no                                                        |
| 11  | Clause 9.1, first paragraph: "MUST be graded and declared separately", set against passage 12                                                                                                                                                                                                                                                        | 5       | yes: the diff rewords sentences in the paragraph          |
| 12  | Clause 9.2, third paragraph: "The declaration is optional", set against passage 11                                                                                                                                                                                                                                                                   | 5       | yes: the diff extends the sentence quoted                 |

Notes, not passages: reader 4's third item, "exercised as its clause 8.1 describes" with clause
4.1, is a remark that the detector specification was not supplied, and so a note however much
of the document it quotes; under question 3, readers 1, 2, 3 and 4 remark the same of 4.1 or
4.4. Passages 5 and 6 are different paragraphs (a heading is a paragraph of its own).

## Findings and where they lie

- **Finding A, passage 1, clause 4.1 first paragraph** (readers 2, 3 and 5): the diff rewrites
  the paragraph. Text the change wrote or altered. Blocks.
- **Finding B, passage 2, clause 4.1 point 2** (readers 2 and 5): the diff rewords the item's
  sentences, and both readers set it against passage 1. Text the change wrote or altered. Blocks.
- **Finding C, passage 3, section 2 closing paragraph** (readers 3 and 5): the diff adds the
  paragraph, and its revision after run 83 is the only change since that run. Text the change
  wrote or altered. Blocks.
- **Finding D, passage 4, section 2's Project record entry** (readers 1 and 4): unchanged by the
  diff, not parted from anything it refers to, and each reader sets it only against unchanged
  paragraphs (reader 1 against 6.2 and 6.4, reader 4 against 6.1). Elsewhere: a finding against
  the document, to be recorded in `acceptance/ROUTED.md`, where the open rows from runs 76 and 81
  on clause 6.1 and on 6.2 and 6.3 against this entry are the nearest; routed, and does not
  block. The marker writes only this record; the ROUTED entry is for the editor.

Passages 5 to 12 are each named by one reader: recorded, not findings, applied at the editor's
discretion.

## Points the rules did not settle

1. **Whether a paragraph cited under question 4 as context is named.** Readers 1 and 4 name the
   Project record entry as what they set another clause against, not as itself confusing.
   Judgement: the Marking section defines naming by quotation or by a clause number with an
   identifying description, not by what the reader calls confusing, so it is named; had it
   stayed open, the open-point rule counts the passage. Either way finding D lies elsewhere and
   does not block.
2. **Whether reader 4 names clause 6.2 or 6.3** by "Clauses 6.2 and 6.3 speak only of
   exceptions". Judgement: not named, because the description identifies a clause and no
   sentence or paragraph within it, which the Marking section requires. Had it been counted, it
   would at most join passage 5 in a finding on unchanged text set against unchanged text, which
   is routed and does not block; the verdict is the same either way.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit a095fa7, named before the readers started. The process files at
c2e3249 (`ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md`, `tools/changes.py`, `spec-qa.py` and the CI workflows) are identical to those
at a095fa7.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: three (findings A,
  B and C). Not met.
- Passages named by two or more readers elsewhere: finding D, routed to `acceptance/ROUTED.md`;
  does not block.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on findings A, B and C; every keyed item passed its threshold.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125971464); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125971023); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125972035).
