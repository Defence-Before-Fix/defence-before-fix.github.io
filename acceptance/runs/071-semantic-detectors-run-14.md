# Run 71: DETECTOR-SPEC.md, semantic detectors, fourteenth run

- **Document**: DETECTOR-SPEC.md
- **Pull request**: 14, open on branch `editor/semantic-detectors`. The readers read commit
  befe52c. Change: a new clause 8.2, that a verdict on a detector names its kind, semantic,
  syntactic or textual, in each configuration it grades; section 9's sentence on that
  obligation; section 2's table rows for the three kinds and for Message.
- **Run within the pull request**: 14 (runs 19 to 30 and run 70 came before; runs 20, 22, 24,
  26, 28 and 30 read this document on an earlier, larger text of the change under the earlier
  acceptance rules).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `d45ab8c1ff1dc2ecabd1bad36eca32c3b0858327c5079cd4b6aea2abcb4e5cc3`) is
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at befe52c, each after one
  `===== FILE: <name> =====` line, one blank line between files; the marker rebuilt it from that
  commit and it matched byte for byte.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model; each sheet is that output's `result`.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  marking instruction and its agent definition, having seen neither the drafting nor the review.

## Marks

Readers are numbered 1 to 5 as their sheets are. Question 3 columns: the eleven clauses, then
the two answers (S8 conformance under section 8, 6.4 whether clause 6.4 changes the verdict).

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3  | 5.4 | 6.1  | 6.2 | 6.3 | 7.1 | S8  | 6.4 |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --- | --- |
| 1      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | miss | ok  | miss | ok  | ok  | ok  | ok  | ok  |
| 2      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | miss | ok  | miss | ok  | ok  | ok  | ok  | ok  |
| 3      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | miss | ok  | miss | ok  | ok  | ok  | ok  | ok  |
| 4      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | miss | ok  | miss | ok  | ok  | ok  | ok  | ok  |
| 5      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | miss | ok  | ok   | ok  | ok  | ok  | ok  | ok  |

Question 1: every reader's first six bullets name, one each, the key's lines for 4.1; 4.2; 4.3;
5.1 to 5.4; 6.1 to 6.3; and 7.1. Reader 2's sixth bullet adds 7.2 as a SHOULD and what
conformance means, and reader 4's sixth adds what conformance means; the key says such a
statement is neither correct nor wrong, and both bullets still name 7.1. Reader 3's seventh
bullet, on conformance, is not marked, since only the first six are. No reader names the 8.2
line, which the count does not need. No bullet asserts anything the key marks wrong.

Question 2: every reader states every required element of each item and quotes the document.
2a: all five state that conformance is every MUST in sections 4 to 7 and that a detector
predating the document can conform, quoting clause 8.1's "A Detector that predates this
document, or whose maintainer has never read it, MAY be graded Conforming on evidence"
(readers 2, 3 and 5 also quote section 8's definition). 2b: all five name both things,
disableable by configuration or detectable, and that either alone is enough, quoting clause
7.1's "For each one it MUST do at least one of two things, and either alone satisfies this
clause". 2c: all five state that the documentation ships with the rule or lives in the installed
copy, at a version tracked together, and resolves without network access, quoting the 6.2 and
6.3 headings; readers 2, 3 and 5 add that a website does not satisfy it, which is not among the
key's wrong assertions.

Question 3: every reader gives the accepted grade on 4.1, 4.2, 4.3, 5.1, 5.2, 5.4, 6.2, 6.3 and
7.1, several with caveats about what the fixture does not say (4.2's output, 4.3's
machine-readable formats), which the key accepts. S8: all five say Lintomatic does not conform,
naming 6.3; all five note that the verdict cannot name Lintomatic's kind because the fixture
does not say it, and that this does not alter the conformance finding, which the key does not
mark. 6.4: all five say it does not change the verdict, because it is a SHOULD.

### Misses

The key's wrong readings for question 3 are 6.3 graded Partial on a proportion, 7.1 graded No
on the missing reason, and the section 8 verdict made to turn on the kind. No miss matches one.
None of the reasoning below quotes the document as `ACCEPTANCE.md` defines quoting (a run of six
or more consecutive words); each paraphrases it or quotes the fixture.

- **5.3, readers 1 to 5, Partial (key: Yes).** Every reader reasons that the one-line output is a
  usable summary but that the fixture never says the command's output gives the location of
  `.lintomatic/report.html`, which they read clause 5.3's second sentence ("both a usable summary
  and the location of the remainder") as requiring. Reader 1 adds, under question 4, that what
  makes a summary "usable" decided its grade. Five of five: the item fails its threshold.
- **6.1, readers 1 to 4, Partial (key: Yes).** Each reasons that `explain` resolves an identifier
  presented alone, but that the two bundled rules printing `No documentation declared` do not
  resolve to documentation, so the mechanism fails for them; reader 4 says it counts the same
  defect under 6.1 and 6.3. Reader 5 gives Yes. Four of five: the item fails its threshold.

Both items fail as keyed items, which `ACCEPTANCE.md` says are fixed in the text that carries
the obligation wherever it lies; clauses 5.3 and 6.1 are not text the diff 9e914fe..befe52c
changes.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..befe52c adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Readers | Changed by the diff |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------- |
| 1   | Clause 8.1, first paragraph: "a [Detector] that has learnt, from its own checks or from a [Practitioner]'s report under the method's clause 3.2, that it fails a MUST in sections 4 to 7 MUST record that gap alongside the version it declares" (readers 4 and 5; reader 1 a shorter quotation of the same sentence); whether the duty binds a detector that makes no declaration, set against passage 2 by readers 1 and 4, and against "the version it declares" within the sentence by reader 5 | 1, 4, 5 | no                  |
| 2   | Clause 8.1, second paragraph: "The declaration is optional" (readers 1 and 4) and "it is not a condition of it" (reader 4), set against passage 1                                                                                                                                                                                                                                                                                                                                                   | 1, 4    | no                  |
| 3   | Clause 7.1, first paragraph: "or make the route detectable, by a [Rule] the project can write in the [Detector] itself" (readers 2 and 3, reader 3 with the rest of the sentence); whether that rule is clause 4.1's bespoke rule, added to configuration, or a change to the detector's own codebase                                                                                                                                                                                               | 2, 3    | no                  |
| 4   | Clause 8.2, first paragraph: "the same configurations the method specification's clause 3.2 counts when it asks for the strongest kind" (readers 2 and 3); which configurations are meant, the method specification not having been supplied. Reader 1 names "the method specification's clause 3.2" with clause 8.2 among terms it read as ordinary English for want of `SPEC.md` (point 2 below)                                                                                                  | 1, 2, 3 | yes                 |
| 5   | Clause 5.3, first paragraph: "the invoked command's own output MUST carry both a usable summary and the location of the remainder"; what makes a summary usable                                                                                                                                                                                                                                                                                                                                     | 1       | no                  |
| 6   | Section 2, introductory paragraph: "Terms from the method specification carry over unchanged", with [Class] and [Owner] pointing to `SPEC.md`, which reader 1 was not given (point 2 below)                                                                                                                                                                                                                                                                                                         | 1       | no                  |

Notes, not passages: none beyond what point 2 below counts as passages.

## Findings and where they lie

- **Finding A, passage 1, clause 8.1 first paragraph** (readers 1, 4 and 5): not changed by the
  diff, and the paragraph the readers set it against (passage 2) is not changed either. Routed
  to `acceptance/ROUTED.md`; does not block.
- **Finding B, passage 2, clause 8.1 second paragraph** (readers 1 and 4): not changed by the
  diff, and set only against passage 1. Routed to `acceptance/ROUTED.md`; does not block.
- **Finding C, passage 3, clause 7.1 first paragraph** (readers 2 and 3): not changed by the diff,
  and set against no changed paragraph. Routed to `acceptance/ROUTED.md`; does not block.
- **Finding D, passage 4, clause 8.2 first paragraph** (readers 2 and 3, and reader 1 under point
  2): the diff adds the whole of clause 8.2. Text the change wrote; blocks.

`acceptance/ROUTED.md` at befe52c lists, under Closed, rows on the passages of findings A and B
(clause 8.1, "MUST record that gap alongside the version it declares" against "The declaration
is optional.") and of finding C (clause 7.1, "by a Rule the project can write in the Detector
itself"), closed by run 66 on `editor/detector-route-rule`, whose rework of those clauses is not
in the text these readers read. Where the routed findings are entered is the editor's decision.

## Points the rules did not settle

1. **Passage 4, readers 2 and 3: a passage or a note.** Each quotes a sentence of clause 8.2 with
   the clause number and says it could not tell which configurations the sentence means,
   because the method specification was not supplied. `ACCEPTANCE.md` makes a remark that
   another document was not supplied a note only where it is "not about a passage of the
   document"; these remarks are about what a quoted sentence means. Marked as passages, which
   is also what the open-point rule says: an open point on whether a reader named a passage
   counts the passage. Finding D turns on this point.
2. **Reader 1's third item: a passage or a note.** Its subject is that `SPEC.md` was not given,
   which reads as a note, but it quotes section 2's "Terms from the method specification carry
   over unchanged" (a run of eight words) and names "the method specification's clause 3.2"
   with clause 8.2, whose first occurrence in 8.2 is the first paragraph. Counted, by the
   open-point rule, as naming section 2's introductory paragraph (passage 6) and clause 8.2's
   first paragraph (passage 4). Finding D does not turn on this point, since readers 2 and 3
   name the same paragraph.
3. **Readers 1 and 4 naming two paragraphs in one item.** Each quotes sentences from both the
   first and the second paragraph of clause 8.1 and sets them against each other. Counted as
   naming both paragraphs, by the open-point rule. Finding A stands on readers 4 and 5 without
   reader 1; finding B depends on this point, and is routed either way.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit f3ec69e, named before the readers started.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item except
  5.3 (none of five) and 6.1 (one of five). Not met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: one (finding D,
  clause 8.2 first paragraph). Not met.
- Passages named by two or more readers elsewhere: three (findings A, B and C), for
  `acceptance/ROUTED.md`.

## Findings applied

None at the time of marking.

## Verdict

FAIL. Question 3's items 5.3 and 6.1 fail the all-but-one threshold, and finding D lies in
clause 8.2's first paragraph, which the change wrote.

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
