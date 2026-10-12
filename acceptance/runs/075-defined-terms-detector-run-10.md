# Run 75: DETECTOR-SPEC.md, defined terms, tenth run

- **Document**: DETECTOR-SPEC.md

- **Pull request and commit read**: the pull request is not yet opened; it will be opened from
  branch `editor/defined-terms`. The readers were given the question set, the document and the
  fixture at dc10670 ("Merge branch 'editor/detector-route-rule' into editor/defined-terms"). The
  branch carries `editor/detector-route-rule` (pull request 23) at d67174c, which reworked clauses
  5.3, 6.1, 7.1 and 8.1 and section 2's table; those paragraphs are that change's text. Read
  against 9e914fe, its merge base with `next`, and beyond the detector change
  (`git diff d67174c dc10670 -- DETECTOR-SPEC.md`), this change renames the defined term Harness
  to Rule harness: the terminology entry's heading, the entry's text (with the added sentence "It
  is not the environment an [Agent] runs in, which this document never means by the word
  *harness*."), section 3's "The red proof" row, the first paragraph of clause 4.2, the second
  paragraph of clause 8.1 ("the reader still runs the [Rule harness]") and the link definitions.
  Since run 69 it rewrote the last sentence of clause 4.2's first paragraph, from "a [Detector]
  failing 4.1 is graded here on its [Bundled rules]" to "A [Detector] that fails clause 4.1
  because it hosts no bespoke [Rules] is graded under this clause on its [Bundled rules] alone."
  Runs 32, 36, 39, 42, 45, 48 and 51 under the earlier rules, and runs 54 and 69 under these,
  came before it in this pull request.

- **Cohort**: five readers, none reused from any earlier run, model alias `haiku`. The cohort's
  model named for the run is `claude-haiku-5-5`, and every reader reported `claude-haiku-5-5`.

- **Isolation and command**, as the editor supplied them: each reader a separate `claude -p`
  process, started through the `ccy-claude` wrapper (which only reattaches the session's
  credential) in a fresh empty directory made by `mktemp -d` outside any repository, with the
  packet on standard input; no tools, no settings, no project context and no saved session; the
  machine applies no managed settings; the editor attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt's sha256 is
  9435f8b51fc3c98b6fbd4f29f0aa0af431ad8f2e9c97eb5d389e1d5ae5aff8ed and that it is byte for byte
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at dc10670, in that order, each
  after one `===== FILE: <name> =====` line, one blank line between files; and that each sheet is
  the `result` of its reader's JSON output, with `is_error` false, subtype `success` and
  `claude-haiku-5-5` the only model in its usage.

- **Readers set aside**: none.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's instruction and its agent definition, having seen neither the drafting nor the review.
  It marked against `ACCEPTANCE.md` and `acceptance/detector/KEY.md` at dc10670, and took no
  judgement from any earlier run record.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | 6.4 |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
| 1      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  |
| 2      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  |
| 3      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  |
| 4      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  |
| 5      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  |

Totals: every keyed item five of five. No miss.

### Question 1

Five of five. Every reader gives six bullets, and each reader's six name at least four
obligations on the key's list (4.1, 4.2, 4.3, 5.1 to 5.4, 6.1 to 6.3, 7.1). Reader 2 splits 5.1
to 5.3 from 5.4, different clauses of one line, which count separately. Readers 1 and 5 add to
their last bullet that a detector conforms only if it meets every MUST in sections 4 to 7; the
key says a bullet stating what conformance means asserts no obligation. No bullet asserts an
obligation the key marks wrong, and none asserts one on neither list.

### Question 2

- **2a**, five of five. Every reader states that a detector conforms when it satisfies every MUST
  in sections 4 to 7 and that a detector predating the document can conform, and quotes 8.1's
  "MAY be graded [Conforming] on evidence: anyone may grade it ..." sentence; readers 1, 3, 4 and
  5 also quote section 8's definition. No reader says a declaration is required or that partial
  satisfaction is conformance.
- **2b**, five of five. Every reader says either one of the two things is enough and names both,
  disableable by configuration and detectable; reader 2 names them in its quotation of 7.1's keyed
  sentence, which runs up to "make the route detectable", well over six consecutive words, and an
  element stated only in the quotation is stated. Readers 2, 4 and 5 also quote 7.1's sentence on
  a detector whose rules never see comments. No reader says the route must be removed or forbidden
  or must require a reason.
- **2c**, five of five. Every reader says the documentation ships with the rule (readers 1 and 4:
  in the installed copy or with the installed rule), at a version tracked together or the same
  version, and that it must resolve without network access, and quotes 6.2 and 6.3 (readers 1, 2,
  3 and 5 one or both headings). Reader 4 states element (3) in its quotation of 6.2's heading,
  "without network access". No reader names a networked location as acceptable; readers 3 and 4
  quote 6.2's sentence that a website catalogue is "the right documentation in the wrong place".

### Question 3

Every reader gives the accepted grade on all eleven clauses, 6.3 No and the rest Yes. Readers 1,
3, 4 and 5 add the caveat that the fixture does not say what `--only` prints, and several that it
names no machine-readable format; the key says a caveat with the accepted grade is correct.
Reader 4 gives 4.2 Yes and adds "If that is not accepted, 4.2 is Partial"; its grade is Yes,
stated outright, and the Partial is a caveat on what the fixture does not say, which the key's
line on caveats settles. Every reader says Lintomatic does not conform, naming 6.3, and that 6.4
does not change the verdict because it is a SHOULD. No miss, so no miss quotes the document.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                                                                        | Clause and paragraph                                        | Readers | In text the change wrote or altered?                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------- | ----------------------------------------------------------------------------- |
| "A [Detector] that fails clause 4.1 because it hosts no bespoke [Rules] is graded under this clause on its [Bundled rules] alone."; reader 1 read it twice, as possibly limiting how 4.2 applies to such a detector; reader 5, set against section 8, could not tell whether such a detector can still conform | 4.2, first paragraph                                        | 1, 5    | Yes: the change wrote this sentence and replaced `[Harness]` in the paragraph |
| "The remainder is the findings the summary leaves out."; reader 2 could not tell whether it restates the previous sentence or adds a condition, reader 4 whether "remainder" means the findings or their location                                                                                              | 5.3, first paragraph                                        | 2, 4    | No: the detector change's text, set against no paragraph this change altered  |
| "where the mechanism works but a [Bundled rule]'s [Identifier] has no documentation to resolve to, that fails clause 6.3, not this clause."; reader 3 had to reconcile it with 6.3                                                                                                                             | 6.1, the paragraph "In both, the mechanism is keyed on ..." | 3       | No (one reader; not a finding)                                                |

No reader made a remark under question 4 that is not about a passage.

## Findings and where they lie

1. **Clause 4.2, first paragraph** (readers 1 and 5): "A [Detector] that fails clause 4.1
   because it hosts no bespoke [Rules] is graded under this clause on its [Bundled rules]
   alone.", read against section 8's "every MUST", whether it limits or waives anything for a
   detector that fails 4.1. This change wrote the sentence, the revision made after run 69, and
   replaced `[Harness]` with `[Rule harness]` in the paragraph's first sentence, so the paragraph
   is text the change wrote or altered and the finding **blocks**.
2. **Clause 5.3, first paragraph** (readers 2 and 4): "The remainder is the findings the summary
   leaves out.", read against the preceding "the location of the remainder". Only the detector
   change altered this paragraph (`git diff d67174c dc10670` does not touch it), and both readers
   set it against the sentence before it in the same paragraph, not against a paragraph this
   change altered. Routed to `acceptance/ROUTED.md`; does not block. The open 5.3 row there,
   raised by run 69, names the earlier wording "MUST carry both a usable summary and the location
   of the remainder"; this passage is the sentence the detector change now carries, and whether
   it is noted on that row or listed afresh is the editor's.

## Points the rules did not settle

None. Every mark under questions 1 to 3 is given by a rule of `ACCEPTANCE.md` or a line of the
key, reader 4's 4.2 caveat by the key's line on caveats; every question 4 passage is a verbatim
quotation with its clause, and each finding's place is settled by the diff.

## Process change

Made under a process change before it merged: pull request 22, at commit bc6ae14, named in the
editor's instruction before the readers started, and followed in full. `ACCEPTANCE.md`,
`acceptance/README.md`, `acceptance/runs/README.md` and `CONTRIBUTING.md` are identical at
bc6ae14 and dc10670.

## Findings applied afterwards

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: met, five of five on 2a, 2b and 2c.
- Restatement and application, all but one reader correct on each keyed item: met, five of five
  on every item.
- A miss the key says counts against the document: none.
- A passage found confusing by two or more readers in text the change wrote or altered: not met,
  finding 1 (4.2, first paragraph).
- A passage found confusing by two or more readers elsewhere: finding 2 (5.3), routed.
- From one reader only, recorded: reader 3's 6.1 passage.

## Verdict

**FAIL**: every keyed item is five of five, but finding 1, clause 4.2's first paragraph, lies in
text the change wrote, the sentence revised after run 69, and blocks.

## Answer sheets

Answer sheets: LINK TO THE PULL REQUEST COMMENT, to be added when the pull request is opened.
