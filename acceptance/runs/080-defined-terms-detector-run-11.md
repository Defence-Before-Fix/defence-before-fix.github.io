# Run 80: DETECTOR-SPEC.md, defined terms, eleventh run

- **Document**: DETECTOR-SPEC.md

- **Pull request and commit read**: the pull request is [24](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24), opened later from
  branch `editor/defined-terms`. The readers were given the question set, the document and the
  fixture at e2e4eef ("Changelog: clause links point at the headings as they are"). The branch
  carries `editor/detector-route-rule` (pull request 23) at d67174c, which reworked clauses 5.3,
  6.1, 7.1 and 8.1 and section 2's table; those paragraphs are that change's text. Read against
  9e914fe, its merge base with `next`, and beyond the detector change
  (`git diff d67174c e2e4eef -- DETECTOR-SPEC.md`), this change renames the defined term Harness
  to Rule harness: the terminology entry's heading, the entry's text (with the added sentence "It
  is not the environment an [Agent] runs in, which this document never means by the word
  *harness*."), section 3's "The red proof" row, the first paragraph of clause 4.2, the second
  paragraph of clause 8.1 ("the reader still runs the [Rule harness]") and the link definitions.
  Since run 75 it removed clause 4.2's sentence on a detector that fails clause 4.1, so that the
  paragraph now ends "bundled or bespoke." Runs 32, 36, 39, 42, 45, 48 and 51 under the earlier
  rules, and runs 54, 69 and 75 under these, came before it in this pull request.

- **Cohort**: five readers, none reused from any earlier run, model alias `haiku`. The cohort's
  model named for the run is `claude-haiku-5-5`, and every reader reported `claude-haiku-5-5`.

- **Isolation and command**, as the editor supplied them: each reader a separate `claude -p`
  process, started through the `ccy-claude` wrapper (which only reattaches the session's
  credential) in a fresh empty directory made by `mktemp -d` outside any repository, with the
  packet on standard input; no tools, no settings, no project context and no saved session; the
  machine applies no managed settings; the editor attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt's sha256 is
  cdc6c22d9617c5de6df7e2f3a9d73ee911ceb8643f4577baec2b7a9477481724 and that it is byte for byte
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at e2e4eef, in that order, each
  after one `===== FILE: <name> =====` line, one blank line between files; and that each sheet is
  the `result` of its reader's JSON output, with `is_error` false, subtype `success` and
  `claude-haiku-5-5` the only model in its usage.

- **Readers set aside**: none.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's instruction and its agent definition, having seen neither the drafting nor the review.
  It marked against `ACCEPTANCE.md` and `acceptance/detector/KEY.md` at e2e4eef, and took no
  judgement from any earlier run record.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2         | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | 6.4 |
| ------ | ------- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
| 1      | correct | ok  | ok  | ok  | Yes | Yes         | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  |
| 2      | correct | ok  | ok  | ok  | Yes | Yes (open)  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  |
| 3      | correct | ok  | ok  | ok  | Yes | **Partial** | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  |
| 4      | correct | ok  | ok  | ok  | Yes | Yes         | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  |
| 5      | correct | ok  | ok  | ok  | Yes | Yes         | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  |

Totals: clause 4.2 four of five, reader 2's mark given under the open-point rule (see below);
every other keyed item five of five. One miss.

### Question 1

Five of five. Every reader gives six bullets, and each reader's six name at least four
obligations on the key's list (4.1, 4.2, 4.3, 5.1 to 5.4, 6.1 to 6.3, 7.1). Readers 3 and 4
split 5.4 from 5.1 to 5.3, different clauses of one line, which count separately. Reader 1's last
bullet adds that requiring a reason is a SHOULD, and reader 3's that a detector conforms when it
meets every MUST in sections 4 to 7; the key says a bullet restating a SHOULD as advice, or
stating what conformance means, asserts no obligation. No bullet asserts an obligation the key
marks wrong, and none asserts one on neither list.

### Question 2

- **2a**, five of five. Every reader states that a detector conforms when it satisfies every MUST
  in sections 4 to 7 and that a detector predating the document can conform, and quotes 8.1's
  "MAY be graded [Conforming] on evidence" sentence; readers 2, 3, 4 and 5 also quote section 8's
  definition. No reader says a declaration is required or that partial satisfaction is
  conformance.
- **2b**, five of five. Every reader names both things, disableable by configuration and
  detectable, says either one alone is enough, and quotes 7.1's keyed sentence (reader 4 up to
  "make the route detectable", well over six consecutive words). Readers 1, 2, 3 and 5 also say,
  quoting 7.1's second paragraph, that the bespoke-rule way is closed to a detector whose rules
  never see comments; that is in the document and is not a wrong assertion. No reader says the
  route must be removed or forbidden or must require a reason.
- **2c**, five of five. Every reader says the documentation ships with the rule (on disk, in the
  installed package or with the installed rule), at a version tracked together with it, and that
  it must be reachable without network access, and quotes 6.2 and 6.3. Reader 4's 6.2 quotation
  puts the heading's subject in square brackets; "MUST work from the installed copy, without
  network access" is a verbatim run of well over six words. No reader names a networked location
  as acceptable; readers 1, 3 and 5 say a website does not serve.

### Question 3

Every reader gives the accepted grade on ten of the eleven clauses, 6.3 No and the rest Yes;
every reader says Lintomatic does not conform, naming 6.3, and that 6.4 does not change the
verdict because it is a SHOULD. Readers 1, 4 and 5 add to 4.2 Yes the caveat that the fixture
does not say what `--only` prints, and several that it names no machine-readable format for 4.3;
the key says a caveat with the accepted grade is correct.

- **Reader 3, clause 4.2, Partial** (miss): "`--only` runs one rule and its exit code shows
  whether it fired, but the fixture never says it prints what the rule printed." The key accepts
  Yes only. The key names no wrong reading for 4.2, so this is a single miss, the reader's, and
  is tolerated by the threshold. The reasoning does not quote the document: it quotes nothing of
  the document's, and "what the rule printed" is four words and not the document's order
  ("what it printed").
- **Reader 2, clause 4.2, Yes on a stated condition**: "this grade assumes the `check` output
  format applies. If it does not, this becomes Partial." Marked correct as an open point; see
  below.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                    | Clause and paragraph                                                                   | Readers | In text the change wrote or altered?                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------- |
| "That way is open only where the [Detector]'s [Rules] can see the route: a [Detector] whose [Rules] never see comments cannot make an ignore comment detectable this way."; the reader could not tell what follows for rules that see comments only partly | 7.1, second paragraph ("A route is detectable when ...")                               | 2       | No: the detector change's text; one reader, not a finding                                                           |
| "A [Detector] that predates this document, or whose maintainer has never read it, MAY be graded [Conforming] on evidence: anyone may grade it."; the reader could not tell whether the MAY permits the grader or describes the detector                    | 8.1, second paragraph ("The declaration is optional ...")                              | 3       | The paragraph is one this change altered (its last sentence's `[Rule harness]` link), but one reader; not a finding |
| "The remainder is the findings the summary leaves out."; the reader took it as circular                                                                                                                                                                    | 5.3, first paragraph                                                                   | 4       | No: the detector change's text; one reader, not a finding                                                           |
| "a [Conforming] [Detector] MUST make that possible without the project building the mechanism first."; set against section 8, the reader could not tell whether it adds an obligation                                                                      | Section 1, the governing principle paragraph                                           | 5       | No; one reader, not a finding                                                                                       |
| "provide a mechanism that resolves a printed identifier to its documentation" against "Print the [Identifier] unaltered; the lookup is the [Toolchain]'s to give"; whether printing alone meets the MUST for a project's own rule                          | 6.1, the heading and the table's "The project's own" row (each a paragraph of its own) | 5       | No: the detector change's text; one reader, not a finding                                                           |
| "resolve … to a page in that shipped documentation"; "page" not defined                                                                                                                                                                                    | 6.3, first paragraph                                                                   | 5       | No; one reader, not a finding                                                                                       |

Notes, not passages: reader 3 says the fixture's two sentences on `No documentation declared`
disagree about which rules print it; reader 5 says it was not given SPEC.md or TOOLING-SPEC.md.
Neither is about a passage of the document.

## Findings and where they lie

None. No passage was named by two or more readers: the six passages lie in six different
paragraphs, and no reader names a paragraph another reader names. Nothing is routed to
`acceptance/ROUTED.md` from this run.

## Points the rules did not settle

1. **Reader 2's clause 4.2 grade.** Reader 2 gives Yes and says the grade assumes `--only` prints
   in the `check` format, and that it becomes Partial otherwise. `ACCEPTANCE.md` reads a grade
   given on a stated condition as the grade for the case the fixture presents "where the key says
   which case that is; otherwise the item is unanswered", and the key's 4.2 row does not say
   whether the fixture's `--only` prints what the rule printed. The key also says that "a reader
   who adds a caveat about what the fixture does not say and still gives the accepted grade is
   correct", which describes this answer as well. The two rules give opposite marks and neither
   says which governs, so this is an open point in marking an answer, and it is **marked for the
   reader**, as the open-point rule says: correct. Marked against the reader, 4.2 would carry a
   second miss and fail the all-but-one threshold, and the run would fail. The editor settles it
   in the key (for example by the 4.2 row saying which case the fixture presents, as 13b497b did
   for the toolchain key's 4.3 row) or in `ACCEPTANCE.md`, before the next run of this pull
   request.

No other point: every question 4 passage is a verbatim quotation with its clause, and no two
lie in the same paragraph.

## Process change

Made under a process change before it merged: pull request 22, at commit 13b497b, named in the
editor's instruction before the readers started, and followed in full. `ACCEPTANCE.md`,
`acceptance/README.md`, `acceptance/runs/README.md` and `CONTRIBUTING.md` are identical at
13b497b and e2e4eef.

## Findings applied afterwards

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: met, five of five on 2a, 2b and 2c.
- Restatement and application, all but one reader correct on each keyed item: met; clause 4.2
  four of five (reader 3's miss; reader 2 marked for the reader under the open-point rule),
  every other item five of five.
- A miss the key says counts against the document: none. Reader 3's 4.2 Partial matches no
  wrong reading the key names.
- A passage found confusing by two or more readers in text the change wrote or altered: none.
- A passage found confusing by two or more readers elsewhere: none.
- From one reader only, recorded: the six passages above, one of them (reader 3's, 8.1) in a
  paragraph this change altered.

## Verdict

**PASS**, with reader 2's 4.2 mark given for the reader under the open-point rule; marked the
other way, the run fails on clause 4.2.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125409199); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125408706); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125409592).
