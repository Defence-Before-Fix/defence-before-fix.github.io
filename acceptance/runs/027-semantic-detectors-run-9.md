# Run 27: SPEC.md, semantic detectors, ninth run in pull request 14

- **Document**: SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  branch `editor/semantic-detectors` at 1db0c67, the commit the readers were given; the question
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
  fixture at 1db0c67, in that order, each preceded by one `===== FILE: <name> =====` line, with
  nothing else added apart from one blank line between the end of each file and the next file's
  marker line.
- **Managed (policy) settings**: none; the machine applies no managed settings to the readers and
  no managed settings file is present, as the editor supplied
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. Every sheet has answer text, no process reports an error
  (`is_error` false, subtype `success`), and every reported model is the cohort's model. The
  editor reports no reader set aside for a cause the sheets cannot show.
- **Run within the pull request**: 9, counting void runs; runs in the pull request so far,
  counting void runs: 9, as the editor supplied. Run 28 is made at the same time and does not bear
  on this document.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with
  the editor's instruction and its agent definition, `.claude/agents/dbf-spec-editor.md`, having
  seen neither the drafting nor the review. It read `ACCEPTANCE.md` and
  `acceptance/runs/README.md` in this worktree, which differ from commit 598908b only by this pull
  request's question-set line adding 2d for SPEC.md; the document, question set, key and fixture
  at 1db0c67; run 25 in full, the passages and verdicts of runs 19, 21 and 23, and the headers of
  runs 20, 22, 24 and 26, which are on DETECTOR-SPEC.md; and, for the fourth pass-criteria row,
  the change to SPEC.md between dfb9b68, the document run 25 read, and 1db0c67.

## Marks

`ok` is correct, `miss` is a miss; `T` marks a miss traceable to the text. Judgements J1 to J8
are set out below.

| Reader | Q1      | 2a  | 2b  | 2c  | 2d     | 3.1     | 3.2     | 3.3    | 3.4 | 3.5 | 3.6     | Remediation | Defence | Section 4 | Q4 passages |
| ------ | ------- | --- | --- | --- | ------ | ------- | ------- | ------ | --- | --- | ------- | ----------- | ------- | --------- | ----------- |
| 1      | correct | ok  | ok  | ok  | miss T | Partial | Partial | Yes ok | No  | No  | No      | ok          | ok      | ok        | two         |
| 2      | correct | ok  | ok  | ok  | ok     | No      | No      | Yes ok | No  | No  | No      | ok          | ok      | ok        | two         |
| 3      | correct | ok  | ok  | ok  | miss T | No      | No      | Yes ok | No  | No  | No      | ok          | ok      | ok        | two         |
| 4      | correct | ok  | ok  | ok  | ok     | Partial | Partial | Yes ok | No  | No  | Partial | ok          | ok      | ok        | two         |
| 5      | correct | ok  | ok  | ok  | miss T | No      | Partial | Yes ok | No  | No  | No      | ok          | ok      | ok        | two         |

Every grade under 3.1, 3.2, 3.4, 3.5 and 3.6 is one the key accepts; reader 4's 3.6 Partial
quotes the versioning sentence (J7). No reader grades 3.2, 3.5 or 3.6 Yes, so none of the key's
cases that count against the document arises.

### Question 1

Five of five correct. Every sheet has at least four bullets naming obligations the key lists (the
class bounded both ways with its hazard, the strongest kind of detector and never a test, the
proof in a commit of its own, the sweep with its count and the fix of every instance, permanent
and blocking, the terse message with an identifier resolving to versioned documentation, the
record of a deferred defect), and no bullet asserts an obligation the document does not state.
The section 2 bullets of readers 1, 2 and 4, on building the defence first or attempting rather than
pre-judging, state section 2's obligations (J6 for reader 4). The closing "fix the original defect with a reproduction test"
of readers 1, 3 and 5 is section 2 and section 6. Reader 3's line after its six bullets, on what
belongs to the Owner, states section 4 and is not a seventh bullet; no mark turns on it.

### Question 2

Every reader quoted words of the document for every item, so every miss here is traceable to the
text.

- **2a**, five of five. Each states class, rule, proof, sweep and the fix of every instance, in
  that order, and quotes section 2's sentence "The order is section 3's: attribute the [Defect] to
  a [Class], build the [Rule], prove that it fires, run the [Sweep], then fix every [Instance]."
- **2b**, five of five. Each says only the owner may and an agent may not, and quotes the key's
  section 4 sentence. Every reader says the owner is a human, readers 4 and 5 quoting "The [Owner]
  is always a human."
- **2c**, five of five. Each states all six clauses and a verdict resting on reproduction, and
  each quotes section 7's "MUST rest on reproduction, not on the report"; no reader accepts the
  pull request description as the verdict.
- **2d**, two of five (readers 2 and 4). The key's three elements are (i) the strongest kind, in
  the order semantic, syntactic, textual; (ii) both grounds for a weaker kind; (iii) the reason
  recorded, with at least one place named and the places not given as alternatives (J2).
  - Reader 1: (i) and (ii) in its two quotations, the strongest-kind sentence and the sentence
    stating the two grounds. (iii) missed: "the practitioner must record which ground holds and
    why" names no place, and neither quotation names one (J2).
  - Reader 2: (i) and (ii) in its quotations, (iii) in its sentence, "in the rule's remediation
    docs and in the commit description", with its quotation of "naming the [Detectors] of the
    stronger kind that were considered". Correct.
  - Reader 3: (i) in its quotation. (ii) missed: "A weaker kind is allowed only on two grounds"
    says there are two and states neither, and its only quotation is the strongest-kind sentence.
    (iii) missed: "record which ground holds and why" names no place (J2).
  - Reader 4: (i), (ii) and (iii) in its three quotations, the third giving the places joined by
    "and" (J3). Correct.
  - Reader 5: (i) in its quotation. (ii) missed: "only on one of two grounds" states neither.
    (iii) missed: "record which ground holds at each step down, with the stronger detectors
    considered" names no place (J2).

### Question 3

- **3.1**: readers 2, 3 and 5 No, readers 1 and 4 Partial, each noting that no two independent
  search techniques are recorded.
- **3.2**: readers 1, 4 and 5 Partial, readers 2 and 3 No, each saying the detector or its kind is
  not named; readers 1, 4 and 5 say the rule is not a test, and every reader adds that no grounds
  for a weaker kind are recorded, which the key does not mark wrong.
- **3.3**: five of five Yes. Readers 1, 3, 4 and 5 say the inline ignore is not judged here; none
  attributes it to 3.3.
- **3.4** and **3.5**: five of five No, each naming the inline ignore on `Report::render()`, under
  3.5 as uncovered by any recorded decision.
- **3.6**: five of five. Readers 1, 2, 3 and 5 grade No; reader 4 grades Partial and quotes "A
  [Rule]'s documentation MUST be versioned with the [Rule]." (J7).
- **Remediation**: five of five say it does not conform, each naming 3.4 among the failing clauses
  (J8).
- **Defence**: five of five say it does not conform, each naming 3.6 as not met and 3.2 as well,
  readers 3 and 4 saying 3.2 cannot be shown or confirmed and reader 5 that it is only partial. Every reader also counts 3.1 or 3.5 against the defence; the key does
  not mark that wrong.
- **Section 4**: five of five name the inline ignore on `Report::render()`, and each also names
  leaving the next wider rule unbuilt, which the key accepts alongside it.

### Judgements made in marking

Made as a careful reader of the document would, as `ACCEPTANCE.md` requires. Where a rule settles
the point, the record says which.

- **J1. The sentence.** Where a reader wrote more than one sentence before or around its
  quotations, all of that text is read with the quotations as the answer. No mark turns on it.
- **J2. 2d's element (iii) needs a place named.** The key says of (iii) that "naming one of the
  two places is enough" and that an answer presenting them as alternatives is wrong; "enough" sets
  a minimum, and a key that let an answer name no place would have no minimum to state and no
  alternatives to forbid. Runs 19, 21, 23 and 25 read it the same way. Reader 1's miss on 2d turns
  on it; readers 3 and 5 miss (ii) as well. Read otherwise, reader 1 would be correct and 2d three
  of five; 2d would still fail on readers 3 and 5, whose misses on (ii) rest on no judgement, and
  the verdict would not change.
- **J3. Elided quotations.** A quotation with an ellipsis is read as one quotation per unbroken
  run of words, each in the document's order, and states only what those runs state (reader 4's
  third 2d quotation; reader 5's clause 3.2 passage). Settled by the rule on quoting: consecutive
  words of any length. Every run in reader 4's quotation is verbatim.
- **J4. Clause labels.** A clause number given with a quotation, as question 4 asks, is read as
  the quotation's label, not as naming the whole clause, as runs 21, 23 and 25 read it. Reader 2's
  "Section 3.3, Part B" and reader 3's "Clause 3.3, Part B" labels do not extend their passages to
  all of Part B, so the two are not the same passage: reader 2's lies in the paragraph beginning
  "A [Narrowing] reduces the [Practitioner]'s own work" and the table's first row, reader 3's in
  the paragraph beginning "**An inline ignore comment, an ignore entry or a [Baseline]**".
- **J5. Passages set beside the main one count.** Where a reader says it was confused by two
  passages read together, a careful reader takes both as the confusing passage, since the
  confusion lies in neither alone, as runs 23 and 25 read it. So reader 3's section 7 item covers,
  by its description "the recorded-decision condition that clause 3.5 itself sets", the sentences
  of clause 3.5's opening paragraph that set it; reader 4's clause 3.5 item covers section 7's
  "it fails rather than warns"; reader 2's Part B item covers the table's first row, which gives
  the [Narrowing] to the [Practitioner]; reader 4's clause 3.1 item covers both step 4 and the
  paragraph beginning "**What this clause leaves on the record**". Reader 2's section 2 item says
  that "In 3.1 the same phrase refers to ways of searching for instances" and that it could not
  tell "whether the two uses were meant to share the same test of independence"; the test of
  independence is clause 3.1's sentence "Two techniques are independent when they would miss
  different things.", so the description is read as naming that sentence, as run 25 read reader
  5's like description. A finding turns on this: clause 3.1's paragraph beginning with that
  sentence, run 25's open passage, is not cleared on it. Read as context only, that paragraph is
  named by no reader and is cleared; the verdict would not change.
- **J6. "Two independent search techniques" (reader 4, question 1).** Reader 4's second bullet
  says the out-of-scope conclusion is stated "in one sentence naming two independent search
  techniques"; section 2's sentence asks for "at least two independent techniques tried at
  expressing the [Rule]". Read for its gist, the bullet names section 2's obligation to state that
  conclusion in one sentence naming two independent techniques and to record it, an obligation
  the document states, with the techniques mislabelled; it is marked correct. Read as asserting a
  different obligation, it would be the reader's miss, since the bullet quotes nothing, question 1
  would be four of five and the second criterion still met. Reader 2 names the same sentence under
  question 4.
- **J7. 3.6 Partial and "the versioning sentence" (reader 4).** The key accepts Partial "where the
  reasoning quotes the versioning sentence". Clause 3.6's versioning requirement is now the one
  sentence "**A [Rule]'s documentation MUST be versioned with the [Rule].**", which reader 4 quotes
  verbatim; it is the versioning sentence on either sense run 25 considered, so no mark turns on
  which.
- **J8. The remediation item.** The key's answer is that the remediation does not conform, giving
  3.2, 3.4 and 3.6 as the reason. A reader saying it does not conform and naming among the failing
  clauses one the key names is correct, as runs 23 and 25 marked it; every reader names 3.4. Reader
  4 names 3.1, 3.4 and 3.5, having graded 3.2 and 3.6 Partial; it asserts nothing the key marks
  wrong.

## Passages quoted as confusing

Same passage as `ACCEPTANCE.md` defines it: sentences in common, or the same paragraph; a list
item, table row or terminology entry is its own paragraph.

| Passage                                                       | Clause      | Readers   | Words quoted, verbatim, or the description used                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------- | ----------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Where the grounds for a weaker kind are recorded              | 3.2         | two: 1, 5 | 1: "on the [Rule]'s [Remediation docs] and in the description of the commit that adds the [Rule], moves it to another [Detector], or first records the grounds." 5: "...naming the [Detectors] of the stronger kind that were considered, on the [Rule]'s [Remediation docs] and in the description of the commit that adds the [Rule], moves it to another [Detector], or first records the grounds." Both in the paragraph beginning "On the [Remediation docs] of a [Rule] they write". Run 21's open passage (below) |
| What a defence must satisfy of clause 3.5                     | 3.5 and 7   | two: 3, 4 | 3: "A Defence Conforms if it satisfies clauses 3.1, 3.2, 3.3, 3.5 and 3.6: … it fails rather than warns, …", in section 7's paragraph beginning "**A [Defence] [Conforms]**", set beside, by description, "the recorded-decision condition that clause 3.5 itself sets" (J3, J5). 4: "neither does a [Rule] whose green run depends on a [Suppression] that no recorded decision covers", in clause 3.5's opening paragraph, set beside section 7's "it fails rather than warns" (J5)                                    |
| Independent techniques for expressing a rule and for a search | 2 and 3.1   | one: 2    | "stated in one sentence, naming at least two independent techniques tried at expressing the [Rule]", in section 2's "Attempt rather than pre-judge" paragraph, set beside, by description, clause 3.1's "same test of independence" (J5). Run 25's open clause 3.1 passage (below)                                                                                                                                                                                                                                       |
| Narrowings enumerated and reported as if suppressions         | 3.3, Part B | one: 2    | "Every [Narrowing] MUST be enumerable by the same means as the project's [Exceptions]..." and "a [Narrowing] that excludes more code than the [Rule] still covers MUST be reported to the [Owner] as if it were a [Suppression].", in the paragraph beginning "A [Narrowing] reduces the [Practitioner]'s own work", set beside, by description, the table's [Narrowing] row (J3, J4, J5)                                                                                                                                |
| An inline ignore is not judged under clause 3.3               | 3.3, Part B | one: 3    | "An inline ignore comment, an ignore entry or a Baseline left over an Instance that carries the Hazard is not judged under this clause. Leaving an Instance that carries the Hazard in place behind one is not a Narrowing, whatever note accompanies it. It is a Suppression of the Instance. Clauses 3.4 and 3.5 and section 4 govern it, and it does not fail this clause." (J4)                                                                                                                                      |
| Leaving the next wider rule unbuilt                           | 4           | one: 1    | "It is a reason not to widen unasked, not authority to leave the wider [Rule] out, and recording it as a known gap does not make it the [Practitioner]'s decision.", in section 4's list item beginning "Leaving unbuilt the next wider [Rule]"                                                                                                                                                                                                                                                                          |
| Step 4 and the record of the next wider rule                  | 3.1         | one: 4    | "Where the [Class] stays at the reported [Instance], name the next wider [Rule] and why it was not built.", step 4 of the five steps, set beside "the next wider [Rule] that was not built, with the reason", in the paragraph beginning "**What this clause leaves on the record**" (J5)                                                                                                                                                                                                                                |
| The default owner's decisions recorded                        | 1, Owner    | one: 5    | "The default [Owner] is usually the person under the same deadline as the [Practitioner], so a decision they take under section 4 to keep an [Instance] unfixed, [Suppress], [Baseline] or remove a [Rule] MUST be recorded in the project record with its justification."                                                                                                                                                                                                                                               |

Readers' accounts of what they could not tell are recorded with the passage they attach to and are
not suggestions; none of the sheets proposes a change.

**Earlier passages (the fourth row).** The open passages are those earlier runs of this document
found confusing by two or more and did not clear: run 25's three, of which one is run 21's clause
3.2 passage, not cleared by runs 23 or 25. Every other passage of runs 19, 21 and 23 was cleared
in runs 21, 23 and 25. As the paragraphs read in the changed document:

- Clause 3.2's grounds and record, run 21's passage, which run 23 read as the grounds sentence of
  the paragraph beginning "**Qualifying is not the same as being the right host.**", the paragraph
  now beginning "For the second ground", and the record paragraph beginning "On the \[Remediation
  docs\] of a [Rule] they write", whose record sentences run 23 found kept from run 21's paragraph.
  Readers 1 and 5 name the last part of the record paragraph's second sentence. Not cleared.
- Clause 3.5's sentence on the entry point for a [Bundled defence], now the paragraph beginning "A
  [Bundled defence] is a [Defence] that a shipped [Toolchain] enables by default": named by no
  reader. Readers 3 and 4 name clause 3.5's opening paragraph, not this one. Cleared.
- Clause 3.1's paragraph beginning "Two techniques are independent when they would miss different
  things.": named by reader 2 by description (J5). Not cleared.

No sentence kept from the cleared paragraph is named elsewhere in the document. Three passages
named here by one reader were once open and have since been cleared: section 4's list item on
leaving the next wider rule unbuilt (run 21, three readers; cleared in run 23), named by reader
1; the Owner entry in section 1 (run 23, two readers; cleared in run 25), named by reader 5; and
section 2's "Attempt rather than pre-judge" paragraph (run 19; cleared in run 21), named by reader
2\. Each is recorded as one reader's. The section 7 and clause 3.5 passage named here by readers 3
and 4 was named by one reader, reader 2, in run 25, and is a new finding here.

## Findings applied

Applied to the text, never to a question, threshold, fixture or key, in c6ee1a8 and the commit after
it that settles its review (key quotations kept verbatim in 224579f and that commit). The editor
first read every sheet, in runs 19 to 27, that named each passage, and fixed the cause the sheets
show. SPEC.md: clause 3.2 states the two grounds in their own sentence after the strongest-kind
sentence and names the two places early in the record sentence; section 7 states that a defence
conforms only where clause 3.5 is met in full, including its recorded-decision condition; clause 3.1
uses "technique" in one sense only and says when a search per spelling counts. A fresh cohort
follows.

## Process change

Made under a process change before it merged: yes, pull request 13 at commit 598908b, named
before the readers started.

## Verdict

**FAIL.** Against the criteria in `ACCEPTANCE.md`:

- Load-bearing statements: not met. 2a, 2b and 2c five of five; 2d two of five. Readers 3 and 5
  state neither ground for a weaker kind, only that there are two; readers 1, 3 and 5 name no
  place for the record (J2).
- Restatement and application: met. Question 1 and every keyed item of question 3 five of five.
- Misses traceable to the text, each a finding: 2d for readers 1, 3 and 5, each quoting clause
  3.2's sentence "A [Rule] the [Practitioner] writes MUST be written in the strongest kind of
  [Detector] that can express it: a [Semantic] one, else a [Syntactic] one, else a [Textual]
  one."; readers 3 and 5 on the grounds for a weaker kind, which they say are two without stating
  them, and readers 1, 3 and 5 on the record of those grounds, which they give without the place
  it is recorded (reader 1's on J2).
- Passages found confusing by two or more, each a finding that blocks until the text is changed
  and a fresh cohort no longer names it: clause 3.2's record paragraph beginning "On the
  [Remediation docs] of a [Rule] they write", the places named at the end of its second sentence
  (two readers), which is also run 21's open passage, not cleared; section 7's paragraph beginning
  "**A [Defence] [Conforms]**", its "it fails rather than warns", against clause 3.5's opening
  paragraph on a [Suppression] no recorded decision covers (two). Run 25's clause 3.1 paragraph
  beginning "Two techniques are independent when they would miss different things." is not
  cleared (one reader, on J5). Run 25's clause 3.5 passage on the [Bundled defence] is cleared.
- Single-reader notes, recorded: section 4's list item on leaving the next wider rule unbuilt
  (reader 1); section 2's "Attempt rather than pre-judge" paragraph, and clause 3.3 Part B's
  paragraph on narrowings enumerated and reported as if suppressions with the table's [Narrowing]
  row (reader 2); clause 3.3 Part B's paragraph on an inline ignore (reader 3); clause 3.1's step
  4 against its record paragraph (reader 4); the Owner entry's sentence on the default owner's
  decisions (reader 5).

Answer sheets, the reader prompt, the command and the marker's instruction: posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090998641), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090998842), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090999356), [comment 4](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090999753).
