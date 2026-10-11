# Run 46: TOOLING-SPEC.md, defined terms, fifth run

- **Document**: TOOLING-SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at c1c461c, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness, Remediation linked, the
  section 3 table's [Remediation docs] cell). Revision 1, after
  [run 33](033-defined-terms-toolchain-run-1.md), is b6e8c2b and b1e7145; revision 2, after
  [run 37](037-defined-terms-toolchain-run-2.md), is 8517aa4; revision 3, after
  [run 40](040-defined-terms-toolchain-run-3.md), is ff77998. The revision after
  [run 43](043-defined-terms-toolchain-run-4.md) is c1c461c:

  - section 2's sentence on an undocumented blocking rule is cut to "... is not yet a [Defence];
    where clauses 4.2, 5.1 and 8.1 say [Defence], they include it.";
  - clause 4.2's sentence on a third-party [Detector]'s native catalogue now says it "is not
    re-shipped here: an [Identifier] the [Detector] resolves under that document's clause 6 meets
    this clause, and one that nothing resolves fails it.";
  - clause 9.1's sentence on section 8 now reads "Section 8, which section 9 adds where the
    [Toolchain] is one the project ships, bears on the artefact grade only; ...";
  - the [Project record] entry now reads "The one place a project writes down every judgement the
    method specification delegates to it, whether a [Calibration], an [Exception] or a
    convention."

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 33, 37, 40 or 43, model alias `haiku`; every
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
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/toolchain/KEY.md`
  at c1c461c, with the judgements of run 33 and of runs 40 and 43

- **Verdict**: FAIL on a miss traceable to the text under 6.1, reader 2, which traces to the
  [Project record] entry revision 4 rewrote, and on four passages found confusing by two or more
  readers:

  - section 2's sentence on an undocumented blocking rule, which revision 4 rewrote;
  - section 9's sentence bringing section 8 into a shipped [Toolchain]'s verdict, with the clause
    9.1 sentence revision 4 rewrote;
  - the [Project record] entry, which revision 4 rewrote, set against clause 6.1;
  - clause 4.1's "in brief, they are six", which revision 3 rewrote.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 4.4 | 4.5 | 5.1     | 5.2 | 5.3 | 6.1             | 6.2      | 6.3 | Section 9 | Agent support | Section 8 | Declaration | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --------------- | -------- | --- | --------- | ------------- | --------- | ----------- | ----------- |
| 1      | correct | ok  | ok  | ok  | No  | No  | Yes | Yes | Yes | Partial | Yes | Yes | Yes             | No, miss | Yes | ok        | ok            | ok        | ok          | one         |
| 2      | correct | ok  | ok  | ok  | No  | No  | Yes | Yes | Yes | No      | Yes | Yes | Partial, miss T | No       | Yes | ok        | ok            | ok        | ok          | four        |
| 3      | correct | ok  | ok  | ok  | No  | No  | Yes | Yes | Yes | No      | Yes | Yes | Yes             | No       | Yes | ok        | ok            | ok        | ok          | four        |
| 4      | correct | ok  | ok  | ok  | No  | No  | Yes | Yes | Yes | Partial | Yes | Yes | Yes             | No       | Yes | ok        | ok            | ok        | ok          | five        |
| 5      | correct | ok  | ok  | ok  | No  | No  | Yes | Yes | Yes | Partial | Yes | Yes | Yes             | No       | Yes | ok        | ok            | ok        | ok          | one         |

`T` marks a miss whose reasoning quotes or states what the document requires. Every 5.1 grade of
Partial or No counts the two `(none)` routes. Reader 1's 6.2 is marked a miss, not traceable,
under J8 (below).

### Question 1

Five of five correct, each with at least four bullets the key lists. None says the toolchain must
be a single product, that a declaration is required, or that the agent summary is a MUST; readers
2 and 4 say section 7's summaries are SHOULDs, and reader 4 says section 8 applies only to a
toolchain the project ships.

### Question 2

All five readers get 2a, 2b and 2c. For 2a, every reader quotes section 1's "A [Toolchain] is
measured at the project level."; readers 1 to 4 quote or state "whatever the project assembles",
and reader 5 states the list of parts without quoting it (run 33's judgement J1). Every reader
quotes the key's sentence for 2b and for 2c.

### Question 3

- **4.3**, five of five Yes. Every reader notes that the fixture names no other route, a baseline
  or a path exclude, and grades on the routes described; none quotes clause 4.3's definition of a
  bypassing route.
- **5.1**, five of five, each counting the `(none)` routes.
- **6.1**, four of five. Readers 1, 3, 4 and 5 grade Yes on `quality-exceptions.toml`, each noting
  that the fixture places no [Calibrations] or conventions. Reader 2 grades Partial: "The fixture
  does not show where calibrations or conventions are recorded, and section 2 defines the project
  record as holding all of them." Its question 4 entry quotes the [Project record] entry, "The one
  place a project writes down every judgement ... whether a [Calibration], an [Exception] or a
  convention", against clause 6.1, and says that question "decided my Partial verdict". The
  reasoning states the entry, so the miss is traceable (run 33's judgement J2). It traces to the
  entry as revision 4 rewrote it, read with clause 6.1's untouched "The [Toolchain] MUST define
  where the [Project record] lives and MUST load it". Two readers made the same miss on the
  entry's earlier wording in run 43.
- **6.2**, five of five No. Readers 2 to 5 mention that nothing rejects a generic justification.
  Reader 1 rests its No on the clause's sentence "A field that is merely present and non-empty
  does not satisfy this clause" and does not mention the generic-justification requirement (J8).
- **Section 9**, **agent support**, **section 8** and **declaration**: five of five give the key's
  answers, each naming 4.1 and 4.2 among the failing clauses, or 4.1 failing and 4.2 not met
  (reader 1). None applies section 8 to Zigpipe; readers 1, 3, 4 and 5 say zig-qa is a separate
  artefact.

### Judgements made in marking

Run 33's judgements J1 to J4, run 40's J5 and run 43's J6 are applied unchanged. J5 and J6 decide
nothing here.

- **J4.** Section 2's sentence "A [Rule] the [Toolchain] runs as [Blocking] alongside its
  [Defences], but whose documentation is missing, is not yet a [Defence]; where clauses 4.2, 5.1
  and 8.1 say [Defence], they include it." is quoted whole by reader 2, from "is not yet a
  [Defence]" by reader 3 and from "where clauses 4.2, 5.1 and 8.1" by reader 4: one sentence, three
  readers. Readers 1 and 5 each quote both section 9's sentence and clause 9.1's sentence on
  section 8, so the two are one passage for both. Readers 2 and 4 quote the same [Project record]
  entry, and the same 4.1 sentence.
- **J8. Reader 1's 6.2.** The key accepts No but says "the reasoning must mention the
  generic-justification requirement", and reader 1's does not. Marked as written, it is a miss.
  It is not traceable: the grade is the key's, and the sentence it rests on is one the fixture
  fails too, so the reasoning does not show the clause read differently. 6.2 is four of five and
  meets its threshold. Marked the other way, 6.2 is five of five; the verdict is FAIL either way.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                 | Clause | Readers        | Text                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------------- | ------------------------------------------------------------------ |
| "... is not yet a [Defence]; where clauses 4.2, 5.1 and 8.1 say [Defence], they include it."                                                                                                                            | 2      | three: 2, 3, 4 | Rewritten by revision 4                                            |
| "where the [Toolchain] is one the project ships, every MUST in section 8 as well", set against 9.1's "Section 8, which section 9 adds where the [Toolchain] is one the project ships, bears on the artefact grade only" | 9, 9.1 | two: 1, 5      | Section 9's sentence untouched base; 9.1's rewritten by revision 4 |
| "The one place a project writes down every judgement the method specification delegates to it, whether a [Calibration], an [Exception] or a convention.", set against clause 6.1                                        | 2, 6.1 | two: 2, 4      | Entry rewritten by revision 4; 6.1 untouched base                  |
| "That document's MUSTs are those of its sections 4 to 7, and every one applies; in brief, they are six."                                                                                                                | 4.1    | two: 2, 4      | Rewritten by revision 3                                            |
| "The [Toolchain] MUST resolve every [Identifier] its [Defences] print", set against "an [Identifier] the [Detector] resolves under that document's clause 6 meets this clause"                                          | 4.2    | one: 3         | The MUST untouched base; the second written by revision 4          |
| "The two verdicts MUST be graded and declared separately, and neither implies the other.", set against 9.2's "The declaration is optional"                                                                              | 9.1    | one: 3         | Untouched base                                                     |
| "A [Toolchain] [Conforms] with [Agent] support if it additionally satisfies section 7."                                                                                                                                 | 9      | one: 2         | Untouched base                                                     |
| "its entry MAY be sourced from wherever it is enabled"                                                                                                                                                                  | 5.3    | one: 3         | Untouched base                                                     |
| "A [Toolchain] is measured at the project level.", set against 9.1's "a [Toolchain] against this document as it stands when installed into a [Consuming project] with nothing else built around it"                     | 1, 9.1 | one: 4         | Untouched base                                                     |
| "It MUST provide the route to each one's full documentation."                                                                                                                                                           | 5.1    | one: 4         | Untouched base                                                     |

Notes on the four blocking passages:

- **Section 2, the undocumented blocking rule.** Reader 2 says the sentence excludes these rules
  from the term and then includes them for three clauses, and could not tell which meaning applies
  elsewhere; reader 3 says the two halves read as contradictory; reader 4 could not tell whether
  clause 4.1's routing sentence, which says [Defence] and is not in the list, covers them. Four
  readers named revision 1's wording in run 40, and three named revision 3's in run 43; three name
  revision 4's.
- **Section 9 and 9.1 on section 8.** Readers 1 and 5 read the two as disagreeing on whether
  section 8 bears on the project-level verdict; both quote revision 4's 9.1 sentence. Neither
  applies section 8 to Zigpipe. Three readers named the pair in run 43.
- **The [Project record] entry and clause 6.1.** Readers 2 and 4 could not tell whether a file
  holding only [Exceptions] is the [Project record] clause 6.1 requires a location for, or whether
  every kind of judgement must sit at that one location. Reader 2 grades 6.1 Partial on it (the
  traceable miss above); reader 4 grades Yes with a caveat. One reader quoted the entry's earlier
  wording against 6.1 and 6.2 in run 40.
- **Clause 4.1, "in brief, they are six".** Readers 2 and 4 could not tell whether the six points
  are the whole of the detector specification's MUSTs or a summary of them; both say they did not
  have that specification. Two readers named the earlier "That document's MUSTs, in brief, are
  six." in run 40, and one named revision 3's sentence in run 43.

Run 43's other failures are clear in this run:

- 4.3 is five of five, and no reader quotes clause 4.3's definition of a bypassing route;
- clause 4.2's native-catalogue sentence, two readers in run 43, is quoted by one reader in
  revision 4's wording;
- 6.1 is four of five, with one traceable miss in place of two.

No reader quotes the Rule harness rows, the [Remediation docs] cell or clause 4.5's
[Remediation] link.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met. 6.1 four of five;
  6.2 four of five under J8; every other item five of five.
- A wrong answer traceable to the text, none: not met. 6.1 for reader 2, tracing to the \[Project
  record\] entry as revision 4 rewrote it, read with clause 6.1, untouched base text.
- A passage found confusing by two or more, none outstanding: not met.
  - Section 2's sentence on an undocumented blocking rule (three readers), rewritten by revision 4.
  - Section 9's sentence with 9.1's on section 8 (two readers); 9.1's sentence rewritten by
    revision 4, section 9's untouched base.
  - The [Project record] entry against clause 6.1 (two readers), the entry rewritten by revision 4.
  - Clause 4.1's "in brief, they are six" (two readers), rewritten by revision 3.
- From one reader only, recorded: the six other passages above.

**FAIL.** The 6.1 miss traces to the [Project record] entry as revision 4 rewrote it. Of the four
blocking passages, three are in sentences revision 4 rewrote (section 2, 9.1 with section 9's base
sentence, and the [Project record] entry) and one in a sentence revision 3 rewrote (4.1). None is
in text the change made.
