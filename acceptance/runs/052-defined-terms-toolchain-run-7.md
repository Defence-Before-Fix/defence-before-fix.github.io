# Run 52: TOOLING-SPEC.md, defined terms, seventh run

- **Document**: TOOLING-SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at d316938, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness, Remediation linked, the
  section 3 table's [Remediation docs] cell). Revision 1, after
  [run 33](033-defined-terms-toolchain-run-1.md), is b6e8c2b and b1e7145; revision 2, after
  [run 37](037-defined-terms-toolchain-run-2.md), is 8517aa4; revision 3, after
  [run 40](040-defined-terms-toolchain-run-3.md), is ff77998; revision 4, after
  [run 43](043-defined-terms-toolchain-run-4.md), is c1c461c; revision 5, after
  [run 46](046-defined-terms-toolchain-run-5.md), is 18f782a. The revision after
  [run 49](049-defined-terms-toolchain-run-6.md) is d316938:

  - section 2's sentence on an undocumented rule now reads "In clauses 4.2, 5.1 and 8.1, [Defence]
    also covers a [Rule] whose documentation is missing but whose firing fails the [Toolchain]'s
    run.", in place of "a [Rule] the [Toolchain] runs as [Blocking] alongside its [Defences] whose
    documentation is missing".

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 33, 37, 40, 43, 46 or 49, model alias `haiku`;
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
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/toolchain/KEY.md`
  at d316938, with the judgements of run 33 and of runs 40, 43, 46 and 49

- **Verdict**: FAIL on a miss traceable to the text under 6.1, reader 4, which traces to the
  [Project record] entry revision 5 rewrote, and on three passages found confusing by two or more
  readers:

  - section 2's sentence on an undocumented rule, which revision 6 rewrote (five readers);
  - clause 5.3's sentence letting a listing entry be sourced from wherever the [Defence] is
    enabled, untouched base text (two readers);
  - clause 9.1's "graded and declared separately" and clause 9.2's sentence on a shipping project's
    declaration, each set against 9.2's "The declaration is optional.", untouched base text (two
    readers, under J4 and J9).

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2      | 4.3 | 4.4 | 4.5 | 5.1      | 5.2 | 5.3 | 6.1             | 6.2 | 6.3 | Section 9 | Agent support | Section 8 | Declaration | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | -------- | --- | --- | --- | -------- | --- | --- | --------------- | --- | --- | --------- | ------------- | --------- | ----------- | ----------- |
| 1      | correct | ok  | ok  | ok  | No  | No       | Yes | Yes | Yes | No       | Yes | Yes | Yes             | No  | Yes | ok        | ok            | ok        | ok          | two         |
| 2      | correct | ok  | ok  | ok  | No  | No       | Yes | Yes | Yes | Partial  | Yes | Yes | Yes             | No  | Yes | ok        | ok            | ok        | ok          | two         |
| 3      | correct | ok  | ok  | ok  | No  | No       | Yes | Yes | Yes | No       | Yes | Yes | Yes             | No  | Yes | ok        | ok            | ok        | ok          | two         |
| 4      | correct | ok  | ok  | ok  | No  | No       | Yes | Yes | Yes | No       | Yes | Yes | Partial, miss T | No  | Yes | ok        | ok            | ok        | ok          | three       |
| 5      | correct | ok  | ok  | ok  | No  | No, if … | Yes | Yes | Yes | No, if … | Yes | Yes | Yes             | No  | Yes | ok        | ok            | ok        | ok          | two         |

`T` marks a miss whose reasoning quotes or states what the document requires. Reader 5's table
grades 4.2 and 5.1 No, and its caveat beneath makes both conditional: "If the rules are Blocking,
4.2 and 5.1 are No. If they are only warnings, they are not Defences and both clauses are Yes." Its
4.2 is marked a miss, not traceable, under J12; its 5.1 is correct, since the key accepts both
branches. Every 5.1 grade of Partial or No counts the two `(none)` routes.

### Question 1

Five of five correct, each with at least four bullets the key lists. None says the toolchain must
be a single product, that a declaration is required, or that the agent summary is a MUST. Reader 1
says a declaration is "not a condition of conformance"; reader 5 calls agent support and the
shipped-artefact self-audit "additional conditions where they apply", which asserts no MUST.

### Question 2

All five readers get 2a, 2b and 2c. For 2a, readers 2 to 5 quote section 1's "A [Toolchain] is
measured at the project level." and every reader quotes "whatever the project assembles to run its
checks through"; reader 1 states the level without quoting it (run 33's J1). Every reader quotes
the key's sentence for 2b and for 2c, and every 2c says the two grades do not imply each other.

### Question 3

- **4.1**, five of five No, each on the two undocumented bundled rules and the 4.1 table's
  "Nothing for those two | Fails" row. Readers 1, 2, 3 and 5 note that the detector specification
  was not in the packet; none grades on it.
- **4.2**, four of five. Readers 1 to 4 grade No on the two `(none)` identifiers. Reader 2 says the
  fixture does not state that the two rules are [Blocking] and counts them because they are
  enabled; reader 3 says they "are enabled and their firing fails `zig-qa run`, so they count as
  defences here". Reader 5's 4.2 is conditional (J12).
- **4.3**, five of five Yes, each grading on the routes the fixture describes.
- **5.1**, five of five: readers 1, 3 and 4 No, reader 2 Partial, reader 5 No under its condition,
  each counting the `(none)` routes.
- **6.1**, four of five. Readers 1, 2, 3 and 5 grade Yes on `quality-exceptions.toml`. Reader 4
  grades Partial: "The fixture defines no location for calibrations or conventions, which 6.1's
  'project record' also covers." (J2, below).
- **6.2**, five of five No, each mentioning that nothing rejects a generic justification.
- **Section 9**, **agent support**, **section 8** and **declaration**: five of five give the key's
  answers. Every section 9 verdict names 4.1 among the failing clauses (run 33's J3). No reader
  applies section 8 to Zigpipe; readers 1, 3, 4 and 5 say zig-qa is a separate artefact.

### Judgements made in marking

Run 33's judgements J1 to J4, run 40's J5, run 43's J6, run 46's J8 and run 49's J11 and J12 are
applied unchanged, with run 47's J9. J5, J6, J8 and J11 decide nothing here.

- **J2, reader 4's 6.1.** The reasoning states that clause 6.1's [Project record] covers
  [Calibrations] and conventions as well as [Exceptions], and grades the clause met in part
  because the fixture places no location for them. That is the [Project record] entry read as
  requiring a place for every kind of judgement, where the entry, as revision 5 rewrote it, says
  "[Calibrations], [Exceptions] and conventions, whichever it has made". Under J2 a reasoning that
  states the clause in the clause's words shows it read differently, so the miss is traceable, as
  run 46 marked its reader 2 on the same reasoning. It traces to the entry with clause 6.1's
  untouched "The [Toolchain] MUST define where the [Project record] lives and MUST load it." Read
  narrowly, as quotation marks around a sentence, reader 4 quotes only the term "project record"
  and the miss would not be traceable; 6.1 is four of five either way, and the verdict is FAIL
  either way.
- **J12, reader 5's 4.2.** As run 49's reader 1, reader 5 makes 4.2 conditional on the two enabled
  rules being [Blocking], which the fixture does not state in that word, so the grade is not the
  key's and is a miss. It is not traceable: reader 5 reads section 2's sentence as written, that it
  reaches an undocumented [Rule] whose firing fails the run, and the open point is a fact about the
  fixture, which reader 3 settles from `zig-qa run` stopping when Lintomatic fails. Read the other
  way, with its question 4 entry, which quotes the same sentence and says "My 4.2 and 5.1 verdicts
  depend on this", as run 43's J6 read a grade with its question 4 entry, it would be a traceable
  miss on section 2's sentence, which blocks under question 4 regardless. 4.2 is four of five and
  meets its threshold; the verdict is FAIL either way.
- **J4.** Section 2's sentence "In clauses 4.2, 5.1 and 8.1, [Defence] also covers a [Rule] whose
  documentation is missing but whose firing fails the [Toolchain]'s run." is quoted whole by all
  five readers. Readers 1, 2 and 5 set it against the section 2 table's [Defence] row, reader 5
  quoting "in force and [Blocking]".
- **J4.** Clause 5.3's "Where such a [Defence] is not expressible in the [Toolchain]'s own
  [Detectors], its entry MAY be sourced from wherever it is enabled" is quoted word for word by
  readers 2 and 4: one sentence, two readers.
- **J4 and J9, clause 9.2's "The declaration is optional."** Reader 4 quotes 9.1's "MUST be graded
  and declared separately" and 9.2's "The declaration is optional.", and could not tell whether
  "declared" in 9.1 means 9.2's declaration. Reader 5 quotes 9.2's "A project or shipped artefact
  MAY declare…" and "A project that ships an artefact carries both levels of clause 9.1 in that
  declaration.", and could not tell whether that makes the declaration mandatory for a shipping
  project "given that the same section says it is "optional"". Reader 5 quotes the one word of the
  shared sentence and points at the sentence, as run 48 counted a reader who restated a sentence.
  Both readers set a sentence about declaring both levels against that one sentence, with the
  same doubt, so it is counted as one passage for both, as J9 counted two different [Owner]
  sentences read with one shared line. Read the other way, by whole quoted sentences only, these
  would be two single-reader notes; the verdict is FAIL either way.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                      | Clause   | Readers             | Text                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------------- | ----------------------- |
| "In clauses 4.2, 5.1 and 8.1, [Defence] also covers a [Rule] whose documentation is missing but whose firing fails the [Toolchain]'s run."                                                                                   | 2        | five: 1, 2, 3, 4, 5 | Rewritten by revision 6 |
| "Where such a [Defence] is not expressible in the [Toolchain]'s own [Detectors], its entry MAY be sourced from wherever it is enabled"                                                                                       | 5.3      | two: 2, 4           | Untouched base          |
| "The declaration is optional.", set against 9.1's "MUST be graded and declared separately" (reader 4) and against 9.2's "A project that ships an artefact carries both levels of clause 9.1 in that declaration." (reader 5) | 9.1, 9.2 | two: 4, 5           | Untouched base          |
| "A [Toolchain] MUST NOT route a [Defence] through a [Detector] that does not [Conform] to [the detector specification].", set against the 4.1 table and clause 4.2                                                           | 4.1      | one: 1              | Untouched base          |
| "graded against this document and section 7 of the method specification on that basis."                                                                                                                                      | 9.1      | one: 3              | Untouched base          |

Notes on the blocking passages and the traceable miss:

- **Section 2, the undocumented rule.** All five readers quote revision 6's wording. Readers 1 and
  4 could not tell whether "fails the [Toolchain]'s run" means [Blocking] or is a term of its own,
  reader 4 saying it is not defined; readers 1, 2 and 5 set the sentence against the [Defence]
  row's "in force and [Blocking]", readers 2 and 5 asking whether an undocumented [Rule] that does
  not block is covered; reader 3 says only that it had to decide how the sentence applied to the
  two undocumented rules. Reader 5's conditional 4.2 grade (J12) turns on the same point. Every
  reader still grades 4.1 No and the toolchain as not conforming. Four readers named revision 1's
  wording in run 40, three revision 3's in run 43, three revision 4's in run 46, three revision
  5's in run 49, and five name revision 6's.
- **Clause 5.3, "its entry MAY be sourced".** Reader 2 could not tell what "such a [Defence]"
  refers back to, or whether "its entry" is the listing entry or the [Defence]; reader 4 could not
  tell whether the sentence, in the paragraph on a shipped [Toolchain], reaches Zigpipe's `zq.*`
  rules. Neither grade turns on it: both grade 5.3 Yes. One reader quoted it in run 49.
- **Clause 9.2, "The declaration is optional."** Readers 4 and 5 could not tell whether a project
  that ships an artefact must declare, given 9.1's "declared separately" and 9.2's "carries both
  levels ... in that declaration". Neither grade turns on it: both say the absence of a
  declaration does not affect Zigpipe's verdict. Four readers set 9.2's gap MUST against the same
  sentence in run 33.
- **The 6.1 miss.** Reader 4 graded 6.1 Partial for want of a location for [Calibrations] and
  conventions the fixture does not say Zigpipe has made. Two readers made this miss in run 43 and
  one in run 46; none did in run 49.

Run 49's failure is not clear: the section 2 sentence, rewritten, is quoted by five readers where
three quoted revision 5's. No reader quotes the Rule harness rows, the [Remediation docs] cell or
clause 4.5's [Remediation] link.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met. 4.2 four of five
  under J12; 6.1 four of five; every other item five of five.
- A wrong answer traceable to the text, none: not met. Reader 4's 6.1, under J2, traces to the
  [Project record] entry revision 5 rewrote, with clause 6.1's untouched MUST.
- A passage found confusing by two or more, none outstanding: not met.
  - Section 2's sentence on an undocumented rule (five readers), rewritten by revision 6.
  - Clause 5.3's sentence on sourcing an entry (two readers), untouched base text.
  - Clause 9.2's "The declaration is optional." against 9.1 and 9.2's sentences on declaring both
    levels (two readers, under J4 and J9), untouched base text.
- From one reader only, recorded: the two other passages above.

**FAIL**, on question 4 and on a traceable miss. The section 2 passage is the sentence revision 6
rewrote; the 6.1 miss traces to revision 5's [Project record] entry; the 5.3 and 9.2 passages are
untouched base text. None is in text the original change made.
