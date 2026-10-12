# Run 31: SPEC.md, defined terms, first run

- **Document**: SPEC.md
- **Pull request**: not yet opened; branch `editor/defined-terms` at 35f42bf, the commit the
  readers were given (be546ea defines Remediation and renames Harness to Rule harness; 35f42bf
  brings the key's 2c quotations to the new wording)
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
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/method/KEY.md` at
  35f42bf
- **Verdict**: FAIL on load-bearing statement 2a, on a miss traceable to the text under 3.3, and
  on two passages found confusing by two or more readers. None of them is in text this change
  touched.

## Marks

| Reader | Q1 restatement | 2a     | 2b  | 2c  | 3.1     | 3.2 | 3.3             | 3.4 | 3.5 | 3.6     | Remediation | Defence | Section 4 | Q4 passages |
| ------ | -------------- | ------ | --- | --- | ------- | --- | --------------- | --- | --- | ------- | ----------- | ------- | --------- | ----------- |
| 1      | correct        | miss T | ok  | ok  | No      | Yes | Yes             | No  | No  | No      | ok          | ok      | ok        | two         |
| 2      | correct        | ok     | ok  | ok  | No      | Yes | Partial, miss T | No  | No  | No      | ok          | ok      | ok        | two         |
| 3      | correct        | ok     | ok  | ok  | Partial | Yes | Yes             | No  | No  | Partial | ok          | ok      | ok        | two         |
| 4      | correct        | miss T | ok  | ok  | Partial | Yes | Yes             | No  | No  | No      | ok          | ok      | ok        | two         |
| 5      | correct        | ok     | ok  | ok  | Partial | Yes | Yes             | No  | No  | No      | ok          | ok      | ok        | three       |

`T` marks a miss whose reasoning quotes the document. Every grade under 3.1, 3.2 and 3.4 to 3.6
is one the key accepts: each 3.1 grade of Partial or No notes that no independent search
technique is recorded, and reader 3's 3.6 Partial quotes the versioning sentence.

### Question 1

Five of five correct. Every sheet has at least four bullets naming obligations the key lists, and
none asserts that the fix comes first, that a test may serve as the detector or that an agent may
baseline.

### Question 2

- **2a**, three of five. Reader 1 gives "build the rule and prove it, then sweep and fix every
  instance" with no attribution to a class, relying on section 2's "building the [Defence] is not
  optional and MUST be attempted before the [Defect] is fixed" and Appendix A's "Only then fix
  the original [Defect]". Reader 4 gives "works out the class and attempts the defence before
  fixing the defect", with no proof and no sweep, relying on the same section 2 sentence and on
  clause 3.1's opening sentence. Both quote the document, so both are findings; neither quoted
  sentence, nor clause 3.4, was changed by this pull request. Readers 2, 3 and 5 state the four
  steps in order.
- **2b**, five of five. All five name the owner and quote section 4's "An [Agent] MUST NOT
  [Baseline], suppress or knowingly leave an [Instance] unfixed on its own authority"; none lets
  the practitioner decide.
- **2c**, five of five. All five quote the changed section 7 sentence, "A [Remediation]
  [Conforms] if all six clauses of section 3 were followed for that [Defect], and the verdict that
  they were rests on reproduction", and state reproduction; none accepts the report as the
  verdict.

### Question 3

- **3.3**, four of five. Reader 2 grades Partial because the inline ignore on `Report::render()`
  "is an exclusion of code that carries the hazard" under Part B, and also fails 3.4 on it. The
  key excuses a reader who attributes the suppression to 3.3 "rather than" 3.4; reader 2
  attributes it to both, which that sentence does not cover (judgement J3). Its reasoning states
  what Part B requires, so the miss is traceable, and it is a finding whatever the count.
- **Remediation**: five of five say it does not conform.
- **Defence**: five of five say it does not conform, each naming 3.6.
- **Section 4**: five of five name the inline ignore; readers 1, 2 and 3 also name the unbuilt
  wider rule as a second or arguable decision, which the key accepts alongside it.

### Judgements made in marking

`ACCEPTANCE.md` at the base gives the key and the thresholds and leaves these open.

- **J1. Which elements of the key's answer to question 2 a sentence must state.** Every element
  that answers a part of the question must be stated; an element the key adds as a gloss is
  met unless the answer asserts its opposite. So 2a's steps must all appear, since the question
  asks what is done and in what order, and readers 1 and 4 miss; 2b's "always a human" is carried
  by "the owner", the defined term, since the question asks who and the key's wrong answers are
  ones that let the practitioner decide. On the stricter reading, that "the owner" does not
  state "always a human", reader 1 would also miss 2b; the verdict does not turn on it.
- **J2. 2c and "reproduction".** An answer that says the verdict rests on reproduction is
  marked correct, as runs 17 and 18 marked it under the same key; the key's wrong answers are one
  that accepts the report and one that says nothing of reproduction.
- **J3. The 3.3 excuse is read as written**, for a reader who attributes the suppression to 3.3
  rather than 3.4, not for one who attributes it to both. Read the other way, reader 2's 3.3 is
  correct and the third criterion loses one finding; the run fails on 2a and on question 4
  either way.
- **J4. The same passage under question 4** is the same sentence, as run 16 counted it: two
  readers quoting different sentences of one paragraph are two single-reader notes. Read by
  paragraph instead, no further passage reaches two readers in this run.

## Passages quoted as confusing

| Passage                                                                                                                                                   | Clause           | Readers        | Changed by this pull request               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------- | ------------------------------------------ |
| "Both bounds measure breadth within one level; the level itself is a separate question, answered against the report."                                     | 3.1              | three: 2, 4, 5 | No                                         |
| "A [Rule] drawn to the exact value or name found in the [Defect] is the same [Narrowing] however it is spelt"                                             | 3.1, lower bound | two: 3, 5      | No                                         |
| "naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search"                               | 2                | one: 1         | No                                         |
| The section 3 table, clause 3.1 row, fourth column, "Whether the next wider [Rule] is built"                                                              | 3                | one: 1         | No                                         |
| "A [Practitioner] who finds that an existing [Rule]'s printed [Identifier] does not resolve records it where clause 3.2's gaps are recorded, ..."         | 3.6              | one: 2         | No; the next sentence of its paragraph was |
| "This does not reopen a [Class] whose bounds a [Hazard] sentence has settled, and it reaches no further than the one wider [Rule] already on the record." | 4                | one: 3         | No                                         |
| The paragraph defining a conforming defence, "A [Defence] [Conforms] if it satisfies clauses 3.1, 3.2, 3.3, 3.5 and 3.6: ..."                             | 7                | one: 4         | No                                         |
| "...the scale at which that becomes true is tremendous."                                                                                                  | 3.4              | one: 5         | No                                         |

Reader 2 also quotes, with the level sentence, the one after it, "the [Class] a [Detector] can
read usually sits one level below that [Hazard]", in the same paragraph. Readers 3 and 5 both read
the lower-bound sentence as using [Narrowing] for drawing a rule too narrowly, which is not what
its definition in section 1 says. No reader quoted the new Remediation entry, a sentence where
Remediation became the defined term, or the Rule harness link in clauses 3.2 and 3.3.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: not met. 2a three of five; 2b and 2c five
  of five.
- Restatement and application, at least four of five on each keyed item: met. 3.3 four of five,
  every other item five of five.
- A wrong answer traceable to the text, none: not met. 2a for readers 1 and 4, and 3.3 for reader
  2, each a finding.
- A passage found confusing by two or more, none outstanding: not met. Clause 3.1's level
  sentence (three readers) and clause 3.1's lower-bound Narrowing sentence (two readers).
- From one reader only, recorded: the six other passages above.

**FAIL.** No failure traces to text this pull request changed: the 2a misses rest on section 2,
clause 3.1 and Appendix A, the 3.3 miss on clause 3.3 Part B, and both blocking passages on
clause 3.1, none of which the change touched. The changed sentence in section 7 was quoted by all
five readers for 2c and answered correctly by all five.
