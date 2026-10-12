# Run 61: SPEC.md, defined terms, eleventh run

- **Document**: SPEC.md

- **Pull request**: [24](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24), opened later from branch `editor/defined-terms`. The
  readers were given commit 988cde2. The change, read against its merge base with `next`,
  9e914fe, adds the Remediation terminology entry and its link definition; links "remediation"
  as [Remediation] in clauses 3.1, 3.3, 3.6, sections 4, 5, 6 and 7 and the 1.1.0 changelog row;
  replaces "a proving harness" in clause 3.2 and "purpose-built [Rule]-testing harnesses" in
  clause 3.3 with [Rule harness], with a link definition to the detector specification; replaces
  "the entire remediation loop" in section 8 with "the entire correction loop"; names in clause
  3.2 and clause 3.5 the substitutes a mechanism gap allows; rewrites clause 3.1's paragraph on
  the two bounds; and, since run 59, adds to section 1's opening a paragraph on terms defined in
  the companion specifications, and opens clause 3.5's "For a [Bundled defence]" paragraph with a
  sentence saying what a [Bundled defence] and a [Consuming project] are. The question set and
  fixture are as at e6bdf40; the key differs from e6bdf40 only in its 2c quotations following
  the text ("A remediation" and "a remediation" became "A Remediation" and "a Remediation").

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

  - the prompt (sha256 `cd1c4a8294bf13f838272ab5bc9cd22605ac82720d271bc37097d46c253167b0`) is
    byte for byte `acceptance/method/QUESTIONS.md`, `SPEC.md` and
    `acceptance/fixtures/remediation-ledger.md` at 988cde2, in that order, each preceded by one
    `===== FILE: <name> =====` line, with one blank line between files, rebuilt from the commit
    and compared;
  - each reader's JSON output has `is_error` false and subtype `success`, reports
    `claude-haiku-5-5`, and each sheet is byte for byte its `result`.

- **Readers set aside**: none. Every answer text is non-empty, no process reported an error, and
  every reader reported the cohort's model.

- **Run within the pull request**: 11. Runs 31 to 52 came before under the earlier rules, and runs
  53 to 59 under these; runs 54 and 55 read the other two documents.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's marking instruction and its agent definition, having seen neither the drafting nor
  the review. It marked against `ACCEPTANCE.md` and `acceptance/method/KEY.md` at 988cde2, by
  the Marking section and the key alone. No earlier run record was read for its judgements; run
  59 was read for the shape of a record only.

## Marks

| Reader | Q1      | 2a       | 2b  | 2c  | 3.1     | 3.2 | 3.3           | 3.4 | 3.5     | 3.6 | Remediation | Defence | Section 4 |
| ------ | ------- | -------- | --- | --- | ------- | --- | ------------- | --- | ------- | --- | ----------- | ------- | --------- |
| 1      | correct | ok       | ok  | ok  | No      | Yes | Yes           | No  | No      | No  | ok          | ok      | ok        |
| 2      | correct | ok       | ok  | ok  | Partial | Yes | Partial, miss | No  | No      | No  | ok          | ok      | ok        |
| 3      | correct | ok       | ok  | ok  | Partial | Yes | Yes           | No  | No      | No  | ok          | ok      | ok        |
| 4      | correct | **miss** | ok  | ok  | Partial | Yes | Yes           | No  | Partial | No  | ok          | ok      | ok        |
| 5      | correct | ok       | ok  | ok  | No      | Yes | Partial       | No  | No      | No  | ok          | ok      | ok        |

Two misses: reader 4 on 2a, reader 2 on 3.3. Both readers' reasoning quotes the document. Neither
matches a wrong reading the key names (the key names none for question 1, none for 3.3, and none
for question 2, where every miss counts against the threshold).

### Question 1

Each reader has at least four bullets naming obligations the key lists and none the key marks
wrong. Reader 1: 3.1 (two bullets, counted once), 3.2 with 3.3, 3.4, 3.5 with 3.6, the original
defect fixed with a reproducing test. Reader 2: 3.1 (two bullets, counted once), 3.2, 3.3, 3.4
with section 4, 3.5 with 3.6 and the reproducing test. Reader 3: 3.1 (with the search bullet,
counted once), 3.2, 3.3, 3.4 with section 4, 3.5 with 3.6 and the reproducing test. Reader 4: 3.1
(two bullets, counted once), 3.2 with 3.6, 3.3 with 3.4, 3.5, the reproducing test with section 4.
Reader 5: 3.1 (two bullets, counted once), 3.2 with 3.6, 3.3 with 3.4, 3.5 with section 4 and the
reproducing test. No reader has the fix first, a test as the detector, or an agent baselining.

### Question 2

- **2a**, four of five. Readers 1, 2, 3 and 5 state the class, the rule, its proof and the sweep,
  with the fixing after the sweep, and quote clause 3.4's "record the total [Instance] count
  before fixing anything". Reader 2 adds that the rule becomes blocking only once every instance
  is fixed; the key does not mark it wrong.
  **Reader 4, miss.** Its sentences are "The practitioner names the class and builds the defence
  first, then fixes. The six clauses come in order, and the count is recorded before any
  fixing." It quotes the preamble ("you first treat that [Instance] as evidence of a [Class], and
  you build the automated [Defence] ..."), section 3's "Six clauses, in order.", clause 3.4's
  opening sentence and Appendix A's "Only then fix the original [Defect] ...". The attribution,
  the rule and the sweep are stated; proving the rule fires is stated neither in its sentences nor
  in any quotation. The only words that could carry it are "Six clauses, in order", which the key
  says names no step and does not state element (1). Element (1) requires all four steps, so the
  answer misses it. The reasoning quotes the document.
- **2b**, five of five. Each names the owner, always a human, and says an agent may not; each
  quotes section 4's "An [Agent] MUST NOT [Baseline], suppress or knowingly leave an [Instance]
  unfixed on its own authority".
- **2c**, five of five. Each states that all six clauses were followed and that the verdict rests
  on reproduction, quoting section 7's conforming-[Remediation] sentence and "A verdict on a
  [Remediation] or a [Defence] MUST rest on reproduction".

### Question 3

- **3.1**: two No (readers 1, 5), three Partial; the key accepts any grade.
- **3.2**: five Yes.
- **3.3**: three Yes (readers 1, 3, 4), accepted without condition; reader 5 Partial, attributing
  the inline ignore on `Report::render()` to an exclusion with no written sentence, which meets
  the condition. **Reader 2, miss**: Partial, on the reasoning that the enforced CI run reports the
  fixture as one of its five findings, whereas the clause says "the enforced run does not report
  it" (clause 3.3, Part C, the paragraph on [Fixtures]). It does not attribute the inline ignore
  to this clause, so the key's condition for Partial is not met. The reasoning quotes the
  document. A single miss on the item; four of five.
- **3.4**: five No, each naming `Report::render()` behind the inline ignore.
- **3.5**: four No, one Partial (reader 4), each on the inline ignore no recorded decision covers.
  No reader graded Yes.
- **3.6**: five No, each naming the wiki.
- **Remediation**: five say it does not conform, each naming 3.4, 3.5 and 3.6.
- **Defence**: five say it does not conform, each naming 3.5's uncovered suppression and 3.6.
- **Section 4**: five name the inline ignore on `Report::render()`. Readers 1, 2, 4 and 5 also
  name, as a second candidate, leaving the wider rule unbuilt; not marked.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Clause     | Readers          | Text                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Section 4's list item "Leaving unbuilt the next wider [Rule] ...": "This does not reopen a [Class] whose bounds a [Hazard] sentence has settled, ..." (reader 1); "Leaving unbuilt the next wider [Rule] that clause 3.1 required the [Practitioner] to name, where it was rejected because no [Instance] of it exists today ..." (reader 2); "where it was rejected because no [Instance] of it exists today rather than because the [Hazard] cannot arise there" (reader 3); "The absence of an [Instance] is the [Practitioner]'s reason not to widen unasked; ..." (reader 5) | 4          | four: 1, 2, 3, 5 | Untouched; reader 2 sets it against section 3's table row for 3.1, reader 3 against clause 3.1, both untouched in what they point at |
| "A [Remediation] [Conforms]": "...and the verdict that they were rests on reproduction, as this section closes by requiring, not on the report." (readers 1, 5)                                                                                                                                                                                                                                                                                                                                                                                                                   | 7          | two: 1, 5        | Altered by the change: "A remediation" became "A [Remediation]"                                                                      |
| Section 2, "Attempt rather than pre-judge": "naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search" (readers 3, 5)                                                                                                                                                                                                                                                                                                                                                                                            | 2          | two: 3, 5        | Untouched                                                                                                                            |
| "Fix them all.": "and the scale at which that becomes true is tremendous" (readers 2, 3), against "No threshold is given here deliberately" in the same paragraph (reader 2)                                                                                                                                                                                                                                                                                                                                                                                                      | 3.4        | two: 2, 3        | Untouched                                                                                                                            |
| The Owner entry: "Where the project has recorded nobody, the [Owner] is whoever instructed the [Practitioner], and [Escalation] goes there", beside "Always a human"                                                                                                                                                                                                                                                                                                                                                                                                              | 1          | one: 1           | Untouched                                                                                                                            |
| Section 3's table, row 3.1, owner column: "Whether the next wider [Rule] is built", set against section 4's list item above                                                                                                                                                                                                                                                                                                                                                                                                                                                       | 3          | one: 2           | Untouched                                                                                                                            |
| Section 3's opening: "Six clauses, in order.", set against Appendix A's last line and clause 3.4's opening                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 3          | one: 4           | Untouched                                                                                                                            |
| Appendix A: "Only then fix the original [Defect] in the normal way"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Appendix A | one: 4           | Untouched                                                                                                                            |
| Clause 3.4's opening: "record the total [Instance] count before fixing anything" (a shorter quotation with its clause number)                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 3.4        | one: 4           | Untouched                                                                                                                            |
| "A [Remediation] MAY be delivered across several changes": "the [Rule] does not become [Blocking] until every [Instance] is fixed", against the paragraph below                                                                                                                                                                                                                                                                                                                                                                                                                   | 4          | one: 4           | Altered by the change: "A remediation" became "A [Remediation]"                                                                      |
| "What to do whilst waiting": "the [Rule] MAY merge at full width with that case recorded as a known [Instance] awaiting the [Owner]"                                                                                                                                                                                                                                                                                                                                                                                                                                              | 4          | one: 4           | Untouched                                                                                                                            |

Notes, not passages: none.

## Findings and where they lie

1. **Section 7, the paragraph "A [Remediation] [Conforms]"**, readers 1 and 5. Both quote its
   closing words, "as this section closes by requiring, not on the report". The change linked a
   term in this paragraph ("A remediation" became "A [Remediation]", now pointing to the new
   terminology entry), and a paragraph in which the pull request changes a term or a link is text
   the change altered. **Blocks.**
2. **Section 4, the list item on leaving the next wider [Rule] unbuilt**, readers 1, 2, 3 and 5.
   Untouched. Reader 2 sets it against section 3's table row for 3.1, untouched. Reader 3 sets it
   against "3.1, which puts the hazard sentence with the [Practitioner]"; the text of clause 3.1 that
   says that is its five steps and its lower-bound list item, both untouched, and neither of the
   two paragraphs the change altered in clause 3.1 is about the hazard sentence or who decides.
   Routed to `acceptance/ROUTED.md` (its existing row, raised again); does not block.
3. **Section 2, "Attempt rather than pre-judge"**, readers 3 and 5. Untouched, and neither reader
   sets it against altered text. Routed to `acceptance/ROUTED.md` (its existing row, raised
   again); does not block.
4. **Clause 3.4, the paragraph "Fix them all."**, readers 2 and 3, on "the scale at which that
   becomes true is tremendous". Untouched, and neither reader sets it against altered text.
   Routed to `acceptance/ROUTED.md` as a new row; does not block.

The run 59 finding, clause 3.5's "For a [Bundled defence]" paragraph, was named by no reader in
this run, nor was section 1's new paragraph on companion terms. Of the passages from one reader
only, one lies in text the change altered: section 4's several-changes paragraph (reader 4).

## Points the rules did not settle

- **Where finding 2 lies, given reader 3's "3.1".** Reader 3 names clause 3.1 by number with a
  description, not a paragraph, and clause 3.1 holds two paragraphs the change altered. The
  marker took the description, "which puts the hazard sentence with the [Practitioner]", as
  identifying the text it sets the list item against, and that text is untouched; so the rules
  settle it as outside the change. Were the description taken not to identify a paragraph, the
  open-point rule would treat finding 2 as the change's own text and it would block as well; the
  verdict is the same either way.
- No other point. No question 1 bullet asserts an obligation on neither list; reader 4's 2a mark
  is settled by the key's required elements and its sentence on "six clauses ... in order".

## Process change

Made under the process change of pull request 22 before it merged, at commit e6bdf40, named
before the readers started. The process files at 988cde2 are identical to those at e6bdf40; the
method key differs only in its 2c quotations following the text.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: not met; 2a is four of five
  (reader 4).
- Restatement and application, all but one reader correct on each keyed item: met; 3.3 is four
  of five (reader 2), every other item five of five.
- A miss the key says counts against the document: none.
- A passage found confusing by two or more readers, in text the change wrote or altered: one,
  section 7's "A [Remediation] [Conforms]" paragraph. Not met.
- A passage found confusing by two or more readers, elsewhere: three, section 4's next-wider list
  item, section 2's "Attempt rather than pre-judge" and clause 3.4's "Fix them all." paragraph,
  routed to `acceptance/ROUTED.md`.
- From one reader only: seven passages, recorded.

**Verdict: FAIL**, on reader 4's miss on 2a and on finding 1.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125402919); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125402498); the prompt, [part 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125403301) and [part 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125403673).
