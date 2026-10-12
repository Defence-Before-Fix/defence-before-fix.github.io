# Run 69: DETECTOR-SPEC.md, defined terms, ninth run

- **Document**: DETECTOR-SPEC.md

- **Pull request and commit read**: the pull request is [24](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24), opened later from
  branch `editor/defined-terms`. The readers were given the question set, the document and the
  fixture at b8ffb28 ("Merge branch 'editor/detector-route-rule' into editor/defined-terms").
  Since run 54 the branch has merged `editor/detector-route-rule` (pull request 23, accepted by
  run 66), which reworked clauses 5.3, 6.1, 7.1 and 8.1 and section 2's table; those paragraphs
  are that change's text. Read against 9e914fe, its merge base with `next`, and beyond the
  detector change (`git diff editor/detector-route-rule b8ffb28 -- DETECTOR-SPEC.md`), this change
  renames the defined term Harness to Rule harness: the terminology entry's heading, the entry's
  text (one sentence added: "It is not the environment an [Agent] runs in, which this document
  never means by the word *harness*."), section 3's "The red proof" row, the first paragraph of
  clause 4.2, the second paragraph of clause 8.1 ("the reader still runs the [Rule harness]") and
  the link definitions. Runs 32, 36, 39, 42, 45, 48 and 51 under the earlier rules, and run 54
  under these, came before it in this pull request.

- **Cohort**: five readers, none reused from any earlier run, model alias `haiku`. The cohort's
  model named for the run is `claude-haiku-5-5`, and every reader reported `claude-haiku-5-5`.

- **Isolation and command**, as the editor supplied them: each reader a separate `claude -p`
  process, started through the `ccy-claude` wrapper (which only reattaches the session's
  credential) in a fresh empty directory made by `mktemp -d` outside any repository, with the
  packet on standard input; no tools, no settings, no project context and no saved session; the
  machine applies no managed settings; the editor attests the rest of the isolation. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt's sha256 is
  988f0fdb18096874183842eca99bfeeb7348cff2334c01302956b35ddc731c70 and that it is byte for byte
  `QUESTIONS.md`, `DETECTOR-SPEC.md` and `fixtures/lintomatic.md` at b8ffb28, in that order, each
  after one `===== FILE: <name> =====` line, one blank line between files; and that each sheet is
  the `result` of its reader's JSON output, with `is_error` false and subtype `success`.

- **Readers set aside**: none.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's instruction and its agent definition, having seen neither the drafting nor the review.
  It marked against `ACCEPTANCE.md` and `acceptance/detector/KEY.md` at b8ffb28, and took no
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

Five of five. Readers 3 and 5 give seven bullets, and only their first six are marked. Every
reader's first six bullets name at least four obligations on the key's list (4.1, 4.2, 4.3, 5.1
to 5.4, 6.1 to 6.3, 7.1); readers 1 and 2 put 6.1 to 6.3 and 7.1 in one bullet. Reader 4's
"every finding must appear in the output of the command run" is the plural the key says is not
wrong. No bullet asserts an obligation the key marks wrong, and none asserts one on neither list.

### Question 2

- **2a**, five of five. Every reader states that a detector conforms when it satisfies every MUST
  in sections 4 to 7 and that a detector predating the document can conform, and quotes 8.1's
  "MAY be graded [Conforming] on evidence: anyone may grade it ..." sentence; readers 1, 2, 4 and
  5 also quote section 8's definition, and readers 2, 3 and 5 8.1's "it is not a condition of
  it". No reader says a declaration is required or that partial satisfaction is conformance.
- **2b**, five of five. Every reader names both the disableable and the detectable route and says
  either alone is enough, and quotes 7.1's keyed sentence (reader 3 with an ellipsis, reader 4 up
  to "make the route detectable", each well over six consecutive words). No reader says the route
  must be removed or forbidden or must require a reason; readers 3 and 5 say 7.2 is a SHOULD.
- **2c**, five of five. Every reader says the documentation ships with the rule (reader 2: "in the
  installed package"), at a version tracked together or the same version, resolvable without
  network access, and quotes 6.2 and 6.3 (reader 2 their headings). No reader names a networked
  location as acceptable; reader 4 says a website catalogue does not count.

### Question 3

Every reader gives the accepted grade on all eleven clauses, 6.3 No and the rest Yes. Several add
the caveat that the fixture does not say what `--only` prints, or names no machine-readable
format; the key says such a caveat with the accepted grade is correct. Every reader says
Lintomatic does not conform, naming 6.3, and that 6.4 does not change the verdict because it is a
SHOULD. No miss, so no miss quotes the document.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                                                                      | Clause and paragraph                            | Readers | In text the change wrote or altered?                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- | ------- | ---------------------------------------------------------------------------- |
| "a [Detector] failing 4.1 is graded here on its [Bundled rules]."; reader 1 could not tell whether bespoke rules are graded at all under 4.2 for such a detector, reader 5 whether it is judged on bundled rules alone or only which rules are tested changes                                                | 4.2, first paragraph                            | 1, 5    | Yes: the change replaced `[Harness]` with `[Rule harness]` in it             |
| "Where the [Detector] writes fuller detail elsewhere, the invoked command's own output MUST carry both a usable summary and the location of the remainder." against "A fuller report written elsewhere ... is not a remainder, and the output need not name it."; how the first applies when the second does | 5.3, first paragraph                            | 2, 4    | No: the detector change's text, set against no paragraph this change altered |
| "The declaration is optional, and so the duty above falls only on a [Detector] that has one; a gap a [Practitioner] finds is recorded under the method's clause 3.2 in any case."; reader 3 says the clause does not say where that record is kept, the method specification not being given                 | 8.1, second paragraph                           | 3       | Yes: the change replaced `[Harness]` with `[Rule harness]` in it             |
| "A [Detector] that predates this document ... MAY be graded [Conforming] on evidence."; reader 4 could not tell whether the MAY permits a grader to assign the verdict or describes the detector's status                                                                                                    | 8.1, second paragraph                           | 4       | Yes: as above                                                                |
| "The lookup for such a [Rule] is an obligation on the project's assembled [Toolchain], under clause 4.2 of the [toolchain specification](TOOLING-SPEC.md)."; the reader could not check it without that document                                                                                             | 6.1, the "For a project's own [Rule]" paragraph | 3       | No (one reader; not a finding)                                               |
| "A [Detector] that is not also shipped as a [Toolchain] leaves `toolchain` empty", against the example's `"toolchain": null`; whether "empty" means null, an empty string or an empty array                                                                                                                  | 8.1, the "In a package.json" paragraph          | 5       | No (one reader; not a finding)                                               |

Reader 3's 8.1 and reader 4's 8.1 passages lie in the same paragraph, so 8.1's second paragraph is
named by readers 3 and 4.

## Findings and where they lie

1. **Clause 4.2, first paragraph** (readers 1 and 5): "a [Detector] failing 4.1 is graded here on
   its [Bundled rules]", what a detector failing 4.1 is graded on. The paragraph's first sentence
   is one in which the change replaced the link `[Harness]` with `[Rule harness]`, so under "Where
   a finding lies" the paragraph is text the change altered, and this finding **blocks**.
2. **Clause 8.1, second paragraph** (readers 3 and 4): reader 3 on the gap "recorded under the
   method's clause 3.2 in any case", reader 4 on "MAY be graded [Conforming] on evidence". The
   paragraph was reworded by the detector change, and in its last sentence this change replaced
   `[Harness]` with `[Rule harness]`, so it is text this change altered and the finding
   **blocks**. It is a finding only if reader 3's remark names a passage; see below.
3. **Clause 5.3, first paragraph** (readers 2 and 4): the "location of the remainder" MUST against
   the later "need not name it". Only the detector change altered this paragraph, and neither
   reader sets it against a paragraph this change altered; routed to `acceptance/ROUTED.md`, a new
   row (the existing 5.3 row from run 32 was closed by run 66 on the text now named). Does not
   block.

## Points the rules did not settle

- **Whether reader 3's 8.1 remark names a passage** (finding 2). Reader 3 quotes the sentence
  verbatim and says the clause does not say where the record is kept, adding that the method
  specification was not given. `ACCEPTANCE.md` makes a remark that another document was not
  supplied a note where the remark is not about a passage; this one quotes a sentence of the
  document and finds that sentence unclear. Marked, by the open-point rule, as counting the
  passage, so finding 2 stands. Finding 1 blocks without it, so the verdict does not turn on it.
- **Reader 3's 6.1 cross-reference passage**, under the same question, is counted as a passage by
  the same rule. It is one reader's, so it does not change the verdict.

No mark is open: every question 1 to 3 mark is given by a rule of `ACCEPTANCE.md` or a line of the
key.

## Process change

Made under a process change before it merged: pull request 22, at commit f3ec69e, named in the
editor's instruction before the readers started, and followed in full. `ACCEPTANCE.md`,
`acceptance/README.md`, `acceptance/runs/README.md` and `CONTRIBUTING.md` are identical at
f3ec69e and b8ffb28.

## Findings applied afterwards

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: met, five of five on 2a, 2b and 2c.
- Restatement and application, all but one reader correct on each keyed item: met, five of five
  on every item.
- A miss the key says counts against the document: none.
- A passage found confusing by two or more readers in text the change wrote or altered: not met,
  findings 1 (4.2, first paragraph) and 2 (8.1, second paragraph).
- A passage found confusing by two or more readers elsewhere: finding 3 (5.3), routed.
- From one reader only, recorded: the two single-reader passages above.

## Verdict

**FAIL**: every keyed item is five of five, but finding 1, clause 4.2's first paragraph, and
finding 2, clause 8.1's second paragraph, each lie in a paragraph whose link the change altered,
and each blocks.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125406516); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125405992); [the prompt](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125407114).
