# Run 49: TOOLING-SPEC.md, defined terms, sixth run

- **Document**: TOOLING-SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at 18f782a, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness, Remediation linked, the
  section 3 table's [Remediation docs] cell). Revision 1, after
  [run 33](033-defined-terms-toolchain-run-1.md), is b6e8c2b and b1e7145; revision 2, after
  [run 37](037-defined-terms-toolchain-run-2.md), is 8517aa4; revision 3, after
  [run 40](040-defined-terms-toolchain-run-3.md), is ff77998; revision 4, after
  [run 43](043-defined-terms-toolchain-run-4.md), is c1c461c. The revision after
  [run 46](046-defined-terms-toolchain-run-5.md) is 18f782a:

  - section 2's sentence on an undocumented blocking rule now reads "In clauses 4.2, 5.1 and 8.1,
    [Defence] also covers a [Rule] the [Toolchain] runs as [Blocking] alongside its [Defences]
    whose documentation is missing.", and no longer says such a rule is not yet a [Defence];
  - clause 4.1's sentence reads "That document's MUSTs are those of its sections 4 to 7, and every
    one applies, not only the six summarised here.";
  - clause 9.1's sentence on section 8 is back to the base wording, "Section 8 bears on the
    artefact grade only; clause 5.3 is its project-level counterpart.";
  - the [Project record] entry reads "The place a project writes down the judgements the method
    specification delegates to it: [Calibrations], [Exceptions] and conventions, whichever it has
    made."

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 33, 37, 40, 43 or 46, model alias `haiku`;
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
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/toolchain/KEY.md`
  at 18f782a, with the judgements of run 33 and of runs 40, 43 and 46

- **Verdict**: FAIL on one passage found confusing by three readers, section 2's sentence on an
  undocumented blocking rule, which revision 5 rewrote. Every keyed item is at least four of five,
  and no miss is traceable to the text under J12.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2      | 4.3 | 4.4 | 4.5 | 5.1      | 5.2 | 5.3 | 6.1 | 6.2 | 6.3 | Section 9 | Agent support | Section 8 | Declaration | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | -------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --------- | ------------- | --------- | ----------- | ----------- |
| 1      | correct | ok  | ok  | ok  | No  | No, if … | Yes | Yes | Yes | No, if … | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | three       |
| 2      | correct | ok  | ok  | ok  | No  | No       | Yes | Yes | Yes | Partial  | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | two         |
| 3      | correct | ok  | ok  | ok  | No  | No       | Yes | Yes | Yes | No       | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | three       |
| 4      | correct | ok  | ok  | ok  | No  | No       | Yes | Yes | Yes | No       | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | two         |
| 5      | correct | ok  | ok  | ok  | No  | No       | Yes | Yes | Yes | Partial  | Yes | Yes | Yes | No  | Yes | ok        | ok            | ok        | ok          | two         |

Reader 1 grades 4.2 "No, if the two rules are Blocking" and 5.1 "No, under the same condition as
4.2". Its 4.2 is marked a miss, not traceable, under J12 (below); its 5.1 is correct, since the
key accepts both branches. Every 5.1 grade of Partial or No counts the two `(none)` routes.

### Question 1

Five of five correct. Readers 1, 3, 4 and 5 each have at least four bullets the key lists;
reader 2 is marked correct under J11 (below). None says the toolchain must be a single product,
that a declaration is required, or that the agent summary is a MUST; reader 2 says section 7's
summary and delivery are SHOULDs.

### Question 2

All five readers get 2a, 2b and 2c. For 2a, every reader quotes section 1's "A [Toolchain] is
measured at the project level."; readers 1 to 4 quote "whatever the project assembles to run its
checks through", and reader 5 states it without quoting it (run 33's J1). Every reader quotes the
key's sentence for 2b and for 2c, and every 2c says the two grades do not imply each other.

### Question 3

- **4.1**, five of five No, each on the two undocumented bundled rules and the 4.1 table's
  "Nothing for those two | Fails" row. Every reader notes that the detector specification was not
  in the packet; none grades on it.
- **4.2**, four of five. Readers 2 to 5 grade No on the two `(none)` identifiers; readers 2, 3, 4
  and 5 each say the fixture does not state that the two rules are [Blocking], and each takes them
  as [Blocking] because they are enabled in the run that stops on failure. Reader 1 grades "No, if
  the two rules are Blocking", adding "If they are only Warnings, they are not Defences under
  clause 4.2 and this clause would be Yes." (J12).
- **4.3**, five of five Yes, each grading on the routes the fixture describes.
- **5.1**, five of five: reader 1 No under its condition, readers 3 and 4 No, readers 2 and 5
  Partial, each counting the `(none)` routes.
- **6.1**, five of five Yes on `quality-exceptions.toml`. Readers 3 and 5 note that the fixture
  places no [Calibrations] or conventions, and grade Yes all the same.
- **6.2**, five of five No, each mentioning that nothing rejects a generic justification. J8
  decides nothing.
- **Section 9**, **agent support**, **section 8** and **declaration**: five of five give the key's
  answers. Every section 9 verdict names 4.1 among the failing clauses (run 33's J3). No reader
  applies section 8 to Zigpipe; readers 1, 2, 3 and 4 say zig-qa is a separate artefact, and reader
  5 asks under question 4 whether publishing zig-qa is shipping it, but grades section 8 as not
  applying.

### Judgements made in marking

Run 33's judgements J1 to J4, run 40's J5, run 43's J6 and run 46's J8 are applied unchanged. J5,
J6 and J8 decide nothing here.

- **J4.** Section 2's sentence "In clauses 4.2, 5.1 and 8.1, [Defence] also covers a [Rule] the
  [Toolchain] runs as [Blocking] alongside its [Defences] whose documentation is missing." is
  quoted whole by readers 2, 3 and 5: one sentence, three readers. Reader 5 also quotes the section
  2 table's [Defence] row, "with its documentation, in force and [Blocking]", which no other
  reader quotes. Reader 4 alone quotes section 9's sentence with 9.1's sentence on section 8.
  Reader 5's second entry names section 9.1 in its heading but quotes section 8's closing
  paragraph and the [Consuming project] entry, not 9.1, and is a different passage. Readers 1 and
  4 quote different sentences of clause 4.1, from different paragraphs.
- **J11. Reader 2's question 1.** Reader 2 has five bullets. Its second, "Wherever the method
  requires a practitioner to do something, the toolchain must make it possible without the
  project building the mechanism itself", is section 1's governing principle, a MUST sentence the
  key's list does not include. Its first, that the toolchain is measured as one assembled whole,
  is section 1's definition and asserts no obligation. Its third, fourth and fifth name between
  them every obligation the key lists, from 4.1 to 8.2. `ACCEPTANCE.md` marks a bullet correct
  "when it names an obligation the document actually states", and the governing principle is one,
  so reader 2 has four correct bullets and none wrong. Read to the key's list alone, reader 2 would
  have three and question 1 would be four of five, which still meets its threshold; the reasoning
  quotes nothing, so either way it is not a traceable miss.
- **J12. Reader 1's conditional 4.2.** The key's verdict is No, and reader 1's is No only on a
  condition, that the two enabled rules are [Blocking], which the fixture does not state in that
  word. A conditional grade is not the key's grade, so it is marked a miss. It is not traceable:
  question 3 counts a divergence against the document only when the reasoning shows the clause
  read differently, and reader 1 reads clause 4.2 and section 2's sentence as they are written,
  that 4.2 reaches an undocumented rule the [Toolchain] runs as [Blocking]; the open point is a
  fact about the fixture, which four other readers settle from "enabled" and the run that stops on
  failure. 4.2 is four of five and meets its threshold. Read the other way, since the reasoning
  quotes clause 4.2, it would be a traceable miss on section 2's sentence, which blocks under
  question 4 regardless; the verdict is FAIL either way.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                        | Clause | Readers        | Text                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | -------------- | --------------------------------------------------------------------- |
| "In clauses 4.2, 5.1 and 8.1, [Defence] also covers a [Rule] the [Toolchain] runs as [Blocking] alongside its [Defences] whose documentation is missing."                                                                      | 2      | three: 2, 3, 5 | Rewritten by revision 5                                               |
| "It is self-contained for grading a [Toolchain].", set against clause 4.1's reliance on the detector specification                                                                                                             | 1, 4.1 | one: 1         | Untouched base                                                        |
| "That document's MUSTs are those of its sections 4 to 7, and every one applies, not only the six summarised here."                                                                                                             | 4.1    | one: 1         | Rewritten by revision 5                                               |
| "The justification MUST name the [Hazard] being accepted and the scope of the [Exception]."                                                                                                                                    | 6.2    | one: 1         | Untouched base                                                        |
| "Where such a [Defence] is not expressible in the [Toolchain]'s own [Detectors], its entry MAY be sourced from wherever it is enabled, provided the listing stays derived under clause 5.2 rather than hand-maintained."       | 5.3    | one: 2         | Untouched base                                                        |
| "This duty, to record the gap in the declaration, falls only on a project or artefact that has one.", set against "Method clause 3.2's duty to record a gap is a separate one, and applies with a declaration or without one." | 9.2    | one: 3         | Both written by revision 3                                            |
| "Irreducible cases MUST be directed to the [Project record]."                                                                                                                                                                  | 4.3    | one: 3         | Untouched base                                                        |
| "where the [Toolchain] is one the project ships, every MUST in section 8 as well", set against 9.1's "Section 8 bears on the artefact grade only"                                                                              | 9, 9.1 | one: 4         | Untouched base; 9.1's sentence back to the base wording by revision 5 |
| "The [Detector] together with that wrapping is then what the [Practitioner] uses and what is judged", with "The [Detector]'s own verdict under that document is unchanged by the wrapping."                                    | 4.1    | one: 4         | Untouched base                                                        |
| "A project that assembles its [Toolchain] without shipping it has no release and no [Consuming project]", with the [Consuming project] entry's "a [Toolchain] shipped by somebody else", against the fixture's "publishes"     | 8, 2   | one: 5         | Untouched base                                                        |

Note on the blocking passage:

- **Section 2, the undocumented blocking rule.** Readers 2 and 3 could not tell whether the
  sentence covers Zigpipe's two enabled bundled rules, whose [Blocking] status the fixture does
  not state; reader 5 sets it against the [Defence] row, "in force and [Blocking]", and could not
  find what applies to an undocumented [Rule] in force but not [Blocking]. Revision 5's wording
  no longer reads as a contradiction to any reader, as revision 4's did to two in run 46; the
  doubt now is the [Blocking] condition. Reader 1's conditional 4.2 grade (J12) turns on the same
  point. Every reader still grades 4.1 No and the toolchain as not conforming. Four readers named
  revision 1's wording in run 40, three revision 3's in run 43, three revision 4's in run 46, and
  three name revision 5's.

Run 46's other failures are clear in this run:

- 6.1 is five of five, with no traceable miss, and no reader quotes the [Project record] entry;
- section 9's sentence with 9.1's on section 8, two readers in run 46 and three in run 43, is
  quoted by one reader (4), with 9.1's sentence in its base wording;
- clause 4.1's sentence on the six, two readers in run 46, is quoted by one reader (1) in
  revision 5's wording.

No reader quotes the Rule harness rows, the [Remediation docs] cell or clause 4.5's [Remediation]
link.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met. 4.2 four of five
  under J12; question 1 five of five under J11; every other item five of five.
- A wrong answer traceable to the text, none: met, under J12.
- A passage found confusing by two or more, none outstanding: not met. Section 2's sentence on an
  undocumented blocking rule (three readers), rewritten by revision 5.
- From one reader only, recorded: the nine other passages above.

**FAIL**, on question 4. The blocking passage is the section 2 sentence revision 5 rewrote. None
is in text the change made.
