# Run 50: SPEC.md, defined terms, seventh run

- **Document**: SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at d316938, the commit the
  readers were given. The change is be546ea and 35f42bf (Remediation defined, Harness renamed
  Rule harness). Revision 1, after [run 31](031-defined-terms-method-run-1.md), is df016ab;
  revision 2, after [run 35](035-defined-terms-method-run-2.md), is 0fd02ef; revision 3, after
  [run 38](038-defined-terms-method-run-3.md), is 8dc5879; revision 4, after
  [run 41](041-defined-terms-method-run-4.md), is 688ae1b; revision 5, after
  [run 44](044-defined-terms-method-run-5.md), is c4e2d86. The revision after
  [run 47](047-defined-terms-method-run-6.md) is 293699e:

  - the [Owner] entry gains one sentence after "Always a human.": "Where this specification says
    "whoever owns the codebase", it means the [Owner]." Section 4's lead-in and clause 3.4 are
    unchanged.

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 31, 35, 38, 41, 44 or 47, model alias `haiku`;
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
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/method/KEY.md` at
  d316938, with the judgements of runs 31, 44 and 47

- **Verdict**: FAIL on two passages found confusing by two or more readers: the [Owner] entry's
  sentence on the default [Owner] (three readers), which revision 4 wrote, and section 4's
  sentence letting a [Rule] merge at full width, read against the sentence that a [Rule] does not
  become [Blocking] until every [Instance] is fixed (two readers), untouched base text. Every keyed
  item is five of five, and no miss is traceable to the text.

## Marks

| Reader | Q1 restatement | 2a  | 2b  | 2c  | 3.1     | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 | Q4 passages |
| ------ | -------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | ----------- | ------- | --------- | ----------- |
| 1      | correct        | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | four        |
| 2      | correct        | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | two         |
| 3      | correct        | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | two         |
| 4      | correct        | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | one         |
| 5      | correct        | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | two         |

Every grade is one the key accepts. Every 3.1 grade of Partial or No notes that no two
independent search techniques are recorded.

### Question 1

Five of five correct, each with at least four bullets the key lists and none it marks wrong.
Readers 1, 2, 3 and 5 add fixing the original defect with a reproduction test, which section 6
states. Every reader puts baselines and suppression with the owner, which section 4 states. No reader says the instance is fixed first, that a test may serve as the detector, or
that an agent may baseline.

### Question 2

- **2a**, five of five, each quoting section 2's "In order, the steps are section 3's: ..." and
  stating the four steps in order. Reader 1 also quotes clause 3.4's MUST sentence, and reader 2
  section 2's "MUST be attempted before the [Defect] is fixed".
- **2b**, five of five, each naming the owner and quoting section 4's sentence on what an [Agent]
  MUST NOT do. Reader 1 says the owner is a human, and readers 3 and 4 quote the [Owner] entry's
  "Always a human."; readers 2 and 5 name the owner without saying so, which run 31's J1 marks
  correct.
- **2c**, five of five, each stating that all six clauses of section 3 were followed and that the
  verdict rests on reproduction. Readers 1, 3, 4 and 5 quote section 7's conforming-[Remediation]
  sentence; readers 2, 3 and 4 quote "A verdict on a [Remediation] or a [Defence] MUST rest on
  reproduction, not on the report".

### Question 3

- **3.1**, five of five: three No and two Partial, each noting that no two independent search
  techniques are recorded.
- **3.2** and **3.3**, five of five Yes. Every 3.3 reasoning rests on commit B being red before
  the fix in a later commit. Readers 1 and 5 say the inline ignore is not judged under 3.3; reader
  4 adds that the description shows no fresh-checkout reproduction of the red run and still grades
  Yes.
- **3.4**, five of five No, each naming the inline ignore on `Report::render()`. Readers 1, 3 and
  5 also note that the count of five includes the [Fixture].
- **3.5**, five of five No, each on the inline ignore no recorded decision covers.
- **3.6**, five of five No, each naming the wiki documentation, not versioned with the rule.
- **Remediation**: five of five say it does not conform, each with 3.4 and 3.6 among the failing
  clauses or, for reader 5, four of the six failing as graded. **Defence**: five of five say it
  does not conform, each naming 3.5 and 3.6; readers 1, 2, 4 and 5 also name 3.1, and reader 3
  says its lower bound is weakened. **Section 4**:
  five of five name the inline ignore on `Report::render()`, and all five also name leaving the
  wider rule unbuilt, which the key accepts.

### Judgements made in marking

Run 31's judgements J1 to J4, run 44's J7 and run 47's J9 are applied unchanged; J3, J7 and J9
decide nothing here.

- **J1, 2b for readers 2 and 5.** "The owner", the defined term, carries "always a human", as in
  run 31.
- **J4.** The [Owner] entry's sentence "That default [Owner] takes the decisions section 4 gives
  the [Owner], but is usually the person under the same deadline as the [Practitioner], so a
  decision of theirs to keep an [Instance] unfixed, [Suppress], [Baseline] or remove a [Rule] MUST
  be recorded in the project record with its justification." is quoted from its start by reader 4,
  from "a decision of theirs" by reader 2, and by its words "usually the person under the same
  deadline as the [Practitioner]" by reader 1, who sets them, with "Always a human", against the
  entry's untouched "Where the project has recorded nobody, the [Owner] is whoever instructed the
  [Practitioner]". Each quotes words of the same sentence, so it is one passage for all three, as
  run 48 counted a reader who quoted a sentence's last words. Readers 1 and 4 ask the same thing,
  whether the instructing party can take section 4's decisions; reader 2 asks about the bracketed
  verb "[Suppress]". Counting reader 2 out, or reader 1, the sentence still has two readers and
  blocks.
- **J4.** Section 4's "the [Rule] MAY merge at full width with that case recorded as a known
  [Instance] awaiting the [Owner]" and "provided the [Rule] does not become [Blocking] until every
  [Instance] is fixed" are each quoted by readers 1 and 3, and each reader sets the one against
  the other, so the two are one passage for both.
- **J4.** Reader 2 quotes section 2's "Failing to write a [Rule] that satisfies clause 3.1's bounds
  is itself the evidence that the [Defect] is out of scope." Reader 3 quotes two other sentences of
  the same "Attempt rather than pre-judge" paragraph, "naming at least two independent attempts at
  writing the [Rule]" and "Two attempts are independent when they would miss different things, as
  two search techniques are under clause 3.1." These are two single-reader notes. Read by
  paragraph, they would be a third blocking passage; the verdict is FAIL either way.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                                                                                                          | Clause    | Readers        | Text                                                                                 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | -------------- | ------------------------------------------------------------------------------------ |
| "That default [Owner] takes the decisions section 4 gives the [Owner], but is usually the person under the same deadline as the [Practitioner], so a decision of theirs to keep an [Instance] unfixed, [Suppress], [Baseline] or remove a [Rule] MUST be recorded in the project record with its justification." | 1 (Owner) | three: 1, 2, 4 | Written by revision 4; reader 1 reads it with the entry's untouched default sentence |
| "the [Rule] MAY merge at full width with that case recorded as a known [Instance] awaiting the [Owner]", set against "provided the [Rule] does not become [Blocking] until every [Instance] is fixed"                                                                                                            | 4         | two: 1, 3      | Untouched base                                                                       |
| "where fixing every [Instance] is genuinely unfeasible, and only a very large change is unfeasible.", set against "No threshold is given here deliberately."                                                                                                                                                     | 3.4       | one: 1         | The first written by revision 4; the second untouched base                           |
| "A clean run of the [Rule] is therefore not evidence of saturation either: ..."                                                                                                                                                                                                                                  | 3.1       | one: 1         | Untouched base                                                                       |
| "Failing to write a [Rule] that satisfies clause 3.1's bounds is itself the evidence that the [Defect] is out of scope."                                                                                                                                                                                         | 2         | one: 2         | Untouched base                                                                       |
| "naming at least two independent attempts at writing the [Rule]", with "Two attempts are independent when they would miss different things, as two search techniques are under clause 3.1."                                                                                                                      | 2         | one: 3         | Both written by revision 3                                                           |
| "An ignore comment or ignore entry placed on one [Instance] counts against none of the three: it leaves the [Rule] and its proof as they were, and clause 3.4 and section 4 judge it."                                                                                                                           | 3.3       | one: 5         | Written by revision 4                                                                |
| "examine a sample of the latter large enough, given how much the surrounding code varies, that a wrong answer there would have been seen."                                                                                                                                                                       | 3.4       | one: 5         | Untouched base                                                                       |

Notes on the two blocking passages:

- **The [Owner] entry's default-owner sentence.** Readers 1 and 4 could not tell whether the person
  who instructed the [Practitioner] can take the decisions section 4 gives the \[Owner\]: reader 4
  sets the sentence against section 4's "MUST go to" list and its "default position is that none
  of these are permitted"; reader 1 against "Always a human", asking what happens when the
  instructing party is an agent. Reader 2 could not read the bracketed verb "[Suppress]" among the
  nouns of the same list. No reader's grade turns on it: the fixture has a named owner, and every
  reader says so. In run 47 reader 2 quoted the entry's untouched default sentence, read with
  section 4's lead-in.
- **Section 4, merging at full width.** Readers 1 and 3 could not reconcile a [Rule] that MAY merge
  with a known [Instance] open with the later proviso that a [Rule] delivered across several
  changes does not become [Blocking] until every [Instance] is fixed. Neither grade turns on it. No
  reader in runs 31 to 47 quoted either sentence.

Run 47's failure is clear in this run: no reader quotes section 4's lead-in "Decisions that MUST go
to whoever owns the codebase" under question 4, and no reader quotes revision 6's sentence. Readers
2 and 4 cite the lead-in in their section 4 answers and give the inline ignore to the owner.

No reader quotes the Remediation entry, the [Remediation docs] links or any other sentence the
original change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met, five of five
  throughout.
- A wrong answer traceable to the text, none: met.
- A passage found confusing by two or more, none outstanding: not met.
  - The [Owner] entry's sentence on the default [Owner] (three readers), written by revision 4.
  - Section 4's full-width merge sentence against the [Blocking] proviso (two readers), untouched
    base text.
- From one reader only, recorded: the six other passages above.

**FAIL**, on question 4 alone. One blocking passage is the sentence revision 4 wrote in the [Owner]
entry; the other is untouched base text. None is in text the original change or revision 6 made.
