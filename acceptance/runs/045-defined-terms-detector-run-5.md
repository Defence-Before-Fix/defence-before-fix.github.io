# Run 45: DETECTOR-SPEC.md, defined terms, fifth run

- **Document**: DETECTOR-SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at c1c461c, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness). Revision 1, after
  [run 32](032-defined-terms-detector-run-1.md), is 681ac42; revision 2, after
  [run 36](036-defined-terms-detector-run-2.md), is 0dac85a; revision 3, after
  [run 39](039-defined-terms-detector-run-3.md), is 7a6b60b. The revision after
  [run 42](042-defined-terms-detector-run-4.md) is 99396df:

  - clause 8.1's gap MUST takes "a [Detector] that declares a version and has learnt ..." as its
    subject and records the gap "alongside that version"; revision 3's sentence after it, "This
    duty, to record the gap in the declaration, falls only on a [Detector] that has one.", is cut;
  - in clause 7.1, the sentence after the keyed MUST now reads "That [Rule], or that check,
    reports each use of the route. The project writes the [Rule], in the [Detector]'s own [Rule]
    language, and the [Detector] runs it as it runs any bespoke [Rule] under clause 4.1." The keyed
    MUST sentence is unchanged.

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 32, 36, 39 or 42, model alias `haiku`; every
  reader reported `claude-haiku-5-5` in its JSON output

- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked two things:

  - the prompt is byte for byte the question set, the document and the fixture at c1c461c, in
    that order. Each is preceded by one `===== FILE: <name> =====` line, and one blank line
    separates each file from the next;
  - each sheet is the `result` of its reader's JSON output (one turn, `is_error` false).

- **Run within the pull request**: 5

- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/detector/KEY.md`
  at c1c461c, with the judgements of run 32

- **Verdict**: FAIL on two passages of clause 7.1 found confusing by two or more readers: the
  untouched "detectable" sentence (three readers), and the sentence revision 4 wrote on who
  writes the detecting [Rule] (two readers). Every keyed item is five of five.

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
summary. Reader 3 says declaring a version is optional.

### Question 2

- **2a**, five of five. Each says every MUST in sections 4 to 7 and that a predating detector can
  conform. Readers 1, 2, 3 and 5 quote section 8's definition and 8.1's "MAY be graded
  [Conforming] on evidence"; reader 4 states the definition and quotes 8.1. Readers 4 and 5 say
  the declaration is optional; no reader says it is required.
- **2b**, five of five, each giving disableable or detectable, each saying either alone is
  enough, and each quoting 7.1. None says the route must be forbidden or a reason required.
- **2c**, five of five, each quoting both 6.2 and 6.3, "at a version tracked together" included,
  and each saying the documentation is reachable offline.

### Question 3

Five of five on every item. Every reader grades 5.3 Yes because the one-line output prints every
finding, so there is no remainder. Every reader grades 7.1 Yes on the disableable branch. Every
reader says Lintomatic does not conform because 6.3 fails, quoting or stating "One [Identifier]
that does not resolve fails this clause", and that 6.4 does not change the verdict because it is
a SHOULD.

### Judgements made in marking

Run 32's judgements J1 to J3 are applied unchanged. Under J3 (the same passage is the same
sentence):

- Clause 7.1's base sentence "make the route detectable, by a [Rule] the project can write in
  the [Detector] itself or by a mechanical check the [Detector] documents." is quoted by readers 2
  and 3 alone and by reader 4 together with the two sentences revision 4 wrote after it. It is
  counted for all three, as run 42 counted its reader 4 on the same base sentence.
- Revision 4's sentence "The project writes the [Rule], in the [Detector]'s own [Rule] language,
  and the [Detector] runs it as it runs any bespoke [Rule] under clause 4.1." is quoted whole by
  reader 5 and by its opening words, "The project writes the [Rule]…", by reader 4, and is counted
  for both. Reader 4's doubt is the base sentence's, whether the [Detector] must supply the
  detecting [Rule]; reader 5's is what the [Detector]'s "own [Rule] language" is. The criterion
  counts the passage, not the doubt. Counting reader 4 for the base sentence only, revision 4's
  sentence would be a single-reader note; the verdict is FAIL either way on the base sentence.

## Passages quoted as confusing

| Passage                                                                                                                                                      | Clause | Readers        | Text                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | -------------- | --------------------------------------------------------------------------- |
| "make the route detectable, by a [Rule] the project can write in the [Detector] itself or by a mechanical check the [Detector] documents."                   | 7.1    | three: 2, 3, 4 | Untouched base; reader 4 quotes revision 4's next two sentences with it     |
| "The project writes the [Rule], in the [Detector]'s own [Rule] language, and the [Detector] runs it as it runs any bespoke [Rule] under clause 4.1."         | 7.1    | two: 4, 5      | Written by revision 4, from revision 3's sentence                           |
| "That [Rule], or that check, reports each use of the route."                                                                                                 | 7.1    | one: 4         | Written by revision 4                                                       |
| "The [Detector] MUST print it, unaltered, alongside every finding the [Rule] reports, in its default output and in every machine-readable format it offers." | 4.3    | one: 1         | Untouched base                                                              |
| "a [Detector] failing 4.1 is graded here on its [Bundled rules]."                                                                                            | 4.2    | one: 3         | Untouched base                                                              |
| "The lookup for such a [Rule] is an obligation on the project's assembled [Toolchain], under clause 4.2 of the [toolchain specification]."                   | 6.1    | one: 3         | Untouched base; the reader says it did not have the toolchain specification |

Notes on the two blocking passages:

- **Clause 7.1, "detectable, by a [Rule] the project can write in the [Detector] itself".**
  Readers 2, 3 and 4 each could not tell whether the [Detector] meets the clause by letting the
  project write such a [Rule] or must supply one itself; reader 2 says "the sentence reads both
  ways". Readers 2 and 3 do not quote revision 4's next sentences, which say the project writes
  it; reader 4 quotes them and still asks. Two readers quoted this sentence in run 42 and five
  quoted revision 2's sentence after it in run 39.
- **Clause 7.1, revision 4's "The project writes the [Rule], in the [Detector]'s own [Rule]
  language".** Reader 5 says the document never says what that language is, and clause 4.1 does
  not name one; reader 4 quotes it as part of the doubt above. Revision 3's version of the
  sentence was quoted by one reader in run 42.

No reader's 7.1 grade turns on either passage, since every reader grades on the disableable
branch.

Run 42's other blocking passage is clear: no reader quotes clause 8.1, which revision 4 rewrote.
No reader quotes the Rule harness entry or any other sentence the original change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met, five of five
  throughout.
- A wrong answer traceable to the text, none: met.
- A passage found confusing by two or more, none outstanding: not met. Clause 7.1's
  "detectable" sentence (three readers), untouched base text. Clause 7.1's sentence on who writes
  the [Rule] (two readers), written by revision 4.
- From one reader only, recorded: the four other passages above.

**FAIL**, on question 4 alone. One blocking passage is untouched base text (7.1's "detectable"
sentence); the other is a sentence revision 4 wrote (7.1's "The project writes the [Rule]").
Neither is in text the change made.
