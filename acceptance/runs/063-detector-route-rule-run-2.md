# Run 63: DETECTOR-SPEC.md, detector route rule, second run

- **Document**: DETECTOR-SPEC.md
- **Pull request**: not yet opened at the time of the run; it is to be opened from branch
  `editor/detector-route-rule`. The readers read commit 4cbecad. Change: clause 7.1's detectable
  route is a bespoke rule the project writes for the detector under clause 4.1, with a paragraph
  on what detectable means; clause 8.1's gap duty falls only on a detector that declares a
  version; clause 5.3 says what the remainder is; clause 6.1 says it asks for the mechanism, a
  missing page failing clause 6.3, and that a path in the message is not enough on its own.
  Revised after run 60 in section 2's table (a Message row) and clause 8.1's second paragraph.
- **Run within the pull request**: 2 (run 60 came before).
- **Cohort**: five readers, none reused from any earlier run. Model named for the run before the
  readers started: `claude-haiku-5-5`. Every reader reported `claude-haiku-5-5`.
- **Isolation**: each reader a separate `claude -p` process, started through the `ccy-claude`
  wrapper (which only reattaches the session's credential) in a fresh empty directory made by
  `mktemp -d` outside any repository, with the packet on standard input; no tools, no settings,
  no project context, no saved session; the machine applies no managed settings. The editor
  attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt (sha256 `30b41f341b26e48b3c8bf1b1d55a25283ffd43c835328eaf5cd9ec021d265e09`) is
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at 4cbecad, each after one
  `===== FILE: <name> =====` line, one blank line between files; the marker rebuilt it from that
  commit and it matched byte for byte.
- **Readers set aside**: none. Every reader's output has `is_error` false, subtype `success`,
  non-empty answer text and the cohort's model.
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

Question 1: correct bullets per reader 6, 6, 6, 6 and 6, one for each line of the key's list
(4.1; 4.2; 4.3; 5.1 to 5.4; 6.1 to 6.3; 7.1). Reader 3's third bullet adds 4.4 as a SHOULD;
readers 2 and 3 add to their sixth bullet that a written reason is a SHOULD; reader 5's sixth
bullet adds the SHOULDs of 7.2, 4.4 and 6.4. Each restates a SHOULD as advice, which the key
says is neither correct nor wrong, and each bullet still names its obligation. No bullet asserts
anything the key marks wrong.

Question 2: every reader states every required element of each item and quotes the document.
For 2a all five state that conformance is every MUST in sections 4 to 7 and that a detector
predating the document can conform, quoting section 8's definition or clause 8.1's "A Detector
that predates this document, or whose maintainer has never read it, MAY be graded Conforming on
evidence" (reader 1's quotation of section 8 drops "[Detector]", and quotes the document by the
nine-word run "if it satisfies every MUST in sections 4 to 7"; its 8.1 quotation is verbatim).
For 2b all five name both things and that either is enough, quoting clause 7.1's "For each one
it MUST do at least one of two things, and either alone satisfies this clause". Readers 2, 3
and 5 add that the bespoke-rule way of detection is closed to a detector whose rules never see
comments; reader 2 goes on to say that for an ignore comment the configuration switch or a
documented mechanical check is what remains. Neither is among the key's wrong assertions for
2b (removing or forbidding the route, or requiring a reason), and the answers are correct by the
rule. For 2c all five state the installed copy, the version tracked together and no network
access, quoting the headings of 6.2 and 6.3.

Question 3: all five give every accepted grade. Reader 2 grades 4.3 "Yes, with a caveat" about
machine-readable formats; the key accepts Yes with no condition on the reasoning and says a
caveat with the accepted grade is correct. S8: all five say Lintomatic does not conform, naming
6.3. 6.4: all five say it does not change the verdict, because it is a SHOULD.

### Misses

None.

## Question 4: passages named

Paragraphs as `ACCEPTANCE.md` defines them; "changed" means the diff 9e914fe..4cbecad adds,
rewords, moves or deletes a sentence in the paragraph, or changes a word, term or link in it.

| #   | Passage (clause, words or description)                                                                                                                                                                                                                                                                                                                            | Readers | Changed by the diff |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------- |
| 1   | Clause 5.3, first paragraph: "a report that only adds detail to those same findings, such as a code snippet, need not be named in the output" (1, took two readings to see whether the exemption covers the HTML report; 2, the subject of "need not be named" took two readings to settle)                                                                       | 1, 2    | yes                 |
| 2   | Clause 6.1, "For a project's own Rule" paragraph: "Where the [Identifier] is itself a URL, as method clause 3.6 allows, the [Detector] prints that URL and has done what this clause asks" (1 and 4, could not check method clause 3.6); "The lookup for such a [Rule] is an obligation on the project's assembled [Toolchain]" (5, set against passages 7 and 8) | 1, 4, 5 | no                  |
| 3   | Clause 4.3, first paragraph: "in its default output and in every machine-readable format it offers"; "machine-readable" not said, so whether the HTML report is covered                                                                                                                                                                                           | 2       | no                  |
| 4   | Clause 6.4, Why paragraph: "the [toolchain specification]'s self-audit makes this check a MUST for the [Toolchain]"; the reader was not given that document                                                                                                                                                                                                       | 2       | yes                 |
| 5   | Clause 8.1, second paragraph: "A Detector that predates this document, or whose maintainer has never read it, MAY be graded Conforming on evidence"; whether the MAY is a permission to the grader or an eligibility of the detector, settled by the next sentence                                                                                                | 3       | yes                 |
| 6   | Clause 7.1, second paragraph: "That way is open only where the [Detector]'s [Rules] can see the route: a [Detector] whose [Rules] never see comments cannot make an ignore comment detectable this way"; what it means for a rule to "see" a comment                                                                                                              | 4       | yes                 |
| 7   | Section 1, the governing principle paragraph: "a [Conforming] [Detector] MUST make that possible without the project building the mechanism first", set against passages 2 and 8                                                                                                                                                                                  | 5       | no                  |
| 8   | Clause 6.1 table, project's own row: "the lookup is the [Toolchain]'s to give", set against passage 7                                                                                                                                                                                                                                                             | 5       | no                  |

Notes, not passages: reader 5 says the fixture's `explain` paragraph and its last paragraph
disagree about which rules print `No documentation declared`; that is about the fixture, not
the document.

## Findings and where they lie

- **Finding A, passage 1, clause 5.3 first paragraph** (readers 1 and 2): the sentence both
  readers quote was added by the change, with "The remainder is the findings the summary leaves
  out." Text the change wrote. Blocks.
- **Finding B, passage 2, clause 6.1 "For a project's own Rule" paragraph** (readers 1, 4 and
  5): the diff does not touch this paragraph, and no reader naming it sets it against a
  paragraph the diff changed (reader 5 sets it against section 1's governing principle and the
  6.1 table's project row, both unchanged). Not the change's text. Routed to
  `acceptance/ROUTED.md`; does not block.

Passages 3 to 8 are each named by one reader: recorded, not findings. Passages 4, 5 and 6 lie
in changed paragraphs but are single.

## Points the rules did not settle

1. **Finding B, readers 1 and 4: a passage named for a reference to a document not supplied.**
   Both quote the URL sentence with its clause number, which `ACCEPTANCE.md` defines as naming a
   passage, and the confusion each gives is that method clause 3.6 is in a document they were
   not given. The rule that a remark that another document was not supplied is a note covers a
   remark "not about a passage of the document"; these remarks are attached to a quoted
   passage. Marked as the open-point rule says: an open point on whether a reader named a
   passage counts the passage. Without readers 1 and 4, reader 5 alone names the paragraph and
   there is no finding B. Finding A does not turn on this point. Reader 2's passage 4 is the
   same case, single either way.

## Process change

The run was made under the acceptance process change of pull request 22 before it merged,
following all of it at commit 4081aa4, named before the readers started.

## Against the criteria

- Load-bearing statements: five of five on 2a, 2b and 2c. Met.
- Restatement and application: five of five on question 1 and on every question 3 item. Met.
- A miss the key says counts against the document: none.
- Passages named by two or more readers in text the change wrote or altered: one (finding A).
  Not met.
- Passages named by two or more readers elsewhere: one (finding B), routed to
  `acceptance/ROUTED.md`.

## Findings applied

None at the time of marking; for the editor, under "After a failure" in `ACCEPTANCE.md`.

## Verdict

FAIL, on finding A alone; every keyed item passed its threshold.

## Answer sheets

Posted on the pull request: LINK TO BE ADDED.
