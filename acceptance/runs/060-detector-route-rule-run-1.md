# Run 60: DETECTOR-SPEC.md, detector route rule, first run

- **Document**: DETECTOR-SPEC.md
- **Pull request**: not yet opened at the time of the run; it is to be opened from branch
  `editor/detector-route-rule`. The readers read commit ed30e69. Change: clause 7.1's detectable
  route is a bespoke rule the project writes for the detector under clause 4.1, with a paragraph
  on what detectable means; clause 8.1's gap duty falls only on a detector that declares a
  version; clause 5.3 says what the remainder is; clause 6.1 says it asks for the mechanism, a
  missing page failing clause 6.3, and that a path in the message is not enough on its own.
- **Run within the pull request**: 1.
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `d3b016b18288e3589df60de97f746a31179924dbdd5faa339c055fbf95d89125`) is
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at ed30e69, each after one
  `===== FILE: <name> =====` line, one blank line between files; the marker rebuilt it from that
  commit and it matched byte for byte.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  marking instruction and its agent definition, having seen neither the drafting nor the review.

## Marks

Readers are numbered 1 to 5 as their sheets are. Question 3 columns: the eleven clauses, then
the two answers (S8 conformance under section 8, 6.4 whether clause 6.4 changes the verdict).

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1  | S8  | 6.4 |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
| 1      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  |
| 2      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  |
| 3      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  |
| 4      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok   | ok  | ok  |
| 5      | correct | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | miss | ok  | ok  |

Question 1: correct bullets per reader 6, 6, 6, 6 and 6, one for each line of the key's list
(4.1; 4.2; 4.3; 5.1 to 5.4; 6.1 to 6.3; 7.1). Reader 1's third bullet adds 4.4 as a SHOULD and
its sixth adds what conformance means beside 7.1; both are, by the key, neither correct nor
wrong, and each bullet still names its obligation. Reader 2's fourth bullet says every finding
must reach the output, which the key says names 5.3 and is not wrong. No bullet asserts anything
the key marks wrong.

Question 2: every reader states every required element of each item and quotes the document.
For 2a all five quote section 8's "A Detector Conforms if it satisfies every MUST in sections 4
to 7" or clause 8.1's "A Detector that predates this document, or whose maintainer has never
read it, MAY be graded Conforming on evidence"; for 2b all five quote clause 7.1's "For each one
it MUST do at least one of two things, and either alone satisfies this clause", and name both
things and that either is enough; for 2c all five quote the headings or first sentences of 6.2
and 6.3. Readers 1 and 2, under 2b, add that the detectable route is closed to a detector whose
rules never see comments, so that it needs the disable route or a documented mechanical check;
that is not among the key's wrong assertions for 2b, and the answers are correct by the rule.

Question 3: readers 1 to 4 give every accepted grade; reader 5 gives every accepted grade on the
ten rows it answers. S8: all five say Lintomatic does not conform, naming 6.3. 6.4: all five say
it does not change the verdict, because it is a SHOULD.

### Misses

- **Reader 5, question 3, clause 7.1**: unanswered. Its table ends at 6.3 and no grade for 7.1
  appears anywhere on the sheet, so the item is a miss under "An unanswered question". There is
  no reasoning, so nothing quotes the document; it is not a reading the key names (7.1 graded
  No on 7.2's reason). The other four readers are correct on the item, so the threshold of all
  but one is met.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..ed30e69 adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                         | Readers | Changed by the diff |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------------------- |
| 1   | Clause 6.1, "For a Bundled rule" paragraph: "A documentation path printed in the [Message] is therefore not enough on its own"; both readers say [Message] is not defined in the document they were given                                                                                                                      | 1, 5    | yes                 |
| 2   | Clause 8.1, second paragraph: "MAY be graded [Conforming] on evidence by anyone who exercises the clauses above against it" (5, whether the MAY is a permission or a possibility); "by anyone who exercises the clauses above against it" (3, whether "the clauses above" are sections 4 to 7 or earlier clauses of section 8) | 3, 5    | yes                 |
| 3   | Clause 6.1, "For a project's own Rule" paragraph: "Where the [Identifier] is itself a URL, as method clause 3.6 allows"; the reader could not check method clause 3.6                                                                                                                                                          | 1       | no                  |
| 4   | Clause 6.1 heading: "The Detector MUST provide a mechanism that resolves a printed identifier to its documentation", set against passage 5                                                                                                                                                                                     | 2       | no                  |
| 5   | Clause 6.1 table, project's own row: "Print the Identifier unaltered; the lookup is the Toolchain's to give", set against passage 4                                                                                                                                                                                            | 2       | no                  |
| 6   | Clause 5.3, first paragraph: "a report that only adds detail to those same findings, such as a code snippet, need not be named in the output"                                                                                                                                                                                  | 2       | yes                 |
| 7   | Clause 8.1, first paragraph: "a [Detector] that declares a version and has learnt ... that it fails a MUST in sections 4 to 7 MUST record that gap alongside that version", set against section 8's definition and the optional declaration                                                                                    | 3       | yes                 |
| 8   | Clause 4.3, first paragraph: "in its default output and in every machine-readable format it offers"; "machine-readable" is not defined                                                                                                                                                                                         | 4       | no                  |

## Findings and where they lie

- **Finding A, passage 1, clause 6.1 "For a Bundled rule" paragraph** (readers 1 and 5): the
  sentence both readers quote was written by the change, replacing "A [Message] that carries its
  own documentation path resolves that [Message], not the [Identifier]." Text the change wrote.
  Blocks.
- **Finding B, passage 2, clause 8.1 second paragraph** (readers 3 and 5): the sentence both
  readers quote is not itself reworded, but the change rewrote the paragraph's first sentence
  ("The declaration is optional, and so the duty above falls only on a [Detector] that has one;
  ...") and added its second. The rule places a finding by paragraph, so the paragraph is the
  change's. Blocks.

Passages 3 to 8 are each named by one reader: recorded, not findings. Nothing is routed to
`acceptance/ROUTED.md` from this run.

## Points the rules did not settle

1. **Passage 1, a term defined in a document not supplied.** Readers 1 and 5 each quote the
   sentence with its clause number, which `ACCEPTANCE.md` defines as naming a passage, and the
   confusion each gives is that [Message] is defined in the method specification, which they
   were not given. The rule that a remark about another document not being supplied is a note,
   not a passage, covers a remark "not about a passage of the document"; these remarks are about
   a quoted passage, so they were read as naming it. Had it been open, the open-point rule on
   whether a reader named a passage counts the passage in any case. Finding A turns on this
   point. Reader 1's passage 3 (method clause 3.6) is the same case, counted the same way, and
   is named by one reader only.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit e6bdf40, named before the readers started.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item but
  7.1, where four of five are correct (reader 5 left it unanswered). Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: two (findings A
  and B). Not met.
- Passages named by two or more readers elsewhere: none.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on findings A and B alone; every keyed item passed its threshold.

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
