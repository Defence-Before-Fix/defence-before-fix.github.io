# Run 19: SPEC.md, semantic detectors, first run

- **Document**: SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  branch `editor/semantic-detectors` at 5b6093f, the commit the readers were given
- **Cohort**: five readers, model alias `haiku`; each reader reported `claude-haiku-5-5`
- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, which only reattaches the session's credential and passes
  arguments through verbatim, in a fresh empty directory made by `mktemp -d` outside any
  repository, with the packet on standard input; no tools, no settings, no project context.
  Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`
- **Managed settings**: the machine applies no managed (policy) settings to the readers; no
  managed settings file is present
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. Every sheet has answer text, no process reports an error
  (`is_error` false, subtype `success`), and every reader reported the cohort's model. The editor
  reports no reader set aside for a cause the sheets cannot show.
- **Run within the pull request**: 1, counting void runs; runs in the pull request so far: 1
- **Marker**: delegated, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with the
  marking instruction and its agent definition, having seen neither the drafting nor the review.
  It read `ACCEPTANCE.md` and `acceptance/runs/README.md` in this worktree, which differ from
  commit a695010 only by this pull request's question-set line for 2d, and the document, question
  set, key and fixture at 5b6093f. The packet's three files match that commit, apart from one
  blank line between the end of each file and the next file's marker line.

## Marks

`ok` is correct, `miss` is a miss; `T` marks a miss traceable to the text; `J1` and `J2` mark a
miss that rests on the judgement of that name below.

| Reader | Q1      | 2a        | 2b        | 2c        | 2d     | 3.1     | 3.2     | 3.3            | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 | Q4 passages |
| ------ | ------- | --------- | --------- | --------- | ------ | ------- | ------- | -------------- | --- | --- | --- | ----------- | ------- | --------- | ----------- |
| 1      | correct | miss T J2 | miss T J1 | miss T J2 | miss T | Partial | Partial | Partial miss T | No  | No  | No  | ok          | ok      | ok        | two         |
| 2      | correct | miss T    | miss T J1 | miss T J2 | miss T | No      | Partial | Yes ok         | No  | No  | No  | ok          | ok      | ok        | two         |
| 3      | correct | miss T    | ok        | miss T    | miss T | No      | Partial | Yes ok         | No  | No  | No  | ok          | ok      | ok        | two         |
| 4      | correct | miss T J2 | miss T J2 | miss T    | miss T | No      | Partial | Partial miss T | No  | No  | No  | ok          | ok      | ok        | three       |
| 5      | correct | miss T J2 | ok        | miss T J2 | miss T | Partial | Partial | Partial miss T | No  | No  | No  | ok          | ok      | ok        | three       |

Every grade under 3.1, 3.2 and 3.4 to 3.6 is one the key accepts, and every 3.1 grade of Partial
or No notes that no independent search technique is recorded.

### Question 1

Five of five correct. Every sheet has at least four bullets naming obligations the key lists, and
no bullet asserts an obligation the document does not state. Reader 1's "neither a single
instance nor every use of a language feature" is supported by section 7 ("drawn to a [Class]
within both bounds and not to the reported [Instance]"); reader 4's search "chosen and run before
the rule exists" is supported by clause 3.1, which has the search recorded before clause 3.2
begins.

### Question 2

Every reader quoted words of the document for every item, so every miss here is traceable to the
text.

- **2a**, none of five. The sentence states the order only partly or not at all:
  - Reader 1 states class, defence built, rule proven, sweep, every instance fixed, in order; it
    says the rule "is proven", not that it fires, and "the defence" rather than a detector rule
    (J2).
  - Reader 2: "attribute the defect to a class and build and prove the defence"; no sweep and no
    fixing of every instance.
  - Reader 3: "The Defence is built and proven first, then the Defect is fixed"; no class
    attribution, no sweep, no fixing of every instance.
  - Reader 4: "then sweep, then fix"; the fix is not stated as every instance (J2).
  - Reader 5: "sweeps for every instance before fixing anything, then fixes the defect"; the fix
    is stated as the defect, not every instance (J2). Its clause 3.4 quotation after the first
    quotation is not part of the sentence (J1).
- **2b**, two of five (readers 3 and 5, who say the owner "is always a human" in the sentence).
  Readers 1 and 2 say the owner is "Always a human" only after the quotation (J1); reader 4 does
  not say it (J2: "the owner" is not read as carrying its definition). All five quote the key's
  section 4 sentence and say an agent may not.
- **2c**, none of five. No sentence says the reviewer reproduces the red and green runs; each says
  only that the verdict rests on "reproduction" (J2). Readers 3 and 4 also leave "not on the
  report" out of the sentence: reader 3 has it only in its quotation, and reader 4's sentence
  ends "The verdict rests on reproduction:" before the quotation. No reader accepts the pull
  request description as the verdict.
- **2d**, none of five. No sentence states the second ground for a weaker kind, that the language
  has no detector of the stronger kind that accepts bespoke rules:
  - Reader 1: "a weaker kind allowed only where the stronger cannot"; one ground; no order of
    kinds and no place for the record in the sentence (J2 for the order).
  - Reader 2: "A weaker kind is allowed only where the stronger cannot express it"; one ground,
    though its quotation gives both; no order and no place (J2 for the order).
  - Reader 3: "only where the stronger one cannot express the Rule"; one ground; no place in the
    sentence, only in the quotation.
  - Reader 4: the sentence before the quotation states only the strongest kind; it states no
    ground at all, and the record and its places come after the quotation (J1).
  - Reader 5: "only when a stronger one cannot express the rule", then "which of the two
    reasons holds and why" without stating the second; places only after the quotation (J1).
    Whether (iii) needs a place named is a judgement (J3); it changes no mark, since every sheet
    already misses (ii).

### Question 3

- **3.3**, two of five (readers 2 and 3, Yes). Readers 1, 4 and 5 grade Partial because the
  inline ignore on `Report::render()` is a Suppression and not a Narrowing under clause 3.3's
  Part B, and also fail 3.4 on it. The key excuses a reader who attributes the suppression to 3.3
  "rather than" 3.4; these readers attribute it to both, which that sentence does not cover, so
  each is a miss. Each reasoning states what the document requires (reader 1: "a suppression,
  with no searched sentence, and it was not referred"; reader 4: "That makes it a Suppression
  under 3.3, not a Narrowing"; reader 5: "its sentence does not address the hazard"), so each is
  traceable.
- **Remediation**: five of five say it does not conform, each naming at least one failing clause
  the key accepts.
- **Defence**: five of five say it does not conform, each naming 3.6.
- **Section 4**: five of five name the inline ignore on `Report::render()`; readers 1, 2, 4 and 5 also
  mention the unbuilt wider rule as a second or arguable decision, which the key accepts alongside
  it.

### Judgements made in marking

Each takes the stricter reading, the one that records more misses, as `ACCEPTANCE.md` requires
where its rules leave a judgement open.

- **J1. The answer's sentence is what precedes its quotation.** Question 2 asks for one sentence
  followed by a quotation, and a mark turns on "its sentence". Text the reader gives before the
  quotation is read as the sentence however it is punctuated, since the questions ask two or
  three things and nothing picks out one full stop; text after the quotation is outside the form
  the question asks for and is not read as part of the sentence. Affects 2b (readers 1, 2), 2d
  (readers 4, 5) and 2a (reader 5).
- **J2. An element of the key's answer is stated only when the sentence says it.** A less
  specific word does not state the more specific element ("fix" is not "fix every instance",
  "reproduction" is not "reproducing the red and green runs", "proven" is not "fires", "the
  strongest kind" is not the order semantic, syntactic, textual), and a defined term is not read
  as carrying its definition into the sentence ("the owner" is not "always a human", "the
  defence" is not "a detector rule"). Affects 2a (readers 1, 4, 5), 2b (reader 4), 2c (readers
  1, 2, 5) and the order in 2d (readers 1, 2, 4). Runs 17 and 18 accepted "reproduction" for 2c;
  those records are examples of style, not of marking.
- **J3. 2d's element (iii) needs a place named.** The key says naming one of the two places "is
  enough", read as requiring at least one. No mark turns on it.
- **The 3.3 excuse is read as written**, covering a reader who attributes the suppression to 3.3
  rather than 3.4, not one who attributes it to both.
- **Not treated as open: the remediation verdict.** The key's section 7 line gives "does not
  conform" as the intended answer, and its "because 3.2, 3.4 and 3.6" is reasoning, not a list a
  reader must reproduce: it leaves out 3.5, which the key also has failing, and where the key
  wants a clause named, for the defence, it says so.

## Passages quoted as confusing

Same passage as `ACCEPTANCE.md` defines it: sentences in common, or the same paragraph.

| Passage                                                             | Clause   | Readers        | Words quoted, verbatim                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------- | -------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The level paragraph, "Both bounds measure breadth within one level" | 3.1      | three: 1, 2, 3 | 1 and 3: "Both bounds measure breadth within one level; the level itself is a separate question, answered against the report." 2: "Where the [Defect] was reported as a behaviour, ... the [Class] a [Detector] can read usually sits one level below that \[Hazard\]: the mechanism of this [Instance], not the failure the report opens with." The bold sentence and the "Where the [Defect]" sentence are one paragraph. |
| The extension-points sentence                                       | 3.2      | three: 3, 4, 5 | "a [Rule] whose construct its extension points cannot reach is one that [Detector] cannot express, and one its kind cannot express where no other [Detector] of that kind reaches it."                                                                                                                                                                                                                                      |
| The search vocabulary in "Attempt rather than pre-judge"            | 2        | two: 2, 5      | "naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search"                                                                                                                                                                                                                                                                                                 |
| The scale at which a baseline is allowed                            | 3.4      | two: 4, 5      | "and the scale at which that becomes true is tremendous."                                                                                                                                                                                                                                                                                                                                                                   |
| The default owner                                                   | 1, Owner | one: 1         | "Where the project has recorded nobody, the [Owner] is whoever instructed the [Practitioner], and [Escalation] goes there."                                                                                                                                                                                                                                                                                                 |
| The limit on the wider-rule bullet                                  | 4        | one: 4         | "This does not reopen a [Class] whose bounds a [Hazard] sentence has settled, and it reaches no further than the one wider [Rule] already on the record."                                                                                                                                                                                                                                                                   |

Of the four passages named by two or more, only the clause 3.2 sentence is text this pull request
adds; the other three predate it. The criterion does not distinguish, so all four are findings.
Reader 2's remarks on what it could not tell are not suggestions and are not recorded as
passages.

## Findings applied

Applied to the text, never to a question, threshold, fixture or key, in 87536c5, 66301b9 and 3b848c7
(key quotations kept verbatim in 85110c1 and ba8a0bd), after an independent review of each round of
edits. SPEC.md: clause 3.2 sets out the two grounds for a weaker kind as a numbered pair and says
the extension-points rule in two plain sentences; clause 3.3 Part B says an instance left behind an
inline ignore is a Suppression, governed by 3.4, 3.5 and section 4, not a Narrowing; clause 3.1 says
what a class's level is; section 2 says what independent techniques are; clause 3.4 says plainly
that a baseline is rare. Separately, pull request 13 changed how question 2 is marked (sentence and
quotation read together, each element for its gist) after this run, so the misses that rested on
judgements J1 and J2 needed no text change. A fresh cohort follows.

## Process change

Made under a process change before it merged: yes, pull request 13 at commit a695010, named
before the readers started.

## Verdict

**FAIL.** Against the criteria in `ACCEPTANCE.md`:

- Load-bearing statements: not met. 2a none of five, 2b two of five, 2c none of five, 2d none of
  five. Without J1 and J2 the result is still a fail: 2d none of five on the second ground, 2a
  three of five (readers 2 and 3 miss), 2c three of five (readers 3 and 4 miss).
- Restatement and application: not met on 3.3, two of five; every other keyed item five of five.
- Misses traceable to the text: every miss on question 2, and 3.3 for readers 1, 4 and 5; each is
  a finding.
- Passages found confusing by two or more: four, each a finding that blocks until the text is
  changed and a fresh cohort no longer names it: clause 3.1's level paragraph, clause 3.2's
  extension-points sentence, section 2's search-vocabulary sentence and clause 3.4's
  "tremendous" sentence.
- Single-reader notes, recorded: section 1's default owner (reader 1); section 4's limit on the
  wider-rule bullet (reader 4).

Answer sheets, the reader prompt, the command and the marker's instruction: posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090071898), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090072435), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090072816), [comment 4](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090073231).
