# Run 86: TOOLING-SPEC.md, toolchain contradictions, fourteenth run

- **Document**: TOOLING-SPEC.md
- **Pull request**: not yet opened at the time of the run; it is to be opened from branch
  `editor/toolchain-contradictions`. The readers read commit 6da7409. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 85 in section 2's closing paragraph alone: it now names clause 4.2 alone as
  the clause that reaches every blocking rule a toolchain runs, documented or not; clause 8.1 is
  no longer named there.
- **Run within the pull request**: 14 (runs 57, 58, 62, 65, 67, 68, 72, 76, 81, 82, 83, 84 and
  85 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `60c864ced29d5011fb73ca0f35139b8bfcc146303dd001952fb43a99bcaa910e`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at 6da7409, each after one
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
| 2      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok   |
| 3      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok   |
| 4      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | miss | ok  | ok  | ok  | ok   |
| 5      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok   |

Grades given, for the items the key accepts more than one: 5.1 Yes (all five; readers 2 and 3
add that the two `(none)` rules are not Defences under section 2 and so outside 5.1); 6.1
Partial (readers 1, 4 and 5, each mentioning that the Project record also holds calibrations and
conventions and the fixture gives no location for those, which meets the key's condition;
reader 5 adds that it would be Yes if the record is read as exceptions only, and the Partial is
the grade it gives for the case) and Yes (readers 2 and 3); 6.2 No (all five), each mentioning
that nothing rejects a generic justification or generic phrasing. All five grade 4.1 No on the
two undocumented bundled rules with nothing supplied for them; readers 2, 3, 4 and 5 say the
detector specification was not supplied and only the restated points were checked, which the
key's 4.1 row accepts. All five grade 4.2 No; readers 1, 4 and 5 state that they read the two
rules as Blocking because they are enabled or because `zig-qa run` stops when Lintomatic fails,
which the key's 4.2 row reads as a No.

Question 1: correct clauses named per reader within the first six bullets. Reader 1: 4.1 with
4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3; 6.1 to 6.3 (five bullets; its first bullet is not needed for
the count and is not decided). Reader 2: 4.1; 4.2; 4.3 with 6.1 and 6.2; 5.1, 5.2, 6.3 and 4.5.
Reader 3: 4.4 and 4.5; 4.1; 4.2; 4.3 with 6.1; 6.2; 5.1 to 5.3 with 6.3. Reader 4: 4.1; 4.2; 4.3
with 4.5; 5.1 to 5.3 with 6.3; 6.1 and 6.2. Reader 5: 4.1; 4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3
with 6.3; 6.1 and 6.2. Four or more correct bullets each. No bullet asserts anything the key
marks wrong. The first bullets of readers 2 and 4 (the toolchain judged as one assembled
whole), the remarks that section 7 or the defaults are SHOULDs (readers 2, 4 and 5), that a
declaration is optional (reader 2) and that a shipping project has two levels (reader 2) are
counted neither way, as the key says.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through"; for 2b all five quote section 9's "The project-level verdict is a single grade; ...";
for 2c all five quote clause 9.1's "The two verdicts MUST be graded and declared separately, and
neither implies the other." No answer gives a grade per part, or a single grade for 2c.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says the toolchain does not conform at
all, or that there is no summary, or both (all five); S8 says Zigpipe ships no tooling to other
projects, and readers 4 and 5 add that section 8 bears on zig-qa's artefact grade (all five);
Decl says the declaration is optional, or that the verdict rests on the exercise of the clauses
(all five).

### Misses

- **Reader 4, clause 6.3: Partial.** The key accepts Yes only, with no condition. The reader
  grants that `zig-qa list --exceptions` lists exceptions in the same format as the rule listing,
  and grades Partial because calibrations and conventions are not described and so cannot be
  shown to be enumerable. The reasoning does not quote the document in that row; it rests on
  section 2's Project record entry, which the reader cites by section in its 6.1 row. It matches
  no wrong reading the key names. A single miss on the item, the reader's, tolerated by the
  threshold: four of five correct.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..6da7409 (9e914fe
being the merge base with `next`) adds, rewords, moves or deletes a sentence in the paragraph,
changes a word, term or link in it, or parts it from what it refers to.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                    | Readers | Changed by the diff                                                                               |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------- |
| 1   | Clause 6.1, first paragraph: "where the Project record lives" (1); "The [Toolchain] MUST define where the [Project record] lives and MUST load it. Not a documentation convention. A path the [Toolchain] loads." (5); each set against passage 2                                         | 1, 5    | no                                                                                                |
| 2   | Section 2, the Project record terminology entry: "Calibrations, Exceptions and conventions", given with "the definition in section 2" (1) and "Section 2 defines the project record as" (5); each set against passage 1                                                                   | 1, 5    | no; the paragraph the diff inserts in section 2 follows it and parts it from nothing it refers to |
| 3   | Clause 5.3, second paragraph: "its entry MAY be sourced from wherever it is enabled" (what "wherever" covers)                                                                                                                                                                             | 1       | no                                                                                                |
| 4   | Clause 4.5, first paragraph: "A [Blocking] failure at the [Detector] level MUST stop the levels below it from being treated as meaningful, in the order method section 5 states." (what the levels below a detector are)                                                                  | 2       | no                                                                                                |
| 5   | Clause 6.2, first paragraph: "It MUST NOT supply a default." (2, set against passage 6); "MUST NOT supply a default" (4, set against passage 6)                                                                                                                                           | 2, 4    | no                                                                                                |
| 6   | Clause 6.4: "6.4, which SHOULDs a documented toolchain default" (2, a description); "SHOULD state its own defaults for anything the method leaves to the project" (4, the heading's words)                                                                                                | 2, 4    | no                                                                                                |
| 7   | Clause 4.1, first paragraph: "The sentences that follow restate the ones most often failed, so that a grader knows where to look first; they are not the whole test, and a grader without that document to hand can check only them, and says so in the verdict." (set against passage 8) | 3       | yes: the diff wrote the sentence                                                                  |
| 8   | Clause 4.1, point 2: "does the [Detector] meet every MUST of sections 4 to 7 of the [detector specification], exercised as its clause 8.1 describes?" (set against passage 7)                                                                                                             | 3       | yes: the diff rewords sentences in point 2                                                        |

Notes, not passages: reader 2's first item quotes clause 4.1 point 2, "with the wrapping in
place, does the [Detector] meet every MUST of sections 4 to 7 ... exercised as its clause 8.1
describes?", and says only that it could not tell what the exercise is "because the detector
specification was not in what I was given". That is a remark that another document was not
supplied, which the Marking section's rule on question 4 records as a note and not a passage,
"however much of the document it quotes to locate the reference"; it is not counted with
reader 3's passage 8. Reader 2's second item also says method section 5 was not given, but
its remark that the clause does not define the levels below a detector is about the passage, so
passage 4 is counted. Under question 3, readers 2, 3, 4 and 5 remark that the detector
specification was not supplied; those are not question 4 answers.

## Findings and where they lie

- **Finding A, passage 1, clause 6.1 first paragraph** (readers 1 and 5): unchanged by the diff,
  not parted from anything it refers to, and each reader sets it only against passage 2, which
  is unchanged. Elsewhere: a finding against the document, recorded in `acceptance/ROUTED.md`,
  where the open row on clause 6.1's first paragraph against section 2's Project record entry is
  the same passage; routed, and does not block.
- **Finding B, passage 2, section 2's Project record entry** (readers 1 and 5): unchanged by the
  diff; the paragraph the diff inserts at the end of section 2 comes after the entry and the
  paragraph that follows it, and parts the entry from nothing it refers to; each reader sets it
  only against passage 1. Elsewhere: routed to `acceptance/ROUTED.md` with finding A, whose open
  row names both; does not block.
- **Finding C, passage 5, clause 6.2 first paragraph** (readers 2 and 4): unchanged by the diff,
  not parted from anything it refers to, each reader setting it only against clause 6.4, which
  is unchanged. Elsewhere: routed to `acceptance/ROUTED.md`, where the open row on this sentence
  against clause 6.4's defaults is the same passage; does not block.
- **Finding D, passage 6, clause 6.4** (readers 2 and 4, counted as the same passage under the
  open-point rule; see below): unchanged by the diff. Elsewhere: routed to
  `acceptance/ROUTED.md` with finding C; does not block.

The marker writes only this record; the ROUTED entries are for the editor. Passages 3, 4, 7 and
8 are each named by one reader: recorded, not findings, applied at the editor's discretion.
Passages 7 and 8 lie in text the change wrote, and are named by reader 3 alone.

## Points the rules did not settle

1. **Whether readers 2 and 4 name the same paragraph of clause 6.4.** Reader 4 quotes the
   heading's words; reader 2 describes 6.4 as one "which SHOULDs a documented toolchain
   default", which could identify the heading (its SHOULD) or the first paragraph ("a documented
   [Toolchain] default"), and a heading is a paragraph of its own. Marked in the direction the
   open-point rule gives: counted as the same passage, so finding D. The verdict does not turn on
   it, since the passage lies outside the change either way.

Considered and settled by a rule, so not open: reader 2's clause 4.1 item is a note under the
Marking section's question 4 rule, as above; and readers 1 and 5 each name both passage 1 and
passage 2, since each gives a clause or section number with words that identify each paragraph.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 568e323, named before the readers started. The process files at
6da7409 (`ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md`, `tools/changes.py`, `spec-qa.py` and the CI workflows and pull request
template under `.github/`) are identical to those at 568e323.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item but
  6.3, which is four of five. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: none. Met.
- Passages named by two or more readers elsewhere: findings A to D, routed to
  `acceptance/ROUTED.md`; do not block.

## Findings applied

None at the time of marking.

## Verdict

PASS. Every keyed item met its threshold, no miss matches a wrong reading the key names, and
no finding lies in text the change wrote or altered.

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
