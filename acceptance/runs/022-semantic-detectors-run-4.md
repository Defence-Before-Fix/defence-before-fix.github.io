# Run 22: DETECTOR-SPEC.md, semantic detectors, fourth run in pull request 14

- **Document**: DETECTOR-SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  editor's branch `editor/semantic-detectors` at 3aefdd1; the question set, key and fixture read
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
  3aefdd1, in that order, each preceded by one `===== FILE: <name> =====` line, with the files
  separated by one blank line and nothing else added (judgement 11)
- **Managed (policy) settings**: none; the machine applies no managed settings and no managed
  settings file is present, as the editor supplied
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. The editor reports none set aside for a cause the sheets cannot
  show; every sheet has answer text, no process reports an error (`is_error` false, subtype
  `success`), and every reported model is the cohort's model
- **Run within the pull request**: 4, counting void runs; run 21, on SPEC.md, was made at the same
  time and does not bear on this document
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with
  the editor's instruction and its agent definition, `.claude/agents/dbf-spec-editor.md`, having
  seen neither the drafting nor the review

## Marks

| Reader | Q1      | 2a   | 2b   | 2c   | 4.1 | 4.2 | 4.3 | 5.1 | 5.2 | 5.3 | 5.4 | 6.1 | 6.2 | 6.3 | 7.1 | Section 8 | Kind       | 6.4 | Q4 passages |
| ------ | ------- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ----------- |
| 1      | miss    | miss | miss | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 3           |
| 2      | correct | miss | miss | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 1           |
| 3      | correct | ok   | miss | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 3           |
| 4      | miss    | ok   | miss | ok   | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 2           |
| 5      | miss    | miss | miss | miss | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok  | ok        | not marked | ok  | 3           |

Every miss under question 2 is traceable to the text: each answer quotes the document in support.
The three misses under question 1 are the readers' own: the bullet each turns on quotes nothing.
No question was left unanswered.

### Question 1

Every restatement names four or more obligations from the key's list. Readers 2 and 3 assert no
obligation the document does not state: correct. Readers 1, 4 and 5 each have a bullet that
requires every finding in the command's own output: reader 1, "the command's own output carries
every finding"; reader 4, "put every finding in the command's own output"; reader 5, "put each
finding and its identifier in the command's own output". Clause 5.3 requires a usable summary
and, where the summary leaves a finding out, a statement of where the rest can be read; printing
every finding is one way to meet it, not the obligation. Each is marked a bullet asserting an
obligation the document does not state, so incorrect (judgement 2). Correct, two of five.

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

| Reader | 2a                                                                                          | 2b                                 | 2c                                                                  |
| ------ | ------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------- |
| 1      | miss: (d) not stated (judgement 3)                                                          | miss: (c) not stated (judgement 4) | ok: all four, (c) from the 6.3 quotation                            |
| 2      | miss: (d) not stated (judgement 3); (a) as "the evidence against the MUSTs", not every MUST | miss: (c) not stated (judgement 4) | ok: all four, (c) from the 6.3 quotation                            |
| 3      | ok: all four; (d) as "rests on evidence rather than on the detector's claim"                | miss: (c) not stated (judgement 4) | ok: all four, from the sentence and the 6.2 and 6.3 headings quoted |
| 4      | ok: all four; (d) as "judged on evidence rather than on any claim it makes"                 | miss: (c) not stated (judgement 4) | ok: all four                                                        |
| 5      | miss: (d) not stated (judgement 3)                                                          | miss: (c) not stated (judgement 4) | miss: (a) and (c) not stated; only 6.2 quoted (judgement 6)         |

No answer asserts anything the document does not state or that the key says makes an answer
wrong: none says a declaration is required, that partial satisfaction is conformance, that the
detector must forbid the route or require a reason, or that a website will do.

### Question 3

The key's intended verdicts are Yes for every clause but 6.3, which is No; the section 8 verdict
is "does not conform", because 6.3 fails; 6.4 does not change the verdict.

- **Every clause**: all five readers give the intended verdict on every clause, 4.1 to 7.1. On
  6.3 each cites that one unresolved identifier fails the clause; no reader grades it Partial on
  the grounds that thirty-eight resolve. On 5.3 and 6.1, the clauses run 20 failed on, all five
  grade Yes.
- **Section 8**: all five say Lintomatic does not conform, because 6.3 fails.
- **Kind**: all five say the fixture does not let them name the kind and name none, so none is
  marked on it. Reader 1 calls its verdict "incomplete on that point" but does not make the
  verdict turn on the kind; readers 3 and 5 say outright that it does not change the verdict.
- **6.4**: all five say it does not change the verdict, because it is a SHOULD. Reader 1 adds that
  whether 6.4 applies as a MUST depends on whether Lintomatic ships inside a Toolchain, which does
  not alter its answer.

### Judgements made in marking

01. **How an open judgement is made.** `ACCEPTANCE.md` at 204f95b says an open judgement is made
    as a careful reader of the document would; the editor's instruction asks for the stricter
    reading wherever the rules leave a judgement open. Each judgement below is made as a careful
    reader would, and where a careful reader could take either reading, the stricter one, the one
    recording more misses or findings, is taken and the judgement says so.
02. **Question 1, "every finding" in the output, readers 1, 4 and 5.** The heading of 5.3 speaks
    of "the result", which a reader may take as every finding, but its body requires only a
    summary and a pointer to what the summary leaves out. A careful reader could read these bullets
    as a compression of 5.3 or as an obligation it does not state; the stricter reading is taken,
    and each is marked incorrect.
03. **2a (d), the declaration optional.** The question's second part asks whether a detector that
    has never heard of the document can conform; the key answers it with both (c) and (d), so (d)
    is an element that answers a part of the question. Its gist is that conformance does not depend
    on a declaration or claim. Readers 3 and 4 say the grade rests on evidence rather than on the
    detector's claim, which the document calls the declaration's purpose ("it is how they claim
    [Conformance]"), and so state it. Readers 2 and 5 say only that the detector is judged on
    evidence; reader 1 says it is judged "not on whether its maintainer has heard of the document".
    Each of the three, with the 8.1 quotation all five give, implies that no declaration is needed
    without saying so; a careful reader could go either way, and the stricter reading is taken.
04. **2b (c), not required to remove or forbid.** The question asks what the detector must do
    about the route, and the key's answer includes what it need not do, so (c) answers the
    question. All five say either of the two things alone is enough. That entails that nothing
    further is required but does not say that the route may stay; a careful reader could go either
    way, and the stricter reading is taken. Marked not stated, as run 20 marked it.
05. **2b (b), the means of detection.** Clause 7.1 defines "Detectable" in its own text, and each
    reader uses "detectable", or reader 4 "findable", in that sense, so (b) is stated: a defined
    term used in its defined sense states what it means. It decides no mark, since every 2b answer
    misses (c).
06. **2c, reader 5.** Its sentence says the documentation "lives in the installed package" and its
    only quotation is 6.2. Neither says the documentation ships with the rule nor that it is
    versioned with it. Element (c) answers where the documentation must live, as part of the key's
    answer to that part; not stated. Whether "in the installed package" carries (a) is open, and
    the stricter reading is taken.
07. **Question 4, a clause number inside a quotation.** Readers 1 to 4 quote the 7.1 sentence that
    contains "of the kind clause 4.1 requires it to host". The clause number is part of the quoted
    run, so it covers the 7.1 sentence; it is not a passage named by clause number and does not
    cover clause 4.1.
08. **Question 4, reader 4's "in the [Detector]".** Taken as one run, these words occur in the 7.1
    sentence and, on the stricter reading, in the 6.3 Why sentence "If its documentation lives only
    in the [Detector]'s repository or on its website, ...", where the following word is
    "[Detector]'s". The quotation is taken to cover both. The second blocks nothing.
09. **Question 4, a passage quoted only to set another against it.** Reader 1 quotes the 8.1
    sentence "A declaration with a non-empty gap record ..." as what it read the other 8.1 sentence
    against. A quotation under question 4 counts whatever it is quoted for, so it is recorded.
10. **The fourth row's "earlier passage".** Read as a passage named by two or more readers in an
    earlier run of this document in this pull request, which is run 20 at 5b6093f. Run 20's
    single-reader passages, the 6.1 paragraph on a project's own rule, the section 1 sentence and
    the section 2 table, are covered by no passage this cohort names, so the stricter reading would
    change nothing.
11. **The packet's blank lines.** The prompt joins the three files with one blank line between
    each file's end and the next file's header. A blank line adds nothing for a reader to read,
    every reader received the same packet, and a packet's form is not a cause in `ACCEPTANCE.md`
    for setting a reader aside, so no reader is set aside for it.

No re-mark.

## Passages quoted as confusing

Grouped by paragraph, as `ACCEPTANCE.md` defines the same passage. A passage blocks when two or
more readers name it, or when it covers a sentence of a paragraph in which one of run 20's
blocking passages lay, as that paragraph reads at 3aefdd1.

| Clause and paragraph                                                                       | Readers    | Words quoted, verbatim                                                                                                                                                                                                                                                                                                                                                                                                                                        | Blocks                                        |
| ------------------------------------------------------------------------------------------ | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| 7.1, first paragraph, the sentence beginning "Detectable means"                            | 1, 2, 3, 4 | 1, 2, 4: "Detectable means the project can find every use of the route, either with a [Rule] the project writes itself in the [Detector], of the kind clause 4.1 requires it to host, or with a mechanical check the [Detector] documents." 3: "either with a [Rule] the project writes itself in the [Detector], of the kind clause 4.1 requires it to host, or with a mechanical check the [Detector] documents." 4 also: "in the [Detector]" (judgement 8) | Yes: four readers, and run 20's 7.1 paragraph |
| 8.1, first paragraph, its last sentence                                                    | 1          | "A declaration with a non-empty gap record is a statement of where the [Detector] stands and is not a claim of [Conformance]." (judgement 9)                                                                                                                                                                                                                                                                                                                  | Yes: run 20's 8.1 first paragraph             |
| 8.1, second paragraph, the sentence beginning "The declaration is for"                     | 1          | "The declaration is for the maintainer: it is how they claim [Conformance] and record the gaps they know of."                                                                                                                                                                                                                                                                                                                                                 | Yes: run 20's 8.1 second paragraph            |
| 6.1, the paragraph beginning "For a [Bundled rule]"                                        | 3          | "A documentation path printed inside the [Message] does not meet this."                                                                                                                                                                                                                                                                                                                                                                                       | Yes: run 20's 6.1 paragraph on a bundled rule |
| 6.1, the paragraph beginning "In both", the sentence beginning "Where the mechanism works" | 5          | "Where the mechanism works but a [Bundled rule]'s [Identifier] has no documentation to resolve to, that fails clause 6.3, not this clause."                                                                                                                                                                                                                                                                                                                   | No                                            |
| 5.3, its paragraph, the sentence beginning "Output that prints"                            | 3          | "Output that prints every finding so meets this clause."                                                                                                                                                                                                                                                                                                                                                                                                      | No                                            |
| 6.4, the Why paragraph                                                                     | 5          | "the [toolchain specification]'s self-audit makes this check a MUST for the [Toolchain]."                                                                                                                                                                                                                                                                                                                                                                     | No                                            |
| 8, the paragraph beginning "A verdict on a [Detector] MUST also name"                      | 5          | "the kind of each configuration it grades"; "the one the [Detector] has without any hosted service or licence tier"                                                                                                                                                                                                                                                                                                                                           | No                                            |
| 6.3, the Why paragraph, the sentence beginning "If its documentation lives"                | 4          | "in the [Detector]" (judgement 8)                                                                                                                                                                                                                                                                                                                                                                                                                             | No                                            |

No reader names clause 4.1, the fifth of run 20's blocking passages (judgement 7).

## Against the criteria

- **Load-bearing statements (every reader on every one)**: not met. 2a three of five correct
  (readers 3 and 4), 2b none of five, 2c four of five (all but reader 5).
- **Restatement and application (all but one on each keyed item)**: not met. Question 1 two of
  five; every clause of question 3, the section 8 verdict and 6.4 five of five.
- **A miss traceable to the text (none)**: not met. Nine, each a finding: 2a by readers 1, 2 and
  5; 2b by all five; 2c by reader 5.
- **A passage found confusing by two or more (none outstanding)**: not met. The 7.1 sentence
  defining "Detectable" is named by four readers; and run 20's blocking passages in 7.1's first
  paragraph, 8.1's first and second paragraphs and 6.1's paragraph on a bundled rule are still
  outstanding, since this cohort names passages that cover sentences of each of those paragraphs.
- **From one reader only**: the 6.1 sentence on a mechanism that works without documentation, the
  5.3 sentence on output that prints every finding, the 6.4 Why sentence, the section 8 paragraph
  on kind and the 6.3 Why sentence, recorded.

**Editor's note on the marker's instruction.** The instruction for this run asked for the stricter
reading wherever the rules leave a judgement open, which the process at 204f95b had replaced with
the judgement of a careful reader. The verdict does not turn on it: the findings that fail the run
rest on rules, not on those judgements.

## Findings applied

Applied to the text, never to a question, threshold, fixture or key, in 72f1679 and the commit after
it that settles a review of those edits (key quotations kept verbatim in c5bfd10). DETECTOR-SPEC.md:
7.1 says in its first sentence that the detector need not remove or forbid the route, and defines
detectable in short sentences; 8.1's two paragraphs and 6.1's sentence on a documentation path
inside a Message are shorter and plainer; section 8 says conformance is judged on the evidence and a
declaration is optional; 5.3 says the output need not print every finding if it says where the rest
can be read. A fresh cohort follows.

## Process change

Made under the process change of pull request 13 before it merged, at commit 204f95b, named
before the readers started; `ACCEPTANCE.md` and `acceptance/runs/README.md` in this worktree
differ from 204f95b only by this pull request's question-set line adding question 2d for SPEC.md,
which does not bear on this document.

## Verdict

FAIL on every blocking criterion. Answer sheets, the readers' prompt and command, and the
marker's instruction: posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090466450), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090466829), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090467103).
