# Run 88: SPEC.md, gap terms, second run

- **Document**: SPEC.md

- **Pull request**: 18, open on branch `editor/gap-terms`. The readers were given commit f984911.
  The change, read against its merge base with `next`, 9e914fe, is a clarity edit to one
  paragraph of clause 3.6, "A [Practitioner] who finds that an existing [Rule]'s printed
  [Identifier] does not resolve": where the mechanism cannot resolve [Identifiers] at all, it now
  says this is a mechanism gap under clause 3.2, not a [Toolchain] gap, and that since it also
  breaches the [toolchain specification](../../TOOLING-SPEC.md)'s own obligations it blocks the
  [Toolchain]'s claim under section 7 until fixed. No other paragraph of SPEC.md changes. No key
  or question changed for this change: no key quotes the altered sentence and the change adds no
  obligation.

- **Cohort**: five readers, none reused from any earlier run; model `claude-haiku-5-5`, the
  cohort's model named for the run before its readers started. Every reader reported
  `claude-haiku-5-5`.

- **Isolation**, as the editor supplied it and attests: each reader a separate `claude -p`
  process, started through the `ccy-claude` wrapper (which only reattaches the session's
  credential), in a fresh empty directory made by `mktemp -d` outside any repository, with the
  packet on standard input; no tools, no settings, no project context, no saved session, and no
  managed settings on the machine. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt's sha256 is `339c36f9a6f4be2d5c860991c0bf4b69667a945d798467a4688ae2354e7a3f2e`,
  checked by the marker against the file; the editor states it is byte for byte
  `acceptance/method/QUESTIONS.md`, `SPEC.md` and `acceptance/fixtures/remediation-ledger.md` at
  f984911, in that order, each after one `===== FILE: <name> =====` line, one blank line between
  files.

- **Readers set aside**: none. Every answer text is non-empty, every reader's JSON has `is_error`
  false and subtype `success`, and every reader reported the cohort's model.

- **Run within the pull request**: 2. Run 34 came before, under the earlier acceptance rules.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's marking instruction and its agent definition, having seen neither the drafting nor
  the review. It marked against `ACCEPTANCE.md` and `acceptance/method/KEY.md` at f984911, by the
  Marking section and the key alone. No judgement was taken from the record of run 34; run 70
  was read for the shape of a record only.

## Marks

| Reader | Q1      | 2a   | 2b  | 2c  | 3.1     | 3.2 | 3.3 | 3.4 | 3.5 | 3.6     | Remediation | Defence | Section 4 |
| ------ | ------- | ---- | --- | --- | ------- | --- | --- | --- | --- | ------- | ----------- | ------- | --------- |
| 1      | correct | ok   | ok  | ok  | Partial | Yes | Yes | No  | No  | Partial | ok          | ok      | ok        |
| 2      | correct | ok   | ok  | ok  | No      | Yes | Yes | No  | No  | No      | ok          | ok      | ok        |
| 3      | correct | miss | ok  | ok  | Partial | Yes | Yes | No  | No  | No      | ok          | ok      | ok        |
| 4      | correct | ok   | ok  | ok  | Partial | Yes | Yes | No  | No  | No      | ok          | ok      | ok        |
| 5      | correct | ok   | ok  | ok  | Partial | Yes | Yes | No  | No  | No      | ok          | ok      | ok        |

One miss in the run: reader 3 on 2a. Every other cell gives the reader's grade, accepted, or "ok"
for a correct answer. No answer matches a wrong reading the key names.

### Question 1

Each reader has at least four bullets naming obligations the key lists and none the key marks
wrong. Only the first six bullets are marked.

- Reader 1: 3.1 (two bullets, the class and hazard and the search, counted once), 3.2 with 3.3,
  3.4, 3.5 with 3.6, the original defect fixed with a reproducing test with section 4.
- Reader 2: 3.1, 3.2, 3.1's search with 3.3, 3.4 with section 4, 3.5 with 3.6, the original
  defect fixed with a reproducing test and the deferred defect recorded (section 2).
- Reader 3: 3.1 (two bullets, counted once), 3.2 never a test, 3.3 with its narrowing sentence
  (Part B), 3.4 with 3.5 and 3.6, the reproducing test with section 4.
- Reader 4: 3.1 (two bullets, counted once), 3.2, 3.3 with 3.4 and 3.6, 3.5 with section 4, the
  deferred defect recorded and the reproducing test.
- Reader 5: 3.1 (two bullets, counted once), 3.2, 3.3, 3.4 with section 4, 3.5 with 3.6. Its
  line after the six bullets, the reproduction test, is not a bullet and is not marked.

No reader has the fix first, a test as the detector, or an agent baselining.

### Question 2

- **2a**, four of five. Readers 1, 2, 4 and 5 each state the four steps, attribution to a class,
  the rule, its proof and the sweep, in that order with the fix after the sweep, and each quotes
  the document (readers 2, 4 and 5 clause 3.4's "The [Practitioner] MUST run the [Rule] across the
  entire codebase and record the total [Instance] count before fixing anything"; reader 1 section
  2's "When it can, building the [Defence] is not optional and MUST be attempted before the
  [Defect] is fixed"). **Reader 3: a miss.** It states "The practitioner builds and proves the
  rule, sweeps and counts, and fixes every instance, all before the defect's own fix", and quotes
  section 2's "When it can, building the [Defence]" sentence, clause 3.4's sweep sentence and
  Appendix A's "Only then fix the original [Defect] in the normal way". Neither its sentences nor
  its quotations state the first step, attributing the defect to a class; [Defence] is defined
  as a [Blocking] [Rule] with its documentation, and [Rule] as one pattern definition within a
  [Detector], so neither term states it. Element (1) is not stated.
- **2b**, five of five. Each names the owner and says an agent may not; each quotes section 4's
  "An [Agent] MUST NOT [Baseline], suppress or knowingly leave an [Instance] unfixed on its own
  authority, whatever the [Instance] count turns out to be."
- **2c**, five of five. Each states that all six clauses of section 3 were followed and that the
  verdict rests on reproduction; each quotes section 7's conforming-remediation sentence.

### Question 3

- **3.1**: four Partial (readers 1, 3, 4, 5), one No (reader 2); the key accepts any grade.
- **3.2**: five Yes.
- **3.3**: five Yes, accepted without condition.
- **3.4**: five No, each naming `Report::render()` left under the inline ignore.
- **3.5**: five No, each on the inline ignore no recorded decision covers.
- **3.6**: one Partial (reader 1), four No, each naming the wiki and the documentation not
  versioned with the rule.
- **Remediation**: five say it does not conform, each naming 3.4 and 3.5 among the clauses not
  followed, readers 2 to 5 also 3.6.
- **Defence**: five say it does not conform. Readers 2 to 5 name 3.5's uncovered suppression and
  3.6. Reader 1 names section 7's requirement that the defence "resolve to documentation versioned
  alongside it" and says "The wiki fails the second requirement", which states clause 3.6's
  requirement in its sense.
- **Section 4**: five name the inline ignore on `Report::render()`. Readers 1 to 5 also name, as
  a second decision, leaving the wider rule unbuilt; not marked.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                                                                                                                     | Clause | Readers          | Text                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ---------------- | ------------------------------------------------------------------------ |
| The two-bounds paragraph: "Both bounds measure breadth within one level; the level itself is a separate question, answered against the report." (readers 1, 2, 3, 4)                                                                                                                                                                                        | 3.1    | four: 1, 2, 3, 4 | Untouched                                                                |
| Section 4's list item on leaving the next wider [Rule] unbuilt: quoted whole, set against the section 3 table's 3.1 row (reader 1); "The absence of an [Instance] is the [Practitioner]'s reason not to widen unasked; ..." (reader 2); "it reaches no further than the one wider [Rule] already on the record." (reader 4)                                 | 4      | three: 1, 2, 4   | Untouched; the 3.1 table row reader 1 sets against it is untouched       |
| The lower-bound list item: "unless the independent search below has found no other [Instance] ... genuinely singular today" with "where it stays because the search found nothing wider" (reader 1); "A [Rule] drawn to the exact value or name found in the [Defect] is the same [Narrowing] however it is spelt." (reader 2, against the Narrowing entry) | 3.1    | two: 1, 2        | Untouched; the Narrowing entry reader 2 sets against it is untouched     |
| "Attempt rather than pre-judge": "naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search" (readers 4, 5; reader 5 against clause 3.1's "The [Rule] itself is never one of the techniques.")                                                                                              | 2      | two: 4, 5        | Untouched; the clause 3.1 sentence reader 5 sets against it is untouched |
| Clause 3.4, "Fix them all.": "and the scale at which that becomes true is tremendous." (readers 3, 5)                                                                                                                                                                                                                                                       | 3.4    | two: 3, 5        | Untouched                                                                |
| The section 3 table's 3.1 row, Owner column: "Whether the next wider [Rule] is built.", set against section 4's next-wider list item                                                                                                                                                                                                                        | 3      | one: 1           | Untouched                                                                |
| Section 7's conforming-[Defence] paragraph: "satisfies clauses 3.1, 3.2, 3.3, 3.5 and 3.6" and "it fails rather than warns", set against clause 3.5's three conditions                                                                                                                                                                                      | 7, 3.5 | one: 3           | Untouched, and clause 3.5's opening paragraph untouched                  |
| Section 5: "a project whose checks run in another order is a project that does not [Conform]", set against section 7's "Nothing here constrains how the project runs its checks or what it does when they fail."                                                                                                                                            | 5, 7   | one: 3           | Untouched, and section 7's conforming-project paragraph untouched        |
| The Owner entry: "Where the project has recorded nobody, the [Owner] is whoever instructed the [Practitioner], and [Escalation] goes there."                                                                                                                                                                                                                | 1      | one: 4           | Untouched                                                                |
| Clause 3.3 Part B, "A [Narrowing] reduces the [Practitioner]'s own work": "a [Narrowing] that excludes more code than the [Rule] still covers MUST be reported to the [Owner] as if it were a [Suppression]."                                                                                                                                               | 3.3    | one: 5           | Untouched                                                                |

Notes, not passages: none. Suggestions volunteered: none.

## Findings and where they lie

The change altered one paragraph, clause 3.6's "A [Practitioner] who finds that an existing
[Rule]'s printed [Identifier] does not resolve". It inserts and moves no paragraph. No reader
names that paragraph, and no reader sets any passage against it.

1. **Clause 3.1, the two-bounds paragraph**, readers 1, 2, 3 and 4. Untouched. Routed to
   `acceptance/ROUTED.md`; its row there is closed by `editor/defined-terms` run 64, whose
   rewrite is not in this branch, so it is noted on that row as raised again on the text before
   that rewrite. Does not block.
2. **Section 4, the list item on leaving the next wider [Rule] unbuilt**, readers 1, 2 and 4.
   Untouched; reader 1 sets it against the section 3 table's 3.1 row, untouched. Routed to
   `acceptance/ROUTED.md` (its existing row, raised again); does not block.
3. **Clause 3.1, the lower-bound list item**, readers 1 and 2. Untouched; reader 2 sets it
   against the Narrowing entry, untouched. Routed to `acceptance/ROUTED.md` (its existing row,
   raised again); does not block.
4. **Section 2, "Attempt rather than pre-judge"**, readers 4 and 5. Untouched; the paragraph
   after it, "There are three ways out", names mechanism and [Toolchain] gaps but is also
   untouched, and no reader names it. Reader 5 sets it against clause 3.1's sentence on the
   [Rule] not being a technique, untouched. Routed to `acceptance/ROUTED.md` (its existing row,
   raised again); does not block.
5. **Clause 3.4, the "Fix them all." paragraph**, readers 3 and 5. Untouched. Routed to
   `acceptance/ROUTED.md` (its existing row, raised again); does not block.

No finding lies in text the change wrote or altered.

## Points the rules did not settle

- **Whether reader 1 names section 4's next-wider list item.** Reader 1 names the section 3
  table's 3.1 row and quotes the section 4 list item whole, as what the row conflicts with.
  The quotation is of six or more words with a clause number, so it names the list item; marked
  so, and by the open-point rule it would count either way. Readers 2 and 4 make the finding
  without it, so the verdict is the same.
- **Considered, and settled by the rules: reader 3 on 2a.** Whether "builds and proves the rule"
  states attribution to a class. The key lists attribution as one of the four steps element (1)
  requires, and the terminology defines [Defence] and [Rule] without the [Class]; neither the
  reader's sentences nor its quotations state it. Marked a miss by the Question 2 rule, not as an
  open point.

## Process change

Made under the process change of pull request 22 before it merged, at commit 40f7895, named
before the readers started. f984911 is the merge of `editor/acceptance-coherent` into this
branch, with 40f7895, the tip of `editor/acceptance-coherent`, its second parent.
`ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md` and `CONTRIBUTING.md` are
identical at 40f7895 and f984911.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: **not met**; 2a four of five
  (reader 3 misses), 2b and 2c five of five.
- Restatement and application, all but one reader correct on each keyed item: met; every item
  five of five.
- A miss the key says counts against the document: none. The key names no wrong reading for 2a;
  the miss fails the question 2 threshold on its own.
- A passage found confusing by two or more readers, in text the change wrote or altered: none.
- A passage found confusing by two or more readers, elsewhere: five, clause 3.1's two-bounds
  paragraph and lower-bound list item, section 4's next-wider list item, section 2's "Attempt
  rather than pre-judge" and clause 3.4's "Fix them all." paragraph, routed to
  `acceptance/ROUTED.md`.
- From one reader only: five passages, recorded.

**Verdict: FAIL**, on question 2: reader 3 misses 2a. Under "After a failure", a failed keyed
item is fixed in the text that carries the obligation, wherever it lies.

## Answer sheets

Posted on the pull request: [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/18#issuecomment-6126480355); [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/18#issuecomment-6126480756); [the prompt, part 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/18#issuecomment-6126481232) and [part 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/18#issuecomment-6126481727).
