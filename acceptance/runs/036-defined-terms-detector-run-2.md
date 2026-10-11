# Run 36: DETECTOR-SPEC.md, defined terms, second run

- **Document**: DETECTOR-SPEC.md
- **Pull request**: not yet opened; branch `editor/defined-terms` at b1e7145, the commit the
  readers were given. The change is be546ea (Harness renamed Rule harness); the revision after
  [run 32](032-defined-terms-detector-run-1.md) is 681ac42 (a [Message] row in section 2, two
  sentences in clause 5.3 on what the remainder is, a sentence in clause 6.1 putting a missing
  bundled page under 6.3, 6.1's [Message] sentence reworded, and 6.4's Why naming 6.3)
- **Cohort**: five readers, none reused from run 32, model alias `haiku`; every reader reported
  `claude-haiku-5-5` in its JSON output
- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt is byte for byte the question set, the document and the
  fixture at b1e7145, in that order, each preceded by one `===== FILE: <name> =====` line, and
  that each sheet is the `result` of its reader's JSON output (one turn, `is_error` false)
- **Run within the pull request**: 2
- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/detector/KEY.md`
  at b1e7145, with the judgements of run 32
- **Verdict**: FAIL on three passages found confusing by two or more readers. One is the clause
  5.3 text the revision added; two are untouched base text. Every keyed item is five of five.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | 6.4 | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------- |
| 1      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | two         |
| 2      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |
| 3      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | two         |
| 4      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | three       |
| 5      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | No  | Yes | ok        | ok  | one         |

Every grade is the key's intended verdict.

### Question 1

Five of five correct, each with at least four bullets the key lists. None says the detector must
enforce a suppression policy, must declare a version, or must list defences or produce an agent
summary. Reader 2 says declaring is optional.

### Question 2

- **2a**, five of five. Each says every MUST in sections 4 to 7 and that a predating detector can
  conform. Readers 2, 3 and 4 also say the declaration is optional, and readers 1 and 5 grade on
  evidence (run 32's judgement J1).
- **2b**, five of five, each giving disableable or detectable, either alone enough, quoting 7.1.
- **2c**, five of five. Reader 4's sentence gives "live in the installed package and be readable
  offline" and quotes 6.2, without 6.3's "at a version tracked together". Under J1 the question's
  "where" is answered by the installed package. The tracked version is a gloss, and its opposite,
  a website, is what reader 4 rejects in so many words. Read strictly, reader 4 would miss 2c and
  the first criterion would fail too. The verdict is FAIL either way.

### Question 3

Five of five on every item. Run 32's two failing items now hold:

- **5.3**: all five grade Yes, four of them reasoning from the new sentences ("so nothing is left
  out", "not a remainder").
- **6.1**: all five grade Yes; readers 3 and 4 put the two undocumented rules under 6.3, reader 4
  noting that "6.1 says so explicitly".

Reader 1 now grades 7.1. Every reader says Lintomatic does not conform because 6.3 fails, and that
6.4 does not change the verdict.

## Passages quoted as confusing

| Passage                                                                                                                                                                       | Clause | Readers        | Text                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------------- | -------------------------------------------------- |
| "The remainder is any finding the summary leaves out. A summary that prints every finding, ... is not a remainder whose location must be printed."                            | 5.3    | three: 1, 3, 5 | Added by the revision                              |
| "make the route detectable, by a [Rule] the project can write in the [Detector] itself or by a mechanical check the [Detector] documents."                                    | 7.1    | three: 1, 3, 4 | Untouched base                                     |
| "a [Detector] that has learnt ... that it fails a MUST in sections 4 to 7 MUST record that gap alongside the version it declares", set against "The declaration is optional." | 8.1    | two: 2, 4      | Untouched base                                     |
| "This applies to every [Rule] the [Detector] runs, bundled or bespoke; a [Detector] failing 4.1 is graded here on its [Bundled rules]."                                       | 4.2    | one: 4         | Untouched base, in the paragraph the change edited |

Notes on the three blocking passages:

- **5.3, the new sentences.** Readers 1, 3 and 5 all quote them under question 4. Reader 1 calls
  the second sentence an exception to the first and was unsure it applies. Reader 3 says it
  "followed it on one reading" but found the two sentences hard to parse quickly. Reader 5 quotes
  them with no comment. All three readers still graded 5.3 as the key intends. Question 4 asks
  for passages found confusing, and all three put this one forward, so it counts.
- **7.1, "write in the [Detector] itself".** Named by one reader in run 32 and by three in this
  run.
- **8.1, the gap MUST against "The declaration is optional".** Named by one reader in run 32, and
  the revision report left it unchanged.

The [Message] passage that four readers named in run 32 is gone: no reader quotes clause 6.1's
reworded sentence or the section 2 table. No reader quotes the Rule harness entry or any other
sentence the original change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met, five of five
  throughout.
- A wrong answer traceable to the text, none: met.
- A passage found confusing by two or more, none outstanding: not met. Clause 5.3's new
  sentences (three readers) are text the revision added. Clause 7.1's "write in the [Detector]
  itself" sentence (three readers) and clause 8.1's gap MUST set against "The declaration is
  optional" (two readers) are untouched base text.
- From one reader only, recorded: clause 4.2's second sentence.

**FAIL**, on question 4 alone. One blocking passage is text the revision added (5.3). The other
two are untouched base text (7.1 and 8.1). None is in text the change made.
