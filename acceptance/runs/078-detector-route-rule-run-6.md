# Run 78: DETECTOR-SPEC.md, detector route rule, sixth run

- **Document**: DETECTOR-SPEC.md
- **Pull request**: [23](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/23), from branch
  `editor/detector-route-rule`. The readers read commit ac14996. Change: clause 7.1's detectable
  route is a bespoke rule the project writes for the detector under clause 4.1, with a paragraph
  on what detectable means; clause 8.1's gap duty falls only on a detector that declares a
  version; clause 5.3 says what the remainder is; clause 6.1 says it asks for the mechanism, a
  missing page failing clause 6.3, and that a path in the message is not enough on its own;
  section 2's table gains a Message row. Revised after run 77 in the one paragraph its finding
  named: clause 5.3's remainder sentence is now three plain sentences (the remainder is the
  findings the summary leaves out; where the output prints every finding there is no remainder;
  a fuller report written elsewhere is not a remainder and the output need not name it); so this
  is a fresh run.
- **Run within the pull request**: 6 (runs 60, 63, 66, 73 and 77 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `9d52a2f0c2c15cb1f4d1b7d628fc403560534fa35cdde941e26efe717846f35c`) is
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at ac14996, each after one
  `===== FILE: <name> =====` line, one blank line between files; the marker rebuilt it from that
  commit and it matched byte for byte.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  marking instruction and its agent definition, having seen neither the drafting nor the review.

## Marks

Readers are numbered 1 to 5 as their sheets are. Question 3 columns: the eleven clauses, then
the two answers (S8 conformance under section 8, 6.4 whether clause 6.4 changes the verdict).

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2  | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | S8  | 6.4 |
| ------ | ------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1      | correct | ok  | ok  | ok  | ok  | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 2      | correct | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 3      | correct | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 4      | correct | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |
| 5      | correct | ok  | ok  | ok  | ok  | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  |

Question 1: every reader has six correct bullets among the first six, one per line of the key's
list (4.1, 4.2, 4.3, 5.1 to 5.4, 6.1 to 6.3, 7.1). Reader 1 gives seven bullets; its seventh, on
section 8, is not marked. Readers 3 and 5 also restate SHOULDs (4.4, 6.4, 7.2) as SHOULDs, and
reader 4's sixth bullet adds what conformance means; the key says neither is correct nor wrong.
Reader 4 says the output carries a pointer to any findings the summary leaves out, which names
5.3. No bullet asserts anything the key marks wrong.

Question 2: every reader states every required element of each item and quotes the document.
For 2a all five state that conformance is every MUST in sections 4 to 7 and that a detector
predating the document can conform, quoting clause 8.1's "A Detector that predates this
document, or whose maintainer has never read it, MAY be graded Conforming on evidence"; readers
1, 3 and 4 also quote section 8's definition, reader 2 its "satisfies every MUST in sections 4
to 7". For 2b all five name both things, disableable by configuration or detectable, and that
either alone is enough, quoting clause 7.1's "For each one it MUST do at least one of two
things, and either alone satisfies this clause"; readers 2, 4 and 5 add that 7.2's reason is a
SHOULD, and reader 3 that a detector whose rules never see comments has only the mechanical
check, the document's own sentence; neither is among the key's wrong assertions. For 2c all five
state that the documentation ships with the rule (reader 2 "inside the installed rule package"),
at a version tracked together or the same version, and reachable without network access,
quoting clause 6.2's heading and clause 6.3's heading or its "Every Identifier a Bundled rule can
print MUST resolve" sentence. None names a website as acceptable; reader 4 quotes 6.2's Why
saying it is not.

Question 3: readers 2 to 5 give every accepted grade; readers 2, 3 and 4 add caveats on 4.2 (the
fixture does not say `--only` prints finding lines) and 4.3 (no machine-readable format
described), and the key says a caveat with the accepted grade is correct. Reader 3 states that
it read the two undocumented rules as bundled and gives No for 6.3 without condition. All five
grade 5.3 Yes because every finding is printed so there is no remainder, and 6.1 Yes; readers 2,
3 and 4 say the two missing pages fail 6.3, not 6.1. No reader grades 6.3 Partial or 7.1 No. S8:
all five say Lintomatic does not conform, naming 6.3 (reader 1 adds its own 4.2 Partial as a
second reason). 6.4: all five say it does not change the verdict, because it is a SHOULD.

### Misses

- **Reader 1, clause 4.2: Partial** (accepted: Yes). Reasoning: `--only` exits 1 when the rule
  fires, so whether it fired is reported, but the fixture never says `--only` prints what the
  rule printed, which 4.2 requires. The quotation in the reasoning is from the fixture ("exits 1
  when the rule fires, 0 when it does not"); clause 4.2 is paraphrased, not quoted, so the
  reasoning does not quote the document. It puts the gap on the fixture's silence. The key names
  no wrong reading for 4.2. A single miss, the reader's, tolerated by the threshold.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..ac14996 adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.
That diff changes section 2's Message row, clause 5.3's first paragraph, clause 6.1's "In both"
and "For a Bundled rule" paragraphs, clause 6.4's Why paragraph, clause 7.1's first and second
paragraphs, and clause 8.1's first and second paragraphs.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                    | Readers | Changed by the diff |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------- |
| 1   | Clause 4.2, first paragraph: "a [Detector] failing 4.1 is graded here on its [Bundled rules]."; reader 2: the sentence's purpose unclear until read as applying 4.2 to bundled rules alone                                                                                                                | 1, 2    | no                  |
| 2   | Clause 6.1, the table row for a project's own Rule: "Print the [Identifier] unaltered; the lookup is the [Toolchain]'s to give", set against the clause heading's "MUST provide a mechanism that resolves a printed identifier to its documentation"                                                      | 1       | no                  |
| 3   | Clause 6.1, the heading, which reader 1 sets against passage 2; counted as named by reader 1 under the open-point rule                                                                                                                                                                                    | 1       | no                  |
| 4   | Clause 8.1, the JSON example: `"method": "1.0.1"`, against the header's method specification version 1.1.0; what the field means                                                                                                                                                                          | 2       | no                  |
| 5   | Clause 8.1, second paragraph: "A [Detector] that predates this document, or whose maintainer has never read it, MAY be graded [Conforming] on evidence: anyone may grade it, ... rests on that check and not on the claim."; how every detector is graded, under a heading about the optional declaration | 3       | yes                 |
| 6   | Clause 4.3, first paragraph: "The [Detector] MUST print it, unaltered, alongside every finding the [Rule] reports, in its default output and in every machine-readable format it offers."; whether the HTML report is a machine-readable format, set against 5.3's "fuller report"                        | 5       | no                  |
| 7   | Clause 5.3, first paragraph, which reader 5 cites ("5.3 calls the HTML a 'fuller report'") in passage 6; counted as named by reader 5 under the open-point rule                                                                                                                                           | 5       | yes                 |

Notes, not passages: reader 2's items on clause 6.1 ("Where the [Identifier] is itself a URL, as
method clause 3.6 allows": the method specification was not provided, so the cross-reference
could not be checked) and on clause 7.1's Why paragraph ([Owner], [Class] and [Hazard] are
defined only in the method specification, which was not given); reader 4's single item, the same
6.1 sentence and the references to method clauses 3.3 (4.2's Why) and 3.2 (8.1), with *Class*
and *Owner*, all because the method specification was not provided. Each is a remark that
another document was not supplied, which `ACCEPTANCE.md` records as a note and not a passage;
see the first point below.

## Findings and where they lie

- **Finding A, passage 1, clause 4.2 first paragraph** (readers 1 and 2): the diff
  9e914fe..ac14996 does not touch clause 4.2, and neither reader sets the paragraph against a
  paragraph the change wrote or altered. A finding against the document, not the change: to be
  recorded in `acceptance/ROUTED.md` as a new open row and routed to a change of its own. Does
  not block.

Passages 2 to 7 are each named by one reader: recorded, not findings. Passages 5 and 7 lie in
changed paragraphs but are single.

## Points the rules did not settle

1. **Remarks that the method specification was not supplied, made by quoting a sentence.**
   Readers 2 and 4 each quote six or more words of clause 6.1's "For a project's own Rule"
   paragraph, with the clause number, and say only that the method specification was not
   provided, so the cross-reference could not be checked. `ACCEPTANCE.md` both says a quotation
   with a clause number names a passage and says a remark "such as that another document was not
   supplied" is a note and not a passage. Run 77 recorded this as an open point and counted the
   passages; `ACCEPTANCE.md` and the key have not changed on it since, so it was not settled
   before this run as "Changing the test" asks. This marker holds that the rule settles it: the
   stated confusion in each item is exactly the rule's own example of a note, and the quotation
   only locates the reference whose target was not supplied; so these are notes, and no open
   point arises. The verdict turns on this. Were it held open and the passages counted, readers 2
   and 4 would form a finding on clause 6.1's "For a project's own Rule" paragraph, unchanged
   and routed (it is already open in `acceptance/ROUTED.md`, runs 28, 63, 66); and reader 4's
   "8.1's 'the method's clause 3.2'", whose words occur in both of clause 8.1's paragraphs, would
   leave open whether reader 4 and reader 3 (passage 5) named the same changed paragraph, which
   the open-point rule counts, so that finding would block. The editor settles the point in
   `ACCEPTANCE.md` before any further run.
2. **Reader 1's passage on clause 6.1** sets the table row against the heading; whether it names
   one passage or both is not settled, so both are counted (passages 2 and 3). Reader 5's
   citation of clause 5.3 is counted the same way (passage 7). No other reader names any of
   these paragraphs, so the verdict does not turn on either.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 13b497b, named before the readers started.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item but
  4.2, which is four of five. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: none, on the
  marking of point 1. Met.
- Passages named by two or more readers elsewhere: one (finding A, clause 4.2), routed to
  `acceptance/ROUTED.md`; does not block.

## Findings applied

None at the time of marking; finding A is to be added to `acceptance/ROUTED.md` by the editor.

## Verdict

PASS, on the marking of point 1. Every keyed item meets its threshold, no miss counts against
the document, and the one finding, clause 4.2's first paragraph, lies outside the text the change
wrote and is routed.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/23#issuecomment-6125343069); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/23#issuecomment-6125342588); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/23#issuecomment-6125343418).
