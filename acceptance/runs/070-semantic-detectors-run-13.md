# Run 70: SPEC.md, semantic detectors, thirteenth run

- **Document**: SPEC.md

- **Pull request**: 14, open on branch `editor/semantic-detectors`. The readers were given commit
  befe52c. The change, read against its merge base with `next`, 9e914fe, adds to clause 3.2 the
  obligation that a [Rule] the [Practitioner] writes is written in the strongest kind of
  [Detector] that can express it, with the two grounds for a weaker kind, the naming of the
  [Detector] and its kind on the [Remediation docs] and the recording of the grounds on the
  [Remediation docs] and in a commit description, the owner's sign-off where the project requires
  it, and a worked example; adds the Textual, Syntactic and Semantic terminology entries and a
  sentence to the Detector entry; rewrites the section 3 map's 3.2 row; adds "of a kind that can
  express the [Rule] within clause 3.1's bounds" to section 2's three-ways-out paragraph and to
  clause 3.2's bespoke-detector and two-kinds-of-gap paragraphs; adds clause 3.6's deferral to
  what clause 3.2 adds; adds the sign-off proviso to section 4's first list and dividing-line
  paragraph; rewrites section 7's conforming-[Defence] sentence; extends Appendix A's "Write a
  custom [Rule]" paragraph; adds three link definitions; and sets the version to 1.2.0-dev. The
  question set gains item 2d for the new obligation; the key gains 2d and the 3.2 lines that go
  with it.

- **Cohort**: five readers, none reused from any earlier run; model `claude-haiku-5-5`, the
  cohort's model named for the run before its readers started. Every reader reported
  `claude-haiku-5-5`.

- **Isolation**, as the editor supplied it and attests: each reader a separate `claude -p`
  process, started through the `ccy-claude` wrapper (which only reattaches the session's
  credential), in a fresh empty directory made by `mktemp -d` outside any repository, with the
  packet on standard input; no tools, no settings, no project context, no saved session, and no
  managed settings on the machine. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The prompt's sha256 is `659a8d793ec9f5e94261703c695c94c17f3045a72f6988899c5734ac7ce59f9c`,
  checked by the marker against the file; the editor states it is byte for byte
  `acceptance/method/QUESTIONS.md`, `SPEC.md` and `acceptance/fixtures/remediation-ledger.md` at
  befe52c, in that order, each after one `===== FILE: <name> =====` line, one blank line between
  files.

- **Readers set aside**: none. Every answer text is non-empty, every reader's JSON has `is_error`
  false and subtype `success`, and every reader reported the cohort's model.

- **Run within the pull request**: 13. Runs 19 to 30 came before, on both documents, under the
  earlier acceptance rules and on an earlier, larger text of the change; runs 19, 21, 23, 25, 27
  and 29 read this document.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's marking instruction and its agent definition, having seen neither the drafting nor
  the review. It marked against `ACCEPTANCE.md` and `acceptance/method/KEY.md` at befe52c, by the
  Marking section and the key alone. No judgement was taken from the records of runs 19 to 30;
  run 64 was read for the shape of a record only.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 2d  | 3.1     | 3.2     | 3.3     | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 |
| ------ | ------- | --- | --- | --- | --- | ------- | ------- | ------- | --- | --- | --- | ----------- | ------- | --------- |
| 1      | correct | ok  | ok  | ok  | ok  | Partial | Partial | Yes     | No  | No  | No  | ok          | ok      | ok        |
| 2      | correct | ok  | ok  | ok  | ok  | No      | Partial | Yes     | No  | No  | No  | ok          | ok      | ok        |
| 3      | correct | ok  | ok  | ok  | ok  | No      | Partial | Yes     | No  | No  | No  | ok          | ok      | ok        |
| 4      | correct | ok  | ok  | ok  | ok  | Partial | Partial | Partial | No  | No  | No  | ok          | ok      | ok        |
| 5      | correct | ok  | ok  | ok  | ok  | Partial | Partial | miss    | No  | No  | No  | ok          | ok      | ok        |

One miss in the run: reader 5 on 3.3, graded Partial without the key's condition. Every other
cell gives the reader's grade, accepted, or "ok" for a correct answer. No answer matches a wrong
reading the key names.

### Question 1

Each reader has at least four bullets naming obligations the key lists and none the key marks
wrong.

- Reader 1: 3.1 (two bullets, counted once), 3.2's detector and its strongest kind with 3.3,
  3.4 with section 4, 3.5 with 3.6, the original defect fixed with a reproduction test and the
  deferred defect recorded.
- Reader 2: 3.1 (two bullets, counted once), 3.2's strongest kind, 3.3, 3.4 with section 4, 3.5
  with 3.6. Its sixth bullet's "A verdict on the result rests on reproduction" describes the
  reviewer, which the key says is neither correct nor wrong.
- Reader 3: 3.1 (two bullets, counted once), 3.2's strongest kind and never a test, 3.3, 3.4 with
  section 4, 3.5 with 3.6 and the reproduction test.
- Reader 4: 3.1 (two bullets, counted once), 3.2's strongest kind, 3.3, 3.4 with section 4, 3.5
  with 3.6 and the reproduction test.
- Reader 5: 3.1 (three bullets, counted once), 3.2's strongest kind with 3.6's identifier, 3.3,
  3.4 with section 4, 3.5 with 3.6.

No reader has the fix first, a test as the detector, an agent baselining, or a weaker kind never
allowed; readers 1, 2, 3 and 5 give the order semantic, syntactic, textual, which the key counts
as naming the strongest-kind line. Readers 3, 4 and 5 also assert, inside a bullet that names
clause 3.3, that an exclusion needs a written sentence or goes to the owner; see the points below.

### Question 2

- **2a**, five of five. Each states the four steps, attribution, the rule, its proof and the
  sweep, in that order with the fixing after the sweep, and each quotes clause 3.4's "The
  [Practitioner] MUST run the [Rule] across the entire codebase and record the total [Instance]
  count before fixing anything" (reader 4 from "record the total"). Reader 2 adds that the
  document "does not place those steps in one consistent sequence", citing Appendix A's fix of
  the original defect last; that is not an assertion the key marks wrong, and its own sequence
  has the fix after the sweep.
- **2b**, five of five. Each names the owner, a human, and says an agent may not; each quotes
  section 4's "An [Agent] MUST NOT [Baseline], suppress or knowingly leave an [Instance] unfixed
  on its own authority, whatever the [Instance] count turns out to be."
- **2c**, five of five. Each states that all six clauses were followed and that the verdict rests
  on reproduction. Readers 1, 2, 3 and 5 quote section 7's conforming-remediation sentence;
  reader 4 states it in its own words and quotes section 7's "A verdict on a remediation or a
  [Defence] MUST rest on reproduction, not on the report".
- **2d**, five of five. Each states the order semantic, else syntactic, else textual, quoting
  clause 3.2's "A [Rule] the [Practitioner] writes MUST be written in the strongest kind of
  [Detector] that can express it". Each quotes the two-grounds sentence, which states both
  grounds; reader 3 also gives them in its own words. Each states that the grounds are
  recorded in both places, the [Remediation docs] and a commit description: readers 1 and 3 in
  their own words, readers 2 and 4 by "two places" with the quotation "on the [Rule]'s
  [Remediation docs], and in the description of a commit", reader 5 by that quotation. No reader
  says the places are alternatives, that a weaker kind is never allowed, or that the owner must
  always approve; reader 1 says sign-off "applies only where the project requires it".

### Question 3

- **3.1**: three Partial (readers 1, 4, 5), two No (readers 2, 3); the key accepts any grade.
- **3.2**: five Partial, each on the detector or its kind not named. No reader graded Yes.
- **3.3**: three Yes (readers 1, 2, 3), accepted without condition. Reader 4 Partial, attributing
  the inline ignore on `Report::render` to Part B: correct. **Reader 5 Partial: a miss.** Its
  reasoning is that the enforced run reports the [Fixture], which "3.3 says it must not", and
  that the [Fixture]'s status after commit C is not explained; it does not attribute the inline
  ignore to this clause, the key's condition for Partial or No. The reasoning paraphrases clause
  3.3 Part C ("the enforced run does not report it") and gives no quotation of the document. The
  key names no wrong reading for 3.3, so this is a single miss, tolerated by the threshold.
- **3.4**: five No, each naming `Report::render()` left under the inline ignore.
- **3.5**: five No, each on the inline ignore no recorded decision covers.
- **3.6**: five No, each naming the wiki and the documentation not versioned with the rule.
- **Remediation**: five say it does not conform, each naming 3.4, 3.5 and 3.6 among the clauses
  not followed.
- **Defence**: five say it does not conform, each naming 3.5's uncovered suppression and 3.6.
- **Section 4**: five name the inline ignore on `Report::render()`. All five also name, as a
  second decision, leaving the wider rule unbuilt; not marked.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                                                                                        | Clause | Readers                    | Text                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Attempt rather than pre-judge": "in the vocabulary clause 3.1 uses for a search" (reader 1); "naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search" (readers 2, 4)                                                                                       | 2      | three: 1, 2, 4             | Untouched. Readers 2 and 4 set it against clause 3.1's search techniques, untouched                                                                         |
| The two-bounds paragraph: "Both bounds measure breadth within one level; the level itself is a separate question, answered against the report." (readers 1, 5)                                                                                                                                                                 | 3.1    | two: 1, 5                  | Untouched. Reader 5 sets it against the lower and upper bounds, untouched                                                                                   |
| The lower-bound list item: "That rejection is tested as a [Narrowing] is under clause 3.3" (reader 1); "A Rule drawn to the exact value or name found in the Defect is the same Narrowing however it is spelt." (reader 3)                                                                                                     | 3.1    | two: 1, 3                  | Untouched. Reader 1 sets it against clause 3.3's test, reader 3 against the Narrowing entry; both untouched                                                 |
| "A remediation MAY be delivered across several changes": "provided the [Rule] does not become [Blocking] until every [Instance] is fixed" (reader 2); "does not become [Blocking] until every [Instance] is fixed" (reader 4)                                                                                                  | 4      | two: 2, 4                  | Untouched. Reader 2 sets it against "What to do whilst waiting", reader 4 against Appendix A's "Make the [Rule] a permanent part" paragraph; both untouched |
| Appendix A's closing paragraph: "Only then fix the original [Defect]" (reader 2, against clause 3.4 and section 2); "Only then fix the original Defect." (reader 3, against clause 3.3's "the fix is committed after it"); "Only then fix the original [Defect] in the normal way, with a test that reproduces it." (reader 4) | App A  | three: 2, 3, 4             | Untouched; the change altered only Appendix A's "Write a custom [Rule]" paragraph, which no reader names. The paragraphs set against it are untouched       |
| Section 4's list item on leaving the next wider [Rule] unbuilt: "The absence of an Instance is the Practitioner's reason not to widen unasked." (reader 3); described as "§4 reserves that decision to the owner", set against clause 3.1's worked example (reader 2)                                                          | 4      | two: 3, and 2 (open point) | Untouched                                                                                                                                                   |
| "What to do whilst waiting": "the [Practitioner] … leaves the [Rule] unmerged rather than merged in a weakened form" and "the [Rule] MAY merge at full width with that case recorded as a known [Instance] awaiting the [Owner]"                                                                                               | 4      | one: 2                     | Untouched                                                                                                                                                   |
| Clause 3.1's worked example: "was not built because most of the codebase's catches are legitimate and the [Owner] has not decided"                                                                                                                                                                                             | 3.1    | one: 2                     | Untouched                                                                                                                                                   |
| Section 2's "When it can" paragraph: "before the [Defect] is fixed", and clause 3.4's opening sentence: "fix every [Instance]", both set against Appendix A's closing paragraph                                                                                                                                                | 2, 3.4 | one: 2                     | Untouched                                                                                                                                                   |
| Clause 3.2's recording paragraph: "which of the two grounds holds at each step down the order [Semantic], [Syntactic], [Textual], and why"                                                                                                                                                                                     | 3.2    | one: 2                     | Written by the change                                                                                                                                       |
| Clause 3.3 Part A, "The proof MUST survive as a commit of its own": "the fix is committed after it"                                                                                                                                                                                                                            | 3.3    | one: 3                     | Untouched                                                                                                                                                   |
| Clause 3.4, "Fix them all.": "the scale at which that becomes true is tremendous."                                                                                                                                                                                                                                             | 3.4    | one: 3                     | Untouched                                                                                                                                                   |
| Appendix A's "Make the [Rule] a permanent part of the project's quality checks, failing rather than [Warning]." paragraph                                                                                                                                                                                                      | App A  | one: 4                     | Untouched                                                                                                                                                   |
| Section 4's lead-in "Decisions that MUST go to whoever owns the codebase:", set against the Owner entry, "Whoever holds authority over a project's [Exceptions] and [Calibrations]"                                                                                                                                            | 4, 1   | one: 5                     | Untouched, and the Owner entry untouched                                                                                                                    |
| Clause 3.3 Part B, "A [Narrowing] reduces the [Practitioner]'s own work": "a [Narrowing] that excludes more code than the [Rule] still covers MUST be reported to the [Owner] as if it were a [Suppression]."                                                                                                                  | 3.3    | one: 5                     | Untouched                                                                                                                                                   |

Notes, not passages: none. Suggestions volunteered: none.

## Findings and where they lie

1. **Section 2, "Attempt rather than pre-judge"**, readers 1, 2 and 4. Untouched; the change's
   words in section 2 are in the next paragraph, "There are three ways out", which no reader
   names. Readers 2 and 4 set it against clause 3.1's search techniques, untouched. Routed to
   `acceptance/ROUTED.md` (its existing row, raised again); does not block.
2. **Clause 3.1, the two-bounds paragraph**, readers 1 and 5. Untouched by this change, and set
   against the bounds list items, untouched. Its row is closed by `editor/defined-terms` run 64,
   whose rewrite is not in this branch; routed to `acceptance/ROUTED.md`, noted on that row as
   raised again on the text before that rewrite; does not block.
3. **Clause 3.1, the lower-bound list item**, readers 1 and 3. Untouched; set against clause
   3.3's test and the Narrowing entry, both untouched. Routed to `acceptance/ROUTED.md` (its
   existing row, raised again); does not block.
4. **Section 4, "A remediation MAY be delivered across several changes"**, readers 2 and 4.
   Untouched; set against "What to do whilst waiting" and Appendix A's "Make the [Rule] a
   permanent part" paragraph, both untouched. Routed to `acceptance/ROUTED.md`, on the existing
   section 4 row that sets "MAY merge at full width" against this sentence; does not block.
5. **Appendix A, "Only then fix the original [Defect] in the normal way"**, readers 2, 3 and 4.
   Untouched: each paragraph of Appendix A's block quote is a paragraph of its own, and the change
   altered only "Write a custom [Rule]". Set against section 2's "When it can", clause 3.4's
   opening sentence, clause 3.3 Part A's "The proof MUST survive" and section 4's several-changes
   paragraph, all untouched. Routed to `acceptance/ROUTED.md` as a new row; does not block.
6. **Section 4, the list item on leaving the next wider [Rule] unbuilt**, reader 3, and reader 2
   by the open-point rule. Untouched; reader 2 sets it against clause 3.1's worked example,
   untouched. Routed to `acceptance/ROUTED.md` (its existing row, raised again); does not block.

No finding lies in text the change wrote or altered. Of the passages from one reader only, one
lies there: clause 3.2's recording paragraph, "at each step down the order" (reader 2). No reader
names the terminology entries for Textual, Syntactic or Semantic, the section 3 map's 3.2 row,
clause 3.2's other new paragraphs, clause 3.6's deferral, section 4's proviso or section 7's
conforming-[Defence] sentence.

## Points the rules did not settle

- **Whether reader 2 names section 4's next-wider list item.** Reader 2 quotes clause 3.1's worked
  example and sets it against "§4 reserves that decision to the owner", a clause number with a
  description that identifies the list item on leaving the next wider [Rule] unbuilt. Marked by
  the open-point rule as naming the passage, which makes finding 6. It lies in untouched text
  either way, so the verdict is the same.
- **Question 1 bullets on [Narrowing].** Readers 3, 4 and 5 each assert, in a bullet that also
  names clause 3.3's proof, that an exclusion or narrowing needs a written sentence, or goes to
  the owner (clause 3.3 Part B). That obligation is in neither of the key's lists. Not counted
  either way; each bullet counts for its clause 3.3 content, and each reader has four or more
  correct bullets without it. An open point for the key.
- **Considered, and settled by the rules.** The marker's agent definition says a miss whose
  reasoning quotes the document is a finding whatever the count; `ACCEPTANCE.md` has no such
  rule, and the marker marked by `ACCEPTANCE.md`. The one miss, reader 5 on 3.3, quotes nothing,
  so the point does not arise in this run.

## Process change

Made under the process change of pull request 22 before it merged, at commit f3ec69e, named
before the readers started. f3ec69e is on `editor/acceptance-coherent`, one commit after
5852a85, which this branch merged; it changes only `acceptance/ROUTED.md`. `ACCEPTANCE.md`,
`acceptance/README.md`, `acceptance/runs/README.md` and `CONTRIBUTING.md` are identical at
f3ec69e and befe52c.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: met; 2a, 2b, 2c and 2d five of
  five.
- Restatement and application, all but one reader correct on each keyed item: met; 3.3 four of
  five, every other item five of five.
- A miss the key says counts against the document: none.
- A passage found confusing by two or more readers, in text the change wrote or altered: none.
- A passage found confusing by two or more readers, elsewhere: six, section 2's "Attempt rather
  than pre-judge", clause 3.1's two-bounds paragraph and lower-bound list item, section 4's
  several-changes paragraph and next-wider list item, and Appendix A's closing paragraph, routed
  to `acceptance/ROUTED.md`.
- From one reader only: nine passages, recorded.

**Verdict: PASS.**

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6125136762); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6125136402); the prompt, [part 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6125137201) and [part 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6125137748).
