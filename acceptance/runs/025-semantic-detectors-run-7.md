# Run 25: SPEC.md, semantic detectors, seventh run in pull request 14

- **Document**: SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  branch `editor/semantic-detectors` at dfb9b68, the commit the readers were given; the question
  set, key and fixture read at the same commit
- **Cohort**: five readers, model alias `haiku`; every reader reported `claude-haiku-5-5`, as the
  editor supplied in the cohort's model list and as each reader's own JSON output shows
- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, which only reattaches the session's credential and passes
  arguments through verbatim, in a fresh empty directory made by `mktemp -d` outside any
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt is byte for byte the question set, the document and the
  fixture at dfb9b68, in that order, each preceded by one `===== FILE: <name> =====` line, with
  nothing else added apart from one blank line between the end of each file and the next file's
  marker line.
- **Managed (policy) settings**: none; the machine applies no managed settings to the readers and
  no managed settings file is present, as the editor supplied
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. Every sheet has answer text, no process reports an error
  (`is_error` false, subtype `success`), and every reported model is the cohort's model. The
  editor reports no reader set aside for a cause the sheets cannot show.
- **Run within the pull request**: 7, counting void runs; runs in the pull request so far,
  counting void runs: 7, as the editor supplied. Run 26 is made at the same time and does not bear
  on this document.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with
  the editor's instruction and its agent definition, `.claude/agents/dbf-spec-editor.md`, having
  seen neither the drafting nor the review. It read `ACCEPTANCE.md` and
  `acceptance/runs/README.md` in this worktree, which differ from commit 598908b only by this pull
  request's question-set line adding 2d for SPEC.md; the document, question set, key and fixture
  at dfb9b68; runs 21 and 23 in full, run 19's verdict, and the headers of runs 20, 22 and 24,
  which are on DETECTOR-SPEC.md; and, for the fourth pass-criteria row, the change to SPEC.md
  between 0b8d699, the document run 23 read, and dfb9b68.

## Marks

`ok` is correct, `miss` is a miss; `T` marks a miss traceable to the text. Judgements J1 to J8
are set out below.

| Reader | Q1      | 2a  | 2b  | 2c  | 2d     | 3.1 | 3.2     | 3.3    | 3.4 | 3.5 | 3.6            | Remediation | Defence | Section 4 | Q4 passages |
| ------ | ------- | --- | --- | --- | ------ | --- | ------- | ------ | --- | --- | -------------- | ----------- | ------- | --------- | ----------- |
| 1      | correct | ok  | ok  | ok  | miss T | No  | Partial | Yes ok | No  | No  | No             | ok          | ok      | ok        | two         |
| 2      | correct | ok  | ok  | ok  | miss T | No  | Partial | Yes ok | No  | No  | Partial miss T | ok          | ok      | ok        | three       |
| 3      | correct | ok  | ok  | ok  | ok     | No  | Partial | Yes ok | No  | No  | Partial miss T | ok          | ok      | ok        | two         |
| 4      | correct | ok  | ok  | ok  | ok     | No  | Partial | Yes ok | No  | No  | No             | ok          | ok      | ok        | two         |
| 5      | correct | ok  | ok  | ok  | miss T | No  | Partial | Yes ok | No  | No  | No             | ok          | ok      | ok        | four        |

Every grade under 3.1, 3.2, 3.4 and 3.5, and every 3.6 grade of No, is one the key accepts; every
3.1 grade of No notes that no independent search technique is recorded. No reader grades 3.2, 3.5
or 3.6 Yes, so none of the key's cases that count against the document arises. The two 3.6 grades
of Partial are marked under J5.

### Question 1

Five of five correct. Every sheet has at least four bullets naming obligations the key lists (the
class bounded both ways with its hazard, the strongest kind of detector and never a test, the
proof in a commit of its own, the sweep with its count and the fix of every instance, permanent
and blocking, the terse message with an identifier resolving to versioned documentation, the
record of a deferred defect), and no bullet asserts an obligation the document does not state.
Reader 5's "strongest kind of detector", naming no fallback, is correct as the key says of a
bullet naming the strongest kind. The closing "fix the original defect with a reproduction test"
of readers 2 and 5 is section 2 and section 6.

### Question 2

Every reader quoted words of the document for every item, so every miss here is traceable to the
text.

- **2a**, five of five. Each states class, rule, proof, sweep and the fix of every instance, in
  that order, and quotes section 2's sentence "The order is section 3's: attribute the [Defect] to
  a [Class], build the [Rule], prove that it fires, run the [Sweep], then fix every [Instance]."
- **2b**, five of five. Each says only the owner may and an agent may not, and quotes the key's
  section 4 sentence. Readers 1, 3, 4 and 5 say the owner is a human; reader 2 says "Only the
  Owner" (J4).
- **2c**, five of five. Each states all six clauses and a verdict resting on reproduction, not on
  the report, in its sentence or its quotation of section 7; readers 1, 4 and 5 quote the red and
  green reruns. No reader accepts the pull request description as the verdict.
- **2d**, two of five (readers 3 and 4). The key's three elements are (i) the strongest kind, in
  the order semantic, syntactic, textual; (ii) both grounds for a weaker kind; (iii) the reason
  recorded, with at least one place named and the places not given as alternatives (J2).
  - Reader 1: (i) in its first quotation; (iii) stated, its second quotation giving the
    remediation docs "and" the commit description. (ii) missed: "A weaker kind is allowed only on
    two grounds" says there are two and states neither, and its quotation of the record sentence,
    "... which of the two grounds holds ... and why", elides the parenthesis that names them (J6).
  - Reader 2: as reader 1. (i) and (iii) stated; (ii) missed: "only on one of two grounds", with
    the same record quotation eliding the grounds (J6).
  - Reader 3: (i) in its sentence and quotation, (ii) in its quotation of the "two grounds only"
    sentence, (iii) with both places joined by "and". Correct.
  - Reader 4: (i), (ii) and (iii) in its three quotations, the places joined by "and". Correct.
  - Reader 5: (ii) stated in its quotation of the "two grounds only" sentence. (i) missed: "the
    strongest kind of detector that can express it", and no quotation names the order semantic,
    syntactic, textual (J3). (iii) missed: its record quotation, "MUST also record, ... which of
    the two grounds holds ... and why", elides the places, and its sentence names none (J2, J6).

### Question 3

- **3.1**: five of five No, each noting that no two independent search techniques are recorded.
- **3.2**: five of five Partial, each saying the rule reads code and is not a test, and each that
  the detector or its kind is not named. Readers 2, 3 and 5 add that no grounds for a weaker kind
  are recorded, which the key does not mark wrong.
- **3.3**: five of five Yes. Readers 2, 3, 4 and 5 say the inline ignore is a [Suppression] judged
  under 3.4 and 3.5, not here; none attributes it to 3.3.
- **3.4** and **3.5**: five of five No, each naming the inline ignore on `Report::render()`, under
  3.5 as uncovered by any recorded decision.
- **3.6**, three of five (readers 1, 4 and 5, No). Readers 2 and 3 grade Partial, which the key
  accepts only "where the reasoning quotes the versioning sentence" (J5).
  - Reader 2: "But it sits on a company wiki, not shipped or versioned with the rule." This
    paraphrases the requirement and quotes nothing. The reasoning states what the document
    requires, so the miss is traceable; reader 2 also names clause 3.6's external URL sentence
    under question 4.
  - Reader 3: 'they are not "shipped with the project" or "versioned alongside the [Rule]" as the
    clause requires.' The first is verbatim from 3.6's opening sentence, which requires shipping,
    not versioning; the second is not the document's words, which are "versions it alongside the
    [Rule]" in 3.6 and "versioned alongside it" in section 7. The reasoning quotes the document,
    so the miss is traceable.
- **Remediation**: five of five say it does not conform, each naming failing clauses the key
  accepts.
- **Defence**: five of five say it does not conform, each naming 3.6 as not met and readers 2, 3
  and 4 naming 3.2 as well. Readers 1, 3, 4 and 5 also count 3.5 against the defence, on the
  uncovered suppression; the key does not mark that wrong.
- **Section 4**: five of five name the inline ignore on `Report::render()`, and each also names
  leaving the next wider rule unbuilt, which the key accepts alongside it.

### Judgements made in marking

Made as a careful reader of the document would, as `ACCEPTANCE.md` requires. Where a rule settles
the point, the record says which.

- **J1. The sentence.** Where a reader wrote more than one sentence before or around its
  quotations, all of that text is read with the quotations as the answer. No mark turns on it.
- **J2. 2d's element (iii) needs a place named.** The key says of (iii) that "naming one of the
  two places is enough" and that presenting them as alternatives is wrong; "enough" sets a
  minimum, and a key that let an answer name no place would have no minimum to state and no
  alternatives to forbid. Runs 19, 21 and 23 read it the same way. Reader 5's (iii) turns on it;
  reader 5 misses (i) as well (J3).
- **J3. 2d's element (i) needs the order (reader 5).** The key's element is "the strongest kind
  that can express the rule, in the order semantic, syntactic, textual", and the question asks
  which kind. "The strongest kind of detector that can express it" names no kind, and "weaker than
  [Semantic]" in its record quotation names the top of the order, not the order. Run 23 read it
  the same way. Read otherwise under both J2 and J3, reader 5 would be correct on 2d; 2d would
  still fail on readers 1 and 2, whose misses on (ii) rest on no judgement.
- **J4. "The Owner" (reader 2, 2b).** Settled by the rule that a defined term used in its defined
  sense states what it means: the [Owner] "is always a human".
- **J5. 3.6 Partial and "the versioning sentence" (readers 2 and 3).** The key accepts Partial
  "where the reasoning quotes the versioning sentence", and `ACCEPTANCE.md` defines quoting: the
  document's consecutive words, verbatim apart from letter case, quotation-mark style and markup;
  a paraphrase is not quoting. Which sentence is the versioning sentence the key leaves open. It
  is taken in the wider sense, either of 3.6's sentences requiring the documentation to be
  versioned with the rule: "A [Rule] and its documentation are one artefact and MUST be versioned
  as one." and "An external URL [Conforms] only where the project controls it and versions it
  alongside the [Rule].", the second because the key's case of a reader who grades Yes "because
  the URL resolves" is a misreading of it. Neither reader quotes either sentence, so both miss on
  3.6, and both reasonings state or quote what the document requires, so both misses are
  traceable. Read leniently, taking reader 3's "versioned alongside the [Rule]" as a quotation of
  the URL sentence despite the changed word, reader 3 would be correct, 3.6 would be four of five
  and the second criterion met; reader 2's traceable miss would stand, and the verdict would not
  change.
- **J6. Elided quotations.** A quotation with an ellipsis is read as one quotation per unbroken
  run of words, each in the document's order, and states only what those runs state (readers 1,
  2 and 5 under 2d; reader 4's section 8 passage). Settled by the rule on quoting: consecutive
  words of any length.
- **J7. Clause labels.** A clause number given with a quotation, as question 4 asks, is read as
  the quotation's label, not as naming the whole clause, as runs 21 and 23 read it. Reader 1's
  "clause 3.3, Part B" label does not extend its passage to all of Part B.
- **J8. Passages set beside the main one count.** Where a reader says it was confused by two
  passages read together, a careful reader takes both as the confusing passage, since the
  confusion lies in neither alone, as run 23 read it. So reader 2's first two items each cover
  both passages they set side by side, reader 4's first item covers all three of its quotations,
  and reader 5's fourth item covers both its quotations. Reader 5's first item quotes section 2
  and describes clause 3.1 as defining "independence for searches", not knowing whether that test
  applies to techniques for writing a rule; the confusion lies in how the two read together, so
  the description is read as naming clause 3.1's definition, the sentence "Two techniques are
  independent when they would miss different things." A finding turns on this: read as context
  only, clause 3.1's paragraph beginning with that sentence would be reader 2's alone. The verdict
  would not change.

## Passages quoted as confusing

Same passage as `ACCEPTANCE.md` defines it: sentences in common, or the same paragraph; a list
item, table row or terminology entry is its own paragraph.

| Passage                                                           | Clause            | Readers          | Words quoted, verbatim, or the description used                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------------------------------------------------- | ----------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Which ground holds when extension points cannot reach a construct | 3.2               | four: 1, 3, 4, 5 | All four: "If a [Detector] passes both but its extension points cannot reach the construct a [Rule] is about, that [Detector] cannot express the [Rule]. If no [Detector] of the stronger kind can reach it, the stronger kind cannot express the \[Rule\]: that is the first ground, not the second." The last two sentences of the paragraph beginning "The second ground asks two questions". Run 23's open passage (below) |
| The entry point for a bundled defence                             | 3.5               | two: 3, 5        | Both: "For a [Bundled defence], the project whose entry point demonstrates it is any project the [Toolchain] is genuinely installed into, the [Consuming project] included", reader 3 to "since that is where the [Rule] will be enforced.", reader 5 ending in an ellipsis; both add that "Bundled defence" and "Consuming project" are not defined in SPEC.md                                                                |
| Two techniques are independent; a rule run is not one of them     | 3.1               | two: 2, 5        | 2: "a clean run of the [Rule]", "not evidence of saturation" and "is never one of the two", set beside clause 3.3's "A single execution of the [Rule] answers both" (J8). 5: by description, "Clause 3.1 defines independence for searches", set beside section 2 (J8). All in the paragraph beginning "Two techniques are independent when they would miss different things."                                                 |
| Narrowings reported to the owner as if suppressions               | 3.3, Part B       | one: 1           | "a [Narrowing] that excludes more code than the [Rule] still covers MUST be reported to the [Owner] as if it were a [Suppression]." (J7)                                                                                                                                                                                                                                                                                       |
| What a defence must satisfy of clause 3.5                         | 3.5 and 7         | one: 2           | Section 7's "it fails rather than warns", in the paragraph beginning "A [Defence] [Conforms]", and clause 3.5's "does not [Conform]", in its opening paragraph (J8)                                                                                                                                                                                                                                                            |
| Proving and sweeping in one run                                   | 3.3, Part A       | one: 2           | "A single execution of the [Rule] answers both", set beside clause 3.1 (above, J8)                                                                                                                                                                                                                                                                                                                                             |
| An external URL                                                   | 3.6               | one: 2           | "An external URL [Conforms] only where the project controls it and versions it alongside the [Rule]."                                                                                                                                                                                                                                                                                                                          |
| Check order and conformance                                       | 5, 7 and 8, Scope | one: 4           | 5: "a project whose checks run in another order is a project that does not [Conform]". 7: "Nothing here constrains how the project runs its checks or what it does when they fail". 8: "How a project chooses to run its quality checks" and "is the project's own business and no part of this specification." (J6, J8)                                                                                                       |
| Independent techniques for expressing a rule                      | 2                 | one: 5           | "at least two independent techniques tried at expressing the [Rule]" and "Two techniques are independent when they would miss different things, as clause 3.1 says of a search.", in the "Attempt rather than pre-judge" paragraph; set beside clause 3.1 (above, J8)                                                                                                                                                          |
| A toolchain gap and the toolchain's claim                         | 3.6 and 3.2       | one: 5           | 3.6: "it is a [Toolchain] gap and blocks the [Toolchain]'s claim under section 7 until fixed." 3.2: "is recorded against the [Toolchain]'s claim under section 7 as well" (J8)                                                                                                                                                                                                                                                 |

Readers' accounts of what they could not tell are recorded with the passage they attach to and are
not suggestions; none of the sheets proposes a change.

**Earlier passages (the fourth row).** The open passages are those earlier runs of this document
found confusing by two or more and did not clear: run 23's three, and run 21's clause 3.2 passage,
which run 23 did not clear (run 19's other three and run 21's other three were cleared in runs 21
and 23). As the paragraphs read in the changed document:

- Clause 3.2's two grounds, run 21's passage, which run 23 read as the grounds sentence of the
  paragraph beginning "**Qualifying is not the same as being the right host.**", the paragraph
  then beginning "The language has a [Detector] of the stronger kind", and the record paragraph
  beginning "On the [Remediation docs] of a [Rule] they write". The second of those now begins
  "The second ground asks two questions"; readers 1, 3, 4 and 5 name its last two sentences. Not
  cleared.
- Clause 3.1's lower-bound list item: named by no reader. Reader 2's and reader 5's clause 3.1
  passage lies in the paragraph beginning "Two techniques are independent", not the list item.
  Cleared.
- The Owner entry in section 1: named by no reader. Cleared.
- The Narrowing entry in section 1: named by no reader. Reader 1's narrowing passage is clause
  3.3 Part B's sentence, which does not occur in the entry. Cleared.

No sentence kept from one of the three cleared paragraphs is named elsewhere in the document.
Reader 5's section 2 passage lies in the "Attempt rather than pre-judge" paragraph that run 19
named and run 21 cleared; it is not an open passage and is recorded above as one reader's. Reader
3 and reader 5's clause 3.5 passage was named by one reader in run 23 and is a new finding here.

## Findings applied

Applied to the text, never to a question, threshold, fixture or key, in 0b2d190 and the commit after
it that settles its review (key quotations kept verbatim in d07c177 and that commit). SPEC.md:
clause 3.2's record sentence states both grounds in its main clause, and its paragraph on the second
ground is four short sentences; clause 3.5 says what a bundled defence is in plain words; clause
3.1's paragraph on independent techniques is shorter; clause 3.6's versioning requirement is one
short sentence. A fresh cohort follows.

## Process change

Made under a process change before it merged: yes, pull request 13 at commit 598908b, named
before the readers started.

## Verdict

**FAIL.** Against the criteria in `ACCEPTANCE.md`:

- Load-bearing statements: not met. 2a, 2b and 2c five of five; 2d two of five. Readers 1 and 2
  state neither ground for a weaker kind, only that there are two; reader 5 does not give the
  order semantic, syntactic, textual (J3) and names no place for the record (J2).
- Restatement and application: not met on 3.6, three of five (readers 2 and 3 grade Partial
  without quoting the versioning sentence, J5); question 1 and every other keyed item five of
  five.
- Misses traceable to the text, each a finding: 2d for readers 1, 2 and 5, each quoting clause
  3.2's record sentence "Where that kind is weaker than [Semantic], the [Practitioner] MUST also
  record, on the [Rule]'s [Remediation docs] and in the description of the commit that adds the
  [Rule], moves it to another [Detector], or first records the grounds, for each step down the
  order [Semantic], [Syntactic], [Textual], which of the two grounds holds (the stronger kind
  cannot express the [Rule], or the language has no [Detector] of the stronger kind that accepts
  bespoke [Rules]) and why, naming the [Detectors] of the stronger kind that were considered."
  with the grounds (readers 1 and 2) or the places (reader 5) elided; 3.6 for readers 2 and 3,
  on clause 3.6's requirement that the documentation be shipped and versioned with the rule.
- Passages found confusing by two or more, each a finding that blocks until the text is changed
  and a fresh cohort no longer names it: clause 3.2's paragraph beginning "The second ground asks
  two questions", its last two sentences (four readers), which is also run 21's open passage, not
  cleared; clause 3.5's sentence on the entry point for a [Bundled defence] (two); clause 3.1's
  paragraph beginning "Two techniques are independent when they would miss different things."
  (two, on J8). Run 23's three passages are cleared.
- Single-reader notes, recorded: clause 3.3 Part B's sentence on narrowings reported to the owner
  (reader 1); clause 3.5's opening paragraph against section 7's defence paragraph, clause 3.3
  Part A's proving-and-sweeping paragraph, and clause 3.6's external URL sentence (reader 2);
  sections 5, 7 and 8 on check order and conformance (reader 4); section 2's "Attempt rather than
  pre-judge" paragraph, and clause 3.6's unresolved identifier paragraph against clause 3.2's
  paragraph on the two kinds of gap (reader 5).

Answer sheets, the reader prompt, the command and the marker's instruction: posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090845841), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090846386), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090846766), [comment 4](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090847033).
