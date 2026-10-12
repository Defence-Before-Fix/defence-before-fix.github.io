# Run 20: DETECTOR-SPEC.md, semantic detectors, second run in pull request 14

- **Document**: DETECTOR-SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  editor's branch `editor/semantic-detectors` at 5b6093f; the question set, key and fixture read
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
  5b6093f, in that order, each preceded by one `===== FILE: <name> =====` line and nothing else
  added.
- **Managed (policy) settings**: none; the machine applies no managed settings and no managed
  settings file is present, as the editor supplied
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. The editor reports none set aside for a cause the sheets cannot
  show; every sheet has answer text, no process reports an error (`is_error` false, subtype
  `success`), and every reported model is the cohort's model
- **Run within the pull request**: 2, counting void runs; run 19, on SPEC.md, was made at the same
  time and does not bear on this document
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with
  the editor's instruction and its agent definition, `.claude/agents/dbf-spec-editor.md`, having
  seen neither the drafting nor the review
- **Verdict**: FAIL

## Marks

| Reader | Q1      | 2a   | 2b   | 2c   | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3  | 5.4 | 6.1  | 6.2 | 6.3 | 7.1 | Section 8 | Kind       | 6.4 | Q4 passages |
| ------ | ------- | ---- | ---- | ---- | --- | --- | --- | --- | --- | ---- | --- | ---- | --- | --- | --- | --------- | ---------- | --- | ----------- |
| 1      | correct | miss | miss | miss | ok  | ok  | ok  | ok  | ok  | miss | ok  | miss | ok  | ok  | ok  | ok        | not marked | ok  | 2           |
| 2      | correct | miss | miss | ok   | ok  | ok  | ok  | ok  | ok  | miss | ok  | miss | ok  | ok  | ok  | ok        | not marked | ok  | 1           |
| 3      | correct | ok   | miss | miss | ok  | ok  | ok  | ok  | ok  | miss | ok  | ok   | ok  | ok  | ok  | ok        | not marked | ok  | 2           |
| 4      | correct | miss | miss | miss | ok  | ok  | ok  | ok  | ok  | miss | ok  | miss | ok  | ok  | ok  | ok        | not marked | ok  | 4           |
| 5      | correct | miss | miss | miss | ok  | ok  | ok  | ok  | ok  | miss | ok  | miss | ok  | ok  | ok  | ok        | not marked | ok  | 2           |

Every miss above is traceable to the text: each one's reasoning quotes the document or states
what a clause requires. No question was left unanswered.

### Question 1

All five restatements name four or more obligations from the key's list (4.1, 4.2, 4.3, 5.1 to
5.4, 6.1 to 6.3, 7.1), and none asserts an obligation the document does not state. Correct, five
of five.

### Question 2

The key's answers state these things, and the key says none of them may be left out:

- 2a: (a) Conformance is satisfying every MUST in sections 4 to 7; (b) judged on evidence; (c) a
  detector that predates the document can conform; (d) the declaration is optional.
- 2b: (a) make the route disableable by configuration, or (b) detectable by a Rule the project can
  write or a mechanical check the Detector documents; (c) the detector is not required to remove or
  forbid it.
- 2c: (a) with the rule; (b) in the installed copy; (c) at a version tracked together; (d) yes,
  reachable offline.

| Reader | 2a                                           | 2b                                                                   | 2c                                     |
| ------ | -------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------- |
| 1      | miss: (b) only in the quotation              | miss: (c) not stated; the means of detection only in the quotation   | miss: (a) not stated (judgement 3)     |
| 2      | miss: (b) and (d) only in the quotation      | miss: (c) not stated; the means of detection only in the quotation   | ok: all four, supported by 6.2 and 6.3 |
| 3      | ok: all four, supported by the 8.1 quotation | miss: (c) not stated; the means of detection only in the quotation   | miss: (c) not stated                   |
| 4      | miss: (d) not stated (judgement 2)           | miss: (c) not stated; the quotation states no key item (judgement 4) | miss: (b) not stated (judgement 3)     |
| 5      | miss: (d) not stated (judgement 2)           | miss: (c) not stated; the quotation states no key item (judgement 4) | miss: (c) not stated                   |

Each miss is traceable: every reader's answer quotes the document in support.

### Question 3

The key's intended verdicts are Yes for every clause but 6.3, which is No; the section 8 verdict
is "does not conform", because 6.3 fails; 6.4 does not change the verdict.

- **5.3, all five readers Partial against Yes.** Each grades 5.3 Partial because the fixture does
  not say the command's output gives the location of `.lintomatic/report.html`. Readers 2, 4 and 5
  state the requirement outright ("the clause requires both halves"; "which the clause requires
  alongside it"; "5.3 requires it to"); reader 1 uses the clause's words "usable summary"; reader
  3 reports the fixture's silence in the row graded against 5.3 (judgement 5). All five are
  traceable to the text.
- **6.1, readers 1, 2, 4 and 5 Partial against Yes.** Each holds that the two bundled identifiers
  printing `No documentation declared` do not resolve to documentation, which each attributes to
  6.1 ("their identifiers resolve to nothing"; "which is not documentation"; "which resolves to no
  documentation"). Traceable. Reader 3 graded Yes.
- **6.3**: No from all five, each citing that one unresolved identifier fails the clause. No reader
  graded it Partial on the grounds that thirty-eight resolve.
- **Section 8**: all five say Lintomatic does not conform and name 6.3 as a failure; readers 1, 2,
  4 and 5 also count their 5.3 and 6.1 Partials, and reader 3 its 5.3 Partial, which repeats those
  misses but does not change the verdict marked here.
- **Kind**: all five say the fixture does not let them name the kind and name none; reader 4 says
  outright that this does not change the verdict. No reader made the verdict turn on the kind, so
  none is marked on it.
- **6.4**: all five say it does not change the verdict, because it is a SHOULD.

### Judgements made in marking

Each takes the stricter reading, the one recording more misses or findings, as `ACCEPTANCE.md`
requires where its rules leave a mark open.

1. **What counts as "its sentence" under question 2.** The rule asks that the answer's sentence
   state each thing the key's answer states and that a quotation support it, so a key item that
   appears only inside the reader's quotation is not stated by the sentence. Where a reader wrote
   two sentences of answer before or between its quotations, both are taken as the answer.
2. **2a (d), readers 4 and 5.** Reader 4 says a detector "can be graded on evidence without its
   maintainer knowing the document", and reader 5 that it is "judged on evidence rather than a
   declaration". Each implies that no declaration is needed; neither says the declaration is
   optional. Marked not stated.
3. **2c (a) and (b), readers 1 and 4.** Reader 1 says the documentation "must ship in the
   installed package, at a version tracked with the rule", which does not say it ships with the
   rule; reader 4 says it "must ship on disk with the rule", which does not say the installed
   copy. Each marked not stated.
4. **2b quotations, readers 4 and 5.** Both quote only "For each one it MUST do at least one of
   two things, and either alone satisfies this clause", which names neither thing and does not say
   that forbidding is not required, so it does not by itself state a key item. A further reason
   for the miss, already a miss on (c). For readers 1 to 4, "make it detectable" without its
   means is also taken as short of (b).
5. **5.3, reader 3.** Its reasoning reports only the fixture's silence on the report's location,
   but it is a grade against clause 5.3 that the clause is partly unmet, and naming the clause a
   case fails attributes a requirement to it. Traceable.
6. **Question 4, a clause named as the context of a confusion.** Readers 1, 3 and 4 explain their
   7.1 confusion by naming clause 4.1 ("Clause 4.1 has the project writing its own rules"; "does
   not fit 4.1's authoring route"; "given 4.1 describes project rules as separate"). Each is taken
   as naming clause 4.1, which covers every sentence of it. Likewise reader 3's "given that the
   declaration is optional" is taken as naming the 8.1 sentence "The declaration is optional.",
   and reader 4's "the table in section 2" as naming that table.
7. **Question 4, single words quoted.** Reader 5's "optional" and "not a condition of" are
   quotations under question 4, and each covers the 8.1 sentence "The declaration is optional."
   or "It is how a maintainer claims Conformance; it is not a condition of it.", the only places
   those words occur.

No re-mark.

## Passages quoted as confusing

Grouped by paragraph, as `ACCEPTANCE.md` defines the same passage.

| Clause and paragraph                                                        | Readers       | Words quoted, verbatim                                                                                                                                                                                                                                                                                                                                                                                       | Blocks |
| --------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| 7.1, first paragraph, the sentence beginning "For each one it MUST"         | 1, 2, 3, 4, 5 | 1, 2: "make the route detectable, by a [Rule] the project can write in the [Detector] itself or by a mechanical check the [Detector] documents." 3, 4, 5: "by a [Rule] the project can write in the [Detector] itself." / "make the route detectable, by a [Rule] the project can write in the [Detector] itself" / "make the route detectable, by a [Rule] the project can write in the [Detector] itself." | Yes    |
| 8.1, first paragraph, the sentence beginning "The same declaration"         | 3, 4, 5       | 3, 4: "a [Detector] that has learnt, from its own checks or from a [Practitioner]'s report under the method's clause 3.2, that it fails a MUST in sections 4 to 7 MUST record that gap alongside the version it declares" (reader 3 with a closing full stop). 5: "a [Detector] that has learnt … that it fails a MUST in sections 4 to 7 MUST record that gap alongside the version it declares."           | Yes    |
| 8.1, second paragraph, "The declaration is optional." and the next sentence | 3, 4, 5       | 4: "The declaration is optional." 5: "optional"; "not a condition of". 3, by description: "given that the declaration is optional" (judgements 6 and 7)                                                                                                                                                                                                                                                      | Yes    |
| 6.1, the paragraph beginning "For a [Bundled rule]", its last sentence      | 1, 4          | 1, 4: "A [Message] that carries its own documentation path resolves that [Message], not the [Identifier]."                                                                                                                                                                                                                                                                                                   | Yes    |
| 4.1, named by clause number                                                 | 1, 3, 4       | No quotation; named as the context of the 7.1 confusion (judgement 6)                                                                                                                                                                                                                                                                                                                                        | Yes    |
| 6.1, the paragraph beginning "For a project's own [Rule]"                   | 4             | "Where the [Identifier] is itself a URL, as method clause 3.6 allows"                                                                                                                                                                                                                                                                                                                                        | No     |
| 1, second paragraph, the sentence beginning "The two are separable"         | 2             | "installed into projects its maintainer will never see"                                                                                                                                                                                                                                                                                                                                                      | No     |
| 2, the terminology table                                                    | 4             | No quotation; "the table in section 2", named as not defining "Message" (judgement 6)                                                                                                                                                                                                                                                                                                                        | No     |

Of these, only the section 2 table lies in text this pull request changed; the passages that block
all lie in text it kept.

## Against the criteria

- **Load-bearing statements (every reader on every one)**: not met. 2a one of five, 2b none of
  five, 2c one of five.
- **Restatement and application (all but one on each keyed item)**: not met. Question 1 five of
  five; 5.3 none of five; 6.1 one of five; every other clause, the section 8 verdict and 6.4 five
  of five.
- **A miss traceable to the text (none)**: not met. Twenty-two, listed per reader above: 2a by
  readers 1, 2, 4 and 5; 2b by all five; 2c by readers 1, 3, 4 and 5; 5.3 by all five; 6.1 by
  readers 1, 2, 4 and 5. Each is a finding.
- **A passage found confusing by two or more (none outstanding)**: not met. Five passages are
  named by two or more readers, as the table above shows.
- **From one reader only**: the 6.1 paragraph on a project's own rule, the section 1 sentence and
  the section 2 table, recorded.

## Findings applied

Applied to the text, never to a question, threshold, fixture or key, in 87536c5, 66301b9 and 3b848c7
(key quotations kept verbatim in 85110c1 and ba8a0bd), after an independent review of each round of
edits. DETECTOR-SPEC.md: 5.3 says what the command's own output must carry, and that where its
summary leaves a finding out it must say where those findings can be read (an obligation change,
recorded in the changelog, so the text says what the key's intended Yes assumed); 6.1 asks for the
resolution mechanism, and missing bundled documentation fails 6.3, with 6.4's Why aligned; 7.1 says
the project writes the detecting rule in the detector itself and the detector need not remove or
forbid the route; 8.1 says what a gap is and that conformance is judged on evidence, with or without
a declaration. Separately, pull request 13 changed how question 2 is marked after this run, so the
misses that rested on judgements 1 to 4 needed no text change. A fresh cohort follows.

## Process change

Made under the process change of pull request 13 before it merged, at commit a695010, named
before the readers started; `ACCEPTANCE.md` and `acceptance/runs/README.md` in this worktree
differ from a695010 only by this pull request's question-set line adding question 2d for SPEC.md,
which does not bear on this document.

## Verdict

FAIL on every blocking criterion. Answer sheets, the readers' prompt and command, and the
marker's instruction: posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090073628), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090074094), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090074397).
