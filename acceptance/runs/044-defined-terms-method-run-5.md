# Run 44: SPEC.md, defined terms, fifth run

- **Document**: SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at c1c461c, the commit the
  readers were given. The change is be546ea and 35f42bf (Remediation defined, Harness renamed
  Rule harness). Revision 1, after [run 31](031-defined-terms-method-run-1.md), is df016ab;
  revision 2, after [run 35](035-defined-terms-method-run-2.md), is 0fd02ef; revision 3, after
  [run 38](038-defined-terms-method-run-3.md), is 8dc5879. The revision after
  [run 41](041-defined-terms-method-run-4.md) is 688ae1b:

  - clause 3.3's opening paragraph says that an ignore comment or ignore entry placed on one
    [Instance] counts against none of the three Parts, and Part B no longer classifies it as a
    [Suppression];
  - the [Owner] entry's default paragraph says the default [Owner] takes the decisions section 4
    gives the [Owner], and "One limit applies to that default." is cut;
  - clause 3.4's [Baseline] MAY reads "MAY be adopted by the [Owner] ... and only a very large
    change is unfeasible", in place of "the scale at which that becomes true is tremendous".

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 31, 35, 38 or 41, model alias `haiku`; every
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
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/method/KEY.md` at
  c1c461c, with the judgements of run 31

- **Verdict**: FAIL on a miss traceable to the text under 3.3, in clause 3.3 Part C's sentence on
  [Fixtures], and on one passage found confusing by two readers, clause 3.3 Part B's sentence on a
  [Narrowing] that excludes more code than the [Rule] still covers. Both are untouched base text.
  Every other keyed item is five of five.

## Marks

| Reader | Q1 restatement | 2a  | 2b  | 2c  | 3.1     | 3.2 | 3.3             | 3.4 | 3.5 | 3.6     | Remediation | Defence | Section 4 | Q4 passages |
| ------ | -------------- | --- | --- | --- | ------- | --- | --------------- | --- | --- | ------- | ----------- | ------- | --------- | ----------- |
| 1      | correct        | ok  | ok  | ok  | No      | Yes | Yes             | No  | No  | No      | ok          | ok      | ok        | one         |
| 2      | correct        | ok  | ok  | ok  | No      | Yes | Yes             | No  | No  | Partial | ok          | ok      | ok        | two         |
| 3      | correct        | ok  | ok  | ok  | No      | Yes | Partial, miss T | No  | No  | No      | ok          | ok      | ok        | one         |
| 4      | correct        | ok  | ok  | ok  | Partial | Yes | Yes             | No  | No  | No      | ok          | ok      | ok        | one         |
| 5      | correct        | ok  | ok  | ok  | No      | Yes | Yes             | No  | No  | No      | ok          | ok      | ok        | two         |

`T` marks a miss whose reasoning quotes or states what the document requires. Every 3.1 grade of
Partial or No notes that no independent search technique is recorded.

### Question 1

Five of five correct, each with at least four bullets the key lists and none it marks wrong.
Readers 1, 2, 3 and 5 add fixing the original defect with a reproduction test, which section 6
states. Readers 1, 2, 3 and 4 put suppression, baselines and unfixed [Instances] with the owner,
which section 4 states.

### Question 2

- **2a**, five of five, each quoting section 2's "In order, the steps are section 3's: ..." and
  stating the four steps in order.
- **2b**, five of five, each naming the owner as a human and quoting section 4's sentence on what
  an [Agent] MUST NOT do.
- **2c**, five of five. Readers 3, 4 and 5 quote section 7's conforming-[Remediation] sentence
  with reproduction. Readers 1 and 2 quote the [Conform] entry, "To satisfy every MUST of the
  relevant section 7 level ...", and section 7's "A verdict on a [Remediation] or a [Defence]
  MUST rest on reproduction, not on the report", and state both; they are marked correct under J1
  and J2 (below).

### Question 3

- **3.3**, four of five. Readers 1, 2, 4 and 5 grade Yes, and each says the inline ignore does not
  count against the clause; reader 2 adds that "clause 3.3 sends it to 3.4 and section 4".
  Reader 3 grades Partial: "the enforced run reports the fixture among its five findings, which
  3.3 Part C says it should not, and the description does not show the fixture excluded before
  the green run at C." The fixture has the CI run for commit B red with five findings, the
  [Fixture] among them, and the key grades 3.3 Yes on that red run. The reasoning states what
  Part C's sentence says, "the [Sweep] excludes it under clause 3.4, and the enforced run does not
  report it", and reads it as a requirement the red run breaks, so the miss is traceable and a
  finding whatever the count. Run 34 marked the same reading of the same sentence as traceable to
  Part C. The sentence is untouched base text. The key's excuse for 3.3 does not apply: it covers
  attributing the suppression to 3.3, which reader 3 does not do.
- **3.4** and **3.5**, five of five No; each 3.4 names the inline ignore.
- **3.6**, five of five. Readers 1, 3, 4 and 5 grade No, naming the wiki documentation, not
  versioned with the rule. Reader 2 grades Partial: the documentation "lives on a company wiki
  rather than being shipped and versioned with the rule, and the spec says a third-party or
  general link does not conform". It is marked as the key's accepted Partial under J7 (below).
- **Remediation**: five of five say it does not conform. **Defence**: five of five say it does
  not conform, each naming 3.6. **Section 4**: five of five name the inline ignore on
  `Report::render()`, and all five also name leaving the wider rule unbuilt, which the key
  accepts.

### Judgements made in marking

Run 31's judgements J1 to J4 are applied unchanged.

- **J1 and J2, 2c for readers 1 and 2.** Each states that the verdict rests on reproduction and
  not on the report, which J2 marks correct. Neither says "all six clauses of section 3" in so
  many words; each says every MUST of the relevant section 7 level, which for a [Remediation] is
  those six clauses and asserts nothing contrary, so under J1 it is met. Read strictly, 2c would
  be three of five and fail the first criterion too; the verdict is FAIL either way.
- **J4.** Readers 3 and 5 quote the same sentence of clause 3.3 Part B. Reader 1's section 2 and
  section 3 sentences and reader 5's section 5 and section 7 sentences are each one entry read as
  a pair, and no other reader quotes any of those four sentences.
- **J7. Reader 2's 3.6 Partial.** The key accepts Partial "where the reasoning quotes the
  versioning sentence". Reader 2 states that sentence's requirement in its words, "versioned with
  the rule", and the URL sentence after it, without quotation marks. The requirement is the
  content of the sentence, so it is read as quoted, in the way run 33's J2 reads a reasoning that
  states a clause in the clause's words. Read narrowly, as quotation marks only, 3.6 would be four
  of five and still meet its threshold, and the grade would not be traceable, since Partial does
  not read the clause differently.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                               | Clause            | Readers   | Text                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------- | ---------------------------------------------------------------------- |
| "a [Narrowing] that excludes more code than the [Rule] still covers MUST be reported to the [Owner] as if it were a [Suppression]"                                                                                    | 3.3, Part B       | two: 3, 5 | Untouched base                                                         |
| "MUST record it where the project's other decisions are enumerable under clause 8.7", set against section 3's "record it with the [Remediation docs] for the [Defence] being built"                                   | 2, 3              | one: 1    | Untouched base                                                         |
| "Where the only thing pending is whether one matched case carries the [Hazard], the [Rule] MAY merge at full width ...", set against "provided the [Rule] does not become [Blocking] until every [Instance] is fixed" | 4, two paragraphs | one: 2    | Untouched base; the change linked [Remediation] in the second sentence |
| "Keeping the narrower [Rule] excludes what that wider [Rule] would add, so the rejection needs what a [Narrowing] needs under clause 3.3"                                                                             | 3.1               | one: 2    | Written by revision 3                                                  |
| "The [toolchain specification](TOOLING-SPEC.md) names a [Toolchain] that also satisfies it as [Conforming] with [Agent] support, which is the claim to make when it is true."                                         | 7                 | one: 4    | Untouched base                                                         |
| "a project whose checks run in another order is a project that does not [Conform]", set against section 7's "Nothing here constrains how the project runs its checks or what it does when they fail."                 | 5, 7              | one: 5    | Untouched base                                                         |

Note on the blocking passage:

- **Clause 3.3 Part B, the over-wide [Narrowing].** Reader 3 could not tell whether "more code
  than the [Rule] still covers" compares the excluded code with the code the [Rule] still covers
  or with something else. Reader 5 quotes the sentence without stating a doubt. Neither grade
  turns on it, since the fixture records no [Narrowing]. No reader in runs 31 to 41 quoted it;
  one reader of run 34, on another branch with the same base, did.

Run 41's failures are clear in this run:

- no reader fails 3.3 on the inline ignore, and four say in terms that it does not count against
  the clause; no reader quotes clause 3.3's opening paragraph, which revision 4 rewrote, or Part
  B's opening;
- no reader quotes the [Owner] entry's default paragraph, which revision 4 rewrote;
- no reader quotes clause 3.4's [Baseline] MAY, which revision 4 rewrote.

No reader quotes the Remediation entry, the [Remediation docs] links or any other sentence the
original change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met (2c under J1 and J2).
- Restatement and application, at least four of five on each keyed item: met. 3.3 four of five,
  every other item five of five.
- A wrong answer traceable to the text, none: not met. Reader 3's 3.3, which traces to clause 3.3
  Part C's sentence on [Fixtures], untouched base text.
- A passage found confusing by two or more, none outstanding: not met. Clause 3.3 Part B's
  sentence on a [Narrowing] that excludes more code than the [Rule] still covers (two readers),
  untouched base text.
- From one reader only, recorded: the five other passages above.

**FAIL.** The 3.3 miss and the blocking passage are both untouched base text. None is in text the
change or any of its revisions made.
