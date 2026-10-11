# Run 48: DETECTOR-SPEC.md, defined terms, sixth run

- **Document**: DETECTOR-SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at 18f782a, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness). Revision 1, after
  [run 32](032-defined-terms-detector-run-1.md), is 681ac42; revision 2, after
  [run 36](036-defined-terms-detector-run-2.md), is 0dac85a; revision 3, after
  [run 39](039-defined-terms-detector-run-3.md), is 7a6b60b; revision 4, after
  [run 42](042-defined-terms-detector-run-4.md), is 99396df. The revision after
  [run 45](045-defined-terms-detector-run-5.md) is f52a510:

  - in clause 7.1, revision 4's two sentences after the keyed MUST, "That [Rule], or that check,
    reports each use of the route. The project writes the [Rule], in the [Detector]'s own [Rule]
    language, ...", are replaced by one: "The [Detector] need not ship that \[Rule\]: it is enough
    that the project can write it, as a bespoke [Rule] under clause 4.1." The keyed MUST sentence
    is unchanged.

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 32, 36, 39, 42 or 45, model alias `haiku`;
  every reader reported `claude-haiku-5-5` in its JSON output

- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked two things:

  - the prompt is byte for byte the question set, the document and the fixture at 18f782a, in
    that order. Each is preceded by one `===== FILE: <name> =====` line, and one blank line
    separates each file from the next;
  - each sheet is the `result` of its reader's JSON output (one turn, `is_error` false).

- **Run within the pull request**: 6

- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/detector/KEY.md`
  at 18f782a, with the judgements of run 32

- **Verdict**: FAIL on two passages found confusing by two or more readers: clause 7.1's
  "detectable" sentence read against the sentence revision 5 wrote after it (four readers), and
  clause 6.1's sentence sending a project rule's lookup to the toolchain specification (two
  readers). Every keyed item is five of five.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | 6.4 | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------- |
| 1      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | two         |
| 2      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | two         |
| 3      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | two         |
| 4      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | two         |
| 5      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | three       |

Every grade is the key's intended verdict.

### Question 1

Five of five correct, each with six bullets the key lists. None says the detector must enforce a
suppression policy, must declare a version, or must list defences or produce an agent summary.

### Question 2

- **2a**, five of five. Each says every MUST in sections 4 to 7 and that a predating detector can
  conform, and each quotes 8.1's "MAY be graded [Conforming] on evidence". Readers 1, 2 and 5 also
  quote section 8's definition; readers 3 and 4 state it. Readers 1, 3 and 4 say the verdict rests
  on evidence, not on a declaration; no reader says a declaration is required.
- **2b**, five of five, each giving disableable or detectable and each saying, or quoting, that
  either alone is enough. Readers 1, 3 and 5 quote the whole keyed sentence of 7.1; readers 2 and
  4 quote its first half. None says the route must be forbidden or a reason required.
- **2c**, five of five, each quoting both 6.2 and 6.3, "at a version tracked together" included,
  and each saying the documentation is reachable offline.

### Question 3

Five of five on every item. Every reader grades 5.3 Yes because the one-line output prints every
finding, so there is no remainder. Every reader grades 7.1 Yes on the disableable branch. Every
reader says Lintomatic does not conform because 6.3 fails, quoting or stating "One [Identifier]
that does not resolve fails this clause", and that 6.4 does not change the verdict because it is
a SHOULD. Readers 3, 4 and 5 add that 7.2, a SHOULD, is unmet, which changes no grade.

### Judgements made in marking

Run 32's judgements J1 to J3 are applied unchanged. Under J3 (the same passage is the same
sentence):

- Clause 7.1's keyed sentence "... or make the route detectable, by a [Rule] the project can
  write in the [Detector] itself or by a mechanical check the [Detector] documents." is quoted by
  readers 1, 2, 3 and 4. Revision 5's sentence after it, "The [Detector] need not ship that
  \[Rule\]: it is enough that the project can write it, as a bespoke [Rule] under clause 4.1.", is
  quoted whole by reader 4, by its first clause by reader 2 and by its last words, "as a bespoke
  [Rule] under clause 4.1", by reader 3. Reader 1 restates it, "the next sentence says the
  detector need not ship that rule", and is counted with them, as run 43 counted its reader 4 on
  a restated sentence. Every one of the four sets the two sentences against each other, so they
  are one passage for all four. Without reader 1 on the second sentence, it still has three
  readers.

- Clause 6.1's "The lookup for such a [Rule] is an obligation on the project's assembled
  [Toolchain], under clause 4.2 of the [toolchain specification](TOOLING-SPEC.md) ..." is quoted
  by readers 1 and 2. Reader 5 quotes a different sentence of the same paragraph, "Where the
  [Identifier] is itself a URL, as method clause 3.6 allows,", and is a single-reader note; read
  by paragraph, the passage would have three readers.

- **J10. A passage quoted because it cites a document the reader was not given.** Readers 1 and 2
  each say of clause 6.1's sentence that they were not given the toolchain specification and so
  could not check what its clause 4.2 requires; reader 5 says the same of three other sentences.
  Question 4 asks for any passage the reader found confusing, the key says to record every
  passage quoted, and the criterion counts two readers quoting the same passage without asking
  why. So such a passage is counted like any other, and clause 6.1's sentence blocks. Read the
  other way, excluding a quotation whose only doubt is a cross-reference to a document outside
  the packet, it would be a recorded note, not a block; the verdict is FAIL either way on 7.1.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                                                                                 | Clause   | Readers          | Text                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------- | -------------------------------------------------------------------------------------------------- |
| "make the route detectable, by a [Rule] the project can write in the [Detector] itself or by a mechanical check the [Detector] documents.", set against "The [Detector] need not ship that \[Rule\]: it is enough that the project can write it, as a bespoke [Rule] under clause 4.1." | 7.1      | four: 1, 2, 3, 4 | The first untouched base, and the sentence the key quotes for 2b; the second written by revision 5 |
| "The lookup for such a [Rule] is an obligation on the project's assembled [Toolchain], under clause 4.2 of the [toolchain specification](TOOLING-SPEC.md)"                                                                                                                              | 6.1      | two: 1, 2        | Untouched base; both readers say they were not given that document                                 |
| "A command, an index file or a URL are all acceptable forms", set against clause 6.2's "without network access"                                                                                                                                                                         | 6.1, 6.2 | one: 3           | Untouched base                                                                                     |
| "a [Detector] failing 4.1 is graded here on its [Bundled rules]."                                                                                                                                                                                                                       | 4.2      | one: 4           | Untouched base                                                                                     |
| "**Why**: clause 3.3 of the method specification requires the [Rule] to be proven by making it go red."                                                                                                                                                                                 | 4.2      | one: 5           | Untouched base; the reader says it was not given the method specification                          |
| "Where the [Identifier] is itself a URL, as method clause 3.6 allows,"                                                                                                                                                                                                                  | 6.1      | one: 5           | Untouched base; as above                                                                           |
| "the method specification's position is that [Suppression] is an [Owner] decision under its clause 3.4 and section 4,"                                                                                                                                                                  | 7.1      | one: 5           | Untouched base; as above                                                                           |

Notes on the two blocking passages:

- **Clause 7.1, "in the [Detector] itself" against "need not ship that [Rule]".** Readers 1, 2
  and 4 could not reconcile a [Rule] the project writes "in the [Detector] itself" with a
  [Detector] that "need not ship" it; reader 2 says the two "pull against each other". Reader 3
  could not tell whether "in the [Detector] itself" means editing the detector's own source or
  registering a [Rule] through clause 4.1. Three readers quoted the base sentence in run 45 and
  two in run 42; revision 5's sentence answers run 45's doubt, whether the [Detector] must ship
  the [Rule], and the readers now set its wording against the base sentence's. No reader's 7.1
  grade turns on it, since every reader grades on the disableable branch, and every reader gets
  2b right on the same sentence.
- **Clause 6.1's lookup sentence.** Readers 1 and 2 could not check what the toolchain
  specification's clause 4.2 requires of a project rule's lookup. Neither grade turns on it: both
  grade 6.1 Yes. One reader quoted it in run 45 for the same reason. It blocks under J10.

Run 45's other blocking passage is gone: no reader quotes "the [Detector]'s own [Rule] language"
or "That [Rule], or that check, reports each use of the route", which revision 5 cut. No reader
quotes the Rule harness entry or any other sentence the original change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met, five of five
  throughout.
- A wrong answer traceable to the text, none: met.
- A passage found confusing by two or more, none outstanding: not met.
  - Clause 7.1's "detectable" sentence against revision 5's sentence after it (four readers); the
    first untouched base text, the second written by revision 5.
  - Clause 6.1's sentence on the lookup for a project's own [Rule] (two readers, under J10),
    untouched base text.
- From one reader only, recorded: the five other passages above.

**FAIL**, on question 4 alone. The 7.1 passage pairs untouched base text with the sentence
revision 5 wrote; the 6.1 passage is untouched base text. Neither is in text the change made.
