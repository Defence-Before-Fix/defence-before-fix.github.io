# Run 43: TOOLING-SPEC.md, defined terms, fourth run

- **Document**: TOOLING-SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at ff77998, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness, Remediation linked, the
  section 3 table's [Remediation docs] cell). Revision 1, after
  [run 33](033-defined-terms-toolchain-run-1.md), is b6e8c2b and b1e7145; revision 2, after
  [run 37](037-defined-terms-toolchain-run-2.md), is 8517aa4. The revision after
  [run 40](040-defined-terms-toolchain-run-3.md) is ff77998:

  - section 2's "Clauses 4.2, 5.1 and 8.1 still reach it: ..." becomes "Clauses 4.2, 5.1 and 8.1
    apply to it as if it were one: it belongs in the listing clause 5.1 requires, and its missing
    documentation fails what each of the three requires of documentation, ...";
  - clause 4.1's "That document's MUSTs, in brief, are six." becomes "That document's MUSTs are
    those of its sections 4 to 7, and every one applies; in brief, they are six.";
  - clause 9.2's gap-duty sentence is shortened, and the sentence on method clause 3.2 now calls
    that duty "a separate one".

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 33, 37 or 40, model alias `haiku`; every reader
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
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/toolchain/KEY.md`
  at ff77998, with the judgements of run 33

- **Verdict**: FAIL on application item 6.1, three of five with both misses traceable to the
  [Project record] entry; on a traceable miss under 4.3; and on three passages found confusing by
  two or more readers:

  - section 9's sentence bringing section 8 into a shipped [Toolchain]'s verdict, with clause
    9.1's "Section 8 bears on the artefact grade only", untouched base text;
  - section 2's sentence on an undocumented blocking rule, which revision 3 rewrote;
  - clause 4.2's sentence on a third-party [Detector]'s native catalogue, untouched base text.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3             | 4.4 | 4.5 | 5.1 | 5.2 | 5.3 | 6.1             | 6.2 | 6.3 | Section 9 | Agent support | Section 8 | Declaration | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --------- | ------------- | --------- | ----------- | ----------- |
| 1      | correct | ok  | ok  | ok  | No  | No  | Yes             | Yes | Yes | No  | Yes | Yes | Yes             | No  | Yes | ok        | ok            | ok        | ok          | three       |
| 2      | correct | ok  | ok  | ok  | No  | No  | Yes             | Yes | Yes | No  | Yes | Yes | Partial, miss T | No  | Yes | ok        | ok            | ok        | ok          | three       |
| 3      | correct | ok  | ok  | ok  | No  | No  | Yes             | Yes | Yes | No  | Yes | Yes | Yes             | No  | Yes | ok        | ok            | ok        | ok          | one         |
| 4      | correct | ok  | ok  | ok  | No  | No  | Partial, miss T | Yes | Yes | No  | Yes | Yes | Yes             | No  | Yes | ok        | ok            | ok        | ok          | two         |
| 5      | correct | ok  | ok  | ok  | No  | No  | Yes             | Yes | Yes | No  | Yes | Yes | Partial, miss T | No  | Yes | ok        | ok            | ok        | ok          | two         |

`T` marks a miss whose reasoning quotes or states what the document requires. Every 5.1 grade of
No counts the two `(none)` routes, and every 6.2 grade of No mentions the generic-justification
requirement.

### Question 1

Five of five correct, each with at least four bullets the key lists. None says the toolchain must
be a single product, that a declaration is required, or that the agent summary is a MUST. Reader
5's last bullet calls section 8 "conditional", for a shipped [Toolchain], which asserts no
obligation the document does not state.

### Question 2

All five readers get 2a, 2b and 2c. For 2a, readers 1, 4 and 5 quote section 1's two sentences
with the list of parts; readers 2 and 3 quote them without it and state "whatever the project
assembles" (run 33's judgement J1). Every reader quotes the key's sentence for 2b and for 2c.

### Question 3

- **4.3**, four of five. Readers 1, 2, 3 and 5 grade Yes on the one route the fixture describes.
  Reader 4 grades Partial because "the fixture does not say whether other routes, such as rule
  switches in `lintomatic.toml` or baselines, are closed" (judgement J6, below).
- **5.1**, five of five No, each counting the `(none)` routes.
- **6.1**, three of five. Readers 2 and 5 grade Partial. Reader 5: "section 2 defines the project
  record as also holding calibrations and conventions, and the fixture gives no location for
  those." Reader 2: "The project record also covers calibrations and conventions, and the fixture
  gives no location for either." Each states the [Project record] entry in its own words, "[Calibrations],
  [Exceptions] and conventions", so each miss is traceable (run 33's judgement J2). They trace
  to that entry read with clause 6.1's "The [Toolchain] MUST define where the [Project record]
  lives and MUST load it", both untouched base text. One reader quoted the same entry against
  6.1 and 6.2 as confusing in run 40.
- **Section 9**, **agent support**, **section 8** and **declaration**: five of five give the key's
  answers, each naming 4.1 and 4.2 among the failing clauses. None applies section 8 to Zigpipe,
  although readers 1, 3 and 5 quote section 9 and 9.1 as confusing on section 8.

### Judgements made in marking

Run 33's judgements J1 to J4 are applied unchanged.

- **J4.** Section 2's sentence "Clauses 4.2, 5.1 and 8.1 apply to it as if it were one" is quoted
  verbatim by readers 1 and 2. Reader 4 quotes the paragraph's first sentence and restates the
  second, "says that clauses 4.2, 5.1 and 8.1 apply to a blocking rule without documentation",
  and is counted with them, as run 40 counted its reader 1 on the same sentence. Without reader 4
  the sentence still has two readers and blocks. Readers 1, 3 and 5 each quote both section 9's
  sentence and 9.1's sentence on section 8, so the two are one passage for all three.
- **J6. Reader 4's 4.3.** Its 4.3 row grades on the fixture's silence and quotes nothing. Its
  question 4 entry quotes clause 4.3's "A route bypasses the [Project record] when a finding can be
  silenced through it without an entry appearing in the \[Project record\]: ..." and asks whether a
  rule switched off in configuration is such a route, the doubt the grade turns on. Read
  together, as run 37 read "the clause reaches every route", the reasoning shows the clause read
  differently, and the miss is counted traceable to clause 4.3's body, untouched base text, which
  revision 2's sentence "nothing is owed for a route it does not have" did not settle for this
  reader. Read narrowly, the 4.3 row alone, it is not traceable. 4.3 is four of five either way,
  and the verdict is FAIL either way.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                                | Clause | Readers        | Text                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------------- | --------------------------------------------------------- |
| "where the [Toolchain] is one the project ships, every MUST in section 8 as well", set against 9.1's "Section 8 bears on the artefact grade only; clause 5.3 is its project-level counterpart."                                        | 9, 9.1 | three: 1, 3, 5 | Untouched base                                            |
| "Clauses 4.2, 5.1 and 8.1 apply to it as if it were one: ...", set against clause 4.2's "every [Identifier] its [Defences] print" or its native-catalogue sentence                                                                     | 2      | three: 1, 2, 4 | Rewritten by revision 3                                   |
| "A third-party [Detector]'s native catalogue, which the [Toolchain] orchestrates without claiming as its own, is resolved under that document's clause 6 and is not re-shipped here.", set against section 2's sentence above          | 4.2    | two: 2, 4      | Untouched base, set against a sentence revision 3 rewrote |
| "That document's MUSTs are those of its sections 4 to 7, and every one applies; in brief, they are six."                                                                                                                               | 4.1    | one: 2         | Rewritten by revision 3                                   |
| "The [Toolchain] MUST reject a justification that could be pasted onto any [Exception] unchanged, by a check it documents: ...", read with the clause's requirement to name the [Hazard] and the scope                                 | 6.2    | one: 2         | Untouched base                                            |
| "A route bypasses the [Project record] when a finding can be silenced through it without an entry appearing in the \[Project record\]: an inline [Suppression] comment, a per-line ignore and a silently generated [Baseline] all do." | 4.3    | one: 4         | Untouched base                                            |
| "A project or a shipped artefact MAY declare ...", set against "A project that ships an artefact carries both levels of clause 9.1 in that declaration"                                                                                | 9.2    | one: 5         | Untouched base                                            |

Notes on the three blocking passages:

- **Section 9 and 9.1 on section 8.** Readers 1, 3 and 5 read section 9 as putting section 8 into
  the project-level verdict where the [Toolchain] is shipped, and 9.1 as keeping it out; reader 1
  calls 9.1 "the opposite of clause 9 on the same point". None of them applies section 8 to
  Zigpipe, which ships nothing. No reader quoted either sentence in runs 33 to 40, though reader 3
  of run 40 put section 8 "outside the MUST grade" in question 1.
- **Section 2, the undocumented blocking rule.** Reader 1 had to combine the sentence with 4.2's
  "every [Identifier] its [Defences] print" to know whether 4.2 covers the undocumented rules.
  Readers 2 and 4 set it against 4.2's native-catalogue sentence and could not tell which governs
  Lintomatic's two undocumented bundled rules. Four readers named revision 1's wording in run 40;
  three name revision 3's.
- **Clause 4.2, the native catalogue.** The same doubt from the other side, readers 2 and 4: the
  sentence seems to send a third-party [Detector]'s catalogue back to the detector
  specification, where section 2 applies 4.2 to its undocumented blocking rules. Every reader
  still grades 4.2 No. One reader quoted the same sentence in run 37, against revision 1's
  section 2 paragraph.

Run 40's other failures are clear in this run:

- clause 9.2's gap-duty sentence, which revision 3 shortened (two readers in run 40); no reader
  quotes it or the sentence on method clause 3.2;
- clause 4.1's "in brief, are six" (two readers in run 40); one reader quotes revision 3's
  replacement.

No reader quotes the Rule harness rows, the [Remediation docs] cell or clause 4.5's
[Remediation] link.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: not met. 6.1 three of
  five; 4.3 four of five; every other item five of five.
- A wrong answer traceable to the text, none: not met. 6.1 for readers 2 and 5, tracing to the
  [Project record] entry with clause 6.1, untouched base text; 4.3 for reader 4 under J6, tracing
  to clause 4.3's body, untouched base text.
- A passage found confusing by two or more, none outstanding: not met.
  - Section 9's sentence with 9.1's on section 8 (three readers), untouched base text.
  - Section 2's sentence on an undocumented blocking rule (three readers), rewritten by revision 3.
  - Clause 4.2's native-catalogue sentence (two readers), untouched base text.
- From one reader only, recorded: the four other passages above.

**FAIL.** The 6.1 and 4.3 misses trace to untouched base text. One blocking passage is a sentence
revision 3 rewrote (section 2), and two are untouched base text (section 9 with 9.1, and 4.2).
None is in text the change made.
