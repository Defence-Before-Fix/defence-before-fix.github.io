# Run 55: TOOLING-SPEC.md, defined terms, eighth run

- **Document**: TOOLING-SPEC.md

- **Pull request**: [24](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24), opened later from branch `editor/defined-terms`. The
  readers were given 8e91f8a, the text returned to the original change (Harness renamed Rule
  harness; [Remediation] and [Remediation docs] linked). The text the change wrote or altered is
  `git diff 9e914fe 8e91f8a -- TOOLING-SPEC.md`, 9e914fe being the merge base with `next`: the
  section 2 table's [Rule harness] row; the section 3 table's red proof row and correct
  construction row; clause 4.1's point 1; and clause 4.5's **Why** paragraph. The rest of the
  diff is link definitions. Runs 33, 37, 40, 43, 46, 49 and 52 came before, under the earlier
  rules.

- **Cohort**: five readers, none reused from any earlier run. The cohort's model, named before
  the readers started, is `claude-haiku-5-5`, and every reader reported `claude-haiku-5-5` in its
  JSON output.

- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, which only reattaches the session's credential, in a fresh
  empty directory made by `mktemp -d` outside any repository, with the packet on standard input;
  no tools, no settings, no project context and no saved session; the machine applies no managed
  settings; the editor attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt's sha256 is
  `2d6a3b43a22fbc8a7b41a37ab0b5fa7e39cd1857e45502797c71d4567d377a10` and that it is byte for
  byte the question set, TOOLING-SPEC.md and `fixtures/zigpipe.md` at 8e91f8a, each after one
  `===== FILE: <name> =====` line, one blank line between files; and that each sheet is the
  `result` of its reader's JSON, `is_error` false, subtype `success`.

- **Readers set aside**: none.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's instruction and its agent definition, having seen neither the drafting nor the review.
  Marked against `ACCEPTANCE.md` at c31d49a (unchanged at 8e91f8a), and
  `acceptance/toolchain/QUESTIONS.md`, `acceptance/toolchain/KEY.md` and the fixture at 8e91f8a.
  No earlier run's judgements were used.

## Marks

| Reader | Q1   | 2a  | 2b  | 2c  | 4.1 | 4.2           | 4.3           | 4.4 | 4.5 | 5.1     | 5.2 | 5.3 | 6.1     | 6.2 | 6.3 | Section 9 | Agent support | Section 8 | Declaration |
| ------ | ---- | --- | --- | --- | --- | ------------- | ------------- | --- | --- | ------- | --- | --- | ------- | --- | --- | --------- | ------------- | --------- | ----------- |
| 1      | miss | ok  | ok  | ok  | No  | Partial, miss | Yes           | Yes | Yes | Partial | Yes | Yes | Yes     | No  | Yes | ok        | ok            | ok        | ok          |
| 2      | ok   | ok  | ok  | ok  | No  | Partial, miss | Yes           | Yes | Yes | Yes     | Yes | Yes | Partial | No  | Yes | ok        | ok            | ok        | ok          |
| 3      | ok   | ok  | ok  | ok  | No  | No            | Yes           | Yes | Yes | Partial | Yes | Yes | Partial | No  | Yes | ok        | ok            | ok        | ok          |
| 4      | ok   | ok  | ok  | ok  | No  | No            | Partial, miss | Yes | Yes | Yes     | Yes | Yes | Partial | No  | Yes | ok (O1)   | ok            | ok        | ok          |
| 5      | ok   | ok  | ok  | ok  | No  | No            | Yes           | Yes | Yes | No      | Yes | Yes | Partial | No  | Yes | ok        | ok            | ok        | ok          |

Every 6.1 Partial mentions that the fixture names no place for [Calibrations] or conventions; every
6.2 No mentions that nothing rejects a generic justification; every section 9 answer but reader
4's names 4.1, 4.2 or 6.2 among the failing clauses; every agent-support answer says section 7 is
unmet or the toolchain does not conform at all; every section 8 answer says Zigpipe ships nothing;
every declaration answer says the declaration is optional or that the verdict rests on the
evidence.

### The misses

No miss matches a wrong reading the key names: no reader grades 6.2 or 4.1 Yes, applies section 8
to Zigpipe, or makes the declaration affect the verdict. No miss's reasoning quotes the document.

- **Reader 1, question 1.** Three bullets name obligations the key lists: 4.1; 4.2, 4.3 and 4.5
  in one bullet; 5.1 to 6.3 in one bullet. Bullet 1 (the governing principle) and bullet 2
  (conformance judged on the assembled whole) are on neither list and are not counted. Bullet 6,
  "Shipped artefacts get their own grade and self-audit", is the case the key calls neither
  correct nor wrong. Three is short of four. The only question 1 miss: four of five.
- **Readers 1 and 2, 4.2, Partial.** Reader 1: the `zq.*` and `proj.*` documentation is on disk,
  but the fixture shows no resolver keyed on the identifier, does not say the `zq.*` pages state
  the correct construction, and the two undocumented rules' identifiers lead nowhere. Reader 2:
  the `zq.*` and `proj.*` documentation resolves; the two undocumented rules are "counted as not
  Defences here (see section 4)", so "their failure sits under 4.1"; its question 4 entry reads
  them out of 4.2 by the section 2 [Defence] row. Two misses on one item: 4.2 is three of five.
- **Reader 4, 4.3, Partial.** The inline route is disabled, but the fixture says nothing of any
  other route, such as a generated baseline, and describes no blocking defence. The only 4.3
  miss: four of five.

## Passages named under question 4

Paragraphs as `ACCEPTANCE.md` counts them: a heading, a list item and a table row each their own.

| #   | Passage, words quoted or description given                                                                                                                                                                  | Clause                                                                                   | Readers    | Changed by the diff |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------- | ------------------- |
| P1  | "A project or artefact that has learnt that it fails a MUST ... MUST record that gap alongside the version, in the same file or one it names"                                                               | 9.2, paragraph 2                                                                         | 1, 2, 4, 5 | No                  |
| P2  | "The declaration is optional." (reader 4 by description, "the same section says the declaration is optional")                                                                                               | 9.2, paragraph 3                                                                         | 1, 2, 4, 5 | No                  |
| P3  | "The project-level verdict is a single grade"; "the [Toolchain] is one the project ships, every MUST in section 8 as well"                                                                                  | 9, paragraph 1                                                                           | 1, 3       | No                  |
| P4  | "Section 8 bears on the artefact grade only"; "against this document and section 7 of the method specification"                                                                                             | 9.1, paragraph 1                                                                         | 1, 3       | No                  |
| P5  | The heading, "MUST forbid, through a defence of its own, every suppression route"                                                                                                                           | 4.3, heading                                                                             | 1, 4, 5    | No                  |
| P6  | "MUST disable every [Suppression] route ... or MUST run a [Blocking] [Defence] that fails on its use"                                                                                                       | 4.3, paragraph 1                                                                         | 1, 4, 5    | No                  |
| P7  | The [Defence] row, "A [Rule] with its documentation, in force and [Blocking]"                                                                                                                               | 2, table row                                                                             | 1, 2, 5    | No                  |
| P8  | "every [Identifier] its [Defences] print", "every [Bundled defence]" (reader 2 by description: what Defences "print")                                                                                       | 4.2, paragraph 1                                                                         | 1, 2, 5    | No                  |
| P9  | "The [Detector] together with that wrapping is then what the [Practitioner] uses and what is judged."                                                                                                       | 4.1, point 1                                                                             | 2          | Yes                 |
| P10 | "The [Detector]'s own verdict under that document is unchanged by the wrapping." (reader 2); "4.1 grades against the detector specification's MUSTs, which this document does not reproduce" (reader 5, O3) | 4.1, point 2, the paragraph beneath the table                                            | 2, 5       | No                  |
| P11 | "provide the route to each one's full documentation"                                                                                                                                                        | 5.1, paragraph 1                                                                         | 2          | No                  |
| P12 | "§4.1 separately fails a Detector for undocumented Bundled rules" (description; O6)                                                                                                                         | 4.1, table row "Two [Bundled rules] have no documentation, Nothing for those two, Fails" | 2          | No                  |
| P13 | "a Defence it routes"                                                                                                                                                                                       | 4.1, paragraph 1                                                                         | 5          | No                  |
| P14 | "meeting its content requirements in full" (O5)                                                                                                                                                             | 5.3, paragraph 1                                                                         | 4          | No                  |
| P15 | "is self-contained for grading a [Toolchain]"                                                                                                                                                               | 1, "How to read this document"                                                           | 5          | No                  |

What each reader set against what: reader 1 P1 against P2, P3 against P4, P5 against P6, P7
against P8; reader 2 P7 against P8, P11 and P12, P9 against P10, P1 against P2; reader 3 P3
against P4; reader 4 P5 against P6, P1 against P2; reader 5 P5 against P6, P1 against P2, P7
against P13 and P8, P15 against P10.

Recorded as a note, not a passage: reader 4's "§4.1: 'exercised as its clause 8.1 describes.' The
detector specification was not supplied, so I could not check the detector's own clauses
directly" (O4). Readers 1, 2, 4 and 5 also note under question 3 that the detector specification
was not supplied.

## Findings and where they lie

- **F1, clause 4.1 point 2's paragraph beneath the table (P10), readers 2 and 5: blocks.** Reader
  2 sets it against point 1's "The [Detector] together with that wrapping is then what the
  [Practitioner] uses and what is judged." (P9) and could not tell whether the wrapped pair or the
  [Detector] alone is graded. Point 1 is a paragraph the change altered: its [Harness] became
  [Rule harness]. A finding set by a reader naming it against such a paragraph lies in text the
  change wrote or altered. Reader 5's naming of P10 is counted under O3.
- **F2, clause 9.2's gap MUST (P1) against "The declaration is optional." (P2), readers 1, 2, 4
  and 5: routed.** Untouched text, set against untouched text. To be noted on its existing
  `acceptance/ROUTED.md` row (runs 33, 52) as raised again by run 55.
- **F3, section 9 (P3) against clause 9.1 (P4) on section 8, readers 1 and 3: routed.** Untouched;
  existing row (runs 43, 46).
- **F4, clause 4.3's heading (P5) against its body (P6), readers 1, 4 and 5: routed.** Untouched;
  existing row (run 33).
- **F5, the section 2 [Defence] row (P7) against clause 4.2 (P8), readers 1, 2 and 5: routed.**
  Untouched: the row is a paragraph of its own, apart from the [Rule harness] row the change
  altered, and no reader naming it sets it against a changed paragraph. Existing row (runs 33 to
  49). Reader 2's 4.2 miss turns on the same reading.

P9, P11 to P15 are named by one reader each: recorded, not blocking.

## Points the rules did not settle

- **O1, reader 4's section 9 reason.** "Three MUSTs are No and two are Partial" names no clause by
  number; read with its own table, the three are 4.1, 4.2 and 6.2. Whether that meets the key's
  "names 4.1, 4.2 or 6.2" is open; marked for the reader, as the open-point rule says.
- **O2, question 1 bullets on neither list.** The governing principle (readers 1, 2 and 4, bullet
  1. and conformance as one project-level grade on the assembled whole (reader 1 bullet 2, readers
     3 and 5 bullet 1) are on neither of the key's lists; not counted, an open point for the key.
- **O3, reader 5's 4.1 reference.** "4.1 grades against the detector specification's MUSTs, which
  this document does not reproduce" gives a clause number and a description, which fit clause 4.1's
  paragraph 1 or point 2's "meet every MUST of sections 4 to 7". Reader 5's question 3 preface
  grades from "the six points stated in 4.1", the brief list in paragraph 1, so the MUSTs it says
  are not reproduced are most plausibly point 2's. Whether it names the same paragraph as reader 2
  is open; counted as the same passage, as the open-point rule says. Without it, F1 would be a
  single-reader passage and not a finding.
- **O4, reader 4's 4.1 remark.** It quotes six words of point 2's paragraph with a clause number,
  but its whole content is that the detector specification was not supplied, the example
  `ACCEPTANCE.md` gives of a remark that is not about a passage. Judged a note. Counted the other
  way it would add a third reader to F1 and change nothing.
- **O5, reader 4's 5.3 quotation**, five words occurring in both of 5.3's paragraphs: recorded at
  the first. One reader either way.
- **O6, reader 2's 4.1 description** of failing undocumented rules: recorded at the table row; it
  could be paragraph 1's "A [Detector] that fails any one of those, after wrapping, fails this
  clause." One reader either way.

## Process change

Made under the process change of pull request 22 before it merged, following all of it at
c31d49a, named before the readers started.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Verdict

- Load-bearing statements, every reader on every item: met, five of five on 2a, 2b and 2c.
- Restatement and application, all but one reader on each keyed item: not met. 4.2 three of five
  (readers 1 and 2 Partial); question 1 and 4.3 four of five; every other item five of five.
- A miss the key says counts against the document: none.
- A passage found confusing by two or more readers in text the change wrote or altered: not met.
  F1, clause 4.1 point 2 set against point 1.
- Found confusing by two or more readers elsewhere: F2 to F5, routed to `acceptance/ROUTED.md`.

**FAIL**, on the 4.2 threshold and on F1.

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125398160); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125397751); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125398563).
