# Run 72: TOOLING-SPEC.md, toolchain contradictions, seventh run

- **Document**: TOOLING-SPEC.md
- **Pull request**: not yet opened at the time of the run; it is to be opened from branch
  `editor/toolchain-contradictions`. The readers read commit cb9b4e5. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 68 in clause 4.2 (which now states only what it requires, with no sentence on
  defences and no list of mechanisms), clause 4.1's first paragraph and section 1's "How to read
  this document".
- **Run within the pull request**: 7 (runs 57, 58, 62, 65, 67 and 68 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `6c9683df16a39ddd12169c438fe1f9c8a32050bd5346a81de4edb1c0d6990472`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at cb9b4e5, each after one
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

Grades given, for the items the key accepts more than one: 5.1 Partial (1, 2), Yes (3, 4, 5);
6.1 Partial (1, 5), Yes (2, 3, 4), each Partial mentioning that the fixture gives no location for
calibrations or conventions; 6.2 No (all five), each mentioning that nothing rejects generic
text or a generic justification. Readers 1, 2, 3 and 4 note that the fixture does not say the
two undocumented rules are Blocking and grade 4.2 No on that assumption or inference, which the
key reads as a No. Readers 1, 4 and 5 grade 4.3 Yes on what the fixture writes, reader 1 by
assuming Lintomatic has no other route; see the points the rules did not settle.

Question 1: correct bullets per reader 6, 5, 5, 6 and 5 (reader 1: 4.1; 4.2; 4.3; 4.5 with 4.4;
5.1 to 5.3 with 6.1 to 6.3; 8.1 and 8.2. Readers 2, 3 and 5: 4.1; 4.2; 4.3 with 4.5; 5.1 to 5.3;
6.1 to 6.3. Reader 4: the governing principle; 4.1; 4.2; 4.3 with 4.5 and 4.4; 5.1 to 5.3; 6.1
to 6.3). No bullet asserts anything the key marks wrong. The first bullets of readers 2, 3 and 5
(the toolchain judged as one assembled whole) and the first sentence of reader 1's sixth (the
project level and a shipped artefact graded separately) state how conformance is measured, which
the key counts neither way.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through", which states element (2); for 2b all five quote section 9's "The project-level
verdict is a single grade; ..."; for 2c all five quote clause 9.1's "The two verdicts MUST be
graded and declared separately, and neither implies the other." No answer gives a grade per
part or a single grade for 2c. Readers 2 and 4 add to 2b that Zigpipe, shipping nothing, has
only the one grade, which the key does not mark wrong.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says the toolchain does not conform
and that there is no agent summary (all five); S8 says Zigpipe ships no tooling (all five,
readers 1, 2, 4 and 5 also placing zig-qa's grade on its own artefact); Decl says the
declaration is optional and the verdict rests on the exercise (all five).

### Misses

None. No answer matches a wrong reading the key names.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..cb9b4e5 adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                | Readers    | Changed by the diff |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------- |
| 1   | Section 2 terminology table, [Defence] row: "A [Rule] with its documentation, in force and [Blocking]", whether the two undocumented rules are Defences; set against clause 4.2's first paragraph (1) and clause 5.1 (1, 2, 3, 4)                                                                                     | 1, 2, 3, 4 | no                  |
| 2   | Clause 5.1, first paragraph: "every [Defence] active in the project" (1, 3, 4), "MUST provide the route to each one's full documentation" (2); set against the Defence row (1, 2, 3, 4) and, by reader 1, against clause 4.2's first paragraph, asking which of 4.2 and 5.1 governs the undocumented rules            | 1, 2, 3, 4 | no                  |
| 3   | Section 1, "How to read this document": "A [Toolchain] can be graded from this document alone", set against clause 4.1's first paragraph                                                                                                                                                                              | 2, 3       | yes                 |
| 4   | Clause 4.1, first paragraph: "that fails any one of that document's MUSTs, restated here or not, fails this clause" (2, 3) and "MUSTs are those of its sections 4 to 7" (2), set against section 1's "graded from this document alone"                                                                                | 2, 3       | yes                 |
| 5   | Clause 4.2, first paragraph: "every [Identifier] its [Blocking] [Rules] print", set against the Defence row and clause 5.1                                                                                                                                                                                            | 1          | yes                 |
| 6   | Clause 9.2, first paragraph: "A project or a shipped artefact MAY declare" against "A project that ships an artefact carries both levels of clause 9.1 in that declaration", read as unconditional                                                                                                                    | 1          | no                  |
| 7   | Clause 6.2, first paragraph: "MUST NOT supply a default", set against the clause 6.4 heading                                                                                                                                                                                                                          | 3          | no                  |
| 8   | Clause 6.4 heading: "SHOULD state its own defaults for anything the method leaves to the project", set against clause 6.2's first paragraph                                                                                                                                                                           | 3          | no                  |
| 9   | Clause 6.2, fourth paragraph: "The justification MUST name the [Hazard] being accepted and the scope of the [Exception]. The [Toolchain] MUST reject a justification that could be pasted onto any [Exception] unchanged, by a check it documents", whether the check must test hazard and scope or only generic text | 4          | no                  |
| 10  | Clause 5.3, second paragraph: "Where such a [Defence] is not expressible in the [Toolchain]'s own [Detectors], its entry MAY be sourced from wherever it is enabled, provided the listing stays derived under clause 5.2 rather than hand-maintained", what "wherever it is enabled" covers                           | 5          | no                  |

Notes, not passages: readers 2, 3 and 5 remark under question 3 that the detector specification
was not supplied; none of those remarks is under question 4. The section 2 table was realigned
by the diff for the Remediation docs row; the Defence row's words, terms and links are
unchanged, so passage 1 is marked unchanged.

## Findings and where they lie

- **Finding A, passage 1, section 2 Defence row** (readers 1, 2, 3 and 4): unchanged, but
  reader 1 sets it against clause 4.2's first paragraph, which the diff rewrote. Text the change
  wrote or altered, under the Marking section's rule on a paragraph a reader sets against one.
  Blocks.
- **Finding B, passage 2, clause 5.1 first paragraph** (readers 1, 2, 3 and 4): unchanged, but
  reader 1 sets it against clause 4.2's first paragraph, asking which of the two governs the
  undocumented rules. Text the change wrote or altered, as for finding A. Blocks.
- **Finding C, passage 3, section 1 "How to read this document"** (readers 2 and 3): the diff
  rewrites the paragraph's opening, adding "A [Toolchain] can be graded from this document
  alone". Text the change wrote or altered. Blocks.
- **Finding D, passage 4, clause 4.1 first paragraph** (readers 2 and 3): the diff rewrites the
  paragraph, adding "That document's MUSTs are those of its sections 4 to 7" and "restated here
  or not". Text the change wrote or altered. Blocks.

Passages 5 to 10 are each named by one reader: recorded, not findings. Passages 7 and 9 both lie
in clause 6.2 but in different paragraphs, so they are not the same passage. No finding lies
elsewhere, so nothing from this run goes to `acceptance/ROUTED.md`.

## Points the rules did not settle

1. **Clause 4.3 graded Yes on a stated assumption.** Reader 1 grades 4.3 Yes and says the
   fixture does not say whether Lintomatic offers any other suppression route, "so this verdict
   assumes it does not"; readers 4 and 5 say their Yes holds "only for what is written". The
   Marking section reads a grade given on a stated condition as the grade for the case the
   fixture presents only where the key says which case that is, and the key's 4.3 row does not
   say whether Lintomatic's only route is the ignore comment. Marked for the reader under the
   open-point rule: correct. Had the three been marked unanswered, 4.3 would have failed the
   all-but-one threshold; the verdict below does not turn on it, since the run fails on the
   findings. For the editor to settle in the key before the next run of this pull request.
2. **Readers 2 and 3 on section 1 against clause 4.1.** Each turns on grading 4.1 without the
   detector specification, which the Marking section calls a note when the remark is not about a
   passage. Both quote section 1's and clause 4.1's sentences and ask how they fit together,
   which is a remark about those passages, so the marker counts them as passages; were that in
   doubt, the open-point rule counts the passage. Findings C and D rest on it; findings A and B,
   and so the verdict, do not.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit bc6ae14, named before the readers started. The process files at
cb9b4e5 (`ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md`, `tools/changes.py`, `spec-qa.py` and the CI workflow) are identical to those
at bc6ae14.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: four (findings A
  to D). Not met.
- Passages named by two or more readers elsewhere: none.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on findings A to D; every keyed item passed.

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
