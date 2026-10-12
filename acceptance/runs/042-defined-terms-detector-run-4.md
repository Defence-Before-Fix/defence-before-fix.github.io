# Run 42: DETECTOR-SPEC.md, defined terms, fourth run

- **Document**: DETECTOR-SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at ff77998, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness). Revision 1, after
  [run 32](032-defined-terms-detector-run-1.md), is 681ac42; revision 2, after
  [run 36](036-defined-terms-detector-run-2.md), is 0dac85a. The revision after
  [run 39](039-defined-terms-detector-run-3.md) is 7a6b60b:

  - clause 7.1's sentence on a [Rule] in the [Detector] itself now says the project writes that
    [Rule], in the [Detector]'s own [Rule] language, and the [Detector] runs it as it runs any
    bespoke [Rule] under clause 4.1;
  - clause 8.1's sentence on the gap duty is shortened to "This duty, to record the gap in the
    declaration, falls only on a [Detector] that has one."

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 32, 36 or 39, model alias `haiku`; every reader
  reported `claude-haiku-5-5` in its JSON output

- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked two things:

  - the prompt is byte for byte the question set, the document and the fixture at ff77998, in
    that order. Each is preceded by one `===== FILE: <name> =====` line, and one blank line
    separates each file from the next;
  - each sheet is the `result` of its reader's JSON output (one turn, `is_error` false).

- **Run within the pull request**: 4

- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/detector/KEY.md`
  at ff77998, with the judgements of run 32

- **Verdict**: FAIL on two passages found confusing by two readers each: clause 8.1's gap MUST
  read with the sentence revision 3 wrote after it, and clause 7.1's untouched "detectable"
  sentence. Every keyed item is five of five.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | 6.4 | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------- |
| 1      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |
| 2      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |
| 3      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |
| 4      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |
| 5      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |

Every grade is the key's intended verdict.

### Question 1

Five of five correct, each with at least four bullets the key lists. None says the detector must
enforce a suppression policy, must declare a version, or must list defences or produce an agent
summary. Reader 5's last bullet adds that the detector "should require a reason" under 7.2, which
the document states as a SHOULD.

### Question 2

- **2a**, five of five. Each says every MUST in sections 4 to 7 and that a predating detector can
  conform, quoting section 8's definition or 8.1's "MAY be graded [Conforming] on evidence". No
  reader says a declaration is required, which is met under run 32's judgement J1.
- **2b**, five of five, each giving disableable or detectable and quoting 7.1. Reader 4 quotes the
  two branches and "A route that can be neither switched off nor seen does not [Conform]." and
  does not say "either alone"; it says neither that the route must be forbidden nor that a reason
  is required, so it is met under J1.
- **2c**, five of five. Readers 1, 2, 3 and 5 quote both 6.2 and 6.3. Reader 4 gives "sit in the
  installed copy and resolve without network access" and quotes 6.2 only, without 6.3's "at a
  version tracked together"; it rejects the website in so many words. As run 36 marked its reader
  4 under J1, the question's "where" is answered by the installed copy, and the tracked version is
  a gloss whose opposite reader 4 rejects. Read strictly, reader 4 would miss 2c and the first
  criterion would fail too. The verdict is FAIL either way.

### Question 3

Five of five on every item. Every reader grades 5.3 Yes because the one-line output prints every
finding, so there is no remainder. Every reader grades 7.1 Yes on the disableable branch. Every
reader says Lintomatic does not conform because 6.3 fails, and that 6.4 does not change the
verdict. Readers 1 and 5 place the two undocumented rules under 6.3 and not 6.1, as 6.1 directs.

### Judgements made in marking

Run 32's judgements J1 to J3 are applied unchanged. Under J3 (the same passage is the same
sentence), reader 4's 7.1 quotation is counted with reader 1's: both quote the base sentence
"make the route detectable, by a [Rule] the project can write in the [Detector] itself or by a
mechanical check the [Detector] documents", and reader 4 quotes revision 3's next sentence with
it. The two readers name different doubts, reader 1 whether the [Detector] must ship the
detecting [Rule] and reader 4 what the "mechanical check" alternative is; the criterion counts the
passage, not the doubt. Readers 2 and 3 each quote the same two sentences of 8.1.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                                                                               | Clause   | Readers   | Text                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------- | ------------------------------------------------------------------ |
| "a [Detector] that has learnt ... that it fails a MUST in sections 4 to 7 MUST record that gap alongside the version it declares", followed by "This duty, to record the gap in the declaration, falls only on a [Detector] that has one."                                            | 8.1      | two: 2, 3 | Added by revision 3, read with the untouched base MUST before it   |
| "make the route detectable, by a [Rule] the project can write in the [Detector] itself or by a mechanical check the [Detector] documents."                                                                                                                                            | 7.1      | two: 1, 4 | Untouched base; reader 4 quotes revision 3's next sentence with it |
| "where the mechanism works but a [Bundled rule]'s [Identifier] has no documentation to resolve to, that fails clause 6.3, not this clause", set against 6.3's "Every [Identifier] a [Bundled rule] can print MUST resolve, under clause 6.1, to a page in that shipped documentation" | 6.1, 6.3 | one: 5    | 6.1's sentence added by revision 1; 6.3's untouched base           |

Reader 2 also notes that it did not have the method or toolchain specifications and read their
terms from context; it says this is not a confusion and names no passage, so it is not counted.

Notes on the two blocking passages:

- **Clause 8.1, the gap duty.** Readers 2 and 3 read the MUST as binding on every [Detector] and
  the next sentence as narrowing it to one with a declaration, which is optional. Reader 2 took
  the second as controlling. Two readers named the base MUST against "The declaration is
  optional" in run 36; one reader named revision 2's sentence in run 39; revision 3's shorter
  sentence is named by two.
- **Clause 7.1, "detectable, by a [Rule] the project can write in the [Detector] itself".**
  Reader 1 could not tell whether the [Detector] must ship the detecting [Rule] or only let the
  project write one under 4.1; reader 1 does not quote revision 3's next sentence, which says the
  project writes it. Reader 4 says the "mechanical check the [Detector] documents" alternative is
  introduced and never described. No reader's 7.1 grade turns on it, since every reader grades on
  the disableable branch.

Run 39's blocking passage, the 7.1 sentence revision 2 added, is gone; revision 3's replacement is
quoted by one reader, reader 4, beside the base sentence. No reader quotes the Rule harness entry
or any other sentence the original change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met, five of five
  throughout.
- A wrong answer traceable to the text, none: met.
- A passage found confusing by two or more, none outstanding: not met. Clause 8.1's gap MUST with
  revision 3's sentence after it (two readers). Clause 7.1's "detectable" sentence (two readers),
  untouched base text.
- From one reader only, recorded: clause 6.1's sentence set against 6.3.

**FAIL**, on question 4 alone. One blocking passage is a sentence revision 3 wrote (8.1), read
against untouched base text; the other is untouched base text (7.1). Neither is in text the change
made.
