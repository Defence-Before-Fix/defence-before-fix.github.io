# Run 29: SPEC.md, semantic detectors, eleventh run in pull request 14

- **Document**: SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  branch `editor/semantic-detectors` at db47301, the commit the readers were given; the question
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
  fixture at db47301, in that order, each preceded by one `===== FILE: <name> =====` line, with
  nothing else added apart from one blank line between the end of each file and the next file's
  marker line.
- **Managed (policy) settings**: none; the machine applies no managed settings to the readers and
  no managed settings file is present, as the editor supplied
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. Every sheet has answer text, no process reports an error
  (`is_error` false, subtype `success`), and every reported model is the cohort's model. The
  editor reports no reader set aside for a cause the sheets cannot show.
- **Run within the pull request**: 11, counting void runs; runs in the pull request so far,
  counting void runs: 11, as the editor supplied. Run 30 is made at the same time and does not
  bear on this document.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with
  the editor's instruction and its agent definition, `.claude/agents/dbf-spec-editor.md`, having
  seen neither the drafting nor the review. It read `ACCEPTANCE.md` and
  `acceptance/runs/README.md` in this worktree, which differ from commit 598908b only by this pull
  request's question-set line adding 2d for SPEC.md; the document, question set, key and fixture
  at db47301; run 27 in full, the passages, judgements and verdict of run 25, the passage history
  of runs 19, 21 and 23, and the headers of runs 20, 22, 24, 26 and 28, which are on
  DETECTOR-SPEC.md; and, for the fourth pass-criteria row, the change to SPEC.md between 1db0c67,
  the document run 27 read, and db47301.

## Marks

`ok` is correct, `miss` is a miss; `T` marks a miss traceable to the text. Judgements J1 to J8
are set out below.

| Reader | Q1      | 2a  | 2b     | 2c  | 2d     | 3.1     | 3.2     | 3.3    | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 | Q4 passages |
| ------ | ------- | --- | ------ | --- | ------ | ------- | ------- | ------ | --- | --- | --- | ----------- | ------- | --------- | ----------- |
| 1      | correct | ok  | ok     | ok  | ok     | No      | Partial | Yes ok | No  | No  | No  | ok          | ok      | ok        | two         |
| 2      | correct | ok  | ok     | ok  | miss T | Partial | Partial | Yes ok | No  | No  | No  | ok          | ok      | ok        | three       |
| 3      | correct | ok  | ok     | ok  | miss T | No      | Partial | Yes ok | No  | No  | No  | ok          | ok      | ok        | four        |
| 4      | correct | ok  | ok     | ok  | miss T | No      | Partial | Yes ok | No  | No  | No  | ok          | ok      | ok        | two         |
| 5      | correct | ok  | miss T | ok  | ok     | No      | Partial | Yes ok | No  | No  | No  | ok          | ok      | ok        | two         |

Every grade under 3.1, 3.2, 3.4, 3.5 and 3.6 is one the key accepts. No reader grades 3.2, 3.5 or
3.6 Yes, so none of the key's cases that count against the document arises.

### Question 1

Five of five correct. Every sheet has at least four bullets naming obligations the key lists (the
class bounded both ways with its hazard, the strongest kind of detector and never a test, the
proof in a commit of its own, the sweep with its count and the fix of every instance, permanent
and blocking, the terse message with an identifier resolving to versioned documentation, the
record of a deferred defect), and no bullet asserts an obligation the document does not state.
The bullets of readers 1, 2, 4 and 5 on attempting rather than pre-judging, or on recording a
no-pattern conclusion in one sentence naming two techniques, state section 2's obligations; reader
5's closing "fix the original defect conventionally with a reproduction test" is section 2 and
section 6.

### Question 2

Every reader quoted words of the document for every item, so every miss here is traceable to the
text.

- **2a**, five of five. Each states class, rule, proof, sweep and the fix of every instance, in
  that order, and quotes section 2's sentence "The order is section 3's: attribute the [Defect] to
  a [Class], build the [Rule], prove that it fires, run the [Sweep], then fix every [Instance]."
- **2b**, four of five. Readers 1 to 4 say only the owner may and an agent may not, and quote the
  key's section 4 sentence; readers 1, 3 and 4 also quote "The [Owner] is always a human." Reader
  5 says "Only a human may adopt a baseline or suppress an instance", quoting the section 4
  sentence and, as an addition, "The [Owner] is always a human."; it does not say the owner is
  who may (J4). Miss, traceable.
- **2c**, five of five. Each states all six clauses and a verdict resting on reproduction, and
  each quotes section 7's definition of a conforming remediation or its "MUST rest on
  reproduction, not on the report"; no reader accepts the pull request description as the
  verdict. Reader 5's withdrawn fragment before its quotation is read under J1.
- **2d**, two of five (readers 1 and 5). The key's three elements are (i) the strongest kind, in
  the order semantic, syntactic, textual; (ii) both grounds for a weaker kind; (iii) the reason
  recorded, with at least one place named and the places not given as alternatives (J2).
  - Reader 1: (i) in its quotation of the strongest-kind sentence; (ii) in its sentence, both
    grounds; (iii) in its sentence and its quotation of the record sentence, both places joined
    by "and". Correct.
  - Reader 2: (i) in its sentence and quotation; (iii) in its quotation of the record sentence.
    (ii) missed: "A weaker kind is allowed only on one of two grounds" states neither ground, and
    neither quotation states one. Miss, traceable.
  - Reader 3: (ii) in its quotation of "A weaker kind is allowed only where ... those are the two
    grounds."; (iii) in its quotation of the record sentence. (i) missed: "the strongest kind of
    detector that can express it" names no kind, and "weaker than [Semantic]" names the top of the
    order, not the order (J3). Miss, traceable.
  - Reader 4: (ii) in its quotation of the grounds sentence; (iii) in its sentence, "in the rule's
    documentation and in the commit". (i) missed as for reader 3: no kind and no order in its
    sentence or quotation (J3). Miss, traceable.
  - Reader 5: (i), (ii) and (iii) in its three quotations, the strongest-kind sentence, the
    grounds sentence and the record sentence. Correct.

### Question 3

- **3.1**: readers 1, 3, 4 and 5 No, reader 2 Partial, each noting that no two independent search
  techniques are recorded.
- **3.2**: five of five Partial, each saying the detector or its kind is not named on the
  documentation and that the rule is not a test; every reader adds that no grounds for a weaker
  kind are recorded, which the key does not mark wrong.
- **3.3**: five of five Yes. Readers 1, 2, 4 and 5 say the inline ignore is not judged here; none
  attributes it to 3.3.
- **3.4** and **3.5**: five of five No, each naming the inline ignore on `Report::render()`, under
  3.5 as uncovered by any recorded decision.
- **3.6**: five of five No, each on the wiki documentation not versioned with the rule.
- **Remediation**: five of five say it does not conform, each naming 3.4 among the failing clauses
  (J7).
- **Defence**: five of five say it does not conform, each naming 3.6 as failing, reader 3 by its
  ground, "its documentation be versioned alongside it" (J8); readers 1, 2 and 5 also name 3.2 as
  not met in full. Every reader also counts 3.5, and most 3.1, against the defence; the key does
  not mark that wrong.
- **Section 4**: five of five name the inline ignore on `Report::render()`, and each also names
  leaving the next wider rule unbuilt, which the key accepts alongside it.

### Judgements made in marking

Made as a careful reader of the document would, as `ACCEPTANCE.md` requires. Where a rule settles
the point, the record says which.

- **J1. The sentence.** Where a reader wrote more than one sentence before or around its
  quotations, all of that text is read with the quotations as the answer. Reader 5's 2c opens with
  a fragment it withdraws in the same line ("... is not the quote here"); the withdrawn fragment
  is not read as part of the answer. No mark turns on it.
- **J2. 2d's element (iii) needs a place named**, as runs 19 to 27 read the key's "naming one of
  the two places is enough". Every reader names both places this run, so no mark turns on it.
- **J3. 2d's element (i) needs the order (readers 3 and 4).** The key's element is "the strongest
  kind that can express the rule, in the order semantic, syntactic, textual", and the question
  asks which kind. "The strongest kind of detector that can express it" names no kind, and
  "weaker than [Semantic]" in a record quotation names the top of the order, not the order. Runs
  23 and 25 read it the same way. Both readers give the order under question 1, but each keyed
  item is marked on its own answer. Read otherwise, readers 3 and 4 would be correct on 2d; 2d
  would still fail on reader 2, whose miss on (ii) rests on no judgement, and the verdict would not
  change.
- **J4. "Only a human" (reader 5, 2b).** The key's answer is the owner of the codebase, always a
  human, and an answer that omits the owner is wrong. Reader 5's sentence names no one but "a
  human", which on its face includes a human practitioner, to whom section 4 gives none of these
  decisions; its added quotation "The [Owner] is always a human." says the owner is human, not
  that the owner is who may. Read together, the answer does not state that the decision is the
  owner's, so it omits the owner. Read otherwise, as naming the owner through the quotation it
  gives in support, 2b would be five of five and the verdict would not change, since 2d fails on
  reader 2 without a judgement.
- **J5. Passages a reader quotes or sets beside its main one count.** Where a reader's question 4
  item quotes words of the document at a named place, or says it was confused by two passages read
  together, a careful reader takes each as a passage it names, since the confusion lies in neither
  alone, as runs 23, 25 and 27 read it. So reader 1's section 2 item also covers clause 3.2's
  paragraph beginning "There are two kinds of gap", where its quoted "mechanism gap" and "the gap
  above" occur in clause 3.2, the first in the same sentence reader 3 quotes; reader 2's section 2
  item, which says "clause 3.1 uses it for searching for instances", covers clause 3.1's sentence
  "In this clause a technique is a way of searching the codebase for [Instances].", as run 27 read
  that reader's like description; reader 3's and reader 4's items each cover both passages they
  quote. Two findings turn on this. Read as context only, reader 1's clause 3.2 passage is one
  reader's, not two, and run 25's clause 3.1 passage is cleared; the verdict would not change.
- **J6. Run 25's clause 3.1 paragraph as it reads in the changed document.** The paragraph that
  began "Two techniques are independent when they would miss different things." is now three
  paragraphs, beginning "In this clause a technique is a way of searching", "A technique counts
  only if" and "The record MUST name both techniques", the last kept verbatim from it. All three
  are taken as that paragraph as it reads now. No mark turns on it: reader 2's description names a
  sentence of the first.
- **J7. The remediation item.** The key's answer is that the remediation does not conform, giving
  3.2, 3.4 and 3.6 as the reason. A reader saying it does not conform and naming among the failing
  clauses one the key names is correct, as runs 23, 25 and 27 marked it; every reader names 3.4,
  and every reader 3.6.
- **J8. The defence item (reader 3).** The key marks correct a reader who names 3.2 or 3.6. Reader
  3 names 3.5 by number and 3.6 by its requirement, that the documentation "be versioned alongside
  it", having graded 3.6 No on that ground; it names 3.6's failure, and is correct.

## Passages quoted as confusing

Same passage as `ACCEPTANCE.md` defines it: sentences in common, or the same paragraph; a list
item, table row or terminology entry is its own paragraph.

| Passage                                                    | Clause    | Readers   | Words quoted, verbatim, or the description used                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------- | --------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Independent techniques for expressing a rule               | 2         | two: 2, 5 | 2: "A technique here is a way of trying to write the [Rule]. Two such techniques are independent when they would miss different things, which is the same test clause 3.1 applies to ways of searching for [Instances]." 5: "The conclusion that no pattern exists MUST be stated in one sentence, naming at least two independent techniques tried at expressing the [Rule], and recorded where the project's other decisions are enumerable under clause 8.7, not only with the fix." Both in the "Attempt rather than pre-judge" paragraph |
| The entry point and substitutes for a bundled defence      | 3.5       | two: 2, 3 | 2: "A mechanism gap that stops the [Toolchain] running its own entry point on its own source moves the demonstration to such a project; it does not weaken it." 3: "The substitutes clause 3.2 allows, for proving under clause 3.3 and for resolution under clause 3.6, do not extend to this clause." Both in the paragraph beginning "A [Bundled defence] is a [Defence] that a shipped [Toolchain] enables by default"; reader 3 sets it beside the clause 3.2 passage below                                                              |
| The two kinds of gap                                       | 3.2       | two: 1, 3 | 3: "uses the substitutes clauses 3.3 and 3.6 already allow". 1: "mechanism gap" and "the gap above", attributed to clause 3.2 (J5). Both in the paragraph beginning "There are two kinds of gap and they lead to different work"                                                                                                                                                                                                                                                                                                              |
| The three ways out, a toolchain gap                        | 2         | one: 1    | "A pattern exists but the language has no extensible [Detector] of a kind that can express the [Rule] within clause 3.1's bounds, and a bespoke one is not practical: a [Toolchain] gap under clause 3.2.", in the paragraph beginning "There are three ways out of the method", set beside clause 3.2's paragraph above (J5)                                                                                                                                                                                                                 |
| A technique in clause 3.1                                  | 3.1       | one: 2    | By description, "clause 3.1 uses it for searching for instances", set beside its section 2 passage above: the sentence "In this clause a technique is a way of searching the codebase for [Instances]." (J5, J6). Run 25's open passage (below)                                                                                                                                                                                                                                                                                               |
| An assumed calibration against escalating doubt            | 3 and 3.1 | one: 3    | "**Where the project has recorded nothing, the [Practitioner] is not blocked.** Proceed on the examples below, **state the [Calibration] assumed**", in section 3's paragraph of that name, set beside "Where the [Practitioner] is not sure, the decision goes to the [Owner] under section 4.", in clause 3.1's lower-bound list item                                                                                                                                                                                                       |
| Merging at full width against not blocking until every fix | 4         | one: 4    | "the [Rule] MAY merge at full width with that case recorded as a known [Instance] awaiting the [Owner]", in the paragraph beginning "**What to do whilst waiting.**", set beside "provided the [Rule] does not become [Blocking] until every [Instance] is fixed", in the paragraph beginning "A remediation MAY be delivered across several changes"                                                                                                                                                                                         |
| Leaving the next wider rule unbuilt                        | 4         | one: 5    | "It is a reason not to widen unasked, not authority to leave the wider [Rule] out, and recording it as a known gap does not make it the [Practitioner]'s decision.", in section 4's list item beginning "Leaving unbuilt the next wider [Rule]"                                                                                                                                                                                                                                                                                               |

Readers' accounts of what they could not tell are recorded with the passage they attach to and are
not suggestions; none of the sheets proposes a change.

**Earlier passages (the fourth row).** The open passages are those earlier runs of this document
found confusing by two or more and did not clear: run 27's two new passages and run 25's clause
3.1 passage, which run 27 did not clear; one of run 27's two is run 21's clause 3.2 passage,
which runs 23, 25 and 27 did not clear. Every other passage of runs 19, 21, 23 and 25 was cleared
in runs 21, 23, 25 and 27. As the paragraphs read in the changed document:

- Clause 3.2's grounds and record, run 21's passage: the paragraph beginning "**Qualifying is not
  the same as being the right host.**", the paragraph beginning "For the second ground", and the
  record paragraph beginning "On the [Remediation docs] of a [Rule] they write". Named by no
  reader. Readers 1 and 3 name clause 3.2's paragraph beginning "There are two kinds of gap",
  which is not one of these. Cleared.
- Section 7's paragraph beginning "**A [Defence] [Conforms]**", with clause 3.5's opening
  paragraph, run 27's passage: named by no reader. Readers 2 and 3 name clause 3.5's \[Bundled
  defence\] paragraph, not its opening paragraph. Cleared.
- Clause 3.1's paragraph that began "Two techniques are independent when they would miss
  different things.", run 25's passage, now the three paragraphs beginning "In this clause a
  technique is a way of searching", "A technique counts only if" and "The record MUST name both
  techniques" (J6): named by reader 2 by description (J5). Not cleared.

No sentence kept from a cleared paragraph is named elsewhere in the document. Four passages named
here were once open and have since been cleared: section 2's "Attempt rather than pre-judge"
paragraph (run 19, two readers; cleared in run 21), named here by readers 2 and 5; clause 3.5's
[Bundled defence] paragraph (run 25, two readers; cleared in run 27), named here by readers 2 and
3; clause 3.1's lower-bound list item (run 23, three readers; cleared in run 25), named here by
reader 3; and section 4's list item on leaving the next wider rule unbuilt (run 21, three readers;
cleared in run 23), named here by reader 5. The first two are named by two readers and are new
findings here; the last two are recorded as one reader's. Clause 3.2's paragraph on the two kinds
of gap, named by one reader in run 25, is named by two here and is a new finding.

## Findings applied

None yet. After six cohorts on this pull request the editor has stopped to put a decision to the
owner before changing the text again: the misses that recur in every run (question 2d's order and
grounds, and on the detector document question 2b's "need not remove or forbid") turn on elements of
the keys that the questions do not ask for directly, and on the fourth row keeping a passage open
while any single reader of a fresh cohort names it. Neither can be changed by the editor, since a
question, a key and a threshold may not be changed to let a run pass.

## Process change

Made under a process change before it merged: yes, pull request 13 at commit 598908b, named
before the readers started.

## Verdict

**FAIL.** Against the criteria in `ACCEPTANCE.md`:

- Load-bearing statements: not met. 2a and 2c five of five; 2b four of five (reader 5, on J4); 2d
  two of five. Reader 2 states neither ground for a weaker kind, only that there are two; readers
  3 and 4 do not give the order semantic, syntactic, textual (J3).
- Restatement and application: met. Question 1 and every keyed item of question 3 five of five.
- Misses traceable to the text, each a finding: 2d for reader 2, quoting clause 3.2's
  strongest-kind and record sentences and saying the grounds are two without stating them; 2d for
  readers 3 and 4, quoting clause 3.2's sentence "A weaker kind is allowed only where the stronger
  kind cannot express the [Rule], or where the language has no [Detector] of the stronger kind
  that accepts bespoke [Rules]; those are the two grounds." and giving the strongest kind without
  the order (on J3); 2b for reader 5, quoting section 4's sentence on an agent's authority and
  saying only "a human" may, without the owner (on J4).
- Passages found confusing by two or more, each a finding that blocks until the text is changed
  and a fresh cohort no longer names it: section 2's "Attempt rather than pre-judge" paragraph, on
  techniques tried at expressing a rule (two readers); clause 3.5's paragraph beginning "A
  [Bundled defence] is a [Defence] that a shipped [Toolchain] enables by default", on the moved
  demonstration and the substitutes that do not extend to it (two); clause 3.2's paragraph
  beginning "There are two kinds of gap and they lead to different work" (two, one on J5). Run
  25's clause 3.1 paragraph on independent techniques is not cleared (one reader, on J5). Run 21's
  clause 3.2 passage on the grounds and their record, and run 27's section 7 and clause 3.5
  passage, are cleared.
- Single-reader notes, recorded: section 2's "There are three ways out of the method" paragraph
  (reader 1); section 3's "Where the project has recorded nothing" paragraph against clause 3.1's
  lower-bound list item (reader 3); section 4's "What to do whilst waiting" paragraph against its
  paragraph on delivering a remediation across several changes (reader 4); section 4's list item
  on leaving the next wider rule unbuilt (reader 5).

Answer sheets, the reader prompt, the command and the marker's instruction: posted on pull request 14 in posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6091186417), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6091186696), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6091187011), [comment 4](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6091187459).
