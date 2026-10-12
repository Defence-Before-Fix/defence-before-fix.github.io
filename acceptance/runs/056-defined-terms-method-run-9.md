# Run 56: SPEC.md, defined terms, ninth run

- **Document**: SPEC.md

- **Pull request**: [24](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24), opened later from branch `editor/defined-terms`. The
  readers were given commit 98b3b0c. The change, read against its merge base with `next`,
  9e914fe, adds the Remediation terminology entry and its link definition; links "remediation"
  as [Remediation] in clauses 3.1, 3.3, 3.6, sections 4, 5, 6 and 7 and the 1.1.0 changelog row;
  replaces "a proving harness" in clause 3.2 and "purpose-built [Rule]-testing harnesses" in
  clause 3.3 with [Rule harness], with a link definition to the detector specification; replaces
  "the entire remediation loop" in section 8 with "the entire correction loop"; and, since run 53,
  names in clause 3.2 and clause 3.5 the substitutes a mechanism gap allows (clause 3.3's
  acceptance or smoke check, and clause 3.6's [Identifier] that can be followed without a
  resolver). The question set, key and fixture are as at 98b3b0c; the key differs from c31d49a
  only in its 2c quotations following the text.

- **Cohort**: five readers, none reused from any earlier run; model `claude-haiku-5-5`, the
  cohort's model named for the run before its readers started. Every reader reported
  `claude-haiku-5-5` in its JSON output.

- **Isolation**, as the editor supplied it and attests: each reader a separate `claude -p`
  process, started through the `ccy-claude` wrapper (which only reattaches the session's
  credential), in a fresh empty directory made by `mktemp -d` outside any repository, with the
  packet on standard input; no tools, no settings, no project context, no saved session, and no
  managed settings on the machine. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked two things:

  - the prompt (sha256 `c614c1b1bca84abd98ddd52379860f4b269289d731354f2790502e97c9d34168`) is
    byte for byte `acceptance/method/QUESTIONS.md`, `SPEC.md` and
    `acceptance/fixtures/remediation-ledger.md` at 98b3b0c, in that order, each preceded by one
    `===== FILE: <name> =====` line, with one blank line between files, rebuilt from the commit
    and hashed;
  - each reader's JSON output has `is_error` false and subtype `success`, and each sheet is its
    `result`.

- **Readers set aside**: none. Every answer text is non-empty, no process reported an error, and
  every reader reported the cohort's model.

- **Run within the pull request**: 9. Runs 31, 35, 38, 41, 44, 47 and 50 came before under the
  earlier rules, and run 53 under these.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's marking instruction and its agent definition, having seen neither the drafting nor
  the review. It marked against `ACCEPTANCE.md` and `acceptance/method/KEY.md` at 98b3b0c; the
  process files there are identical to those at c31d49a. No earlier run record was read for its
  judgements; run 53 was read for the shape of a record only.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 3.1     | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 |
| ------ | ------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | ----------- | ------- | --------- |
| 1      | correct | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 2      | correct | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 3      | correct | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 4      | correct | ok¹ | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 5      | correct | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |

¹ Marked for the reader under the open-point rule; see "Points the rules did not settle".

Every keyed item is five of five. There is no miss, so none whose reasoning quotes the document
and none matching a wrong reading the key names.

### Question 1

Each reader has at least four bullets naming obligations the key lists and none the key marks
wrong. Reader 1: 3.1 (two bullets, counted once), 3.2 with 3.6, 3.3 with 3.4, 3.5 with 3.6,
section 4. Reader 2: 3.1 (two bullets, counted once), 3.2 with 3.3, 3.4, 3.5 with 3.6, section
4\. Reader 3: 3.1, 3.2 with 3.6, 3.3, 3.4, 3.5, section 2's deferred record with section 4. Reader
4: 3.1 (three bullets, counted once), 3.2 with 3.3, 3.4 with section 4, 3.5 with 3.6. Reader 5:
3.1 (two bullets, counted once), 3.2 with 3.3, 3.4 with section 4, 3.5 with 3.6; its sixth bullet
is on neither list and is not counted. No reader has the fix first, a test as the detector, or
an agent baselining.

### Question 2

- **2a**, five of five. Readers 1, 2, 3 and 5 state the class, the rule, its proof and the sweep
  in that order with the fix after, each quoting section 2's "MUST be attempted before the
  [Defect] is fixed"; readers 1, 2 and 3 also quote clause 3.4's MUST sentence. Reader 4 says the
  practitioner "does the six clauses of section 3 in order, then fixes the defect", quoting
  section 3's "Six clauses, in order.", clause 3.3's "The [Defence] is committed with the
  originating [Instance] still present, and the fix is committed after it" and Appendix A's
  closing sentence; it names no step singly and does not mention the sweep. Marked for the reader
  as an open point.
- **2b**, five of five. Each names the owner, says an agent may not, and quotes section 4's "An
  [Agent] MUST NOT [Baseline], suppress or knowingly leave an [Instance] unfixed on its own
  authority".
- **2c**, five of five. Each states that all six clauses were followed and that the verdict rests
  on reproduction. Readers 1, 3, 4 and 5 quote section 7's conforming-[Remediation] sentence and
  its "A verdict on a [Remediation] or a [Defence] MUST rest on reproduction" sentence; reader 2
  quotes the second sentence from "rests on reproduction, not on the report: the reviewer reruns
  the [Defence] red", which quotes the document by its longest verbatim run.

### Question 3

- **3.1**: two No (readers 1, 4), three Partial; the key accepts any grade.
- **3.2**: five Yes.
- **3.3**: five Yes. Readers 1, 3 and 5 say the inline ignore is a suppression graded under 3.4 or
  3.5, not here.
- **3.4**: five No, each naming `Report::render()` left unfixed behind the inline ignore.
- **3.5**: five No, each on the inline ignore no recorded decision covers.
- **3.6**: five No, each naming the wiki or the documentation not versioned with the rule.
- **Remediation**: five say it does not conform, each naming 3.4, 3.5 and 3.6 among the clauses
  not followed.
- **Defence**: five say it does not conform, each naming 3.5's uncovered suppression and 3.6.
- **Section 4**: five name the inline ignore on `Report::render()`. Readers 2, 3 and 5 also name
  leaving the wider rule unbuilt, and reader 1 calls it arguable; neither is marked.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                      | Clause      | Readers          | Text                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| The lower-bound list item: "A [Rule] drawn to the exact value or name found in the [Defect] is the same [Narrowing] however it is spelt" (readers 1, 2, 3, 4), and "unless the independent search below has found no other [Instance] ..." (reader 3)        | 3.1         | four: 1, 2, 3, 4 | Untouched; reader 2 sets it against the [Narrowing] terminology entry, untouched                                                  |
| The paragraph opening "**Both bounds measure breadth within one level; the level itself is a separate question, answered against the report.**"                                                                                                              | 3.1         | two: 4, 5        | Altered by the change: "either one added with this remediation" became "this [Remediation]", with its link, in the same paragraph |
| Section 2, "Attempt rather than pre-judge": "naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search"                                                                                      | 2           | two: 2, 5        | Untouched                                                                                                                         |
| The [Owner] entry: "Where the project has recorded nobody, the [Owner] is whoever instructed the [Practitioner]" with "Always a human" (reader 3); "The default [Owner] is usually the person under the same deadline as the [Practitioner], ..." (reader 5) | 1 (Owner)   | two: 3, 5        | Untouched; reader 3 sets it against section 4's "dividing line" paragraph, untouched                                              |
| "Fix them all.": "and the scale at which that becomes true is tremendous"                                                                                                                                                                                    | 3.4         | one: 1           | Untouched                                                                                                                         |
| "A [Narrowing] reduces the [Practitioner]'s own work": "and a [Narrowing] that excludes more code than the [Rule] still covers MUST be reported to the [Owner] as if it were a [Suppression]"                                                                | 3.3, Part B | one: 1           | Untouched                                                                                                                         |
| "A [Remediation] [Conforms] if all six clauses ...": "and the verdict that they were rests on reproduction, as this section closes by requiring, not on the report"                                                                                          | 7           | one: 1           | Altered by the change: "remediation" became "[Remediation]"                                                                       |
| Section 4's list item "Leaving unbuilt the next wider [Rule] ... where it was rejected because no [Instance] of it exists today rather than because the [Hazard] cannot arise there"                                                                         | 4           | one: 2           | Untouched; set against the section 3 table row below                                                                              |
| The section 3 table's 3.1 row: "Whether the next wider [Rule] is built"                                                                                                                                                                                      | 3 (table)   | one: 2           | Untouched                                                                                                                         |
| "What to do whilst waiting": "the [Rule] MAY merge at full width with that case recorded as a known [Instance] awaiting the [Owner]"                                                                                                                         | 4           | one: 3           | Untouched; set against the paragraph below                                                                                        |
| "A [Remediation] MAY be delivered across several changes": "provided the [Rule] does not become [Blocking] until every [Instance] is fixed"                                                                                                                  | 4           | one: 3           | Altered by the change: "A remediation" became "A [Remediation]"                                                                   |
| "The dividing line": "An [Agent] MUST NOT [Baseline], suppress or knowingly leave an [Instance] unfixed on its own authority"                                                                                                                                | 4           | one: 3           | Untouched                                                                                                                         |
| "There are two kinds of gap": "uses the substitutes clauses 3.3 and 3.6 already allow (clause 3.3's acceptance or smoke check where a [Fixture]-based test is impractical, and clause 3.6's [Identifier] in a form that can be followed without a resolver)" | 3.2         | one: 4           | Altered by the change: the parenthesis is the sentence this run's change added, and "a proving harness" became "a [Rule harness]" |
| "**Then the proof, which runs the other way round, and both ways.**"                                                                                                                                                                                         | 3.3, Part B | one: 5           | Untouched                                                                                                                         |

Notes, not passages: none.

## Findings and where they lie

1. **Clause 3.1, the lower-bound list item**, readers 1, 2, 3 and 4. A list item is a paragraph of
   its own; the change altered the paragraph before the list ("the scope of the [Remediation]"),
   not this item, and no reader naming it sets it against a paragraph the change altered (reader
   2 sets it against the [Narrowing] entry, untouched). Routed to `acceptance/ROUTED.md`; does
   not block.
2. **Clause 3.1, the paragraph opening "Both bounds measure breadth within one level"**, readers
   4 and 5. Both quote its bold opening sentence. That sentence has no blank line after it, so it
   is part of the paragraph that continues "Where the [Defect] was reported as a behaviour", in
   which the change replaced "this remediation" with "this [Remediation]" and its link. A
   paragraph in which the pull request changes a word, a term or a link is text the change
   altered. **Blocks.**
3. **Section 2, "Attempt rather than pre-judge"**, readers 2 and 5. Untouched by the change, and
   neither reader sets it against a paragraph the change altered. Routed to
   `acceptance/ROUTED.md`; does not block.
4. **Section 1, the [Owner] entry**, readers 3 and 5. Untouched; reader 3 sets it against section
   4's "dividing line" paragraph, also untouched. Routed to `acceptance/ROUTED.md`; does not
   block.

Every other passage above is from one reader only: recorded, applied at the editor's discretion.
Three of them lie in text the change altered: section 7's conforming-[Remediation] sentence
(reader 1), section 4's several-changes paragraph (reader 3), and clause 3.2's sentence naming
the substitutes (reader 4), which is the sentence this run's change added.

## Points the rules did not settle

- **Question 2a, reader 4.** The key says an answer naming the steps by their clause numbers in
  order states both elements. Reader 4 says "the six clauses of section 3 in order, then fixes
  the defect" and quotes "Six clauses, in order.", naming the clauses collectively rather than
  each step or each number, and nowhere mentions the sweep. Whether a collective reference to
  section 3's clauses states element (1) is not settled by `ACCEPTANCE.md` or the key. Marked for
  the reader, as the open-point rule says; the key is to settle it before the next run.
- **Question 1, bullets on neither list.** Readers 2, 3, 4 and 5 include fixing the original
  defect last with a test that reproduces it (section 6 and Appendix A), reader 5 as a whole
  bullet, and reader 1 includes "Conformance is shown by reproduction, not by report" (section
  7). The key's list neither names nor marks these wrong. As the rule says, they are not counted
  either way; recorded as an open point for the key. No mark turns on it.
- **Where finding 2 lies.** The rule settles it: the bold sentence is not a heading but the
  opening of a paragraph the change altered. Were the bold sentence taken as a heading of its
  own, the open-point rule on where a finding lies would treat it as the change's text, so the
  direction is the same.

## Process change

Made under the process change of pull request 22 before it merged, at commit c31d49a, named
before the readers started. The process files at 98b3b0c are identical to those at c31d49a; the
key differs only in its 2c quotations following the text.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: met, five of five, with reader 4's
  2a marked for the reader on an open point.
- Restatement and application, all but one reader correct on each keyed item: met, five of five.
- A miss the key says counts against the document: none.
- A passage found confusing by two or more readers, in text the change wrote or altered: one,
  clause 3.1's "Both bounds measure breadth within one level" paragraph. Not met.
- A passage found confusing by two or more readers, elsewhere: three, clause 3.1's lower-bound
  item, section 2's "Attempt rather than pre-judge" and the [Owner] entry, routed to
  `acceptance/ROUTED.md`.
- From one reader only: ten passages, recorded.

**Verdict: FAIL**, on finding 2 alone.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125399432); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125398949); the prompt, [part 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125399926) and [part 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125400428).
