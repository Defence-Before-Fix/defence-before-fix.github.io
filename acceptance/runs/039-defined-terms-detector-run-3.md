# Run 39: DETECTOR-SPEC.md, defined terms, third run

- **Document**: DETECTOR-SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at 8517aa4, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness). Revision 1, after
  [run 32](032-defined-terms-detector-run-1.md), is 681ac42. The revision after
  [run 36](036-defined-terms-detector-run-2.md) is 0dac85a:

  - clause 5.3's two sentences on what the remainder is are reworded;
  - clause 7.1 has a sentence saying what a [Rule] in the [Detector] itself is;
  - clause 8.1 has a sentence saying the gap duty falls on a [Detector] that has a declaration.

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 32 or 36, model alias `haiku`; every reader
  reported `claude-haiku-5-5` in its JSON output

- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked two things:

  - the prompt is byte for byte the question set, the document and the fixture at 8517aa4, in
    that order. Each is preceded by one `===== FILE: <name> =====` line, and one blank line
    separates each file from the next;
  - each sheet is the `result` of its reader's JSON output (one turn, `is_error` false).

- **Run within the pull request**: 3

- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/detector/KEY.md`
  at 8517aa4, with the judgements of run 32

- **Verdict**: FAIL on one passage found confusing by all five readers: clause 7.1's sentence
  that revision 2 added, read against the base sentence before it. Every keyed item is five of
  five.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | 6.4 | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------- |
| 1      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |
| 2      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |
| 3      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | three       |
| 4      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |
| 5      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |

Every grade is the key's intended verdict.

### Question 1

Five of five correct, each with at least four bullets the key lists. None says the detector must
enforce a suppression policy, must declare a version, or must list defences or produce an agent
summary. Reader 5 says a declaration is optional.

### Question 2

- **2a**, five of five. Each says every MUST in sections 4 to 7 and that a predating detector can
  conform, quoting 8.1's "MAY be graded [Conforming] on evidence". Readers 2 and 3 also say the
  declaration is not required. Readers 1, 4 and 5 do not mention it, which is met under run 32's
  judgement J1, since none says a declaration is required.
- **2b**, five of five, each giving disableable or detectable, either alone enough, quoting 7.1.
- **2c**, five of five, each giving the installed copy and no network access and quoting both 6.2
  and 6.3, "at a version tracked together" included. Run 36's strict-reading note on 2c does not
  arise.

### Question 3

Five of five on every item. Every reader grades 5.3 Yes because the one-line output prints every
finding, so "there is no remainder". Every reader grades 7.1 Yes on the disableable branch, and
reader 1 notes it "did not need the detectable branch". Every reader says Lintomatic does not
conform because 6.3 fails, and that 6.4 does not change the verdict.

### Judgements made in marking

Run 32's judgements J1 to J3 are applied unchanged. None affects a mark or the count of a passage
here. The 7.1 passage is the same sentence for all five readers. Readers 1 to 4 quote it together
with the base sentence before it, and reader 5 quotes it alone and reads it "alongside" that
sentence.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                                                                              | Clause | Readers             | Text                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ------------------- | ----------------------------------------------- |
| "A [Rule] in the [Detector] itself is one that reports each use of the route, written in the [Detector]'s own [Rule] format and run by the [Detector], as a project's bespoke [Rule] under clause 4.1 is.", set against "by a [Rule] the project can write in the [Detector] itself" | 7.1    | five: 1, 2, 3, 4, 5 | Added by revision 2, set against untouched base |
| "That duty falls on a [Detector] that has a declaration, because the gap is recorded alongside the version declared; a [Detector] with no declaration has no version to record a gap alongside.", read with the gap MUST before it                                                   | 8.1    | one: 3              | Added by revision 2                             |
| "Terms from the method specification carry over unchanged", with the method and toolchain specifications not supplied                                                                                                                                                                | 2      | one: 3              | Untouched base                                  |

Note on the blocking passage. All five readers could not tell whether the rule that detects the
route is written by the project or shipped and run by the [Detector]. Reader 3 says the first
sentence "reads as though the project writes the rule into the detector" and the second
"describes a rule the detector runs". Reader 2 says "A [Rule] the project can write in the
[Detector] itself" points one way and "run by the [Detector], as a project's bespoke [Rule] under
clause 4.1 is" the other. The base sentence was named by one reader in run 32 and three in run
36; with the added sentence, it is named by five. No reader's 7.1 grade turns on it, since every
reader grades on the disableable branch.

Run 36's other two blocking passages are clear in this run:

- clause 5.3's remainder sentences, which revision 2 reworded (three readers in run 36); no reader
  quotes them;
- clause 8.1's gap MUST set against "The declaration is optional" (two readers in run 36); one
  reader quotes the sentence revision 2 added after it.

No reader quotes the Rule harness entry or any other sentence the original change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met, five of five
  throughout.
- A wrong answer traceable to the text, none: met.
- A passage found confusing by two or more, none outstanding: not met. Clause 7.1's added sentence
  defining a [Rule] in the [Detector] itself, set against the base sentence before it (five
  readers).
- From one reader only, recorded: clause 8.1's added sentence and section 2's "Terms from the
  method specification carry over unchanged".

**FAIL**, on question 4 alone. The blocking passage is a sentence revision 2 added (7.1), read
against untouched base text. It is not in text the change made.
