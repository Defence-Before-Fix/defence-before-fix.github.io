# Run 64: SPEC.md, defined terms, twelfth run

- **Document**: SPEC.md

- **Pull request**: [24](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24), opened later from branch `editor/defined-terms`. The
  readers were given commit 694033b. The change, read against its merge base with `next`,
  9e914fe, adds to section 1's opening a paragraph on terms defined in the companion
  specifications; adds the Remediation terminology entry and its link definition; links
  "remediation" as [Remediation] in clauses 3.1, 3.3, 3.6, sections 4, 5, 6 and 7 and the 1.1.0
  changelog row; replaces "a proving harness" in clause 3.2 and "purpose-built [Rule]-testing
  harnesses" in clause 3.3 with [Rule harness], with a link definition to the detector
  specification; replaces "the entire remediation loop" in section 8 with "the entire correction
  loop"; names in clause 3.2 and clause 3.5 the substitutes a mechanism gap allows; rewrites
  clause 3.1's paragraph on the two bounds; opens clause 3.5's "For a Bundled defence" paragraph
  with a sentence saying what a [Bundled defence] and a [Consuming project] are; and, since run
  61, adds to section 2's "MUST be attempted" paragraph a sentence giving section 3's order,
  rewrites clause 3.3 Part C's paragraph on [Fixtures] so that the red run of Part A may report a
  [Fixture] and the green run under clause 3.5 does not report it as an [Instance], and rewords
  section 7's conforming-[Remediation] sentence so that it ends "not on the report; the closing
  paragraph of this section says what reproduction requires".
  The question set and fixture are as at 4081aa4; the key differs from 4081aa4 only in its 2c
  quotations following the text ("A remediation" and "a remediation" became "A Remediation" and
  "a Remediation").

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

  - the prompt (sha256 `7c03aba3b877ac0406f6f75059dbc2e2f826a1cfef7076ef621369d4876cae20`) is
    byte for byte `acceptance/method/QUESTIONS.md`, `SPEC.md` and
    `acceptance/fixtures/remediation-ledger.md` at 694033b, in that order, each preceded by one
    `===== FILE: <name> =====` line, with one blank line between files, rebuilt from the commit
    and compared;
  - each reader's JSON output has `is_error` false and subtype `success`, reports
    `claude-haiku-5-5`, and each sheet is byte for byte its `result`.

- **Readers set aside**: none. Every answer text is non-empty, no process reported an error, and
  every reader reported the cohort's model.

- **Run within the pull request**: 12. Runs 31 to 52 came before under the earlier rules, and runs
  53 to 61 under these; runs 54 and 55 read the other two documents.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's marking instruction and its agent definition, having seen neither the drafting nor
  the review. It marked against `ACCEPTANCE.md` and `acceptance/method/KEY.md` at 694033b, by
  the Marking section and the key alone. No earlier run record was read for its judgements; run
  61 was read for the shape of a record only.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 3.1     | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 |
| ------ | ------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | ----------- | ------- | --------- |
| 1      | correct | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 2      | correct | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 3      | correct | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 4      | correct | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 5      | correct | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |

No misses. No answer matches a wrong reading the key names.

### Question 1

Each reader has at least four bullets naming obligations the key lists and none the key marks
wrong. Reader 1: 3.1 (two bullets, counted once), 3.2 with 3.3, 3.4 with section 4, 3.5 with
3.6, the deferred defect recorded (section 2) and the original defect fixed with a reproducing
test. Reader 2: 3.1, 3.2, 3.3, 3.4, 3.5 with 3.6, section 4 with the deferred defect. Reader 3:
the defence built before the fix, 3.1 (two bullets, counted once), 3.2 with 3.6, 3.3 with 3.4,
3.5 with section 4 and the reproducing test. Reader 4: 3.1 (two bullets, counted once), 3.2 with
3.3, 3.4, 3.5 with 3.6, section 4 with the deferred defect. Reader 5: 3.1 (two bullets, counted
once), 3.2 with 3.3, 3.4, 3.5 with 3.6, section 4 with the deferred defect and the reproducing
test. Reader 5's second bullet has the search "chosen and run before the rule exists", where
clause 3.1 says before the [Rule] is run against the codebase; it still names the clause 3.1
search, already counted, and asserts no obligation on neither list. No reader has the fix first,
a test as the detector, or an agent baselining.

### Question 2

- **2a**, five of five. Each states attributing the defect to a class, building the rule,
  proving it fires and running the sweep, with every instance fixed after, and each quotes
  section 2's "The order is section 3's: attribute the [Defect] to a [Class], build the [Rule],
  prove that it fires, run the [Sweep], then fix every [Instance]." Readers 4 and 5 also quote
  clause 3.4's opening sentence; readers 3 and 5 Appendix A's "Only then fix the original
  [Defect] in the normal way, with a test that reproduces it."
- **2b**, five of five. Each names the owner, always a human, and says an agent may not; each
  quotes section 4's "An [Agent] MUST NOT [Baseline], suppress or knowingly leave an [Instance]
  unfixed on its own authority, whatever the [Instance] count turns out to be."
- **2c**, five of five. Each states that all six clauses were followed and that the verdict rests
  on reproduction, not on the report, quoting section 7's conforming-[Remediation] sentence;
  readers 1, 2, 4 and 5 also quote or paraphrase its closing paragraph on what the reviewer
  reruns.

### Question 3

- **3.1**: three Partial (readers 1, 3, 5), two No (readers 2, 4); the key accepts any grade.
- **3.2**: five Yes.
- **3.3**: five Yes, accepted without condition.
- **3.4**: five No, each naming `Report::render()` left behind the inline ignore.
- **3.5**: five No, each on the inline ignore no recorded decision covers. No reader graded Yes.
- **3.6**: five No, each naming the wiki and the documentation not versioned with the rule.
- **Remediation**: five say it does not conform, each naming 3.4, 3.5 and 3.6.
- **Defence**: five say it does not conform. Readers 1, 2, 4 and 5 name 3.5's uncovered
  suppression and 3.6; reader 3 names 3.6's documentation not "versioned alongside it".
- **Section 4**: five name the inline ignore on `Report::render()`. Readers 2, 3, 4 and 5 also
  name, as a second candidate, leaving the wider rule unbuilt; not marked.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Clause     | Readers                           | Text                                                                                                                                                                                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The lower-bound list item: "That rejection is tested as a Narrowing is under clause 3.3: ..." (reader 1); "A [Rule] drawn to the exact value or name found in the [Defect] is the same [Narrowing] however it is spelt" (readers 2, 3, 5); "unless the independent search below has found no other [Instance] and the [Practitioner] records that the [Class] is genuinely singular today" (reader 4)                                                                       | 3.1        | five: 1, 2, 3, 4, 5               | Untouched. Readers 2 and 5 set it against the Narrowing entry, reader 4 against section 4's next-wider list item; both untouched                                                                        |
| The Owner entry: "The default Owner is usually the person under the same deadline ..." (reader 1); "Always a human." beside "the [Owner] is whoever instructed the [Practitioner]" (reader 3); the verb "Suppress" and whether the default-owner sentences cover the other decisions section 4 lists (reader 4); described as "section 1 defines [Owner] as the holder of authority over [Exceptions] and [Calibrations]" (reader 2, set against clause 3.4 and Appendix A) | 1          | four: 1, 3, 4, and 2 (open point) | Untouched. Reader 4 sets it against section 4's list of the Owner's decisions, reader 2 against clause 3.4's "Adopting one is a decision" paragraph and Appendix A's authority paragraph; all untouched |
| "Attempt rather than pre-judge": "naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search" (readers 3, 5)                                                                                                                                                                                                                                                                                                 | 2          | two: 3, 5                         | Untouched. Both set it against clause 3.1's search techniques; see the points below                                                                                                                     |
| Section 4's list item on leaving the next wider [Rule] unbuilt: "This does not reopen a [Class] whose bounds a [Hazard] sentence has settled, ..." (reader 3); "The absence of an [Instance] is the [Practitioner]'s reason not to widen unasked; ..." (reader 4, quoted against clause 3.1's lower bound)                                                                                                                                                                  | 4          | two: 3, 4                         | Untouched                                                                                                                                                                                               |
| Part B, the paragraph "A [Narrowing] reduces the [Practitioner]'s own work": "a [Narrowing] that excludes more code than the [Rule] still covers MUST be reported to the [Owner] as if it were a [Suppression]"                                                                                                                                                                                                                                                             | 3.3        | one: 2                            | Untouched                                                                                                                                                                                               |
| "whoever owns the codebase", in clause 3.4's "Adopting one is a decision" paragraph and Appendix A, set against the Owner entry                                                                                                                                                                                                                                                                                                                                             | 3.4, App A | one: 2                            | Untouched                                                                                                                                                                                               |
| The paragraph "Two techniques are independent": "'the [Rule] found nothing the reading had missed' is one technique and a [Rule] run, not two techniques, and the stopping criterion cannot be applied to it" (labelled by the reader as the stopping criterion)                                                                                                                                                                                                            | 3.1        | one: 3                            | Untouched                                                                                                                                                                                               |
| The two-bounds paragraph: "The two bounds settle how wide the [Class] is drawn, not at which level of abstraction", and that the text does not say where the level is decided                                                                                                                                                                                                                                                                                               | 3.1        | one: 4                            | Written by the change                                                                                                                                                                                   |
| The paragraph on an [Identifier] that does not resolve: "records it where clause 3.2's gaps are recorded ... with no [Rule] build of their own to attach it to", set against clause 3.2's paragraph on where a gap is recorded                                                                                                                                                                                                                                              | 3.6        | one: 4                            | Altered by the change: "the remediation" became "the [Remediation]"; clause 3.2's paragraph untouched                                                                                                   |
| "What to do whilst waiting": "the [Rule] MAY merge at full width with that case recorded as a known [Instance]"                                                                                                                                                                                                                                                                                                                                                             | 4          | one: 5                            | Untouched; set against the paragraph below                                                                                                                                                              |
| "A [Remediation] MAY be delivered across several changes": "the [Rule] does not become [Blocking] until every [Instance] is fixed"                                                                                                                                                                                                                                                                                                                                          | 4          | one: 5                            | Altered by the change: "A remediation" became "A [Remediation]"                                                                                                                                         |
| "A [Defence] [Conforms]": the list "3.1, 3.2, 3.3, 3.5 and 3.6" followed by a summary naming "fails rather than warns" but not 3.5's suppression condition                                                                                                                                                                                                                                                                                                                  | 7          | one: 5                            | Altered by the change: "a [Conforming] remediation" became "a [Conforming] [Remediation]"                                                                                                               |

Notes, not passages: none.

## Findings and where they lie

1. **Clause 3.1, the lower-bound list item**, all five readers. A list item is a paragraph of its
   own; the change did not touch it (the change altered the lead-in paragraph above it, "A
   [Defect] usually belongs to several overlapping [Classes]", which no reader names). The
   paragraphs readers set it against, the Narrowing entry (readers 2, 5) and section 4's
   next-wider list item (reader 4), are untouched; reader 1 sets it against no paragraph. Routed
   to `acceptance/ROUTED.md` (its existing row, raised again); does not block.
2. **Section 1, the Owner entry**, readers 1, 3 and 4, and reader 2 by the open-point rule.
   Untouched, and the paragraphs set against it (section 4's list of decisions, clause 3.4's
   "Adopting one is a decision" paragraph, Appendix A's authority paragraph) are untouched.
   Routed to `acceptance/ROUTED.md` (its existing row, raised again); does not block.
3. **Section 2, "Attempt rather than pre-judge"**, readers 3 and 5. Untouched; the change's
   sentence in section 2 is in the paragraph before it. Routed to `acceptance/ROUTED.md` (its
   existing row, raised again); does not block.
4. **Section 4, the list item on leaving the next wider [Rule] unbuilt**, readers 3 and 4.
   Untouched; reader 4 sets it against clause 3.1's lower-bound list item, untouched. Routed to
   `acceptance/ROUTED.md` (its existing row, raised again); does not block.

The run 61 finding, section 7's "A [Remediation] [Conforms]" paragraph, was named by no reader in
this run; nor were section 2's new sentence on the order, section 1's paragraph on companion
terms, clause 3.3's [Fixtures] paragraph or clause 3.5's "For a [Bundled defence]" paragraph. Of
the passages from one reader only, four lie in text the change wrote or altered: clause 3.1's
two-bounds paragraph and clause 3.6's unresolved-[Identifier] paragraph (reader 4), and section
4's several-changes paragraph and section 7's conforming-[Defence] paragraph (reader 5).

## Points the rules did not settle

- **Whether reader 2 names the Owner entry.** Reader 2 gives section 1 and a description, "defines
  [Owner] as the holder of authority over [Exceptions] and [Calibrations]", as what it sets
  clause 3.4 and Appendix A against. Marked by the open-point rule as naming the passage. The
  entry is a finding on readers 1, 3 and 4 alone, so the count and the verdict are the same
  either way.
- **Considered, and settled by the rules: where finding 3 lies.** Both readers set the paragraph
  against clause 3.1's search: reader 3 by its own quoted words, "the vocabulary clause 3.1 uses
  for a search", reader 5 as "the same two techniques that 3.1 requires for the search". Clause
  3.1 holds two paragraphs the change altered, the overlapping-[Classes] lead-in and the
  two-bounds paragraph, but neither speaks of search techniques; the text the readers identify is
  step 2 of the five steps, the saturation paragraph and the "Two techniques are independent"
  paragraph, all untouched. The descriptions identify that text, so the finding does not lie in
  the change's text by the rule on paragraphs set against altered ones.
- No other point. No question 1 bullet asserts an obligation on neither list.

## Process change

Made under the process change of pull request 22 before it merged, at commit 4081aa4, named
before the readers started. `ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md`,
the question set and the fixture are identical at 4081aa4 and 694033b; the method key differs
only in its 2c quotations following the text.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: met; 2a, 2b and 2c five of five.
- Restatement and application, all but one reader correct on each keyed item: met; every item
  five of five.
- A miss the key says counts against the document: none.
- A passage found confusing by two or more readers, in text the change wrote or altered: none.
- A passage found confusing by two or more readers, elsewhere: four, clause 3.1's lower-bound
  list item, section 1's Owner entry, section 2's "Attempt rather than pre-judge" and section 4's
  next-wider list item, routed to `acceptance/ROUTED.md`.
- From one reader only: eight passages, recorded.

**Verdict: PASS.**

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125404459); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125404026); the prompt, [part 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125405086) and [part 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125405631).
