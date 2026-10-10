# Run 32: DETECTOR-SPEC.md, defined terms, first run

- **Document**: DETECTOR-SPEC.md
- **Pull request**: not yet opened; branch `editor/defined-terms` at 35f42bf, the commit the
  readers were given (be546ea renames Harness to Rule harness in the terminology entry, the
  section 3 table, clause 4.2 and clause 8.1, and says the term never means an agent's
  environment)
- **Cohort**: five readers, model alias `haiku`; every reader reported `claude-haiku-5-5` in its
  JSON output
- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt is byte for byte the question set, the document and the
  fixture at 35f42bf, in that order, each preceded by one `===== FILE: <name> =====` line, and
  that each sheet is the `result` of its reader's JSON output (one turn, `is_error` false)
- **Run within the pull request**: 1
- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/detector/KEY.md`
  at 35f42bf
- **Verdict**: FAIL on application items 5.3 and 6.1, on misses traceable to the text, and on
  one passage found confusing by four readers. None of them is in text this change touched.

## Marks

| Reader | Q1      | 2a  | 2b  | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3             | 5.4 | 6.1             | 6.2 | 6.3 | 7.1        | Section 8 | 6.4 | Q4 passages |
| ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --------------- | --- | --- | ---------- | --------- | --- | ----------- |
| 1      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Partial, miss T | Yes | Partial, miss T | Yes | No  | not graded | ok        | ok  | one         |
| 2      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Partial, miss T | Yes | Yes             | Yes | No  | Yes        | ok        | ok  | two         |
| 3      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Partial, miss T | Yes | Yes             | Yes | No  | Yes        | ok        | ok  | three       |
| 4      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Partial, miss T | Yes | Partial, miss T | Yes | No  | Yes        | ok        | ok  | one         |
| 5      | correct | ok  | ok  | ok  | Yes | Yes | Yes | Yes | Yes | Partial, miss T | Yes | Partial, miss T | Yes | No  | Yes        | ok        | ok  | two         |

`T` marks a miss whose reasoning quotes or states what the document requires.

### Question 1

Five of five correct. Every sheet has at least four bullets naming obligations the key lists, and
none says the detector must enforce a suppression policy, must declare a version, or must list
defences or produce an agent summary. Reader 5's sixth bullet, that a detector conforms when it
meets every MUST in sections 4 to 7, is section 8 and is not wrong.

### Question 2

- **2a**, five of five. All five say a detector conforms when it satisfies every MUST in sections
  4 to 7, and that one written before the document can conform, quoting clause 8.1's "MAY be
  graded [Conforming] on evidence by anyone who exercises the clauses above against it". Readers
  2, 3 and 4 say the grade rests on evidence and not on a declaration; readers 1 and 5 do not
  mention the declaration (judgement J1). None says a declaration is required or that partial
  satisfaction is conformance.
- **2b**, five of five. All five give disableable by configuration or detectable, either alone
  enough, quoting clause 7.1; none says the route must be forbidden or must take a reason.
- **2c**, five of five. All five give the installed copy, shipped with the rule at a version
  tracked together, and offline, quoting clauses 6.2 and 6.3; none names a website.

### Question 3

The key's intended verdicts are Yes for every clause but 6.3, which is No.

- **5.3, none of five.** All five grade Partial because the fixture does not say that the
  command's output gives the location of `.lintomatic/report.html`, and clause 5.3 says "the
  invoked command's own output MUST carry both a usable summary and the location of the
  remainder" (reader 1: "The clause requires both halves"; reader 4: "the output must carry both
  halves"). Each reasoning states what the clause requires, so each miss is traceable to clause
  5.3's second sentence. The key's Yes rests on the one-line form being printed whether or not
  the report is enabled, and does not address that sentence; that is for the editor, since a
  key is corrected only where it misquoted the document and a fixture is never changed to let a
  run pass.
- **6.1, two of five** (readers 2 and 3, Yes). Readers 1, 4 and 5 grade Partial because two
  bundled identifiers print "No documentation declared", which reader 1 calls "not a resolution"
  and reader 5 says is "not resolution"; each reads clause 6.1 as requiring every identifier to
  resolve to documentation, where the key reads it as requiring the mechanism and puts the two
  rules under 6.3. Each is traceable.
- **7.1, four of five.** Reader 1's table stops at 6.3 and grades no 7.1. An item left unanswered
  is a miss with no reasoning, so it is not traceable (judgement J2).
- **Section 8**: five of five say Lintomatic does not conform, each naming 6.3; readers 1, 4 and
  5 also count their 5.3 and 6.1 Partials, which repeats those misses.
- **6.4**: five of five say it does not change the verdict, because it is a SHOULD.

### Judgements made in marking

`ACCEPTANCE.md` at the base gives the key and the thresholds and leaves these open.

- **J1. Which elements of the key's answer to question 2 a sentence must state.** Every element
  that answers a part of the question must be stated; an element the key adds as a gloss is met
  unless the answer asserts its opposite. 2a asks what conforming means and whether a detector
  that predates the document can conform; readers 1 and 5 answer both, and the key's wrong
  answers on the declaration are ones that say it is required, which neither does. 2b's "not
  required to remove or forbid" is met in the same way by "either alone is enough". On the
  stricter reading readers 1 and 5 would miss 2a, failing the first criterion as well; the
  verdict is FAIL either way.
- **J2. An unanswered item** is one miss and not traceable, since there is no reasoning to quote
  the document.
- **J3. The same passage under question 4** is the same sentence, as run 16 counted it. Read by
  paragraph instead, readers 2 and 3 would share a second passage, clause 8.1's paragraph
  beginning "The declaration is optional", which would also block; the verdict does not turn on
  it.

## Passages quoted as confusing

| Passage                                                                                                                                    | Clause | Readers          | Changed by this pull request                    |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ---------------- | ----------------------------------------------- |
| "A [Message] that carries its own documentation path resolves that [Message], not the [Identifier]."                                       | 6.1    | four: 2, 3, 4, 5 | No                                              |
| "make the route detectable, by a [Rule] the project can write in the [Detector] itself or by a mechanical check the [Detector] documents." | 7.1    | one: 1           | No                                              |
| "The declaration is optional." set against "a Detector that has learnt ... MUST record that gap alongside the version it declares."        | 8.1    | one: 2           | No                                              |
| "a [Detector] failing 4.1 is graded here on its [Bundled rules]."                                                                          | 4.2    | one: 3           | No; the sentence before it in the paragraph was |
| "MAY be graded [Conforming] on evidence by anyone who exercises the clauses above against it."                                             | 8.1    | one: 3           | No; the last sentence of its paragraph was      |
| "Terms from the method specification carry over unchanged."                                                                                | 2      | one: 5           | No                                              |

All four readers of the 6.1 sentence say the same thing: [Message] is a method-specification term
that this document's section 2 table does not gloss, and its definition was not in what they were
given. Reader 5's section 2 note is the same point from the other end. No reader quoted the Rule
harness entry, its new sentence on the word *harness*, or any other sentence the change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met. 2a, 2b and 2c five of five.
- Restatement and application, at least four of five on each keyed item: not met. 5.3 none of
  five and 6.1 two of five; 7.1 four of five; every other item five of five.
- A wrong answer traceable to the text, none: not met. 5.3 for all five readers and 6.1 for
  readers 1, 4 and 5, each a finding.
- A passage found confusing by two or more, none outstanding: not met. Clause 6.1's [Message]
  sentence, four readers.
- From one reader only, recorded: the five other passages above.

**FAIL.** No failure traces to text this pull request changed: clauses 5.3 and 6.1 and the 6.1
[Message] sentence are untouched by it. The [Message] passage is, though, a defined-terms point of
the kind this pull request is about: a borrowed term the section 2 table does not gloss.
