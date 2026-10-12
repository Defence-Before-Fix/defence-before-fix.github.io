# Run 53: SPEC.md, defined terms, eighth run

- **Document**: SPEC.md

- **Pull request**: [24](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24), opened later from branch `editor/defined-terms`. The
  readers were given commit 8e91f8a, at which the text is returned to the original change,
  be546ea (Remediation defined, Harness renamed Rule harness). The change, read against its merge
  base with `next`, 9e914fe, adds the Remediation terminology entry and its link definition;
  links "remediation" as [Remediation] in clauses 3.1, 3.3, 3.6, sections 4, 5, 6 and 7 and the
  1.1.0 changelog row; replaces "a proving harness" in clause 3.2 and "purpose-built [Rule]-testing
  harnesses" in clause 3.3 with [Rule harness], with a link definition to the detector
  specification; and replaces "the entire remediation loop" in section 8 with "the entire
  correction loop". The question set, key and fixture are as at 8e91f8a.

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

  - the prompt (sha256 `2551669b31dedc45ab0fe09028d3c19ad70a5ea63009d33b6c390d7a02417b09`) is
    byte for byte `acceptance/method/QUESTIONS.md`, `SPEC.md` and
    `acceptance/fixtures/remediation-ledger.md` at 8e91f8a, in that order, each preceded by one
    `===== FILE: <name> =====` line, with one blank line between files;
  - each sheet is the `result` of its reader's JSON output: one turn, `is_error` false, subtype
    `success`.

- **Readers set aside**: none. Every answer text is non-empty, no process reported an error, and
  every reader reported the cohort's model.

- **Run within the pull request**: 8. Runs 31, 35, 38, 41, 44, 47 and 50 came before, under the
  earlier rules.

- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) given the
  editor's marking instruction and its agent definition, having seen neither the drafting nor
  the review. It marked against `ACCEPTANCE.md` and `acceptance/method/KEY.md` at 8e91f8a; the
  process files there are identical to those at c31d49a. No earlier run record was read for its
  judgements.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 3.1     | 3.2 | 3.3     | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 |
| ------ | ------- | --- | --- | --- | ------- | --- | ------- | --- | --- | --- | ----------- | ------- | --------- |
| 1      | correct | ok  | ok  | ok  | No      | Yes | Yes     | No  | No  | No  | ok          | ok      | ok        |
| 2      | correct | ok  | ok  | ok  | No      | Yes | Yes     | No  | No  | No  | ok          | ok      | ok        |
| 3      | correct | ok  | ok  | ok  | Partial | Yes | Partial | No  | No  | No  | ok          | ok      | ok        |
| 4      | correct | ok  | ok  | ok  | Partial | Yes | Yes     | No  | No  | No  | ok          | ok      | ok        |
| 5      | correct | ok  | ok  | ok  | Partial | Yes | Yes     | No  | No  | No  | ok          | ok      | ok        |

Every keyed item is five of five. There is no miss, so none whose reasoning quotes the document
and none matching a wrong reading the key names.

### Question 1

Each reader has at least four bullets naming obligations the key lists and none the key marks
wrong. Reader 1: 3.1, 3.2 with 3.3, 3.4 with section 4, 3.5 with 3.6, and section 2's deferred
record. Reader 2: 3.1 (three bullets, counted once), 3.2 with 3.6, 3.3 with 3.4, 3.5 with section 4
and the deferred record. Reader 3: 3.1, 3.2 with 3.3, 3.4 with section 4, 3.5 with 3.6, the
deferred record. Reader 4: 3.1, 3.2 with 3.3, 3.4, 3.5 with 3.6, section 4. Reader 5: 3.1, 3.2,
3.3, 3.4 with 3.5, 3.6 with section 4. No reader has the fix first, a test as the detector, or an
agent baselining.

### Question 2

- **2a**, five of five. Reader 1 names the six clauses by number in order, quoting section 3's
  "Six clauses, in order." and clause 3.4's MUST sentence. Readers 2, 3, 4 and 5 state the class,
  the rule, its proof and the sweep in that order with the fix after, each quoting clause 3.4's
  "record the total [Instance] count before fixing anything" and section 2's "MUST be attempted
  before the [Defect] is fixed".
- **2b**, five of five. Each names the owner, says an agent may not, and quotes section 4's "An
  [Agent] MUST NOT [Baseline], suppress or knowingly leave an [Instance] unfixed on its own
  authority". Reader 2 adds the default owner for a project that recorded none, which the key
  accepts.
- **2c**, five of five. Each states that all six clauses were followed and that the verdict rests
  on reproduction, quoting section 7's conforming-[Remediation] sentence; readers 1, 2, 3, 4 and 5
  also quote "A verdict on a [Remediation] or a [Defence] MUST rest on reproduction".

### Question 3

- **3.1**: two No, three Partial; the key accepts any grade.
- **3.2**: five Yes.
- **3.3**: four Yes; reader 3 Partial, attributing the inline ignore on `Report::render()` to this
  clause, which meets the key's condition.
- **3.4**: five No, each naming `Report::render()` left unfixed behind the inline ignore.
- **3.5**: five No, each on the inline ignore no recorded decision covers.
- **3.6**: five No, each naming the wiki or the documentation not versioned with the rule.
- **Remediation**: five say it does not conform, each naming 3.4, 3.5 and 3.6 among the clauses
  not followed.
- **Defence**: five say it does not conform, each naming 3.5's uncovered suppression and 3.6.
- **Section 4**: five name the inline ignore on `Report::render()`. Readers 1, 2 and 4 also name
  leaving the wider rule unbuilt, which is not marked.

## Passages named under question 4

| Passage                                                                                                                                                                                                                                                                                                                        | Clause      | Readers        | Text                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | -------------- | ------------------------------------------------------------------------------------------- |
| The paragraph opening "For a [Bundled defence], the project whose entry point demonstrates it is any project the [Toolchain] is genuinely installed into": reader 2 and reader 3 quote its first sentence, reader 3 also "The substitutes clause 3.2 allows, for proving under clause 3.3 and for resolution under clause 3.6" | 3.5         | two: 2, 3      | Untouched; reader 3 sets it against clause 3.2 (below)                                      |
| Section 2, "Attempt rather than pre-judge": "naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search"                                                                                                                                                        | 2           | three: 3, 4, 5 | Untouched                                                                                   |
| Section 4's list item "Leaving unbuilt the next wider [Rule] ... rejected because no [Instance] of it exists today rather than because the [Hazard] cannot arise there"                                                                                                                                                        | 4           | two: 1, 4      | Untouched; reader 1 sets it against clause 3.1's lower bound, untouched                     |
| The lower-bound list item: "unless the independent search below has found no other [Instance] and the [Practitioner] records that the [Class] is genuinely singular today", and "A [Rule] drawn to the exact value or name found in the [Defect] is the same [Narrowing] however it is spelt"                                  | 3.1         | one: 1         | Untouched                                                                                   |
| "Fix them all.": "the scale at which that becomes true is tremendous"                                                                                                                                                                                                                                                          | 3.4         | one: 1         | Untouched                                                                                   |
| The [Owner] entry: "Whoever holds authority over a project's [Exceptions] and [Calibrations]", with the default-owner sentence described                                                                                                                                                                                       | 1 (Owner)   | one: 2         | Untouched                                                                                   |
| Section 4's lead-in, "Decisions that MUST go to whoever owns the codebase", given by clause number and description                                                                                                                                                                                                             | 4           | one: 2         | Untouched                                                                                   |
| "Those belong to whoever owns the codebase"                                                                                                                                                                                                                                                                                    | Appendix A  | one: 2         | Untouched                                                                                   |
| "Then the proof, which runs the other way round, and both ways.", with "Where the narrower shape was chosen from the outset and no wider [Rule] was ever built"                                                                                                                                                                | 3.3, Part B | one: 2         | Untouched                                                                                   |
| "There are two kinds of gap": "uses the substitutes clauses 3.3 and 3.6 already allow"                                                                                                                                                                                                                                         | 3.2         | one: 3         | Altered by the change: "a proving harness" became "a [Rule harness]" in the sentence quoted |
| Clause 3.4's opening MUST sentence, by description: "clause 3.4 says to fix every instance after the sweep"                                                                                                                                                                                                                    | 3.4         | one: 3         | Untouched                                                                                   |
| "Only then fix the original [Defect] in the normal way"                                                                                                                                                                                                                                                                        | Appendix A  | one: 3         | Untouched                                                                                   |
| "'the [Rule] found nothing the reading had missed' is one technique and a [Rule] run, not two techniques"                                                                                                                                                                                                                      | 3.1         | one: 5         | Untouched                                                                                   |
| "Accepting a known [Instance] as unfixed for any reason"                                                                                                                                                                                                                                                                       | 4           | one: 5         | Untouched                                                                                   |
| "What to do whilst waiting": "the [Rule] MAY merge at full width with that case recorded as a known [Instance] awaiting the [Owner]"                                                                                                                                                                                           | 4           | one: 5         | Untouched                                                                                   |

Notes, not passages: reader 2 says [Bundled defence] and [Consuming project] link to
TOOLING-SPEC.md, which it was not given; reader 3 says [Bundled defence] appears in the link
definitions but not in the terminology. Both readers also quote the 3.5 paragraph, so it is named
by each.

## Findings and where they lie

1. **Clause 3.5, the [Bundled defence] paragraph**, readers 2 and 3. The paragraph is not one the
   change altered. Reader 3 sets its sentence "The substitutes clause 3.2 allows, for proving under
   clause 3.3 and for resolution under clause 3.6" against clause 3.2's "uses the substitutes
   clauses 3.3 and 3.6 already allow", in the paragraph "There are two kinds of gap", in which the
   change replaced "a proving harness" with "a [Rule harness]" and its link. A finding in a
   paragraph a reader naming it sets against such a paragraph lies in text the change altered.
   **Blocks.**
2. **Section 2, "Attempt rather than pre-judge"**, readers 3, 4 and 5. Untouched by the change,
   and no reader sets it against a paragraph the change altered. Routed to
   `acceptance/ROUTED.md`; does not block.
3. **Section 4, the list item on leaving the next wider [Rule] unbuilt**, readers 1 and 4. Reader
   1 quotes it whilst setting clause 3.1's lower-bound item against it; reader 4 quotes it directly.
   Untouched, and the lower-bound item it is set against is untouched. Routed to
   `acceptance/ROUTED.md`; does not block.

Every other passage above is from one reader only: recorded, applied at the editor's discretion.

## Points the rules did not settle

- **Question 1, bullets on neither list.** Readers 1, 2, 3 and 4 each include, in a bullet that
  also names a listed obligation, fixing the original defect with a test that reproduces it
  (sections 6 and Appendix A), which the key's list neither names nor marks wrong. As the rule
  says, that assertion is not counted either way; it is recorded as an open point for the key.
  No mark turns on it.
- **Where finding 1 lies.** No open point is needed: reader 3's second item sets the 3.5 sentence
  against the 3.2 sentence directly. Reader 3's first item also sets the 3.5 paragraph against the
  link-definition block, to which the change added `[rule harness]` and `[remediation]`; whether
  that block is a paragraph is not settled by `ACCEPTANCE.md`, and the verdict does not rest on it.

## Process change

Made under the process change of pull request 22 before it merged, at commit c31d49a, named
before the readers started. The process files at 8e91f8a are identical to those at c31d49a.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, every reader correct on every item: met, five of five.
- Restatement and application, all but one reader correct on each keyed item: met, five of five.
- A miss the key says counts against the document: none.
- A passage found confusing by two or more readers, in text the change wrote or altered: one, the
  clause 3.5 [Bundled defence] paragraph, set by reader 3 against the 3.2 paragraph the change
  altered. Not met.
- A passage found confusing by two or more readers, elsewhere: two, section 2's "Attempt rather
  than pre-judge" and section 4's wider-[Rule] list item, routed to `acceptance/ROUTED.md`.
- From one reader only: twelve passages, recorded.

**Verdict: FAIL**, on finding 1 alone.

## Answer sheets

Posted on the pull request: [answer sheets](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125395288); [command, models, marker instruction and agent definition](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125394821); the prompt, [part 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125395713) and [part 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/24#issuecomment-6125396060).
