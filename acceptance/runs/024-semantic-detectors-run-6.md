# Run 24: DETECTOR-SPEC.md, semantic detectors, sixth run in pull request 14

- **Document**: DETECTOR-SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  editor's branch `editor/semantic-detectors` at 0b8d699; the question set, key and fixture read
  at the same commit
- **Cohort**: five readers, model alias `haiku`; every reader reported `claude-haiku-5-5`, as the
  editor supplied in the cohort's model list and as each reader's own JSON output shows
- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, which only reattaches the session's credential and passes
  arguments through verbatim, in a fresh empty directory made by `mktemp -d` outside any
  repository, with the packet on standard input, with no tools, no settings, no project context
  and no saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt is the question set, the document and the fixture at
  0b8d699, in that order, each preceded by one `===== FILE: <name> =====` line, with the files
  separated by one blank line and nothing else added, the same form as run 22's packet
- **Managed (policy) settings**: none; the machine applies no managed settings and no managed
  settings file is present, as the editor supplied
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. The editor reports none set aside for a cause the sheets cannot
  show; every sheet has answer text, no process reports an error (`is_error` false, subtype
  `success`), and every reported model is the cohort's model
- **Run within the pull request**: 6, counting void runs; run 23, on SPEC.md, was made at the same
  time and does not bear on this document
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with
  the editor's instruction and its agent definition, `.claude/agents/dbf-spec-editor.md`, having
  seen neither the drafting nor the review

## Marks

| Reader | Q1      | 2a   | 2b   | 2c  | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | Kind       | 6.4 | Q4 entries |
| ------ | ------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ---------- |
| 1      | correct | miss | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 1          |
| 2      | correct | ok   | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 1          |
| 3      | miss    | miss | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 2          |
| 4      | correct | ok   | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 2          |
| 5      | correct | miss | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 2          |

"Q4 entries" counts the passages each reader lists under question 4; the words each quotes are in
the table of passages below. Every miss under question 2 is traceable to the text: each answer
quotes the document in support. The miss under question 1 is the reader's own: the bullet it turns
on quotes nothing. No question was left unanswered.

### Question 1

Every restatement names four or more obligations from the key's list. Readers 1, 2, 4 and 5 assert
no obligation the document does not state: correct. Reader 2's "A reason is SHOULD-required"
states 7.2 as the SHOULD it is, and reader 4's "A detector conforms when it meets every MUST in
sections 4 to 7" states section 8's definition, not an obligation; neither is wrong. Reader 5's
"the command's own output must carry a usable summary with each finding's location and
identifier" follows 5.3's own words (judgement 2). Reader 3's fourth bullet says "each finding must
appear in the output of the command the practitioner ran"; clause 5.3 says "The summary need not
list every finding", so the bullet asserts an obligation the document does not state: incorrect
(judgement 2). Correct, four of five.

### Question 2

The key's answers state these elements:

- 2a: (a) Conformance is satisfying every MUST in sections 4 to 7; (b) judged on evidence; (c) a
  detector that predates the document can conform; (d) the declaration is optional.
- 2b: (a) make the route disableable by configuration, or (b) detectable by a Rule the project can
  write or a mechanical check the Detector documents; (c) the detector is not required to remove or
  forbid it.
- 2c: (a) with the rule; (b) in the installed copy; (c) at a version tracked together; (d) yes,
  reachable offline.

Each answer is read as its sentence and its quotation together, for the gist of each element.

| Reader | 2a                                                                                           | 2b                                                                        | 2c                                                             |
| ------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------- |
| 1      | miss: (d) not stated; (b) from the 8.1 quotation (judgement 3)                               | miss: (c) not stated (judgement 4)                                        | ok: all four, (c) from the 6.3 quotation                       |
| 2      | ok: all four; (d) from the section 8 quotation, "a declaration under clause 8.1 is optional" | miss: (c) not stated (judgement 4)                                        | ok: all four, (c) from the 6.3 quotation                       |
| 3      | miss: (d) not stated; (b) from the 8.1 quotation (judgement 3)                               | miss: (c) not stated (judgement 4); (b) by the defined term (judgement 5) | ok: all four, (c) from the 6.3 quotation                       |
| 4      | ok: all four; (d) from the section 8 quotation                                               | miss: (c) not stated (judgement 4); (b) as "findable by the project"      | ok: all four                                                   |
| 5      | miss: (d) not stated (judgement 3)                                                           | miss: (c) not stated (judgement 4)                                        | ok: all four, from the sentence and the 6.3 and 6.2 quotations |

No answer asserts anything the document does not state or that the key says makes an answer
wrong: none says a declaration is required, that partial satisfaction is conformance, that the
detector must forbid the route or require a reason, or that a website will do.

### Question 3

The key's intended verdicts are Yes for every clause but 6.3, which is No; the section 8 verdict
is "does not conform", because 6.3 fails; 6.4 does not change the verdict.

- **Every clause**: all five readers give the intended verdict on every clause, 4.1 to 7.1. On
  6.3 each cites that one unresolved identifier fails the clause; no reader grades it Partial on
  the grounds that thirty-eight resolve. Reader 2 calls the fixture ambiguous on whether the two
  rules are bundled, and grades No either way.
- **Section 8**: all five say Lintomatic does not conform, because 6.3 fails.
- **Kind**: all five say the fixture does not let them name the kind and name none, so none is
  marked on it. Readers 2 and 5 call that part of the verdict incomplete or undetermined but do not
  make the verdict turn on it; readers 3 and 4 say outright that the kind does not change the
  verdict.
- **6.4**: all five say it does not change the verdict, because it is a SHOULD. Reader 1 adds that a
  maintainer declaring a version would record 6.3 and 6.4 under `known-gaps`, although 8.1 defines a
  gap as a failed MUST; reader 3 adds that 6.4 becomes a MUST only inside a Toolchain. Neither aside
  alters the answer marked (judgement 6).

### Judgements made in marking

01. **How an open judgement is made.** As `ACCEPTANCE.md` at 204f95b says, and as the editor's
    instruction asks: as a careful reader of the document would, with the reason stated. Where a
    rule settles a mark, the rule is applied as written, however the result looks.
02. **Question 1, the output bullets of readers 3 and 5.** Clause 5.3 at 0b8d699 says "The summary
    need not list every finding". Reader 3's "each finding must appear in the output" contradicts
    that sentence, and a careful reader takes it as an obligation the document does not state.
    Reader 5's "a usable summary with each finding's location and identifier" repeats the clause's
    "a usable summary, each finding in it with where it is and its [Identifier]", and a careful
    reader takes "each finding" there as each finding in the summary, as the clause does.
03. **2a (d), the declaration optional, readers 1, 3 and 5.** As run 22 held, (d) answers the
    question's second part, whether a detector that has never heard of the document can conform.
    Each of the three quotes the 8.1 sentence that a detector whose maintainer has never read the
    document "MAY be graded [Conforming] on evidence"; none says that a declaration is optional or
    not needed. That no declaration is needed follows from the quotation but is not said by it.
    `ACCEPTANCE.md` names the ways an element is stated: the document's words, a paraphrase, a
    synonym, a defined term in its defined sense. An element reached only by inference from another
    is not among them, and a careful reader of that rule does not add it; this keeps marking
    mechanical, as the question set section asks. Marked not stated. Readers 2 and 4 quote section
    8's "a declaration under clause 8.1 is optional", and so state it.
04. **2b (c), not required to remove or forbid, all five.** As run 22 held, (c) answers what the
    detector must do about the route, from the side of what it need not do. Every reader says, or
    quotes, that either of the two things alone satisfies the clause. That entails that removal or
    forbidding is not required, but does not say it, and 7.1's first sentence, "The [Detector] does
    not have to remove or forbid an inline [Suppression] route", which says it, is quoted by none.
    By the same reasoning as judgement 3, marked not stated.
05. **2b (b), the means of detection.** As in run 22: clause 7.1 defines "Detectable" in its own
    text, and each reader uses "detectable", or reader 4 "findable by the project", in that sense,
    so (b) is stated. It decides no mark, since every 2b answer misses (c).
06. **Asides outside the keyed answer.** Reader 1's statement that 6.4 would be recorded as a known
    gap, and reader 3's on when 6.4 is a MUST, are not keyed items; each sheet's answer to whether
    6.4 changes the verdict is the key's, and is marked so.
07. **Question 4, single words and short runs quoted.** Reader 3 quotes "configuration", "in
    configuration" and "configuration file"; reader 4 quotes "credits"; reader 5 quotes "MAY".
    `ACCEPTANCE.md` says a quotation "of any length" covers every sentence an occurrence of the
    quoted words overlaps, "at every place that run occurs", with letter case ignored. The rule
    settles it: "configuration" covers eight sentences, among them 4.1's first and the 7.1 sentence
    "For each one it MUST do at least one of two things ..."; "MAY" covers nine, among them the 7.1
    sentence "The [Detector] MAY ship them." and the 8.1 sentence beginning "A [Detector] that
    predates". Each place is listed in the table below.
08. **Question 4, a heading.** A heading counts as one sentence; it is taken as its own paragraph,
    not part of the paragraph below it, since it is a separate block of the document. Reader 5's
    "MAY" covers the headings of 6.5, 7.1 and 8.1; none of those decides anything, since the
    paragraphs below 7.1 and 8.1 that block are covered by other sentences.
09. **Question 4, reader 4's closing remark.** "Several clauses also cite method-specification
    clauses (3.2, 3.4, 3.6, 8.1–8.3) and the toolchain specification, which were not in the packet."
    It names clauses of the method specification, not of this document, and says nothing was
    confusing; a careful reader takes it as a remark about the packet, not a passage named. Taken
    otherwise it would add nothing that changes the verdict.
10. **The open passages, and clause 4.1.** The passages runs 20 and 22 found confusing by two or
    more, and not since cleared, are taken as: 7.1's first paragraph; 8.1's first paragraph; 8.1's
    second paragraph; and 6.1's paragraph beginning "For a [Bundled rule]". Clause 4.1, named by
    three readers of run 20, is taken as cleared by run 22: the document's text changed after run
    20 and no reader of run 22 named a passage covering a sentence of 4.1. A careful reader takes
    "until the text is changed" as the document's text, since the same row speaks of "the changed
    document". Read the other way, 4.1 would still be open and outstanding, since reader 3's
    "configuration" covers its first sentence; the verdict does not turn on it.

No re-mark.

## Passages quoted as confusing

Grouped by paragraph, as `ACCEPTANCE.md` defines the same passage. A passage blocks when two or
more readers name it, or when it covers a sentence of a paragraph in which one of the open
passages lay (judgement 10), as that paragraph reads at 0b8d699.

| Clause and paragraph                                                                                  | Readers    | Words quoted, verbatim                                                                                                                                                                                                                                                                                 | Blocks                                                         |
| ----------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| 8, the paragraph beginning "A verdict on a [Detector] MUST also name", its first and second sentences | 1, 3, 4, 5 | 1, 4, 5: "The kind named is the one the [Detector] has without any hosted service or licence tier, as clause 5.4 credits no finding reported only there." 4 also: "credits". 3: "A verdict on a [Detector] MUST also name the kind of each configuration it grades"; and "configuration" (judgement 7) | Yes: four readers                                              |
| 7.1, first paragraph, the sentences "The [Detector] MAY ship them." and "For each one it MUST ..."    | 3, 5       | 3: "configuration", covering "make the route disableable by configuration". 5: "MAY", covering "The [Detector] MAY ship them." (judgement 7)                                                                                                                                                           | Yes: two readers, and the open 7.1 paragraph of runs 20 and 22 |
| 8.1, second paragraph, the sentence beginning "A [Detector] that predates"                            | 5          | "A [Detector] that predates this document, or whose maintainer has never read it, MAY be graded [Conforming] on evidence by anyone who exercises the clauses above against it, and a verdict on any [Detector], declared or not, rests on that exercise and not on the claim." Also "MAY"              | Yes: the open 8.1 second paragraph of runs 20 and 22           |
| 4.1, first paragraph, "Configuration of an existing [Rule] set is not sufficient."                    | 3          | "configuration" (judgement 7)                                                                                                                                                                                                                                                                          | No (judgement 10)                                              |
| 8, second paragraph, its first sentence                                                               | 2          | "Partial [Conformance] MUST NOT be described as [Conformance]."                                                                                                                                                                                                                                        | No                                                             |
| 8, third paragraph, its first sentence                                                                | 2          | "This document defines one level,"                                                                                                                                                                                                                                                                     | No                                                             |
| 4.2, first paragraph, its second sentence                                                             | 3          | "a [Detector] failing 4.1 is graded here on its [Bundled rules]"; "every [Rule] the [Detector] runs, bundled or bespoke"                                                                                                                                                                               | No                                                             |
| 4.3, first paragraph, the sentences ending "configuration file." and "in configuration is not."       | 3          | "configuration"; "in configuration"; "configuration file" (judgement 7)                                                                                                                                                                                                                                | No                                                             |
| 4.3, the table rows for `proj.no-raw-sql` and `rule 7`                                                | 3          | "configuration"; "in configuration"; "configuration file" (judgement 7)                                                                                                                                                                                                                                | No                                                             |
| 2, the terminology table, the row for [Semantic], [Syntactic], [Textual]                              | 3          | "configuration" (judgement 7)                                                                                                                                                                                                                                                                          | No                                                             |
| 6.4, the Why paragraph                                                                                | 4          | "the [toolchain specification](TOOLING-SPEC.md)'s self-audit makes this check a MUST for the [Toolchain]"                                                                                                                                                                                              | No                                                             |
| 1, first paragraph; 2, the definition of [Rule author]; 6.3, first paragraph; 6.5, first paragraph    | 5          | "MAY", each by an occurrence of "MAY" or "May" (judgement 7)                                                                                                                                                                                                                                           | No                                                             |
| The headings of 6.5, 7.1 and 8.1                                                                      | 5          | "MAY" (judgements 7 and 8)                                                                                                                                                                                                                                                                             | No                                                             |

Of the open passages, 8.1's first paragraph and 6.1's paragraph beginning "For a [Bundled rule]"
are cleared: the text of each changed after run 22, and no reader of this cohort names a passage
covering a sentence of either. 7.1's first paragraph and 8.1's second paragraph are still
outstanding. The section 8 paragraph on kind was also named by one reader of run 22.

## Against the criteria

- **Load-bearing statements (every reader on every one)**: not met. 2a two of five correct
  (readers 2 and 4), 2b none of five, 2c five of five.
- **Restatement and application (all but one on each keyed item)**: met. Question 1 four of five;
  every clause of question 3, the section 8 verdict and 6.4 five of five.
- **A miss traceable to the text (none)**: not met. Eight, each a finding: 2a by readers 1, 3 and
  5; 2b by all five.
- **A passage found confusing by two or more (none outstanding)**: not met. The section 8
  paragraph on kind is named by four readers, and 7.1's first paragraph by two; and the open
  passages in 7.1's first paragraph and 8.1's second paragraph are still outstanding, since this
  cohort names passages covering sentences of each.
- **From one reader only**: the section 8 sentences on partial conformance and on one level, the
  4.1, 4.2 and 4.3 passages, the section 2 table row, the 6.4 Why paragraph and the other places
  reader 5's "MAY" covers, recorded.

## Findings applied

Applied to the text, never to a question, threshold, fixture or key, in b172fd6 (key quotations kept
verbatim in 296aad5). DETECTOR-SPEC.md: 8.1's sentence that a detector may be graded on evidence
says the declaration is optional; 7.1's sentence that either means alone satisfies the clause says
neither requires the detector to remove or forbid the route; section 8's paragraph on naming the
kind, 7.1's first paragraph and 8.1's second paragraph are in short, plain sentences. Pull request
13 now limits a question 4 quotation to the place the reader names, so this run's one-word
quotations would no longer reach other passages. A fresh cohort follows.

## Process change

Made under the process change of pull request 13 before it merged, at commit 204f95b, named
before the readers started; `ACCEPTANCE.md` and `acceptance/runs/README.md` in this worktree
differ from 204f95b only by this pull request's question-set line adding question 2d for SPEC.md,
which does not bear on this document.

## Verdict

FAIL on the first, third and fourth criteria. Answer sheets, the readers' prompt and command, and
the marker's instruction: posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090685442), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090685662), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090685883).
