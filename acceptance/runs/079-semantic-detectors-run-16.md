# Run 79: DETECTOR-SPEC.md, semantic detectors, sixteenth run

- **Document**: DETECTOR-SPEC.md
- **Pull request**: 14, open on branch `editor/semantic-detectors`. The readers read commit
  23f5bf0. Change: a new clause 8.2, that a verdict on a detector names its kind, semantic,
  syntactic or textual, in each configuration it grades; section 9's sentence on that
  obligation; section 2's table row for the three kinds. The branch carries
  `editor/detector-route-rule` (pull request 23) at its commit d67174c, whose rework of clauses
  5.3, 6.1, 7.1 and 8.1 and whose Message row in section 2 are that change's text, not this
  one's. Since run 74, clause 8.2's sentence on which configuration's kind is named (one needing
  no hosted service and no licence tier) has been removed; the clause's first paragraph now ends
  at "as section 2 glosses it".
- **Run within the pull request**: 16 (runs 19 to 30, 70, 71 and 74 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `7b94f116b3f875170cdfd9fd61f845b3cf7f233723bbd749dd38e93adb6a1fd9`) is
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at 23f5bf0, each after one
  `===== FILE: <name> =====` line, one blank line between files; the marker rebuilt it from that
  commit and it matched byte for byte.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model; each sheet is that output's `result`.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  marking instruction and its agent definition, having seen neither the drafting nor the review.

## Marks

Readers are numbered 1 to 5 as their sheets are. Question 3 columns: the eleven clauses, then
the two answers (S8 conformance under section 8, 6.4 whether clause 6.4 changes the verdict).

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | S8  | 6.4 |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 2      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 3      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 4      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 5      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |

Question 1: readers 1, 2 and 4 name, one bullet each, the key's lines for 4.1; 4.2; 4.3; 5.1 to
5.4; 6.1 to 6.3; and 7.1. Reader 3 names the same six, its sixth bullet adding what conformance
means, which the key says is neither correct nor wrong. Reader 5's first bullet states what
conformance means (neither correct nor wrong); its others name 4.1, 4.2, 4.3 (as "every rule has
a stable identifier", which the key says names 4.3), 5.1 to 5.4, and, in its sixth bullet, both
6.1 to 6.3 and 7.1 (point 2 below). No reader names the 8.2 line, and no bullet asserts anything
the key marks wrong: none says the detector must be of one kind or must state its own kind.

Question 2: every reader states every required element of each item and quotes the document.
2a: all five state that conformance is every MUST in sections 4 to 7 and that a detector
predating the document can conform; readers 1, 2, 3 and 5 quote section 8's definition, and all
five quote clause 8.1's "A Detector that predates this document, or whose maintainer has never
read it, MAY be graded Conforming on evidence". 2b: all five name both things, disableable by
configuration or detectable, and say either alone is enough, quoting clause 7.1's "For each one
it MUST do at least one of two things, and either alone satisfies this clause" (readers 1, 3 and
4 with an ellipsis or ending in one; the run before it is well over six words). Readers 2 and 5
add that a written reason is a SHOULD under 7.2, which is not a wrong assertion. 2c: all five
state that the documentation ships with the rule in the installed copy, at a version tracked
together, and resolves without network access, quoting the 6.2 and 6.3 headings (reader 2 also
6.3's first sentence, reader 3 also 6.5's sentence on the installed file); reader 1 adds that a
website does not satisfy it, which is not among the key's wrong assertions.

Question 3: every reader gives the accepted grade on all eleven clauses, several with caveats on
what the fixture does not say (what `--only` prints under 4.2, machine-readable formats under
4.3), which the key accepts since no row carries a condition. Reader 2's 4.2 is Yes with the
remark that it would be Partial if `--only` printed nothing; the grade given is Yes, and the key
says a caveat on what the fixture does not say leaves the accepted grade correct. S8: all five
say Lintomatic does not conform, naming 6.3 or the two undocumented bundled rules; all five say
the verdict cannot name Lintomatic's kind because the fixture does not say it, and that the
conformance finding stands, which the key does not mark. None makes the verdict turn on the
kind. 6.4: all five say it does not change the verdict, because it is a SHOULD.

### Misses

None. No answer matches a wrong reading the key names for question 1 or question 3.

## Question 4: passages named

Reader 1 wrote "none". Paragraphs as `ACCEPTANCE.md` defines them; "this change's text" means a
paragraph the diff d67174c..23f5bf0 adds, rewords, moves, deletes a sentence from, or changes a
word, term or link in. The diff 9e914fe..23f5bf0 shows this change and the merged detector
change together.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                                                  | Readers | This change's text |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------ |
| 1   | Clause 6.4, **Why** paragraph: "Where the [Detector] is shipped inside a [Toolchain], the [toolchain specification]'s self-audit makes this check a MUST for the [Toolchain]; a [Detector] released on its own is asked for it as a SHOULD because ..."; the "because" reads as a reason for a MUST as well as for a SHOULD                                                             | 2       | no                 |
| 2   | Clause 7.1, **Why** paragraph: "is an [Owner] decision under its clause 3.4 and section 4"; Owner is defined in the unsupplied method specification (point 1 below)                                                                                                                                                                                                                     | 3       | no                 |
| 3   | Clause 4.1, **Why** paragraph: "the [Classes] that matter most to a project"; Class is defined in the unsupplied method specification (point 1 below)                                                                                                                                                                                                                                   | 3       | no                 |
| 4   | Clause 7.1, second paragraph ("A route is detectable when ..."): "That way is open only where the [Detector]'s [Rules] can see the route: a [Detector] whose [Rules] never see comments cannot make an ignore comment detectable this way.", read with "the [Detector] ships no such [Rule] itself, and need not"; how the detector's MUST is discharged when the project does the work | 4       | no                 |
| 5   | Clause 4.3, first paragraph: "A prefix the [Detector] adds from the invoking directory or the [Rule]'s location is derived from the file path. A namespace the [Rule author] assigns once in configuration is not."; whether a detector-added prefix not derived from location is allowed                                                                                               | 4       | no                 |
| 6   | Clause 6.1, heading: "The [Detector] MUST provide a mechanism that resolves a printed identifier to its documentation"; whether the MUST applies to project rules at all                                                                                                                                                                                                                | 5       | no                 |
| 7   | Clause 6.1, paragraph "For a project's own Rule": "what it owes is the half it can give: the [Identifier] printed unaltered under clause 4.3"; set against passage 6                                                                                                                                                                                                                    | 5       | no                 |

Notes, not passages: reader 2's remark that the fixture does not say whether Lintomatic sits
inside a toolchain, so it read it as standalone.

Passages 2 and 4 are both in clause 7.1 but in different paragraphs (the **Why** paragraph and
the second paragraph), so they are not the same passage; passages 6 and 7 are both reader 5's.

## Findings and where they lie

None. No passage is named by two or more readers, so nothing blocks and nothing is routed to
`acceptance/ROUTED.md` from this run. Passages 1 to 7 are each one reader's and are recorded
only; none lies in text this change wrote or altered (clauses 6.1 and 7.1 are the detector
change's text at d67174c, and clauses 4.1, 4.3 and 6.4 are unchanged by d67174c..23f5bf0).
No reader named clause 8.2, section 9 or section 2's kinds row.

## Points the rules did not settle

1. **Reader 3's question 4: passages or notes.** Each item's subject is a term defined only in
   the method specification, which was not supplied, which reads as a note; but each quotes six
   or more consecutive words of the document with a clause number. Counted, by the open-point
   rule (an open point on whether a reader named a passage counts the passage), as naming
   clause 7.1's **Why** paragraph and clause 4.1's **Why** paragraph. No finding turns on this
   point: no other reader names either paragraph.
2. **Reader 5's sixth question 1 bullet names two lines of the key's list** (6.1 to 6.3, and
   7.1). The rules say how bullets naming one line count, not how one bullet naming two lines
   counts. Marked for the reader, by the open-point rule; no mark turns on it, since reader 5's
   bullets name at least four lines of the key without it (4.1, 4.2, 4.3, 5.1 to 5.4).

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 13b497b, named before the readers started. `ACCEPTANCE.md`,
`acceptance/README.md`, `acceptance/runs/README.md` and `CONTRIBUTING.md` are identical at
13b497b and 23f5bf0.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none. Met.
- Passages named by two or more readers in text the change wrote or altered: none. Met.
- Passages named by two or more readers elsewhere: none.

## Findings applied

None at the time of marking.

## Verdict

PASS. Every reader is correct on every keyed item, no miss counts against the document, and no
passage is named by two or more readers.

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
