# Run 85: TOOLING-SPEC.md, toolchain contradictions, thirteenth run

- **Document**: TOOLING-SPEC.md
- **Pull request**: not yet opened at the time of the run; it is to be opened from branch
  `editor/toolchain-contradictions`. The readers read commit 58924a8. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 84: clause 4.1's first paragraph now has one test, every MUST of the detector
  specification's sections 4 to 7, with the restated sentences as where a grader looks first and
  not the whole test, a grader without that document checking only them and saying so; section
  1's "How to read this document" says the same; section 2's closing paragraph says in plain
  sentences that clause 5.1 does not require an undocumented blocking rule to be listed and that
  clauses 4.2 and 8.1 reach it.
- **Run within the pull request**: 13 (runs 57, 58, 62, 65, 67, 68, 72, 76, 81, 82, 83 and 84
  came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `6d37cc625287ae0258a845657c48a96b7a53c698d998d6cde43c5c9e064a53ea`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at 58924a8, each after one
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

Grades given, for the items the key accepts more than one: 5.1 Yes (all five; readers 4 and 5
add that the two `(none)` rules are not Defences under section 2 and so outside 5.1); 6.1
Partial (readers 1 and 5, each mentioning that the Project record also holds calibrations and
conventions and the fixture gives no location for those, which meets the key's condition) and
Yes (readers 2, 3 and 4); 6.2 No (all five), each mentioning that nothing rejects a generic
justification or generic phrases. All five grade 4.1 No on the two undocumented bundled rules
with nothing supplied for them, each saying the detector specification was not supplied and
only the restated points were checked, which the key's 4.1 row accepts. All five grade 4.2 No;
readers 1, 2, 3 and 5 state that they read the two rules as Blocking because `zig-qa run` stops
when Lintomatic fails, which the key's 4.2 row reads as a No, and reader 4 states they are
Blocking for the same reason.

Question 1: correct clauses named per reader within the first six bullets. Reader 1: 4.1 with
4.2; 4.3 with 4.4 and 4.5; 5.1 to 5.3; 6.1 to 6.3. Reader 2: 4.1; 4.2; 4.3 with 6.1 and 6.2;
4.4 and 4.5; 5.1, 5.2 and 6.3. Reader 3: 4.1 with 4.2; 4.3 with 4.4 and 4.5; 5.1 to 5.3; 6.1 to
6.3. Reader 4: the governing principle with 4.1 and 4.2; 4.3 with 4.5; 5.1 to 5.3 with 6.3; 6.1
and 6.2. Reader 5: 4.1; 4.2; 4.3 with 6.2; 5.1, 5.2, 6.1 and 6.3; 4.4 and 4.5. Four or more
correct bullets each. No bullet asserts anything the key marks wrong. Every reader's first
bullet (the toolchain judged as one assembled whole), the remarks that section 7 or clause 6.4
is a SHOULD or recommended (readers 1, 2, 3 and 5), that a declaration is optional or not a
condition (readers 1, 3 and 4), and that a shipped artefact gets its own grade (readers 1, 3, 4
and 5) are counted neither way, as the key says.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through"; for 2b all five quote section 9's "The project-level verdict is a single grade; ...";
for 2c all five quote clause 9.1's "The two verdicts MUST be graded and declared separately, and
neither implies the other." No answer gives a grade per part, or a single grade for 2c.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says the toolchain does not conform at
all, or that there is no summary, or both (all five); S8 says Zigpipe ships no tooling to other
projects (all five); Decl says the declaration is optional, or that the verdict rests on the
exercise of the clauses (all five).

### Misses

None. No answer matches a wrong reading the key names.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..58924a8 (9e914fe
being the merge base with `next`) adds, rewords, moves or deletes a sentence in the paragraph,
changes a word, term or link in it, or parts it from what it refers to.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                | Readers | Changed by the diff                                                       |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------- |
| 1   | Section 2, closing paragraph: "Clauses 4.2 and 8.1 reach every [Blocking] [Rule] a [Toolchain] runs, documented or not" (3, 5, each set against passage 2); "a [Blocking] [Rule] whose documentation is missing is not yet a [Defence]. Clause 5.1 does not require it to be listed, because that clause lists [Defences]" (4, set against passage 3) | 3, 4, 5 | yes: added by the diff, and reworded in the revision after run 84         |
| 2   | Clause 8.1, first paragraph: "A third-party [Detector]'s native catalogue, which the [Toolchain] orchestrates without claiming as its own, is outside this audit", set against passage 1                                                                                                                                                              | 3, 5    | yes: the diff rewords a sentence in the paragraph; set against passage 1  |
| 3   | Section 2, the Defence row of the table: "A [Rule] with its documentation, in force and [Blocking]", set against passage 1                                                                                                                                                                                                                            | 4       | the row's words unchanged (the table is realigned); set against passage 1 |
| 4   | Clause 6.2, first paragraph: "It MUST NOT supply a default" (1, set against passage 5; 2, quoting the whole sentence, set against passage 6)                                                                                                                                                                                                          | 1, 2    | no                                                                        |
| 5   | Clause 6.4 heading: "The toolchain SHOULD state its own defaults for anything the method leaves to the project"                                                                                                                                                                                                                                       | 1       | no                                                                        |
| 6   | Clause 6.4, first paragraph: "a documented [Toolchain] default is what the [Practitioner] falls back to"                                                                                                                                                                                                                                              | 2       | no                                                                        |
| 7   | Section 3, the Identifier resolution row: "clause 4.2 here for the rest", set against passage 8                                                                                                                                                                                                                                                       | 2       | no in itself; set against passage 8, which the diff wrote                 |
| 8   | Clause 4.2, first paragraph: "every [Blocking] [Rule] the [Toolchain] runs, the project's own and the bundled alike", set against passage 7                                                                                                                                                                                                           | 2       | yes: added by the diff                                                    |
| 9   | Clause 6.2, last paragraph: "That check cannot verify truth, and a [Toolchain]'s [Conformance] MUST NOT be read as having verified it" (what "it" refers to) and "MUST reject a justification that could be pasted onto any [Exception] unchanged, by a check it documents" (whether the phrases are examples or the full set)                        | 4       | no                                                                        |

Notes, not passages: none under question 4. Under question 3, every reader remarks that the
detector specification was not supplied; those remarks are not question 4 answers and are not
marked as passages. Passages 4, 5 and 6 are three paragraphs (a heading is a paragraph of its
own), so readers 1 and 2 name the same passage only in passage 4.

## Findings and where they lie

- **Finding A, passage 1, section 2 closing paragraph** (readers 3, 4 and 5): the diff adds the
  paragraph and the revision after run 84 rewrote it. Text the change wrote or altered. Blocks.
  Readers 3 and 5 read its claim that clause 8.1 reaches every Blocking Rule a Toolchain runs as
  contradicting clause 8.1's exclusion of a third-party Detector's native catalogue.
- **Finding B, passage 2, clause 8.1 first paragraph** (readers 3 and 5): the diff rewords the
  sentence on what the check covers ("as its own, whatever kind of [Detector] carries it, and a
  missing page is what the check exists to find"), and both readers set the paragraph against
  passage 1, which the diff wrote. Text the change wrote or altered. Blocks.
- **Finding C, passage 4, clause 6.2 first paragraph** (readers 1 and 2): unchanged by the diff,
  not parted from anything it refers to, and each reader sets it only against unchanged text
  (reader 1 against the clause 6.4 heading, reader 2 against clause 6.4's first paragraph).
  Elsewhere: a finding against the document, to be recorded in `acceptance/ROUTED.md`, where the
  open row from run 83 on this sentence against clause 6.4's defaults is the same passage;
  routed, and does not block. The marker writes only this record; the ROUTED entry is for the
  editor.

Passages 3 and 5 to 9 are each named by one reader: recorded, not findings, applied at the
editor's discretion.

## Points the rules did not settle

1. **Whether reader 4's third item names passage 1 as confusing**, since the reader says it read
   the paragraph and the Defence row as consistent after checking both. Judgement: the Marking
   section defines naming by quotation or by a clause number with an identifying description,
   not by what the reader calls confusing, so it is named. The verdict does not turn on it:
   readers 3 and 5 alone make passage 1 a finding.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 852dcd8, named before the readers started. The process files at
58924a8 (`ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md`, `tools/changes.py`, `spec-qa.py` and the CI workflows) are identical to those
at 852dcd8.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
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

Posted on the pull request: LINK TO BE ADDED.
