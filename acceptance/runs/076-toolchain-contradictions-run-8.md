# Run 76: TOOLING-SPEC.md, toolchain contradictions, eighth run

- **Document**: TOOLING-SPEC.md
- **Pull request**: [25](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25), opened later from branch
  `editor/toolchain-contradictions`. The readers read commit fa79f8a. Change: section 9 against
  clause 9.1 on section 8; clauses 4.2 and 8.1 on a blocking rule whose documentation is missing;
  clause 9.2's gap duty against the optional declaration; clause 4.3's heading against its body;
  clause 4.1's count of the detector specification's MUSTs and its point 2 on what is judged.
  Revised after run 72: section 2 gains a paragraph under its table saying a blocking rule whose
  documentation is missing is not yet a defence and is what clauses 4.2, 5.1 and 8.1 exist to
  catch; clause 5.1 says the listing covers every blocking rule, documented or not, with a
  missing route showing; section 1's "How to read this document" and clause 4.1's first
  paragraph both say a verdict from this document alone rests on what is restated and a grader
  with the detector specification holds the detector to all of it. The key's 4.3 row now says
  which case the fixture presents.
- **Run within the pull request**: 8 (runs 57, 58, 62, 65, 67, 68 and 72 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `18f9a24ca270450e83434b252e766ca54bcc6fa744f855bcc76bc0c59613fe3a`) is
  `QUESTIONS.md`, `TOOLING-SPEC.md` and `fixtures/zigpipe.md` at fa79f8a, each after one
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

Grades given, for the items the key accepts more than one: 5.1 Yes (all five); 6.1 Yes (all
five); 6.2 No (all five), each mentioning that nothing rejects generic text. Readers 1, 3, 4 and
5 note that the fixture does not say the two undocumented rules are Blocking and grade 4.2 No on
that assumption, which the key's 4.2 row reads as a No. Readers 1, 2, 3, 4 and 5 grade 4.3 Yes
on the suppression route the fixture describes, several saying the fixture is silent on other
routes; the key's 4.3 row says the fixture presents one route, the ignore comment, so under the
Marking section a grade on that condition is the grade for this case.

Question 1: correct clauses named per reader, distinct within the key's list: reader 1, the
governing principle; 4.1; 4.2; 4.3, 4.4 and 4.5; 5.1 to 5.3 with 6.1 to 6.3; section 8 as
shipped toolchains' self-audit duties. Readers 2 and 3: 4.1; 4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3
with 6.1 to 6.3. Reader 4: 4.2; 4.3; 4.4 and 4.5; 5.1 to 5.3; 6.1 to 6.3. Reader 5: 4.1 and
4.2; 4.3 with 6.2; 4.4 and 4.5; 5.1 to 5.3 with 6.1 and 6.3. No bullet asserts anything the key
marks wrong. Every reader's first bullet (the toolchain judged as one assembled whole), reader
1's two levels of grading, reader 5's single project-level grade, and the remarks that section 7
is recommended or a SHOULD (readers 1, 2, 3, 5) and that section 8 applies only to shipped
artefacts (reader 5) are counted neither way, as the key says.

Question 2: every reader states both required elements of each item and quotes the document.
For 2a all five quote section 1, "It is whatever the project assembles to run its checks
through"; for 2b all five quote section 9's "The project-level verdict is a single grade; ...";
for 2c all five quote clause 9.1's "The two verdicts MUST be graded and declared separately, and
neither implies the other." No answer gives a grade per part or a single grade for 2c. Reader 2
adds to 2b that a second grade exists only where the project ships something, and reader 5 that
a failure in any part a clause touches fails that clause for the whole; the key marks neither
wrong.

Question 3: the four answers are given by every reader as the key accepts, with reasons meeting
its conditions: S9 names 4.1, 4.2 and 6.2 (all five); AS says there is no agent summary (all
five), readers 3, 4 and 5 adding that the toolchain does not conform at all; S8 says Zigpipe
ships no tooling (all five), readers 2, 3, 4 and 5 placing section 8 on zig-qa's own artefact
grade; Decl says the declaration is optional and the verdict rests on the exercise (all five).

### Misses

None. No answer matches a wrong reading the key names.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..fa79f8a (9e914fe
being the merge base with `next`) adds, rewords, moves or deletes a sentence in the paragraph,
or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                                                                 | Readers       | Changed by the diff |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ------------------- |
| 1   | Clause 4.1, first paragraph: "The sentences that follow restate the ones most often failed, and a verdict from this document alone rests on them; a grader with that document to hand holds the [Detector] to every one of its MUSTs, restated here or not" (1, 2, 4, 5), and "rests on them" beside "holds the [Detector] to every one of them" (3); which governs without the detector specification | 1, 2, 3, 4, 5 | yes                 |
| 2   | Section 2, the paragraph "These are additional.", after the terminology table and before the added term entries: what it is additional to                                                                                                                                                                                                                                                              | 2, 5          | open; see below     |
| 3   | Clause 6.1, first paragraph: "The [Toolchain] MUST define where the [Project record] lives and MUST load it", set against section 2's Project record entry ("[Calibrations], [Exceptions] and conventions"): one location for the whole record or one per kind                                                                                                                                         | 3, 4          | no                  |
| 4   | Section 1, "How to read this document": "The table in section 2 glosses every term it borrows", where Suppression, Baseline, Agent, Conform, Warning and Fixture are not in the table                                                                                                                                                                                                                  | 1             | yes                 |
| 5   | Clause 4.3, first paragraph: "Irreducible cases MUST be directed to the [Project record], where clause 6.2 requires a justification": what "directed" requires of a toolchain                                                                                                                                                                                                                          | 3             | yes                 |

Notes, not passages: readers 1, 3 and 4 remark under question 3 that the detector specification
was not supplied. Readers 1 to 5 tie the same remark to passage 1 under question 4, where it is
part of naming that passage.

## Findings and where they lie

- **Finding A, passage 1, clause 4.1 first paragraph** (all five readers): the diff rewrites the
  paragraph, adding "That document's MUSTs are those of its sections 4 to 7", "a verdict from
  this document alone rests on them" and "restated here or not". Text the change wrote or
  altered. Blocks.
- **Finding B, passage 2, section 2 "These are additional."** (readers 2 and 5): the paragraph's
  own words are unchanged, but the diff inserts the new paragraph "A [Blocking] [Rule] whose
  documentation is missing is not yet a [Defence]. ..." between the terminology table and it, so
  that it no longer follows the table it refers to. Whether that is text the change wrote or
  altered is an open point (below); marked as the change's own text. Blocks.
- **Finding C, passage 3, clause 6.1 first paragraph** (readers 3 and 4): unchanged, and set
  against section 2's Project record entry, which is also unchanged. Elsewhere: recorded in
  `acceptance/ROUTED.md` as a finding against the document, routed to a change of its own, and
  does not block. The marker writes only this record; the ROUTED row is for the editor to add.

Passages 4 and 5 are each named by one reader, in paragraphs the diff changed: recorded, not
findings, applied at the editor's discretion.

## Points the rules did not settle

1. **Where finding B lies.** The Marking section counts a paragraph as the change's when the
   diff adds, rewords, moves or deletes a sentence in it, or changes a word, term or link, or
   when a reader sets it against such a paragraph. The diff does none of those to "These are
   additional." itself; it inserts a paragraph immediately before it, between it and the table
   whose terms it says the following entries are additional to. Reader 2 places it by "It
   follows the terminology table", reader 5 by "after the terminology table and before the new
   term definitions"; neither names the inserted paragraph. Whether a paragraph displaced from
   its referent by an insertion has been moved, or is set against the inserted paragraph by a
   reader who is confused by what it refers to, the rules do not say. The open-point rule treats
   a finding whose location is open as the change's own text, so it is marked as blocking.
   Run 72's ten passages did not include it, which is consistent with the insertion being its
   cause. For the editor to settle in `ACCEPTANCE.md`, if it needs settling, before the next run
   of this pull request.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 13b497b, named before the readers started. The process files at
fa79f8a (`ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md`, `tools/changes.py`, `spec-qa.py` and the CI workflows) are identical to those
at 13b497b.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: two (findings A
  and B). Not met.
- Passages named by two or more readers elsewhere: one (finding C), routed to
  `acceptance/ROUTED.md`; does not block.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on findings A and B; every keyed item passed.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125966495); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125966048); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/25#issuecomment-6125966891).
