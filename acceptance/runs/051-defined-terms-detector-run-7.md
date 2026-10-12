# Run 51: DETECTOR-SPEC.md, defined terms, seventh run

- **Document**: DETECTOR-SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at d316938, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness). Revision 1, after
  [run 32](032-defined-terms-detector-run-1.md), is 681ac42; revision 2, after
  [run 36](036-defined-terms-detector-run-2.md), is 0dac85a; revision 3, after
  [run 39](039-defined-terms-detector-run-3.md), is 7a6b60b; revision 4, after
  [run 42](042-defined-terms-detector-run-4.md), is 99396df; revision 5, after
  [run 45](045-defined-terms-detector-run-5.md), is f52a510. The revision after
  [run 48](048-defined-terms-detector-run-6.md) is 572ffb5:

  - in clause 7.1, revision 5's sentence after the keyed MUST, "The [Detector] need not ship that
    \[Rule\]: it is enough that the project can write it, as a bespoke [Rule] under clause 4.1.", is
    replaced by "A [Rule] "in the [Detector] itself" is a bespoke [Rule] under clause 4.1." The
    keyed MUST sentence is unchanged;
  - clause 6.1's lookup sentence reads "The lookup for such a [Rule], from the [Identifier] to its
    documentation on disk, is an obligation on the project's assembled [Toolchain], under clause
    4.2 of the [toolchain specification](TOOLING-SPEC.md) ...".

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 32, 36, 39, 42, 45 or 48, model alias `haiku`;
  every reader reported `claude-haiku-5-5` in its JSON output

- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked two things:

  - the prompt is byte for byte the question set, the document and the fixture at d316938, in
    that order. Each is preceded by one `===== FILE: <name> =====` line, and one blank line
    separates each file from the next;
  - each sheet is the `result` of its reader's JSON output (one turn, `is_error` false).

- **Run within the pull request**: 7

- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/detector/KEY.md`
  at d316938, with the judgements of runs 32 and 48

- **Verdict**: FAIL on one passage found confusing by all five readers: clause 7.1's "detectable"
  sentence read with the sentence revision 6 wrote after it. Load-bearing statement 2a is four of
  five under J1 (reader 3, not traceable); every other keyed item is five of five.

## Marks

| Reader | Q1      | 2a   | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | 6.4 | Q4 passages |
| ------ | ------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------- |
| 1      | correct | ok   | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |
| 2      | correct | ok   | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | three       |
| 3      | correct | miss | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |
| 4      | correct | ok   | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |
| 5      | correct | ok   | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |

Every question 3 grade is the key's intended verdict.

### Question 1

Five of five correct, each with six bullets the key lists. None says the detector must enforce a
suppression policy, must declare a version, or must list defences or produce an agent summary.

### Question 2

- **2a**, four of five. Readers 1, 2, 4 and 5 each say every MUST in sections 4 to 7 and that a
  predating detector can conform, and each quotes 8.1's "MAY be graded [Conforming] on evidence";
  readers 1, 2 and 4 also quote section 8's definition, and reader 5 states it. Reader 3 says only
  that a predating detector can conform "because conformance is judged on evidence and the
  declaration is optional", quoting 8.1, and does not say what conforming is (J1, below). No reader
  says a declaration is required.
- **2b**, five of five, each giving disableable or detectable and each saying, or quoting, that
  either alone is enough. Reader 2 quotes the whole keyed sentence of 7.1; readers 1, 3, 4 and 5
  quote it as far as "either alone satisfies this clause" or beyond. Reader 4 says "detectable by a mechanical check" and leaves out the
  project's [Rule], without saying that route is not open (J1). None says the route must be
  forbidden or a reason required.
- **2c**, five of five, each saying the documentation ships with the rule and is reachable
  offline. Readers 1, 3, 4 and 5 quote both 6.2 and 6.3; reader 2 quotes 6.2 and states 6.3,
  "at a version tracked together" included.

### Question 3

Five of five on every item. Every reader grades 4.2 Yes, noting that the fixture does not say what
`--only` prints and taking it from `check`'s one-line output. Every reader grades 5.3 Yes because
the one-line output prints every finding, so there is no remainder. Every reader grades 7.1 Yes on
the disableable branch. Every reader says Lintomatic does not conform because 6.3 fails, readers 1,
2 and 4 quoting "One [Identifier] that does not resolve fails this clause", and that 6.4 does not
change the verdict because it is a SHOULD. Readers 3 and 5 say 7.2 is a SHOULD and do not grade it.

### Judgements made in marking

Run 32's judgements J1 to J3 and run 48's J10 are applied unchanged; J10 decides nothing here.

- **J1, 2a for reader 3.** 2a asks what it means for a detector to conform and whether a detector
  that predates the document can conform. Reader 3's sentence answers the second part only; its
  "judged on evidence" says how a verdict is reached, not what is being judged. Under J1 every
  element that answers a part of the question must be stated, so it is a miss. It is not
  traceable: the answer asserts nothing the document contradicts, and the same reader states
  section 8's definition in its question 1 bullets and its section 8 verdict, so the document was
  not read differently. Read the other way, taking the sheet as a whole, 2a is five of five; the
  verdict is FAIL either way on 7.1.
- **J1, 2b for reader 4.** The key's "by a Rule the project can write or a mechanical check it
  documents" glosses how a route is made detectable. Reader 4 names only the mechanical check and
  asserts nothing against the [Rule], so 2b is met. Read strictly, 2b would be four of five and
  fail the first criterion too; the verdict is FAIL either way.
- **J3.** Clause 7.1's keyed sentence "... or make the route detectable, by a [Rule] the project
  can write in the [Detector] itself or by a mechanical check the [Detector] documents." and
  revision 6's sentence after it, "A [Rule] "in the [Detector] itself" is a bespoke [Rule] under
  clause 4.1.", are quoted together by all five readers, reader 2 eliding the middle with an
  ellipsis. Each sets the one against the other, so they are one passage for all five.
- **J10.** Reader 4 says it could not check the cross-references to the method and toolchain
  specifications and "took them as stated", naming method clauses 3.6 and 8.3. It quotes no
  passage, so there is nothing to count; it is recorded here only.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                      | Clause | Readers             | Text                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------- | -------------------------------------------------------------------------------------------------- |
| "make the route detectable, by a [Rule] the project can write in the [Detector] itself or by a mechanical check the [Detector] documents.", with "A [Rule] "in the [Detector] itself" is a bespoke [Rule] under clause 4.1." | 7.1    | five: 1, 2, 3, 4, 5 | The first untouched base, and the sentence the key quotes for 2b; the second written by revision 6 |
| "This applies to every [Rule] the [Detector] runs, bundled or bespoke; a [Detector] failing 4.1 is graded here on its [Bundled rules]."                                                                                      | 4.2    | one: 2              | Untouched base                                                                                     |
| "A [Detector] that predates this document ... MAY be graded [Conforming] on evidence by anyone ...", set against section 8's definition                                                                                      | 8.1    | one: 2              | Untouched base                                                                                     |

Note on the blocking passage:

- **Clause 7.1, "in the [Detector] itself".** Every reader reads "a [Rule] the project can write in
  the [Detector] itself" as the project writing into the detector's own source, and none could
  square that with a bespoke [Rule] under clause 4.1, which the project registers from outside it:
  readers 1, 3 and 5 say so outright, reader 4 asks whether a project's own rule file counts as "in
  the [Detector]", and reader 2 could not tell whether the phrase points at who writes the [Rule]
  or where it sits. Revision 6's identity sentence was read by every reader and did not settle it.
  No reader's 7.1 grade turns on it, since every reader grades on the disableable branch, and every
  reader gets 2b right on the same sentence. Three readers quoted the base sentence in run 36, two
  in run 42, three in run 45 and four in run 48; all five quote it now.

Run 48's other blocking passage is clear: no reader quotes clause 6.1's lookup sentence, in revision
6's wording or any other. No reader quotes the Rule harness entry or any other sentence the
original change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: not met under J1. 2a is four of five, reader
  3 leaving out what conforming is; not traceable. 2b and 2c are five of five.
- Restatement and application, at least four of five on each keyed item: met, five of five
  throughout.
- A wrong answer traceable to the text, none: met.
- A passage found confusing by two or more, none outstanding: not met. Clause 7.1's "detectable"
  sentence with revision 6's sentence after it (five readers); the first untouched base text, the
  second written by revision 6.
- From one reader only, recorded: the two other passages above.

**FAIL**, on question 4, and on 2a under J1. The 7.1 passage pairs untouched base text with the
sentence revision 6 wrote. None is in text the original change made.
