# Run 59: SPEC.md, defined terms, tenth run

- **Document**: SPEC.md

- **Pull request**: not yet opened; it will be opened on branch `editor/defined-terms`. The
  readers were given commit 48f6e7c. The change, read against its merge base with `next`,
  9e914fe, adds the Remediation terminology entry and its link definition; links "remediation"
  as [Remediation] in clauses 3.1, 3.3, 3.6, sections 4, 5, 6 and 7 and the 1.1.0 changelog row;
  replaces "a proving harness" in clause 3.2 and "purpose-built [Rule]-testing harnesses" in
  clause 3.3 with [Rule harness], with a link definition to the detector specification; replaces
  "the entire remediation loop" in section 8 with "the entire correction loop"; names in clause
  3.2 and clause 3.5 the substitutes a mechanism gap allows; and, since run 56, rewrites clause
  3.1's paragraph on the two bounds, which now opens "The two bounds settle how wide the [Class]
  is drawn, not at which level of abstraction." The question set, key and fixture are as at
  48f6e7c; the key differs from c31d49a only in its 2c quotations following the text.

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

  - the prompt (sha256 `d4ab496502da78593bf6dbc821eb8de904b0318ceee3969c359dfa55c79fba46`) is
    byte for byte `acceptance/method/QUESTIONS.md`, `SPEC.md` and
    `acceptance/fixtures/remediation-ledger.md` at 48f6e7c, in that order, each preceded by one
    `===== FILE: <name> =====` line, with one blank line between files, rebuilt from the commit
    and compared;
  - each reader's JSON output has `is_error` false and subtype `success`, reports
    `claude-haiku-5-5`, and each sheet is its `result`.

- **Readers set aside**: none. Every answer text is non-empty, no process reported an error, and
  every reader reported the cohort's model.

- **Run within the pull request**: 10. Runs 31 to 52 came before under the earlier rules, and runs
  53 to 56 under these; runs 54 and 55 read the other two documents.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's marking instruction and its agent definition, having seen neither the drafting nor
  the review. It marked against `ACCEPTANCE.md` and `acceptance/method/KEY.md` at 48f6e7c; the
  process files there are identical to those at c31d49a. The instruction also listed
  `acceptance/fixtures/zigpipe.md`; the method question set names
  `fixtures/remediation-ledger.md` and the packet carries that fixture, so that is the one
  marked against. No earlier run record was read for its judgements; run 56 was read for the
  shape of a record only.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 3.1     | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 |
| ------ | ------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | ----------- | ------- | --------- |
| 1      | correct | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 2      | correct | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 3      | correct | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 4      | correct | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |
| 5      | correct | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        |

Every keyed item is five of five. There is no miss, so none whose reasoning quotes the document
and none matching a wrong reading the key names.

### Question 1

Each reader has at least four bullets naming obligations the key lists and none the key marks
wrong. Reader 1: 3.1 (three bullets, counted once), 3.2 with 3.3, 3.4 with section 4, 3.5 with
3.6. Reader 2: 3.1, 3.2 with 3.6, 3.3, 3.4, 3.5 with section 4, section 2's deferred record.
Reader 3: 3.1 (two bullets, counted once), 3.2, 3.3, 3.4 with section 4, 3.5 with 3.6. Reader 4:
3.1 (two bullets, counted once), 3.2 with 3.3, 3.4, 3.5 with 3.6, section 4. Reader 5: 3.1 (two
bullets, counted once), 3.2, 3.3, 3.4 with section 4, 3.5 with 3.6 and section 2's deferred
record. No reader has the fix first, a test as the detector, or an agent baselining.

### Question 2

- **2a**, five of five. Each states the class, the rule, its proof and the sweep in that order,
  with the fixing after the sweep. Readers 1, 2, 3 and 5 quote clause 3.4's "record the total
  [Instance] count before fixing anything"; reader 4 quotes section 2's "MUST be attempted before
  the [Defect] is fixed" and clause 3.1's step 5. Reader 2 adds that the rule does not become
  blocking until every instance is fixed, and reader 4 places the original defect's fix after
  enforcement and documentation; the key marks neither wrong. Reader 5 remarks, inside its 2a
  answer, that section 3 and Appendix A order the fix differently; that is not a question 4
  answer and names no passage.
- **2b**, five of five. Each names the owner, says an agent may not, and quotes section 4's "An
  [Agent] MUST NOT [Baseline], suppress or knowingly leave an [Instance] unfixed on its own
  authority".
- **2c**, five of five. Each states that all six clauses were followed and that the verdict rests
  on reproduction, quoting section 7's conforming-[Remediation] sentence; readers 2, 3, 4 and 5
  also quote "A verdict on a [Remediation] or a [Defence] MUST rest on reproduction".

### Question 3

- **3.1**: one No (reader 3), four Partial; the key accepts any grade.
- **3.2**: five Yes.
- **3.3**: five Yes; reader 4's "Yes (with a caveat)" is a Yes, not a grade given on a condition.
  Readers 1, 3 and 5 grade the inline ignore under 3.4 or 3.5 instead.
- **3.4**: five No, each naming `Report::render()` left unfixed behind the inline ignore.
- **3.5**: five No, each on the inline ignore no recorded decision covers.
- **3.6**: five No, each naming the wiki.
- **Remediation**: five say it does not conform, each naming 3.4, 3.5 and 3.6.
- **Defence**: five say it does not conform, each naming 3.5's uncovered suppression and 3.6.
- **Section 4**: five name the inline ignore on `Report::render()`. Readers 2, 3 and 5 also name
  leaving the wider rule unbuilt; not marked.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                                                                                                                                                                                                                | Clause      | Readers             | Text                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| The lower-bound list item: "That rejection is tested as a [Narrowing] is under clause 3.3: a sentence stating why the [Hazard] cannot arise in the code the wider [Rule] would add" (readers 1, 3, 4); "A [Rule] drawn to the exact value or name found in the [Defect] is the same [Narrowing] however it is spelt" (readers 2, 5); "unless the independent search below has found no other [Instance] and the [Practitioner] records ..." (reader 3) | 3.1         | five: 1, 2, 3, 4, 5 | Untouched; reader 3 sets it against section 4's next-wider list item and clause 3.3's Part B, reader 5 against the [Narrowing] entry, all untouched |
| Section 2, "Attempt rather than pre-judge": "naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search" (reader 2); "in the vocabulary clause 3.1 uses for a search, and recorded where the project's other decisions are enumerable under clause 8.7, not only with the fix" (reader 5)                                                                                               | 2           | two: 2, 5           | Untouched                                                                                                                                           |
| Section 4's list item "Leaving unbuilt the next wider [Rule] ...": "The absence of an [Instance] is the [Practitioner]'s reason not to widen unasked; ..." (reader 1); "because no [Instance] of it exists today", quoted against the lower-bound item (reader 3)                                                                                                                                                                                      | 4           | two: 1, 3           | Untouched                                                                                                                                           |
| "For a [Bundled defence], the project whose entry point demonstrates it is any project the [Toolchain] is genuinely installed into" (reader 2); "clause 3.5 uses '[Bundled defence]' and '[Consuming project]'", not defined in section 1 (reader 4)                                                                                                                                                                                                   | 3.5         | two: 2, 4           | Altered by the change: its sentence naming the substitutes clause 3.2 allows was rewritten                                                          |
| "What to do whilst waiting": "the [Rule] MAY merge at full width with that case recorded as a known [Instance] awaiting the [Owner]"                                                                                                                                                                                                                                                                                                                   | 4           | one: 1              | Untouched; set against the paragraph below                                                                                                          |
| "A [Remediation] MAY be delivered across several changes": "provided the [Rule] does not become [Blocking] until every [Instance] is fixed", quoted against the paragraph above                                                                                                                                                                                                                                                                        | 4           | one: 1              | Altered by the change: "A remediation" became "A [Remediation]"                                                                                     |
| "Fix them all.": "the scale at which that becomes true is tremendous"                                                                                                                                                                                                                                                                                                                                                                                  | 3.4         | one: 3              | Untouched                                                                                                                                           |
| "There are two kinds of gap": "Where that record lives is the [Toolchain]'s own [Conformance] declaration, ... or the [detector specification](DETECTOR-SPEC.md)'s clause 8.1 for a [Detector]", against this document's own clause 8.1; and its "[Rule harness]" and "[Identifier] resolver", not defined in section 1                                                                                                                                | 3.2         | one: 4              | Altered by the change: "a proving harness" became "a [Rule harness]", and the parenthesis naming the substitutes was added                          |
| "[Rules] are software": its "[Rule harness]", not defined in section 1                                                                                                                                                                                                                                                                                                                                                                                 | 3.3, Part C | one: 4              | Altered by the change: "purpose-built [Rule]-testing harnesses" became "a purpose-built [Rule harness]"                                             |
| "**Three of them turn on a judgement this specification deliberately does not close**": what "them" refers to                                                                                                                                                                                                                                                                                                                                          | 3           | one: 5              | Untouched                                                                                                                                           |

Notes, not passages: none. Reader 4's remark that the companion specifications were not supplied
is part of an answer that names passages; see "Points the rules did not settle".

## Findings and where they lie

1. **Clause 3.1, the lower-bound list item**, all five readers. A list item is a paragraph of its
   own; the change altered the paragraph before the list and the paragraph after it, not this
   item, and no reader naming it sets it against a paragraph the change altered. Routed to
   `acceptance/ROUTED.md`; does not block.
2. **Section 2, "Attempt rather than pre-judge"**, readers 2 and 5. Untouched, and neither reader
   sets it against altered text. Routed to `acceptance/ROUTED.md`; does not block.
3. **Section 4, the list item on leaving the next wider [Rule] unbuilt**, readers 1 and 3.
   Untouched; reader 3 sets it against clause 3.1's lower-bound item, also untouched. Routed to
   `acceptance/ROUTED.md`; does not block.
4. **Clause 3.5, the paragraph opening "For a [Bundled defence]"**, readers 2 and 4. Both point at
   its first sentence, which is unchanged, but the change rewrote the paragraph's sentence on the
   substitutes clause 3.2 allows ("allows, for proving under clause 3.3 and for resolution under
   clause 3.6" became "allows for a mechanism gap, the smoke check ... and the [Identifier] that
   can be followed without a resolver"). A paragraph in which the pull request rewords a sentence
   is text the change altered. **Blocks.**

The run 56 finding, clause 3.1's paragraph on the two bounds, was named by no reader in this run.
Of the passages from one reader only, four lie in text the change altered: section 4's
several-changes paragraph (reader 1), and clause 3.2's two-kinds-of-gap paragraph and clause
3.3's "[Rules] are software" paragraph, both on [Rule harness], the link this change added
(reader 4).

## Points the rules did not settle

- **Whether reader 4's third answer names passages or is a note.** It reads "Clause 3.2 and clause
  3.3 use '[Rule harness]' and '[Identifier] resolver', and clause 3.5 uses '[Bundled defence]' and
  '[Consuming project]'. None of these is defined in section 1. They link to the companion
  specifications, which I was not given." `ACCEPTANCE.md` makes a remark that another document
  was not supplied a note, and makes a clause number with a shorter quotation that identifies a
  sentence or paragraph a passage. Each clause number with its term identifies one paragraph, and
  the complaint is that the term is undefined where it is used, so the marker took it as naming
  those three paragraphs. The open-point rule on whether a reader named a passage counts the
  passage, so the direction is the same either way. Finding 4 turns on this.
- **Whether a quotation given in contrast names its paragraph.** Reader 1 quotes section 4's
  several-changes paragraph against "What to do whilst waiting", and reader 3 quotes section 4's
  next-wider list item against clause 3.1's lower bound. Each is a quotation of six or more
  consecutive words, which `ACCEPTANCE.md` says names a passage; counted, which the open-point
  rule also directs. Finding 3 turns on reader 3's.
- **Question 1, bullets on neither list.** Readers 1, 2 and 3 include fixing the original defect
  with a test that reproduces it (section 6 and Appendix A). The key's list neither names nor
  marks it wrong; not counted either way, and recorded as an open point for the key. No mark
  turns on it.

## Process change

Made under the process change of pull request 22 before it merged, at commit c31d49a, named
before the readers started. The process files at 48f6e7c are identical to those at c31d49a; the
key differs only in its 2c quotations following the text.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: met, five of five.
- Restatement and application, all but one reader correct on each keyed item: met, five of five.
- A miss the key says counts against the document: none.
- A passage found confusing by two or more readers, in text the change wrote or altered: one,
  clause 3.5's "For a [Bundled defence]" paragraph. Not met.
- A passage found confusing by two or more readers, elsewhere: three, clause 3.1's lower-bound
  item, section 2's "Attempt rather than pre-judge" and section 4's next-wider list item, routed
  to `acceptance/ROUTED.md`.
- From one reader only: six passages, recorded.

**Verdict: FAIL**, on finding 4 alone.

## Answer sheets

Answer sheets, prompt, command and marker instruction: LINK TO PULL REQUEST COMMENT
