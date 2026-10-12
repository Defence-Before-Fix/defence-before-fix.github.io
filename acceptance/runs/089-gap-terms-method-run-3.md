# Run 89: SPEC.md, gap terms, third run

- **Document**: SPEC.md

- **Pull request**: [18](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/18),
  open on branch `editor/gap-terms`. The readers were given commit 30fc055. The change, read
  against its merge base with `next`, 9e914fe, is a clarity edit to two paragraphs. In clause 3.6,
  the paragraph "A [Practitioner] who finds that an existing [Rule]'s printed [Identifier] does not
  resolve" now says that where the mechanism cannot resolve [Identifiers] at all, it is a
  mechanism gap under clause 3.2, not a [Toolchain] gap, and that because it also breaches the
  [toolchain specification](../../TOOLING-SPEC.md)'s own obligations it is recorded against the
  [Toolchain]'s claim as well, where clause 3.2 says, and blocks that claim under section 7 until
  fixed. In section 2, the paragraph "When it can, building the [Defence] is not optional" gains a
  sentence: "The method begins at clause 3.1, working out what [Class] the [Defect] belongs to;
  section 3 gives the order of the steps that follow." That sentence follows run 88, which failed
  on a keyed miss on 2a. No other paragraph of SPEC.md changes, and no paragraph is inserted or
  moved. No key or question changed for this change: no key quotes either altered paragraph and
  the change adds no obligation.

- **Cohort**: five readers, none reused from any earlier run; model `claude-haiku-5-5`, the
  cohort's model named for the run before its readers started. Every reader reported
  `claude-haiku-5-5`.

- **Isolation**, as the editor supplied it and attests: each reader a separate `claude -p`
  process, started through the `ccy-claude` wrapper (which only reattaches the session's
  credential), in a fresh empty directory made by `mktemp -d` outside any repository, with the
  packet on standard input; no tools, no settings, no project context, no saved session, and no
  managed settings on the machine. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt's sha256 is `5107692ff60d3f875239d122ee15ad46f4f1c00b37dbf4872ac76ccc064cb31c`.
  The marker rebuilt it from `acceptance/method/QUESTIONS.md`, `SPEC.md` and
  `acceptance/fixtures/remediation-ledger.md` at 30fc055, in that order, each after one
  `===== FILE: <name> =====` line, one blank line between files, and found it byte for byte
  identical.

- **Readers set aside**: none. Every answer text is non-empty, every reader's JSON has `is_error`
  false and subtype `success`, and every reader reported the cohort's model.

- **Run within the pull request**: 3. Run 34, under the earlier acceptance rules, and run 88,
  under this one, came before.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's marking instruction and its agent definition, having seen neither the drafting nor
  the review. It marked against `ACCEPTANCE.md` and `acceptance/method/KEY.md` at 30fc055, by the
  Marking section and the key alone. No judgement was taken from the record of run 34. Run 88
  was read for the shape of a record only.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 3.1     | 3.2 | 3.3     | 3.4 | 3.5     | 3.6 | Remediation | Defence | Section 4 |
| ------ | ------- | --- | --- | --- | ------- | --- | ------- | --- | ------- | --- | ----------- | ------- | --------- |
| 1      | correct | ok  | ok  | ok  | Partial | Yes | Yes     | No  | Partial | No  | ok          | ok      | ok        |
| 2      | correct | ok  | ok  | ok  | Partial | Yes | Partial | No  | No      | No  | ok          | ok      | ok        |
| 3      | correct | ok  | ok  | ok  | No      | Yes | Partial | No  | No      | No  | ok          | ok      | ok        |
| 4      | correct | ok  | ok  | ok  | Partial | Yes | Yes     | No  | No      | No  | ok          | ok      | ok        |
| 5      | correct | ok  | ok  | ok  | Partial | Yes | Yes     | No  | No      | No  | ok          | ok      | ok        |

No miss in the run. Every other cell gives the reader's grade, accepted, or "ok" for a correct
answer. No answer matches a wrong reading the key names. Reader 1's 2a is marked for the reader
on an open point, recorded below.

### Question 1

Each reader has at least four bullets naming obligations the key lists, and none the key marks
wrong.

- Reader 1: 3.1 (two bullets, the class and hazard and the search, counted once), 3.2 with 3.3,
  3.4 with 3.3's narrowing sentence, 3.5 with 3.6, the deferred defect recorded (section 2) with
  section 4. Five.
- Reader 2: 3.1 (bullets 1 and 3, counted once), 3.2 with 3.3, 3.4 with section 4, 3.5 with 3.6.
  Four. Bullet 2, that building a defence is mandatory and attempted before the fix and that
  expressibility is not pre-judged (section 2), is on neither of the key's lists: not counted,
  and recorded as an open point for the key.
- Reader 3: 3.1 (two bullets, counted once), 3.2 with 3.6, 3.3, 3.4 with section 4, 3.5 with the
  original defect fixed with a reproducing test. Five.
- Reader 4: 3.1 (two bullets, counted once), 3.2 with 3.3, 3.4 with section 4, 3.5 with 3.6, the
  original defect fixed with a reproducing test and the deferred defect recorded. Five.
- Reader 5: 3.1 (two bullets, counted once), 3.2 with 3.6, 3.3 with its narrowing sentence (Part
  B), 3.4 with 3.5, section 4 with the original defect fixed with a reproduction test. Five.

No reader has the fix first, a test as the detector, or an agent baselining.

### Question 2

- **2a**, five of five. Readers 2, 3, 4 and 5 each state the four steps, attribution to a class,
  the rule, its proof and the sweep, in that order with the original defect fixed after the sweep
  ("The originating defect is fixed last", reader 2; "then sweeps and records the count, all
  before fixing", reader 3; "sweeps the codebase, recording the count, before fixing any instance
  (3.4). The defect is fixed last", reader 4; "records the sweep count, fixes every instance ...
  Only after that do they fix the original defect", reader 5), and each quotes clause 3.4's "The
  [Practitioner] MUST run the [Rule] across the entire codebase and record the total [Instance]
  count before fixing anything". Reader 1 states "Attribute the defect to a class, search
  independently for other instances, then build and prove the rule with the originating instance
  still present, and only then fix. Sweep and fix every instance.", and quotes section 2's "When
  it can, building the [Defence] is not optional and MUST be attempted before the [Defect] is
  fixed", clause 3.1's "The [Practitioner] MUST first establish what [Class] the [Defect] belongs
  to" and clause 3.3's "The [Defence] is committed with the originating [Instance] still present,
  and the fix is committed after it." Whether it states the sweep before the fix is an open
  point, below; marked for the reader. No reader has the fix before the rule, the sweep before
  the proof, or a test as the detector.
- **2b**, five of five. Each names the owner and says an agent may not; each quotes section 4's
  "An [Agent] MUST NOT [Baseline], suppress or knowingly leave an [Instance] unfixed on its own
  authority, whatever the [Instance] count turns out to be."
- **2c**, five of five. Each states that all six clauses of section 3 were followed and that the
  verdict rests on reproduction; each quotes section 7's conforming-remediation sentence.

### Question 3

- **3.1**: four Partial (readers 1, 2, 4, 5), one No (reader 3); the key accepts any grade.
- **3.2**: five Yes.
- **3.3**: three Yes (readers 1, 4, 5), accepted without condition; two Partial (readers 2 and 3),
  each attributing the inline ignore on `Report::render()` to this clause, which meets the key's
  condition.
- **3.4**: five No, each naming `Report::render()` or the instance left unfixed behind the inline
  ignore.
- **3.5**: one Partial (reader 1), four No, each on the inline ignore that no recorded decision
  covers.
- **3.6**: five No, each naming the wiki and the documentation not versioned with the rule.
- **Remediation**: five say it does not conform, each naming 3.4 and 3.5 among the clauses not
  followed, readers 2 to 5 also 3.6.
- **Defence**: five say it does not conform, each naming 3.6 and 3.5's uncovered suppression.
- **Section 4**: five name the inline ignore on `Report::render()`. Readers 1 to 5 also name, as a
  second decision, leaving the wider rule unbuilt; not marked.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                                                                                                                     | Clause | Readers        | Text                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------------- | ---------------------------------------------------------------------- |
| "Attempt rather than pre-judge": "naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search" (readers 1, 5; reader 5 against the search techniques clause 3.1 describes); "recorded where the project's other decisions are enumerable under clause 8.7, not only with the fix." (reader 4) | 2      | three: 1, 4, 5 | Untouched; the clause 3.1 search reader 5 sets against it is untouched |
| Section 4's list item on leaving the next wider [Rule] unbuilt: "This does not reopen a [Class] whose bounds a [Hazard] sentence has settled, and it reaches no further than the one wider [Rule] already on the record." (readers 2, 3); "The absence of an [Instance] is the [Practitioner]'s reason not to widen unasked; ..." (reader 4)                | 4      | three: 2, 3, 4 | Untouched                                                              |
| Clause 3.3 Part B, the paragraph opening "**Then the proof, which runs the other way round, and both ways.**"                                                                                                                                                                                                                                               | 3.3    | two: 1, 4      | Untouched                                                              |
| The lower-bound list item: "A [Rule] drawn to the exact value or name found in the [Defect] is the same [Narrowing] however it is spelt.", each against the defined sense of [Narrowing]                                                                                                                                                                    | 3.1    | two: 2, 3      | Untouched; the Narrowing entry they set it against is untouched        |
| The two-bounds paragraph: "Both bounds measure breadth within one level; the level itself is a separate question, answered against the report."                                                                                                                                                                                                             | 3.1    | two: 2, 3      | Untouched                                                              |
| Clause 3.4, "Fix them all.": "and the scale at which that becomes true is tremendous."                                                                                                                                                                                                                                                                      | 3.4    | two: 3, 5      | Untouched                                                              |
| Section 4, "What to do whilst waiting": "the [Rule] MAY merge at full width with that case recorded as a known [Instance] awaiting the [Owner]" (reader 4 names it and sets it against the paragraph below; reader 5 quotes it as what it sets the paragraph below against)                                                                                 | 4      | two: 4, 5      | Untouched                                                              |
| Section 4, "A remediation MAY be delivered across several changes": "provided the [Rule] does not become [Blocking] until every [Instance] is fixed" (reader 5 names it, calling it "the paragraph on waiting", and sets it against the paragraph above; reader 4 quotes it as what it sets the paragraph above against)                                    | 4      | two: 4, 5      | Untouched                                                              |
| Clause 3.5, the bundled-defence paragraph: "The substitutes clause 3.2 allows, for proving under clause 3.3 and for resolution under clause 3.6, do not extend to this clause"                                                                                                                                                                              | 3.5    | one: 1         | Untouched; the reader sets it against nothing                          |
| The Owner entry: "That record MUST mark the decision as taken by a default [Owner] and state why nobody better placed was reachable, where the next reader can see who decided and why."                                                                                                                                                                    | 1      | one: 1         | Untouched                                                              |
| The Narrowing entry, described as defining [Narrowing] "as reducing scope so a rule stops reporting code that lacks the hazard" (reader 3, "the terminology section"). Reader 2 refers to it as "elsewhere", with no clause number or quotation, and so does not name it                                                                                    | 1      | one: 3         | Untouched                                                              |
| Section 7's conforming-[Defence] paragraph: "it fails rather than warns", set against clause 3.5's "every [Suppression] it carries is covered by a recorded decision"                                                                                                                                                                                       | 7      | one: 5         | Untouched                                                              |
| Clause 3.5's opening paragraph: "every [Suppression] it carries is covered by a recorded decision", quoted as what section 7's summary omits                                                                                                                                                                                                                | 3.5    | one: 5         | Untouched                                                              |

No reader names either paragraph the change altered, section 2's "When it can" paragraph or
clause 3.6's "A [Practitioner] who finds" paragraph, and no reader sets a passage against either.
Reader 1's clause 3.5 passage mentions "resolution under clause 3.6" but sets it against no
paragraph. Notes, not passages: none. Suggestions volunteered: none.

## Findings and where they lie

The change altered two paragraphs, section 2's "When it can, building the [Defence] is not
optional" and clause 3.6's "A [Practitioner] who finds that an existing [Rule]'s printed
[Identifier] does not resolve". It inserts and moves no paragraph, so it parts no paragraph from
what it refers to.

1. **Section 2, "Attempt rather than pre-judge"**, readers 1, 4 and 5. Untouched; it is the
   paragraph after "When it can" but a separate one, and the change inserted nothing between
   them. Reader 5 sets it against clause 3.1's search, untouched. Routed to
   `acceptance/ROUTED.md` (its existing row, raised again); does not block.
2. **Section 4, the list item on leaving the next wider [Rule] unbuilt**, readers 2, 3 and 4.
   Untouched. Routed to `acceptance/ROUTED.md` (its existing row, raised again); does not block.
3. **Clause 3.3 Part B, the "Then the proof, which runs the other way round, and both ways."
   paragraph**, readers 1 and 4. Untouched. Routed to `acceptance/ROUTED.md` (a new row); does
   not block.
4. **Clause 3.1, the lower-bound list item**, readers 2 and 3. Untouched; the Narrowing entry they
   set it against is untouched. Routed to `acceptance/ROUTED.md` (its existing row, raised
   again); does not block.
5. **Clause 3.1, the two-bounds paragraph**, readers 2 and 3. Untouched. Routed to
   `acceptance/ROUTED.md` (its existing row, raised again); does not block.
6. **Clause 3.4, the "Fix them all." paragraph**, readers 3 and 5. Untouched. Routed to
   `acceptance/ROUTED.md` (its existing row, raised again); does not block.
7. **Section 4, the "What to do whilst waiting" paragraph and the "A remediation MAY be delivered
   across several changes" paragraph**, each named by readers 4 and 5, each reader setting one
   against the other. Both untouched. Routed to `acceptance/ROUTED.md` (the existing row that
   sets these two sentences against each other, raised again); does not block.

No finding lies in text the change wrote or altered.

## Points the rules did not settle

- **Reader 1 on 2a: whether the answer states the sweep before the fix.** Element (1) requires
  the sweep among the steps before the fix, and element (2) the fix after the sweep. Reader 1's
  first sentence ends "and only then fix", after the proof, and its second, "Sweep and fix every
  instance.", puts the sweep before fixing every instance, the originating one among them. Read
  for its sense, the answer can be taken either as the second sentence spelling out what the fix
  involves, which states the sweep before it, or as the original defect fixed before a later
  sweep, which does not; its quotations do not settle it, since none is of clause 3.4's sweep
  sentence. The key names no wrong reading for a fix before the sweep. Neither the Question 2
  rule nor the key settles which sense is stated, so by the open-point rule it is marked for the
  reader: correct. For the editor to settle in the key or `ACCEPTANCE.md`.
- **Reader 2's question 1 bullet 2**: that building a [Defence] is mandatory and attempted before
  the fix, without pre-judging whether the [Class] is expressible (section 2). The obligation is
  on neither of the key's lists, so the bullet is not counted either way; an open point for the
  key. The reader has four correct bullets without it, so the mark is the same.
- **Whether reader 3 names the Narrowing entry**: it gives "the terminology section", a section's
  name rather than its number, with a description that identifies the entry. Counted as named
  under the open-point rule. With reader 2 not naming it, it is one reader's passage either way.
- **Considered, and settled by the rules: section 4's two paragraphs, readers 4 and 5.** Each
  reader quotes six or more words of each paragraph, with the section number, so each names
  both; two readers name each, and each is a finding. Both are untouched, so the verdict does not
  turn on it.

## Process change

Made under the process change of pull request 22 before it merged, at commit 40f7895, named
before the readers started. 40f7895, the tip of `editor/acceptance-coherent`, was merged into
this branch at f984911. `ACCEPTANCE.md`, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md`, `acceptance/method/` and `acceptance/fixtures/` are identical at 40f7895 and
30fc055.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: met; 2a, 2b and 2c five of five,
  reader 1's 2a on the open-point rule.
- Restatement and application, all but one reader correct on each keyed item: met; every item
  five of five.
- A miss the key says counts against the document: none.
- A passage found confusing by two or more readers, in text the change wrote or altered: none.
- A passage found confusing by two or more readers, elsewhere: seven findings, section 2's
  "Attempt rather than pre-judge", section 4's next-wider list item, clause 3.3's "Then the proof"
  paragraph, clause 3.1's lower-bound list item and two-bounds paragraph, clause 3.4's "Fix them
  all." paragraph, and section 4's waiting and several-changes paragraphs, routed to
  `acceptance/ROUTED.md`.
- From one reader only: five passages, recorded.

**Verdict: PASS.**

## Answer sheets

Posted on the pull request: [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/18#issuecomment-6126743123); [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/18#issuecomment-6126743699); [the prompt, part 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/18#issuecomment-6126744327) and [part 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/18#issuecomment-6126744809).
