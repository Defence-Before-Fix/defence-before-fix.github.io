# Run 33: TOOLING-SPEC.md, defined terms, first run

- **Document**: TOOLING-SPEC.md
- **Pull request**: not yet opened; branch `editor/defined-terms` at 35f42bf, the commit the
  readers were given (be546ea renames Harness to Rule harness in the section 2 table, the section
  3 table and clause 4.1, links Remediation in clause 4.5, and makes the section 3 table's
  "remediation text" the [Remediation docs] content)
- **Cohort**: five readers, model alias `haiku`; every reader reported `claude-haiku-5-5` in its
  JSON output
- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt is byte for byte the question set, the document and the
  fixture at 35f42bf, in that order, each preceded by one `===== FILE: <name> =====` line, and
  that each sheet is the `result` of its reader's JSON output (one turn, `is_error` false)
- **Run within the pull request**: 1
- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/toolchain/KEY.md`
  at 35f42bf
- **Verdict**: FAIL on application items 4.2 and 4.3, on misses traceable to the text, and on four
  passages found confusing by two or more readers. None of them is in text this change touched.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2             | 4.3             | 4.4 | 4.5 | 5.1     | 5.2 | 5.3 | 6.1 | 6.2 | 6.3 | Section 9 | Agent support | Section 8 | Declaration | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | --------------- | --------------- | --- | --- | ------- | --- | --- | --- | --- | --- | --------- | ------------- | --------- | ----------- | ----------- |
| 1      | correct | ok  | ok  | ok  | No  | No              | Yes             | Yes | Yes | Partial | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | four        |
| 2      | correct | ok  | ok  | ok  | No  | Partial, miss T | Partial, miss T | Yes | Yes | Partial | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | three       |
| 3      | correct | ok  | ok  | ok  | No  | Partial, miss T | Yes             | Yes | Yes | Partial | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | four        |
| 4      | correct | ok  | ok  | ok  | No  | No              | Yes             | Yes | Yes | Partial | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | three       |
| 5      | correct | ok  | ok  | ok  | No  | No              | Partial, miss T | Yes | Yes | No      | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | two         |

`T` marks a miss whose reasoning quotes or states what the document requires. Every 5.1 grade of
Partial or No counts the two `(none)` routes, and every 6.2 grade of No mentions the
generic-justification requirement, as the key requires.

### Question 1

Five of five correct. Every sheet has at least four bullets naming obligations the key lists, and
none says the toolchain must be a single product, that a declaration is required, or that the
agent summary is a MUST; reader 3 says section 7 is a SHOULD.

### Question 2

- **2a**, five of five. All five say conformance is measured at the project level, quoting
  section 1's "A [Toolchain] is measured at the project level."; readers 1, 2, 3 and 5 say the
  toolchain is whatever the project assembles to run its checks, and reader 4 that it is "the
  project's whole assembled toolchain, not ... any single package" (judgement J1). None grades
  per tool or only a packaged product.
- **2b**, five of five, each quoting section 9's "The project-level verdict is a single grade".
- **2c**, five of five, each giving two grades, neither implying the other, quoting clause 9.1.

### Question 3

- **4.2, three of five** (readers 1, 4 and 5, No). Reader 2 grades Partial because the content
  and placement "largely exist" and "the fixture describes no lookup keyed on the identifier",
  the clause's own words; reader 3 grades Partial because "38 of 40 bundled identifiers resolve
  offline", reading the clause as satisfied in part where it asks for every identifier. Each
  reasoning states what the clause requires, so each is traceable (judgement J2).
- **4.3, three of five** (readers 1, 3 and 4, Yes). Reader 2 grades Partial because "The header
  requires forbidding 'through a defence of its own', and a config flag is not a defence",
  quoting the clause heading against its body; reader 5 because the fixture does not show
  "every" route closed, quoting the clause. Both are traceable, and reader 2's reasoning is the
  passage four readers name under question 4.
- **Section 9**: five of five say the toolchain does not conform, each naming 4.1 among the
  failures (judgement J3).
- **Agent support**, **section 8** and **declaration**: five of five give the key's answer. No
  reader applies 8.1 to Zigpipe; readers 2, 3 and 4 add that zig-qa's own artefact grade is a
  separate verdict, which is the key's correct reading.

### Judgements made in marking

`ACCEPTANCE.md` at the base gives the key and the thresholds and leaves these open.

- **J1. Which elements of the key's answer to question 2 a sentence must state.** Every element
  that answers a part of the question must be stated; an element the key adds as a gloss is met
  unless the answer asserts its opposite. 2a asks the level and what the toolchain is: "whatever
  the project assembles" states the second, and the key's list of third-party, first-party and
  project-level parts is a gloss whose opposite, a single tool or packaged product, no reader
  asserts. On the stricter reading every reader would miss 2a, failing the first criterion as
  well; the verdict is FAIL either way.
- **J2. A traceable miss under question 3.** The criterion's words are a miss "whose reasoning
  quotes the document", and question 3 counts a divergence against the document when the
  reasoning shows the clause was read differently. A reasoning that states the clause's
  requirement in the clause's words, or grades it as met in part where it says every, is taken as
  doing both. Read narrowly, as quotation marks only, reader 3's 4.2 miss would not be traceable;
  4.2 fails its threshold either way.
- **J3. The section 9 verdict** is marked on "does not conform" with at least one failing clause
  the key has failing. The key's "because 4.1 and 4.2 fail" is reasoning, not a list a reader
  must reproduce; readers 2 and 3, who grade 4.2 Partial, have that miss counted under 4.2.
- **J4. The same passage under question 4** is the same sentence, as run 16 counted it.

## Passages quoted as confusing

| Passage                                                                                                                                                                                 | Clause | Readers          | Changed by this pull request     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ---------------- | -------------------------------- |
| The heading, "MUST forbid, through a defence of its own", against the body's "MUST disable every [Suppression] route ... or MUST run a [Blocking] [Defence] that fails on its use"      | 4.3    | four: 1, 2, 3, 5 | No                               |
| "A project or artefact that has learnt that it fails a MUST of the document it declares against MUST record that gap alongside the version", set against "The declaration is optional." | 9.2    | four: 1, 2, 3, 4 | No                               |
| The section 2 table's [Defence] row, "A [Rule] with its documentation, in force and [Blocking]", against undocumented rules treated as defences in 4.1, 4.2 and 5.1                     | 2      | three: 1, 2, 4   | No; another row of the table was |
| "a [Toolchain] against this document as it stands when installed into a [Consuming project] with nothing else built around it"                                                          | 9.1    | two: 4, 5        | No                               |
| "meet clauses 5.1 to 5.4 of the [detector specification]", that document not supplied                                                                                                   | 4.4    | one: 1           | No                               |
| The agent-support grade, "A [Toolchain] [Conforms] with [Agent] support if it additionally satisfies section 7.", where section 7 is SHOULDs                                            | 9      | one: 3           | No                               |
| "The table in section 2 glosses every term it borrows" and "self-contained for grading a [Toolchain]", where [Hazard] and [Remediation docs] are not in the table                       | 1      | one: 3           | No                               |

Reader 3's last passage bears on this pull request's subject: section 1 says the section 2 table
glosses every borrowed term, and the change adds a link to [Remediation] in clause 4.5 and a
[Remediation docs] cell in the section 3 table, neither term being in the section 2 table. The
reader named the clause 4.2 use, which predates the change. No reader quoted the Rule harness
rows, clause 4.1's "[Rule harness] script", or the changed sentence in clause 4.5.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met. 2a, 2b and 2c five of five.
- Restatement and application, at least four of five on each keyed item: not met. 4.2 and 4.3
  three of five; every other item five of five.
- A wrong answer traceable to the text, none: not met. 4.2 for readers 2 and 3 and 4.3 for
  readers 2 and 5, each a finding.
- A passage found confusing by two or more, none outstanding: not met. Clause 4.3's heading and
  body, and clause 9.2's gap sentence, four readers each; the section 2 [Defence] row, three;
  clause 9.1's artefact sentence, two.
- From one reader only, recorded: the three other passages above.

**FAIL.** No failure traces to text this pull request changed: clauses 4.2, 4.3, 9.1 and 9.2 and
the section 2 [Defence] row are untouched by it.
