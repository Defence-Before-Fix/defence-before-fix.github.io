# Run 81: TOOLING-SPEC.md, toolchain contradictions, ninth run

- **Document**: TOOLING-SPEC.md
- **Pull request**: not yet opened at the time of the run; it is to be opened from branch
  `editor/toolchain-contradictions`. The readers read commit 0373a27. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 76: clause 4.1's first paragraph and section 1's "How to read this document"
  now give one test, a grader checks the restated sentences and takes a verdict already given on
  the detector under the detector specification as settled; and the paragraph on a blocking rule
  whose documentation is missing, which sat under section 2's table and parted "These are
  additional." from it, now ends section 2 after the Project record entry.
- **Run within the pull request**: 9 (runs 57, 58, 62, 65, 67, 68, 72 and 76 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `09c3a3ba5bcd441d513797fcd973e2d0873473ca867aa774ff94643902147e6d`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at 0373a27, each after one
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

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 4.4 | 4.5 | 5.1 | 5.2 | 5.3 | 6.1 | 6.2 | 6.3  | S9  | AS  | S8  | Decl |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | ---- |
| 1      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok   |
| 2      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | miss | ok  | ok  | ok  | ok   |
| 3      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok   |
| 4      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok   |
| 5      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok   |

Grades given, for the items the key accepts more than one: 5.1 Yes (all five); 6.1 Partial
(readers 1, 2 and 5, each mentioning that the fixture names a place for exceptions and none for
calibrations or conventions) and Yes (readers 3 and 4); 6.2 No (all five), each mentioning that
nothing rejects generic text. Readers 1, 2, 3, 4 and 5 grade 4.2 No reading the two undocumented
rules as Blocking, which the key's 4.2 row reads as a No. All five grade 4.3 Yes on the one route
the fixture describes, which the key's 4.3 row says is the case the fixture presents. Readers 3,
4 and 5 give their 6.1 grade with a remark on what it would be in another case; see the points
below.

Question 1: correct clauses named per reader, distinct within the key's list: reader 1, 4.1;
4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3 with 6.1 to 6.3. Reader 2: 4.1; 4.2; 4.3; 5.1 to 5.3 with
6.1 and 6.2; 4.5. Reader 3: 4.1 with 4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3; 6.1 to 6.3. Reader 4:
4.1; 4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3 with 6.1 to 6.3. Reader 5: 4.1; 4.2 with 4.3; 4.4 and
4.5; 5.1 to 5.3 with 6.1 and 6.3; 6.2 with 8.1 and 8.2. No bullet asserts anything the key marks
wrong. Every reader's first bullet (the toolchain judged as one assembled whole) and reader 2's
remark that section 7 is SHOULDs and the declaration optional are counted neither way, as the
key says.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through"; for 2b all five quote section 9's "The project-level verdict is a single grade; ...";
for 2c all five quote clause 9.1's "The two verdicts MUST be graded and declared separately, and
neither implies the other." No answer gives a grade per part or a single grade for 2c.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says there is no agent summary (all
five), readers 3, 4 and 5 adding that the toolchain does not conform at all; S8 says Zigpipe
ships no tooling (all five), reader 1 adding that zig-qa's own artefact grade is not described
and giving no verdict on it; Decl says the declaration is optional and the verdict rests on the
exercise (all five).

### Misses

- **Reader 2, 6.3, Partial.** The key accepts Yes only. Reasoning: `zig-qa list --exceptions`
  lists exceptions in the rule listing's format, but calibrations and conventions are not
  described as enumerable, "so the same gap as 6.1 applies". The reasoning quotes nothing of the
  document; it carries over the reader's 6.1 reading of section 2's Project record entry. The key
  names no wrong reading for 6.3, so this is the reader's single miss on the item, tolerated by
  the threshold.

No answer matches a wrong reading the key names.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..0373a27 (9e914fe
being the merge base with `next`) adds, rewords, moves or deletes a sentence in the paragraph,
changes a word, term or link in it, or parts it from what it refers to.

| #   | Passage (clause, words or description)                                                                                                                                                                                      | Readers    | Changed by the diff                                                                                          |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------ |
| 1   | Clause 5.1, first paragraph: "every [Defence] active in the project" with "The listing covers every [Blocking] [Rule] the [Toolchain] runs, documented or not"; a listing of Defences that covers what is not a Defence     | 1, 5       | yes: the second sentence quoted is added by the diff                                                         |
| 2   | Clause 6.1, first paragraph: "The [Toolchain] MUST define where the [Project record] lives and MUST load it"; one location for the whole record or one per kind                                                             | 1, 2, 3, 4 | no                                                                                                           |
| 3   | Section 2, the Project record entry: "[Calibrations], [Exceptions] and conventions" (1, 3), the whole entry quoted (2, 4), set against passage 2                                                                            | 1, 2, 3, 4 | no: its words are unchanged; the diff inserts a paragraph after it, but it refers to nothing that follows it |
| 4   | Clauses 6.2 and 6.3, described as speaking only of exceptions, set against passage 3                                                                                                                                        | 1, 2       | no; whether this names a passage is open, see below                                                          |
| 5   | Section 2, the Defence row: "A [Rule] with its documentation, in force and [Blocking]", set against passage 1                                                                                                               | 1          | no: the diff re-pads the table for an added row; the row's words are unchanged                               |
| 6   | Section 2, the paragraph "A [Blocking] [Rule] whose documentation is missing is not yet a [Defence]", set against passage 1                                                                                                 | 5          | yes: added by the diff                                                                                       |
| 7   | Clause 5.3, first paragraph: "Every [Defence] the project has written itself MUST appear in the listing clause 5.1 requires, meeting its content requirements in full"; what the content requirements are                   | 2          | no                                                                                                           |
| 8   | Clause 4.1, first paragraph: "takes a verdict already given on the [Detector] under that document as settled"; whether to grade the detector itself or only the restated sentences, with no verdict given                   | 3          | yes: rewritten by the diff                                                                                   |
| 9   | Clause 9.2, first paragraph: "A project or a shipped artefact MAY declare" followed by "A project that ships an artefact carries both levels of clause 9.1 in that declaration"; an obligation inside an optional provision | 3          | no                                                                                                           |

Passage 8 is a passage and not a note: reader 3 says it was given no verdict on Lintomatic, but
its confusion is what the sentence asks a grader to do, not that another document was missing.
Reader 3 cites the next paragraph of 9.2 as confirming the declaration optional, which does not
set passage 9 against it.

Notes, not passages: under question 3, readers 1 and 5 remark that the detector specification
was not supplied or not seen in full, and readers 2 and 4 that the fixture gives no verdict on
Lintomatic under it.

## Findings and where they lie

- **Finding A, passage 1, clause 5.1 first paragraph** (readers 1 and 5): the diff adds the
  sentence "The listing covers every [Blocking] [Rule] the [Toolchain] runs, documented or not,
  and a [Rule] whose route to documentation is missing is listed with that gap showing." Reader 5
  also sets the paragraph against section 2's added paragraph (passage 6). Text the change wrote
  or altered. Blocks.
- **Finding B, passages 2 and 3, clause 6.1 first paragraph against section 2's Project record
  entry** (readers 1, 2, 3 and 4): both paragraphs unchanged, and no reader naming them sets
  either against a changed paragraph. Elsewhere: a finding against the document, recorded in
  `acceptance/ROUTED.md` (its 6.1 row, raised by run 76, gains run 81), routed to a change of its
  own, and does not block. The marker writes only this record; the ROUTED entry is for the
  editor.
- **Finding C, passage 4, clauses 6.2 and 6.3** (readers 1 and 2), counted as named under the
  open-point rule (below): unchanged, and set against the unchanged Project record entry.
  Elsewhere: routed to `acceptance/ROUTED.md` with finding B, whose passage it belongs to; does
  not block.

Passages 5 to 9 are each named by one reader: recorded, not findings, applied at the editor's
discretion.

## Points the rules did not settle

1. **6.1 grades given with a remark on another case.** Reader 3 gives "Yes, with a caveat", that
   it would be Partial if calibrations or conventions are recorded elsewhere and never read;
   reader 4 gives Yes and says it would be Partial if those belong to the project record; reader
   5 gives Partial and says it becomes Yes if the project has neither. The Marking section reads
   a grade given on a stated condition as the grade for the case the fixture presents only where
   the key says which case that is, and the key's 6.1 row does not say it in those terms.
   Judgement: each reader states one grade outright and the remark names what it would be in a
   different case, so the stated grade is the grade; each is one the key accepts, and readers 1,
   2 and 5's Partial meets the key's condition. Had the remark made the grade conditional, the
   open-point rule marks it for the reader. Marked for the readers.
2. **Whether passage 4 is named.** Readers 1 and 2 say clauses 6.1 to 6.3, or 6.2 and 6.3,
   "mention only exceptions" or "speak only of exceptions", which describes the clauses and
   identifies no one sentence or paragraph. The open-point rule counts the passage; it lies in
   unchanged text and does not affect the verdict.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 389ef3f, named before the readers started. The process files at
0373a27 (`ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md`, `tools/changes.py`, `spec-qa.py` and the CI workflows) are identical to those
at 389ef3f.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item but 6.3,
  where four of five. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: one (finding A).
  Not met.
- Passages named by two or more readers elsewhere: findings B and C, routed to
  `acceptance/ROUTED.md`; do not block.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on finding A; every keyed item passed.

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
