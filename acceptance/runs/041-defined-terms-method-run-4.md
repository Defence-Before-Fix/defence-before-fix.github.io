# Run 41: SPEC.md, defined terms, fourth run

- **Document**: SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at ff77998, the commit the
  readers were given. The change is be546ea and 35f42bf (Remediation defined, Harness renamed
  Rule harness). Revision 1, after [run 31](031-defined-terms-method-run-1.md), is df016ab;
  revision 2, after [run 35](035-defined-terms-method-run-2.md), is 0fd02ef. The revision after
  [run 38](038-defined-terms-method-run-3.md) is 8dc5879:

  - section 2 names "two independent attempts at writing the [Rule]" where it named "techniques
    tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search", and says
    when two attempts are independent;
  - clause 3.1's lower bound says what the rejection of the next wider [Rule] needs, and that
    without it leaving that [Rule] unbuilt is the [Owner]'s decision;
  - section 4's bullet on the next wider [Rule] is restated as one test, the [Hazard] sentence;
  - clause 3.1's level sentence, section 2's "the first from the second" and clause 3.6's "no
    [Rule] build of their own" are reworded.

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 31, 35 or 38, model alias `haiku`; every reader
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
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/method/KEY.md` at
  ff77998, with the judgements of run 31

- **Verdict**: FAIL on a miss traceable to the text under 3.3, in clause 3.3 Part B's opening
  paragraph, and on two passages found confusing by two readers each, both untouched base text:
  the default [Owner] sentence in section 1 and clause 3.4's "tremendous". Every other keyed item
  is five of five.

## Marks

| Reader | Q1 restatement | 2a  | 2b  | 2c  | 3.1 | 3.2 | 3.3             | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 | Q4 passages |
| ------ | -------------- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ----------- | ------- | --------- | ----------- |
| 1      | correct        | ok  | ok  | ok  | No  | Yes | Yes             | No  | No  | No  | ok          | ok      | ok        | three       |
| 2      | correct        | ok  | ok  | ok  | No  | Yes | Yes             | No  | No  | No  | ok          | ok      | ok        | three       |
| 3      | correct        | ok  | ok  | ok  | No  | Yes | Yes             | No  | No  | No  | ok          | ok      | ok        | one         |
| 4      | correct        | ok  | ok  | ok  | No  | Yes | Yes             | No  | No  | No  | ok          | ok      | ok        | two         |
| 5      | correct        | ok  | ok  | ok  | No  | Yes | Partial, miss T | No  | No  | No  | ok          | ok      | ok        | one         |

`T` marks a miss whose reasoning quotes or states what the document requires. Every 3.1 grade of
No notes that no independent search technique is recorded.

### Question 1

Five of five correct, each with at least four bullets the key lists and none it marks wrong.
All five add fixing the original defect with a reproduction test, which section 6 states. Reader 4 says a no-pattern conclusion names "two independent attempts", the wording
revision 3 put in section 2.

### Question 2

- **2a**, five of five, each quoting section 2's "In order, the steps are section 3's: ..." and
  stating the four steps in order.
- **2b**, five of five, each naming the owner and quoting section 4's sentence on what an [Agent]
  MUST NOT do. All five also say the owner is a human, and readers 1, 2 and 4 quote "Always a
  human."
- **2c**, five of five, each quoting section 7's conforming-[Remediation] sentence with
  reproduction.

### Question 3

- **3.3**, four of five. Reader 3 grades "Yes, with a caveat" on whether the enforced run excludes
  the [Fixture], and is marked Yes. Reader 5 grades Partial: the inline ignore on
  `Report::render()` "is a suppression at the call site, not a narrowing with a recorded
  sentence, so the proof is undermined by a later commit", and fails 3.4 on the same ignore. Its
  section 4 answer adds "section 3.3 states that an exclusion without a hazard-absence sentence
  'is Suppression.'" The key's excuse covers a reader who attributes the suppression to 3.3
  rather than 3.4, not to both (run 31's judgement J3, kept). The reasoning states what Part B's
  opening paragraph says, "a [Suppression] at the call site", so the miss is traceable and a
  finding whatever the count, as runs 31 and 35 marked the same case. It traces to that
  paragraph, which says Part B "does not judge" such an ignore and that it "leaves the [Rule] and
  its proof as they were"; reader 5 took the classification and not the second half. Revision 1
  wrote the paragraph and revision 2 moved it to the Part's opening; revision 3 did not touch it.
- **3.4**, **3.5** and **3.6**, five of five No. Each 3.4 names the inline ignore, and each 3.6
  names the wiki documentation, not versioned with the rule.
- **Remediation**: five of five say it does not conform. **Defence**: five of five say it does
  not conform, each naming 3.6. **Section 4**: five of five name the inline ignore on
  `Report::render()`, and all five also name leaving the wider rule unbuilt, which the key
  accepts. Each rests that on section 4's new bullet, quoting or restating "that most of what it
  would match is legitimate".

### Judgements made in marking

Run 31's judgements J1 to J4 are applied unchanged. J3 decides reader 5's 3.3, above. Under J4
(the same passage is the same sentence), reader 2's two sentences of the [Owner] entry, "Where the
project has recorded nobody, ..." and "One limit applies to that default.", are a single-reader
note, separate from the sentence readers 1 and 3 quote. Read by paragraph, the [Owner] entry's
default paragraph is one passage named by three readers; it blocks either way.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                                                        | Clause            | Readers   | Text                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------- | ---------------------------------------------------------------------- |
| "so a decision they take under section 4 to keep an [Instance] unfixed, [Suppress], [Baseline] or remove a [Rule] MUST be recorded in the project record with its justification", set against section 4's "An [Agent] MUST NOT [Baseline] ..." | 1, Owner          | two: 1, 3 | Untouched base                                                         |
| "A [Baseline] of the existing [Instances] ... MAY be adopted where fixing every [Instance] is genuinely unfeasible, and the scale at which that becomes true is tremendous."                                                                   | 3.4               | two: 1, 5 | Untouched base                                                         |
| "Where the project has recorded nobody, the [Owner] is whoever instructed the [Practitioner], and [Escalation] goes there. One limit applies to that default."                                                                                 | 1, Owner          | one: 2    | Untouched base                                                         |
| "Two attempts are independent when they would miss different things, as two search techniques are under clause 3.1."                                                                                                                           | 2                 | one: 2    | Added by revision 3                                                    |
| "For a [Bundled defence], the project whose entry point demonstrates it is any project the [Toolchain] is genuinely installed into, the [Consuming project] included"                                                                          | 3.5               | one: 2    | Untouched base                                                         |
| "'the [Rule] found nothing the reading had missed' is one technique and a [Rule] run, not two techniques, and the stopping criterion cannot be applied to it."                                                                                 | 3.1               | one: 1    | Untouched base                                                         |
| "Where the only thing pending is whether one matched case carries the [Hazard], the [Rule] MAY merge at full width ...", set against "provided the [Rule] does not become [Blocking] until every [Instance] is fixed"                          | 4, two paragraphs | one: 4    | Untouched base; the change linked [Remediation] in the second sentence |

Notes on the two blocking passages:

- **Section 1, the default [Owner]'s recorded decision.** Readers 1 and 3 set the sentence
  against section 4's "An [Agent] MUST NOT [Baseline], suppress or knowingly leave an [Instance]
  unfixed on its own authority", and could not tell whether a default [Owner] may take those
  decisions or only must record that they did. One reader quoted the [Owner] default in run 38,
  a different sentence of it.
- **Clause 3.4, "tremendous".** Reader 1 could not tell what "that" refers to or what scale is
  meant. Reader 5 read the first half as a permission that section 4 then places with the
  [Owner], and "tremendous" as ambiguous. One reader quoted the same sentence in run 31.

Run 38's failures are clear in this run:

- no reader quotes section 2's "techniques tried at expressing the [Rule]", which revision 3
  replaced; one reader quotes the new independence sentence after it;
- no reader quotes clause 3.1's lower bound, which revision 3 rewrote;
- no reader quotes section 4's bullet on the next wider [Rule], which revision 3 restated, and
  all five apply it to the fixture.

No reader quotes the reworded 3.1 level sentence, section 2's "the first way out from the
second", clause 3.6's reworded sentence, the Remediation entry or any other sentence the original
change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met. 3.3 four of five,
  every other item five of five.
- A wrong answer traceable to the text, none: not met. Reader 5's 3.3, which traces to clause 3.3
  Part B's opening paragraph, text revision 1 wrote.
- A passage found confusing by two or more, none outstanding: not met. The [Owner] entry's
  default-[Owner] recording sentence (two readers) and clause 3.4's "tremendous" sentence (two
  readers), both untouched base text.
- From one reader only, recorded: the five other passages above.

**FAIL.** The 3.3 miss traces to a paragraph revision 1 wrote. Both blocking passages are
untouched base text. None is in text the change or revision 3 made.
