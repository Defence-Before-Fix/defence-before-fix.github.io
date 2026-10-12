# Run 34: SPEC.md, gap terms, first run

- **Document**: SPEC.md
- **Pull request**: 18, branch `editor/gap-terms` at ac326b5, the commit the readers were given
  (clause 3.6: a mechanism that cannot resolve identifiers at all is a mechanism gap under clause
  3.2, not a toolchain gap, and blocks the toolchain's claim because it also breaches the
  toolchain specification)
- **Cohort**: five readers, model alias `haiku`; every reader reported `claude-haiku-5-5` in its
  JSON output
- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt is byte for byte the question set, the document and the
  fixture at ac326b5, in that order, each preceded by one `===== FILE: <name> =====` line, and
  that each sheet is the `result` of its reader's JSON output (one turn, `is_error` false)
- **Run within the pull request**: 1
- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands on `next` at 9e914fe, and `acceptance/method/KEY.md` at ac326b5,
  which this pull request does not change
- **Verdict**: FAIL on load-bearing statement 2a, on application item 3.3, on misses traceable to
  the text, and on three passages found confusing by two readers each. None of them is in text
  this change touched.

## Marks

| Reader | Q1 restatement | 2a     | 2b  | 2c  | 3.1     | 3.2 | 3.3             | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 | Q4 passages |
| ------ | -------------- | ------ | --- | --- | ------- | --- | --------------- | --- | --- | --- | ----------- | ------- | --------- | ----------- |
| 1      | correct        | miss T | ok  | ok  | No      | Yes | Partial, miss T | No  | No  | No  | ok          | ok      | ok        | four        |
| 2      | correct        | miss T | ok  | ok  | Partial | Yes | Yes             | No  | No  | No  | ok          | ok      | ok        | two         |
| 3      | correct        | ok     | ok  | ok  | Partial | Yes | Yes             | No  | No  | No  | ok          | ok      | ok        | three       |
| 4      | correct        | miss T | ok  | ok  | Partial | Yes | Yes             | No  | No  | No  | ok          | ok      | ok        | three       |
| 5      | correct        | miss T | ok  | ok  | Partial | Yes | Partial, miss T | No  | No  | No  | ok          | ok      | ok        | two         |

`T` marks a miss whose reasoning quotes the document. Every grade under 3.1, 3.2 and 3.4 to 3.6
is one the key accepts, and every 3.1 grade of Partial or No notes that no independent search
technique is recorded.

### Question 1

Five of five correct. Every sheet has at least four bullets naming obligations the key lists, and
none asserts that the fix comes first, that a test may serve as the detector or that an agent may
baseline.

### Question 2

- **2a**, one of five (reader 3, quoting clause 3.4). The other four leave out a step the key's
  answer requires, each quoting section 2's "building the [Defence] is not optional and MUST be
  attempted before the [Defect] is fixed":
  - Reader 1: class, search, "builds and proves the rule before fixing anything"; no sweep and no
    fixing of every instance.
  - Reader 2: "builds the defence, in the order of clauses 3.1 to 3.6"; names no step.
  - Reader 4: class, rule attempted, then "sweeps and fixes all instances"; no proof.
  - Reader 5: class, rule, proof, sweep "before fixing anything"; no fixing of every instance.
    Each quotes the document, so each is a finding; neither section 2 nor clause 3.4 was changed by
    this pull request.
- **2b**, five of five. All five name the owner and quote section 4's "An [Agent] MUST NOT
  [Baseline], suppress or knowingly leave an [Instance] unfixed on its own authority".
- **2c**, five of five. All five state the six clauses and reproduction, quoting section 7; none
  accepts the report as the verdict.

### Question 3

- **3.3**, three of five (readers 2, 3 and 4, Yes).
  - Reader 1 grades Partial because the CI run reports the fixture as one of five findings,
    whilst Part C says "the enforced run does not report it". The reasoning quotes the clause, so
    the miss is traceable to clause 3.3 Part C.
  - Reader 5 grades Partial because the inline ignore was an exclusion with "no recorded sentence
    and no referral", quoting Part B's "Doubt is [Suppression]", and also fails 3.4 on it. The
    key's excuse covers a reader who attributes the suppression to 3.3 "rather than" 3.4, not to
    both (judgement J3), so this is a miss, traceable.
- **Remediation**: five of five say it does not conform.
- **Defence**: five of five say it does not conform, each naming 3.6.
- **Section 4**: five of five name the inline ignore; readers 1 to 4 also name the unbuilt wider
  rule as a second or arguable decision, which the key accepts alongside it.

### Judgements made in marking

`ACCEPTANCE.md` on `next` gives the key and the thresholds and leaves these open. They are the
judgements run 31 makes on the same key.

- **J1. Which elements of the key's answer to question 2 a sentence must state.** Every element
  that answers a part of the question must be stated; an element the key adds as a gloss is met
  unless the answer asserts its opposite. 2a asks what is done and in what order, so each step
  must appear; 2b's "always a human" is carried by "the owner", the defined term, since the
  question asks who. No 2b mark turns on it: readers 3, 4 and 5 also quote "Always a human", and
  readers 1 and 2 would miss only on the stricter reading.
- **J2. 2c and "reproduction".** An answer that says the verdict rests on reproduction is marked
  correct, as runs 17 and 18 marked it under the same key.
- **J3. The 3.3 excuse is read as written**, for a reader who attributes the suppression to 3.3
  rather than 3.4. Read the other way, reader 5's 3.3 is correct and 3.3 is four of five; the run
  fails on 2a, on reader 1's 3.3 and on question 4 either way.
- **J4. The same passage under question 4** is the same sentence, as run 16 counted it.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                   | Clause           | Readers   | Changed by this pull request |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------- | ---------------------------- |
| "A [Rule] drawn to the exact value or name found in the [Defect] is the same [Narrowing] however it is spelt, and where it stays because the search found nothing wider, the record MUST also name the next wider [Rule]" | 3.1, lower bound | two: 2, 3 | No                           |
| "The absence of an [Instance] is the [Practitioner]'s reason not to widen unasked; it is not authority to exclude the extension."                                                                                         | 4                | two: 1, 3 | No                           |
| "The conclusion that no pattern exists MUST be stated in one sentence, naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search, ..."                    | 2                | two: 3, 5 | No                           |
| "unless the independent search below has found no other [Instance] and the [Practitioner] records that the [Class] is genuinely singular today"                                                                           | 3.1, lower bound | one: 2    | No                           |
| "That rejection is tested as a [Narrowing] is under clause 3.3."                                                                                                                                                          | 3.1, lower bound | one: 1    | No                           |
| "Decisions that MUST go to whoever owns the codebase", set against the Owner entry                                                                                                                                        | 4                | one: 1    | No                           |
| "...bears on the project's claim rather than the [Toolchain]'s."                                                                                                                                                          | 3.6              | one: 1    | Yes: the sentence it ends    |
| "Then the proof, which runs the other way round, and both ways."                                                                                                                                                          | 3.3, Part B      | one: 2    | No                           |
| "a [Narrowing] that excludes more code than the [Rule] still covers MUST be reported to the [Owner] as if it were a [Suppression]."                                                                                       | 3.3, Part B      | one: 4    | No                           |
| "...the scale at which that becomes true is tremendous."                                                                                                                                                                  | 3.4              | one: 4    | No                           |
| "The attempt that separates the first from the second is complete when..."                                                                                                                                                | 2                | one: 4    | No                           |
| The Owner entry's "Always a human." set against "Where the project has recorded nobody, the [Owner] is whoever instructed the [Practitioner]"                                                                             | 1, Owner         | one: 5    | No                           |

Reader 2 quotes two sentences of the lower-bound bullet. Its second sentence is the one reader 3
quotes, so the two readers share that passage. Readers 1 and 2 quote two further sentences of the
same bullet, each single. Reader 1's 3.6 passage is the last clause of the one sentence this pull
request rewrote. The words quoted predate the change, but under J4 the passage is that sentence.
It is one reader only, so it is recorded and does not block. No keyed item turns on that sentence,
since every reader grades 3.6 No on the wiki documentation.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: not met. 2a one of five; 2b and 2c five of
  five.
- Restatement and application, at least four of five on each keyed item: not met. 3.3 three of
  five; every other item five of five.
- A wrong answer traceable to the text, none: not met. 2a for readers 1, 2, 4 and 5, and 3.3 for
  readers 1 and 5, each a finding.
- A passage found confusing by two or more, none outstanding: not met. Clause 3.1's lower-bound
  sentence, section 4's "not to widen unasked" sentence and section 2's search-vocabulary
  sentence, two readers each.
- From one reader only, recorded: the nine other passages above, among them reader 1's passage
  in the changed clause 3.6 sentence.

**FAIL.** No failure traces to text this pull request changed. The 2a misses rest on section 2
and clause 3.4. The 3.3 misses rest on clause 3.3 Parts B and C. The three blocking passages are
in clause 3.1, section 4 and section 2. One reader quoted part of the changed 3.6 sentence as
confusing, and no other reader did.
