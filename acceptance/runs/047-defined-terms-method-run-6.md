# Run 47: SPEC.md, defined terms, sixth run

- **Document**: SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at 18f782a, the commit the
  readers were given. The change is be546ea and 35f42bf (Remediation defined, Harness renamed
  Rule harness). Revision 1, after [run 31](031-defined-terms-method-run-1.md), is df016ab;
  revision 2, after [run 35](035-defined-terms-method-run-2.md), is 0fd02ef; revision 3, after
  [run 38](038-defined-terms-method-run-3.md), is 8dc5879; revision 4, after
  [run 41](041-defined-terms-method-run-4.md), is 688ae1b. The revision after
  [run 44](044-defined-terms-method-run-5.md) is c4e2d86:

  - clause 3.3 Part B's reporting MUST reads "a [Narrowing] that excludes more code than it leaves
    the [Rule] covering MUST be reported to the [Owner] as if it were a [Suppression]", in place of
    "more code than the [Rule] still covers";
  - clause 3.3 Part C's sentence on [Fixtures] ends "the [Sweep] excludes it under clause 3.4, so
    there is no circularity ...", and no longer says that the enforced run does not report it.

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 31, 35, 38, 41 or 44, model alias `haiku`;
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
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/method/KEY.md` at
  18f782a, with the judgements of runs 31 and 44

- **Verdict**: FAIL on one passage found confusing by two readers: section 4's "Decisions that
  MUST go to whoever owns the codebase", each reader setting it against a sentence of the [Owner]
  entry. It is untouched base text. Every keyed item is five of five, and no miss is traceable to
  the text.

## Marks

| Reader | Q1 restatement | 2a  | 2b  | 2c  | 3.1     | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 | Q4 passages |
| ------ | -------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | ----------- | ------- | --------- | ----------- |
| 1      | correct        | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | two         |
| 2      | correct        | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | two         |
| 3      | correct        | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | three       |
| 4      | correct        | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | two         |
| 5      | correct        | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | two         |

Every grade is one the key accepts. Every 3.1 grade of Partial or No notes that no independent
search technique is recorded.

### Question 1

Five of five correct, each with at least four bullets the key lists and none it marks wrong.
Readers 1, 3 and 4 add fixing the original defect with a reproduction test, which section 6
states. Readers 1, 3 and 5 put suppression, baselines and unfixed [Instances] with the owner,
which section 4 states. No reader says the instance is fixed first, that a test may serve as the
detector, or that an agent may baseline.

### Question 2

- **2a**, five of five, each quoting section 2's "In order, the steps are section 3's: ..." and
  stating the four steps in order.
- **2b**, five of five, each naming the owner and quoting section 4's sentence on what an [Agent]
  MUST NOT do. Readers 1, 2 and 3 say the owner is a human; readers 4 and 5 name the owner without
  saying so, which run 31's J1 marks correct.
- **2c**, five of five, each quoting section 7's conforming-[Remediation] sentence and stating
  that the verdict rests on reproduction, not on the report. Reader 1 also quotes "A verdict on a
  [Remediation] or a [Defence] MUST rest on reproduction, not on the report."

### Question 3

- **3.1**, five of five: three No and two Partial, each noting that no two independent search
  techniques are recorded.
- **3.2** and **3.3**, five of five Yes. Every 3.3 reasoning rests on commit B being red with the
  originating [Instance] present and surviving the merge. No reader grades 3.3 on the inline
  ignore or on the fixture's red run reporting the [Fixture].
- **3.4**, five of five No, each naming the inline ignore on `Report::render()`. Readers 2, 4 and
  5 also note that the count of five includes the [Fixture].
- **3.5**, five of five No, each on the uncovered inline ignore.
- **3.6**, five of five No, each naming the wiki documentation, not versioned with the rule.
- **Remediation**: five of five say it does not conform. **Defence**: five of five say it does
  not conform, each naming 3.6 and 3.5, and readers 1, 3, 4 and 5 also the 3.1 search. **Section
  4**: five of five name the inline ignore on `Report::render()`, and all five also name leaving
  the wider rule unbuilt, which the key accepts.

### Judgements made in marking

Run 31's judgements J1 to J4 and run 44's J7 are applied unchanged; J3 and J7 decide nothing here.

- **J1, 2b for readers 4 and 5.** "The owner", the defined term, carries "always a human", as in
  run 31.
- **J4.** Readers 3 and 4 quote different sentences of clause 3.1's lower-bound bullet, and
  readers 3 and 5 different sentences of section 2's "Attempt rather than pre-judge" paragraph;
  each is a single-reader note. Read by paragraph, both would block.
- **J9. Section 4's list lead-in as a sentence.** Section 4's "**Decisions that MUST go to whoever
  owns the codebase:**" introduces a list and ends with a colon. Reader 1 quotes it as "Decisions
  that MUST go to whoever owns the codebase" and reader 2 as "MUST go to whoever owns the
  codebase.", which reader 2 attributes to section 4 and clause 3.4; clause 3.4's own sentence
  reads "a decision for whoever owns the codebase", so reader 2's words are section 4's line.
  The line carries a MUST and is the unit both readers point at, word for word, with the same
  doubt, so it is counted as one sentence under J4 and as one passage for both. Each reader also
  quotes a different sentence of the [Owner] entry, reader 1 its first and reader 2 its default
  sentence, and these are counted as read with the lead-in, as run 46 counted the section 9 and
  9.1 pair. Read the other way, with the lead-in not a sentence, the two [Owner] sentences would
  be two single-reader notes and the run would meet every criterion; read by paragraph, they
  would still be one passage, and so would the two pairs under J4 above. The stricter reading is
  taken, since the criterion counts a passage pointed at and the bar only moves up. The verdict
  turns on this judgement.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                                                                                     | Clause           | Readers   | Text                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------- | ----------------------------------------------------------------------------- |
| "Decisions that MUST go to whoever owns the codebase", set against the [Owner] entry's "Whoever holds authority over a project's [Exceptions] and [Calibrations]." (reader 1) and "Where the project has recorded nobody, the [Owner] is whoever instructed the [Practitioner]." (reader 2) | 4, 1 (Owner)     | two: 1, 2 | Untouched base, the lead-in and both [Owner] sentences                        |
| "Then the proof, which runs the other way round, and both ways.", with "Where the narrower shape was chosen from the outset and no wider [Rule] was ever built, the before state is a [Fixture] of the wider pattern the [Rule] does not catch ..."                                         | 3.3, Part B      | one: 1    | Untouched base                                                                |
| "The test is the [Hazard], never the count.", set against "a [Narrowing] that excludes more code than it leaves the [Rule] covering MUST be reported to the [Owner] as if it were a [Suppression]"                                                                                          | 3.3, Part B      | one: 2    | The first untouched base; the second written by revision 5                    |
| "Failing to write a [Rule] that satisfies clause 3.1's bounds is itself the evidence that the [Defect] is out of scope."                                                                                                                                                                    | 2                | one: 3    | Untouched base                                                                |
| "A [Rule] drawn to the exact value or name found in the [Defect] is drawn to the [Instance] in the same way, however it is spelt."                                                                                                                                                          | 3.1, lower bound | one: 3    | Written by revision 1                                                         |
| "only where it does not is the location the project's choice, and then the only requirement is that somebody deciding what to invest in the [Toolchain] would find it."                                                                                                                     | 3.2              | one: 3    | Untouched base                                                                |
| "The attempt that separates the first way out from the second, no pattern from no extensible [Detector], is complete when ..."                                                                                                                                                              | 2                | one: 4    | Rewritten by revision 3                                                       |
| "unless the independent search below has found no other [Instance] and the [Practitioner] records that the [Class] is genuinely singular today", with "Where it stays because the search found nothing wider,"                                                                              | 3.1, lower bound | one: 4    | The first untouched base; the second made a sentence of its own by revision 1 |
| "it fails rather than warns", in section 7's [Defence] sentence, set against clause 3.5's "every [Suppression] it carries is covered by a recorded decision"                                                                                                                                | 7, 3.5           | one: 5    | Untouched base                                                                |
| "naming the attempts is what lets them judge whether the attempt was one"                                                                                                                                                                                                                   | 2                | one: 5    | Rewritten by revision 3                                                       |

Note on the blocking passage:

- **Section 4's lead-in with the [Owner] entry.** Readers 1 and 2 could not tell whether "whoever
  owns the codebase", in section 4's lead-in and in clause 3.4, names the same authority as the
  defined [Owner], or whether the phrase is meant as the defined term. The lead-in is not linked
  to [Owner], and a bullet of the list beneath it says "leaves the decision with the [Owner]". Neither
  reader's grades turn on it: both give section 4's inline ignore to the owner, and the fixture
  has a named owner. No reader in runs 31 to 44 quoted the lead-in.

Run 44's failures are clear in this run:

- no reader fails 3.3, and no reader reads Part C as saying the enforced run must not report the
  [Fixture]; no reader quotes Part C;
- Part B's reporting MUST, two readers in run 44, is quoted by one reader in revision 5's
  wording, set against an untouched sentence of the same Part.

No reader quotes the Remediation entry, the [Remediation docs] links or any other sentence the
original change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met, five of five
  throughout.
- A wrong answer traceable to the text, none: met.
- A passage found confusing by two or more, none outstanding: not met. Section 4's "Decisions
  that MUST go to whoever owns the codebase", read with the [Owner] entry (two readers, under
  J9), untouched base text.
- From one reader only, recorded: the nine other passages above.

**FAIL**, on question 4 alone, and on a reading the record states (J9). The blocking passage is
untouched base text. None is in text the change or any of its revisions made.
