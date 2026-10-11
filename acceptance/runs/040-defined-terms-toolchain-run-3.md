# Run 40: TOOLING-SPEC.md, defined terms, third run

- **Document**: TOOLING-SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at 8517aa4, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness, Remediation linked, the
  section 3 table's [Remediation docs] cell). Revision 1, after
  [run 33](033-defined-terms-toolchain-run-1.md), is b6e8c2b and b1e7145. The revision after
  [run 37](037-defined-terms-toolchain-run-2.md) is 8517aa4:

  - section 2's "These are additional." becomes "The three terms below are this document's own,
    defined here rather than borrowed.";
  - clause 4.3 has a sentence saying the routes are the ones each [Detector] offers;
  - clause 9.2 has a sentence saying the gap duty falls on a project or artefact that has a
    declaration. The sentence run 37 named, "... makes no claim for a gap record to qualify", is
    replaced by "A project or artefact with no declaration therefore has no gap record under this
    clause."

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 33 or 37, model alias `haiku`; every reader
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
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/toolchain/KEY.md`
  at 8517aa4, with the judgements of run 33

- **Verdict**: FAIL on three passages, each found confusing by two or more readers:

  - section 2's sentence on an undocumented blocking rule, which revision 1 added;
  - clause 9.2's sentence, which revision 2 added;
  - clause 4.1's "in brief, are six", untouched base text.

  Every keyed item is five of five.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 4.4 | 4.5 | 5.1     | 5.2 | 5.3 | 6.1 | 6.2 | 6.3 | Section 9 | Agent support | Section 8 | Declaration | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --------- | ------------- | --------- | ----------- | ----------- |
| 1      | correct | ok  | ok  | ok  | No  | No  | Yes | Yes | Yes | No      | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | three       |
| 2      | correct | ok  | ok  | ok  | No  | No  | Yes | Yes | Yes | Partial | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | two         |
| 3      | correct | ok  | ok  | ok  | No  | No  | Yes | Yes | Yes | No      | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | three       |
| 4      | correct | ok  | ok  | ok  | No  | No  | Yes | Yes | Yes | No      | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | three       |
| 5      | correct | ok  | ok  | ok  | No  | No  | Yes | Yes | Yes | No      | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | one         |

Every grade is one the key accepts. Every 5.1 grade of Partial or No counts the two `(none)`
routes, and every 6.2 grade of No mentions the generic-justification requirement.

### Question 1

Five of five correct, each with at least four bullets the key lists. None says the toolchain must
be a single product, that a declaration is required, or that the agent summary is a MUST. Readers
1, 2, 3 and 4 say the declaration is optional or not a condition of conformance. Reader 3's last bullet
puts section 8's self-audit for shipped toolchains "outside the MUST grade" (judgement J5, below).

### Question 2

All five readers get 2a, 2b and 2c. For 2a, readers 1, 3 and 5 quote section 1's two sentences,
"A [Toolchain] is measured at the project level. It is whatever the project assembles ...".
Reader 4 quotes the two without the list of parts. Reader 2 quotes only the first and states
"whatever the project assembles" in its own words (run 33's judgement J1). Every reader quotes
the key's sentences for 2b and 2c.

### Question 3

- **4.3**, five of five Yes, against three of five in run 37. Every reader grades on the one route
  the fixture describes, the disabled inline comment. Every reader notes that the fixture names no
  other route, such as a baseline, and none grades it down for that.
- **5.1**, five of five within the key: four No and one Partial, each counting the `(none)`
  routes.
- **Section 9**, **agent support**, **section 8** and **declaration**: five of five give the key's
  answers, each naming 4.1 and 4.2 among the failing clauses. None applies section 8 to Zigpipe,
  and four quote section 8's "has no release and no [Consuming project]".

### Judgements made in marking

Run 33's judgements J1 to J4 are applied unchanged.

- **J4.** Section 2's sentence "Clauses 4.2, 5.1 and 8.1 still reach it: ..." is the same sentence
  for readers 2, 4 and 5, who quote it, and for reader 1. Reader 1 quotes its words "Clauses 4.2,
  5.1 and 8.1" and sets them against clause 4.2's MUST sentence. Counting reader 1 out, the
  sentence still has three readers and blocks.
- **J5.** Question 1 is wrong when a bullet asserts an obligation the document does not state, and
  the key lists such assertions. Reader 3's last bullet asserts none. It says section 8's
  self-audit for a shipped toolchain sits "outside the MUST grade", where section 9 includes it
  for a toolchain the project ships. It is marked correct, since five of reader 3's six bullets
  name obligations the key lists. Read strictly, question 1 would be four of five and still meet
  its threshold. The reader's reasoning does not quote the document, so either way it is not a
  traceable miss, and reader 3's section 8 answer for Zigpipe is the key's.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                    | Clause   | Readers          | Text                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------- | ------------------------------------------------------------ |
| "Clauses 4.2, 5.1 and 8.1 still reach it: its missing documentation is the failure clauses 4.2 and 8.1 exist to catch, not a reason they do not apply.", with "is not yet a [Defence]" before it, set against 5.1 or 4.2   | 2        | four: 1, 2, 4, 5 | Added by revision 1                                          |
| "That duty falls on a project or artefact that has a declaration, because the gap is recorded alongside the version declared.", set against "is still recorded as that clause says, ... with a declaration or without one" | 9.2      | two: 3, 4        | Added by revision 2, set against a sentence revision 1 added |
| "That document's MUSTs, in brief, are six.", set against "every MUST of sections 4 to 7 of the [detector specification]"                                                                                                   | 4.1      | two: 1, 3        | Untouched base                                               |
| "It is self-contained for grading a [Toolchain]."                                                                                                                                                                          | 1        | one: 1           | Untouched base                                               |
| "The two verdicts MUST be graded and declared separately", set against 9.2's "The declaration is optional."                                                                                                                | 9.1, 9.2 | one: 2           | Untouched base                                               |
| "Partial [Conformance] MUST NOT be described as [Conformance]."                                                                                                                                                            | 9        | one: 3           | Untouched base                                               |
| The [Project record] entry's "[Calibrations], [Exceptions] and conventions", set against clauses 6.1 and 6.2                                                                                                               | 2        | one: 4           | Untouched base                                               |

Notes on the three blocking passages:

- **Section 2, the undocumented blocking rule.** Readers 2, 4 and 5 could not tell how clause 5.1,
  written of "every [Defence] active", reaches a rule the same paragraph says is not yet a
  [Defence], or whether 5.1 is breached or only reached. Reader 1 asks the same of clause 4.2's
  "every [Identifier] its [Defences] print". Every reader still graded 5.1 within the key. The
  paragraph was added by revision 1, after run 33, and no reader quoted it in run 37.
- **Clause 9.2, the added sentence.** Readers 3 and 4 set it against revision 1's sentence that a
  gap method clause 3.2 requires "is still recorded ... with a declaration or without one". They
  could not tell whether the duty to record a gap applies without a declaration. Run 37's sentence
  on 9.2 is gone, and three readers named it then; two name its replacement now.
- **Clause 4.1, "in brief, are six".** Readers 1 and 3 could not tell whether the six are the
  whole obligation or a summary of "every MUST of sections 4 to 7". Reader 2 of run 37 quoted the
  same sentence.

Run 37's other failures are clear in this run:

- 4.3 is five of five;
- no reader quotes section 2's "These are additional." or its replacement;
- no reader quotes clause 4.3's new sentence.

No reader quotes the Rule harness rows, the [Remediation docs] cell or clause 4.5's
[Remediation] link.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met, five of five
  throughout.
- A wrong answer traceable to the text, none: met.
- A passage found confusing by two or more, none outstanding: not met.
  - Section 2's sentence on an undocumented blocking rule (four readers), added by revision 1.
  - Clause 9.2's sentence on whom the gap duty falls (two readers), added by revision 2.
  - Clause 4.1's "That document's MUSTs, in brief, are six." (two readers), untouched base text.
- From one reader only, recorded: the four other passages above.

**FAIL**, on question 4 alone. Two blocking passages are sentences the revisions added (section 2
and 9.2), and one is untouched base text (4.1). None is in text the change made.
