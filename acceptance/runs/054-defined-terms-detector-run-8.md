# Run 54: DETECTOR-SPEC.md, defined terms, eighth run

- **Document**: DETECTOR-SPEC.md

- **Pull request and commit read**: the pull request is [24](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24), opened later from
  branch `editor/defined-terms`. The readers were given the question set, the document and the
  fixture at 8e91f8a ("the text returned to the original change"). The change, read against
  9e914fe, its merge base with `next`, renames the defined term Harness to Rule harness: the
  terminology entry's heading, the entry's text (one sentence added: "It is not the environment an
  [Agent] runs in, which this document never means by the word *harness*."), section 3's "The red
  proof" row, the first paragraph of clause 4.2, the second paragraph of clause 8.1 ("the reader
  still runs the [Rule harness]") and the link definitions. Runs 32, 36, 39, 42, 45, 48 and 51
  came before it in this pull request, under the earlier rules.

- **Cohort**: five readers, none reused from any earlier run, model alias `haiku`. The cohort's
  model named for the run is `claude-haiku-5-5`, and every reader reported `claude-haiku-5-5`.

- **Isolation and command**, as the editor supplied them: each reader a separate `claude -p`
  process, started through the `ccy-claude` wrapper (which only reattaches the session's
  credential) in a fresh empty directory made by `mktemp -d` outside any repository, with the
  packet on standard input; no tools, no settings, no project context and no saved session; the
  machine applies no managed settings; the editor attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt's sha256 is
  3e8e8c8fbc15b37683168c5989892eb6212739fa4ea9ea38a36f0ee1c782a8fb and that it is byte for byte
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at 8e91f8a, in that order, each
  after one `===== FILE: <name> =====` line, one blank line between files; and that each sheet is
  the `result` of its reader's JSON output, with `is_error` false and subtype `success`.

- **Readers set aside**: none.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's instruction and its agent definition, having seen neither the drafting nor the review.
  It marked against `ACCEPTANCE.md` and `acceptance/detector/KEY.md` at 8e91f8a, and read no run
  record of this branch for its judgements.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3            | 5.4 | 6.1            | 6.2 | 6.3 | 7.1 | Section 8 | 6.4 |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | --- | --- | --- | --------- | --- |
| 1      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Partial (miss) | Yes | Partial (miss) | Yes | No  | Yes | ok        | ok  |
| 2      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Partial (miss) | Yes | Yes            | Yes | No  | Yes | ok        | ok  |
| 3      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Partial (miss) | Yes | Yes            | Yes | No  | Yes | ok        | ok  |
| 4      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | No (miss)      | Yes | Yes            | Yes | No  | Yes | ok        | ok  |
| 5      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Partial (miss) | Yes | Partial (miss) | Yes | No  | Yes | ok        | ok  |

Totals: question 1 five of five; 2a, 2b and 2c five of five; 5.3 none of five; 6.1 three of five;
every other question 3 item five of five.

### Question 1

Five of five. Each reader gives six bullets, at least four naming obligations on the key's list
(4.1, 4.2, 4.3, 5.1 to 5.4, 6.1 to 6.3, 7.1). Readers 2 and 5 add, inside their sixth bullet, what
conformance means, which the key says asserts no obligation. Reader 4's "Findings must reach the
command's own output" is the plural the key says is not wrong. No bullet asserts an obligation the
key marks wrong, and none asserts one on neither list.

### Question 2

- **2a**, five of five. Every reader states that a detector conforms when it satisfies every MUST
  in sections 4 to 7 and that a detector predating the document can conform. Readers 1, 3, 4 and
  5 quote section 8's definition and 8.1's "MAY be graded [Conforming] on evidence ..." sentence;
  reader 2 quotes 8.1's "graded Conforming on evidence by anyone who exercises the clauses above
  against it" and "optional. It is how a maintainer claims Conformance; it is not a condition of
  it". No reader says a declaration is required or that partial satisfaction is conformance.
- **2b**, five of five. Every reader names both the disableable and the detectable route, and
  says one alone is enough; readers 2 and 5 name the two routes in the quotation of 7.1's keyed
  sentence, which states the element. Every reader quotes that sentence. No reader says the route
  must be removed or forbidden or must require a reason; readers 2 and 4 say 7.2 is a SHOULD.
- **2c**, five of five. Every reader says the documentation ships with the rule in the installed
  copy, at the same or a tracked-together version, reachable without network access, and quotes
  6.2 and 6.3. Reader 2 states element (2) in its quotation of 6.3. No reader names a networked
  location as acceptable; reader 2 quotes 6.2's reason that a website is "the right documentation
  in the wrong place".

### Question 3

Accepted grades given by every reader on 4.1, 4.2, 4.3, 5.1, 5.2, 5.4, 6.2, 6.3 and 7.1. Every
reader says Lintomatic does not conform, naming 6.3; readers 1, 2, 3 and 5 also name 5.3 as
Partial and reader 4 as failing, and readers 1 and 5 also name 6.1, which the condition does not
exclude. Every reader says 6.4 does not change the verdict because it is a SHOULD.

The misses, none matching a wrong reading the key names (the key names readings for 6.3 and 7.1
only), and none quoting six or more consecutive words of the document in its reasoning:

- **5.3, every reader.** The key accepts Yes only. Readers 1, 2, 3 and 5 grade Partial and reader
  4 grades No, each for the same reason: the one-line summary is on standard output, but nothing
  in the fixture says that output gives the location of `.lintomatic/report.html`, where the
  fuller detail goes. Reader 2 calls this "the second limb of the MUST"; reader 4 says "The clause
  requires both."
- **6.1, readers 1 and 5.** The key accepts Yes only. Both grade Partial: `explain` is keyed on the
  identifier alone, but two bundled identifiers resolve to "No documentation declared", so they do
  not resolve to documentation. Both also grade 6.3 No on the same two rules.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                   | Clause and paragraph                                    | Readers | In text the change wrote or altered?                                                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------- |
| "A [Message] that carries its own documentation path resolves that [Message], not the [Identifier]."; each reader says Message is not defined in what it was given                                                                                        | 6.1, the "For a [Bundled rule]" paragraph               | 1, 4, 5 | No                                                                                                                  |
| "make the route detectable, by a [Rule] the project can write in the [Detector] itself"; readers 3 and 4 could not tell what it means, reader 4 whether it is a rule in the detector's own set or one the project loads into it; reader 5 quotes it alone | 7.1, first paragraph                                    | 3, 4, 5 | No                                                                                                                  |
| "The same declaration is where a gap against this document is recorded once it is known: a [Detector] that has learnt ... MUST record that gap alongside the version it declares", set by both readers against the declaration being optional             | 8.1, first paragraph                                    | 2, 3    | Yes: set against 8.1's second paragraph, "The declaration is optional. ...", whose last sentence the change altered |
| "A [Detector] that predates this document ... MAY be graded [Conforming] on evidence by anyone who exercises the clauses above"; whether MAY grants a permission or describes what is possible                                                            | 8.1, second paragraph                                   | 1       | Yes (one reader; not a finding)                                                                                     |
| "Where the [Identifier] is itself a URL, as method clause 3.6 allows" and "under clause 4.2 of the [toolchain specification]"; the reader could not check them without the other documents                                                                | 6.1, the "For a project's own [Rule]" paragraph         | 1       | No (one reader; not a finding)                                                                                      |
| Section 3's "Choosing it once" and 4.3's "The [Rule author] chooses it once", against the 4.3 table's "Assigned once by the [Detector]'s maintainer" and the Bundled rule entry                                                                           | Section 3, "The [Identifier]" row; 4.3, first paragraph | 3       | No (one reader; not a finding)                                                                                      |

## Findings and where they lie

1. **Clause 8.1, first paragraph** (readers 2 and 3): the MUST to record a known gap "alongside
   the version it declares" against the declaration being optional. Reader 2 sets it against
   "a declaration, which the same clause says is optional", reader 3 against "The same section
   says the declaration is optional". The words "The declaration is optional" are 8.1's second
   paragraph, in which the change replaced the link `[Harness]` with `[Rule harness]`. Under
   "Where a finding lies", a paragraph a reader naming the finding sets against a paragraph whose
   link the change changed is text the change wrote or altered, so this finding **blocks**. Were
   it doubted whether "the same clause" means that paragraph or 8.1's heading, the open-point
   rule treats the finding as the change's own text, so it blocks either way.
2. **Clause 6.1, the "For a [Bundled rule]" paragraph** (readers 1, 4 and 5): the [Message]
   sentence. Not in text the change wrote or altered, and set against no such paragraph; routed to
   `acceptance/ROUTED.md`, a new row. Does not block.
3. **Clause 7.1, first paragraph** (readers 3, 4 and 5): "by a [Rule] the project can write in the
   [Detector] itself". Not in text the change wrote or altered, and set against no such paragraph;
   routed to `acceptance/ROUTED.md`, where it is the existing 7.1 row, to be noted as raised again
   by run 54. Does not block.

## Points the rules did not settle

- **Whether the [Message] sentence was named** (finding 2). Readers 1, 4 and 5 quote it and give
  as their difficulty that the definition is in the method specification, which they were not
  given. `ACCEPTANCE.md` makes a remark that another document was not supplied a note, not a
  passage, where the remark is not about a passage; these quote a sentence of the document and say
  they could not tell what it means. Marked, by the open-point rule, as counting the passage. It
  is routed, so it does not change the verdict.
- **Reader 1's 6.1 cross-reference passage**, under the same question, is counted as a passage by
  the same rule. It is one reader's, so it does not change the verdict.

No mark is open: every question 1 to 3 mark is given by a rule of `ACCEPTANCE.md` or a line of the
key. For the editor, not as a judgement on any mark: the key's 5.3 row accepts Yes with the note
that the HTML report "need not be named", and all five readers instead apply 5.3's sentence "the
invoked command's own output MUST carry both a usable summary and the location of the remainder"
to the fixture's "Fuller detail, including a snippet, is written to `.lintomatic/report.html`".
`acceptance/ROUTED.md` already lists 5.3's "the location of the remainder", from run 32.

## Process change

Made under a process change before it merged: pull request 22, at commit c31d49a, named in the
editor's instruction before the readers started, and followed in full.

## Findings applied afterwards

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: met, five of five on 2a, 2b and 2c.
- Restatement and application, all but one reader correct on each keyed item: not met. 5.3 is
  none of five; 6.1 is three of five.
- A miss the key says counts against the document: none.
- A passage found confusing by two or more readers in text the change wrote or altered: not met,
  finding 1 (8.1, first paragraph).
- A passage found confusing by two or more readers elsewhere: findings 2 and 3, routed.
- From one reader only, recorded: the three single-reader passages above.

## Verdict

**FAIL**: application items 5.3 (none of five) and 6.1 (three of five) fail the threshold, and
finding 1, clause 8.1's gap-record MUST set against the paragraph the change altered, blocks.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125396813); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125396439); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125397292).
