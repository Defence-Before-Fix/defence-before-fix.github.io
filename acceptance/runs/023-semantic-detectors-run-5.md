# Run 23: SPEC.md, semantic detectors, fifth run in pull request 14

- **Document**: SPEC.md
- **Pull request**: [14](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14),
  branch `editor/semantic-detectors` at 0b8d699, the commit the readers were given; the question
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
  fixture at 0b8d699, in that order, each preceded by one `===== FILE: <name> =====` line, with
  nothing else added apart from one blank line between the end of each file and the next file's
  marker line.
- **Managed (policy) settings**: none; the machine applies no managed settings to the readers and
  no managed settings file is present, as the editor supplied
- **The rest of the isolation**: attested by the editor
- **Readers set aside**: none. Every sheet has answer text, no process reports an error
  (`is_error` false, subtype `success`), and every reported model is the cohort's model. The
  editor reports no reader set aside for a cause the sheets cannot show.
- **Run within the pull request**: 5, counting void runs; runs in the pull request so far: 5 (19,
  20, 21, 22 and this one). Run 24, on DETECTOR-SPEC.md, is made at the same time and does not
  bear on this document.
- **Marked by**: a delegated marker, a fresh `dbf-spec-editor` agent (Claude Opus) dispatched with
  the editor's instruction and its agent definition, `.claude/agents/dbf-spec-editor.md`, having
  seen neither the drafting nor the review. It read `ACCEPTANCE.md` and
  `acceptance/runs/README.md` in this worktree, which differ from commit 204f95b only by this pull
  request's question-set line adding 2d for SPEC.md; the document, question set, key and fixture
  at 0b8d699; run 21 in full and run 19 in part; and, for the fourth pass-criteria row, the change
  to SPEC.md between 3aefdd1, the document run 21 read, and 0b8d699. It also looked at the key's
  commit history, which a delegated marker is not given; no mark rests on it (J2 is reasoned from
  the key's text at 0b8d699).

## Marks

`ok` is correct, `miss` is a miss; `T` marks a miss traceable to the text. Judgements J1 to J8
are set out below.

| Reader | Q1      | 2a  | 2b  | 2c  | 2d     | 3.1     | 3.2     | 3.3    | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 | Q4 passages |
| ------ | ------- | --- | --- | --- | ------ | ------- | ------- | ------ | --- | --- | --- | ----------- | ------- | --------- | ----------- |
| 1      | correct | ok  | ok  | ok  | miss T | No      | No      | Yes ok | No  | No  | No  | ok          | ok      | ok        | six         |
| 2      | correct | ok  | ok  | ok  | miss T | Partial | Partial | Yes ok | No  | No  | No  | ok          | ok      | ok        | three       |
| 3      | correct | ok  | ok  | ok  | miss T | No      | Partial | Yes ok | No  | No  | No  | ok          | ok      | ok        | three       |
| 4      | correct | ok  | ok  | ok  | miss T | No      | Partial | Yes ok | No  | No  | No  | ok          | ok      | ok        | two         |
| 5      | correct | ok  | ok  | ok  | miss T | No      | Partial | Yes ok | No  | No  | No  | ok          | ok      | ok        | three       |

Every grade under 3.1, 3.2 and 3.4 to 3.6 is one the key accepts. No reader grades 3.2, 3.5 or
3.6 Yes, so none of the key's cases that count against the document arises.

### Question 1

Five of five correct. Every sheet has at least four bullets naming obligations the key lists
(class and hazard, the strongest kind of detector, the proof in a commit of its own, the sweep and
the fix of every instance, permanent and blocking, the terse message with an identifier resolving
to versioned documentation), and no bullet asserts an obligation the document does not state.
Reader 5's second bullet, recording one sentence naming two techniques tried where no rule can be
written, is section 2's "Attempt rather than pre-judge" paragraph; the closing "fix the original
defect with a reproducing test" of readers 2, 3 and 5 is section 6 and Appendix A's last sentence.

### Question 2

Every reader quoted words of the document for every item, so every miss here is traceable to the
text.

- **2a**, five of five. Each states class, rule, proof, sweep and the fix of every instance, in
  that order, and quotes section 2's sentence "The order is section 3's: attribute the [Defect] to
  a [Class], build the [Rule], prove that it fires, run the [Sweep], then fix every [Instance]."
- **2b**, five of five. Readers 1, 2, 3 and 4 say the owner is a human; reader 5 says "Only the
  Owner" (J4). All five quote the key's section 4 sentence and say an agent may not.
- **2c**, five of five. Each states all six clauses and a verdict resting on reproduction, not on
  the report, in its sentence or its quotation of section 7; reader 2's second quotation gives the
  red and green reruns. No reader accepts the pull request description as the verdict.
- **2d**, none of five. The key's three elements are (i) the strongest kind, in the order
  semantic, syntactic, textual; (ii) both grounds for a weaker kind; (iii) the reason recorded,
  with at least one place named and the places not given as alternatives (J2).
  - Reader 1: (i) in its first quotation. (ii) missed: "A weaker kind is allowed 'on two grounds
    only'" says there are two and states neither, and its second quotation, "which of the two
    grounds above holds and why, naming the [Detectors] of the stronger kind that were
    considered", does not state them either. (iii) missed: that quotation stops before the places.
  - Reader 2: (i) and (ii) stated, the second quotation giving both grounds. (iii) missed: "the
    practitioner must record which ground holds and why", with a quotation ending at "were
    considered...", names no place (J2).
  - Reader 3: (i) and (iii) stated, its second quotation naming the remediation docs "and" the
    commit description. (ii) missed: "A weaker kind is allowed only on one of two grounds", and no
    quotation states them.
  - Reader 4: (i) and (ii) stated. (iii) missed: "The record must include 'for each step down from
    [Semantic], which of the two grounds above holds and why, naming the [Detectors] of the
    stronger kind that were considered'" names no place (J2).
  - Reader 5: (ii) and (iii) stated, the places given with "and". (i) missed: "A Rule must be
    written in the strongest detector kind that can express it", and neither quotation names
    semantic, syntactic or textual (J3).

### Question 3

Five of five on every keyed item.

- **3.3**: five of five Yes. Each says the inline ignore is a [Suppression] not judged under this
  clause, as Part B's opening now says; none attributes it to 3.3. Reader 5's caveat that the
  fixture does not show a fresh-checkout reproduction leaves its grade at Yes.
- **Remediation**: five of five say it does not conform, each naming at least one failing clause
  the key accepts.
- **Defence**: five of five say it does not conform, each naming 3.6, and readers 1, 2, 3 and 4
  naming 3.2 as well.
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
  alternatives to forbid. Runs 19 and 21 read it the same way. Readers 2 and 4 miss on this
  alone; read otherwise, both would be correct on 2d and the 2d miss would rest on readers 1, 3
  and 5. The verdict does not turn on it.
- **J3. 2d's element (i) needs the order (reader 5).** The key's element is "the strongest kind
  that can express the rule, in the order semantic, syntactic, textual". "The strongest detector
  kind that can express it" names no kind, and the question asks which kind. Read otherwise,
  reader 5 would be correct on 2d; the verdict would not change.
- **J4. "The Owner" (reader 5, 2b).** Settled by the rule that a defined term used in its defined
  sense states what it means: [Owner] is "Always a human".
- **J5. Every passage under question 4 counts, including one set beside the main passage.**
  Settled in part by the rule that "a quotation under question 4, of any length" covers what its
  words overlap, and that a passage named "by clause number or description" covers what it names.
  Where a reader says it was confused by two passages read together, a careful reader takes both
  as the confusing passage, since the confusion lies in neither alone. So reader 1's description
  of the Narrowing entry, its "Fix them all" and its section 4 sentence, and reader 3's
  description of the Semantic entry's "need not accept bespoke [Rules]" sentence, are recorded as
  passages. The finding on the Narrowing entry turns on this: read only as context, reader 1's
  description would leave the entry to reader 4 alone. No other finding turns on it.
- **J6. Elided quotations.** A quotation with an ellipsis is read as one quotation per unbroken
  run of words, each in the document's order (reader 5's 3.3 passage, reader 2's 3.5 passage).
  Settled by the rule on quoting: consecutive words of any length.
- **J7. Clause labels.** A clause number given with a quotation, as question 4 asks, is read as
  the quotation's label, not as naming the whole clause, as run 21 read it. Reader 5's "Clause
  3.3, Part B" label on "the [Practitioner]'s to decide", which lies in the paragraph introducing
  the three parts, does not extend the passage to all of Part B.
- **J8. The earlier 3.2 passage, as it reads in the changed document.** Run 21's passage lay in
  clause 3.2's two numbered grounds and the paragraph that began "For the second ground". In the
  changed document the grounds are one sentence at the end of the paragraph beginning
  "**Qualifying is not the same as being the right host.**", and the "For the second ground"
  paragraph is split: its sentences on when the language has a detector of the stronger kind and
  when one accepts bespoke rules, reworded, form the paragraph beginning "The language has a
  [Detector] of the stronger kind", and its record sentences, kept, form the next paragraph,
  beginning "On the [Remediation docs] of a [Rule] they write". All three are read as that
  earlier paragraph and list as they now read.

## Passages quoted as confusing

Same passage as `ACCEPTANCE.md` defines it: sentences in common, or the same paragraph; a list
item, table row or terminology entry is its own paragraph.

| Passage                                                                      | Clause       | Readers        | Words quoted, verbatim, or the description used                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------- | ------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The lower bound, the exact value or name and the rejection of the wider rule | 3.1          | three: 1, 2, 4 | 1 and 4: "A [Rule] drawn to the exact value or name found in the [Defect] is the same [Narrowing] however it is spelt." 2: "That rejection is tested as a [Narrowing] is under clause 3.3: a sentence stating why the [Hazard] cannot arise in the code the wider [Rule] would add, confirmed by search, with uncertainty routed upwards under section 4." All in the lower-bound list item |
| The Owner entry                                                              | 1, Owner     | two: 1, 5      | 1: "Where the project has recorded nobody, the [Owner] is whoever instructed the [Practitioner]." 5: "Always a human." and "Where the project has recorded nobody, the [Owner] is whoever instructed the [Practitioner]."                                                                                                                                                                   |
| The Narrowing entry                                                          | 1, Narrowing | two: 1, 4      | 4: "[Narrowing] that excludes code which does carry the [Hazard] is a [Suppression]." 1: by description, "The terminology section defines [Narrowing] as reducing a rule's scope to stop reporting code without the hazard" (J5)                                                                                                                                                            |
| When the language has a detector of the stronger kind                        | 3.2          | one: 3         | "The language has a [Detector] of the stronger kind when the project already runs one, or the language's own [Detector] ecosystem offers one." Run 21's open passage (J8)                                                                                                                                                                                                                   |
| The two grounds for a weaker kind                                            | 3.2          | one: 3         | "no [Detector] of the stronger kind that accepts bespoke [Rules]", in the sentence that allows a weaker kind on two grounds. Run 21's open passage (J8)                                                                                                                                                                                                                                     |
| A semantic detector need not accept bespoke rules                            | 1, Semantic  | one: 3         | By description, "which the terminology says may not accept bespoke rules" (J5)                                                                                                                                                                                                                                                                                                              |
| Where a gap is recorded                                                      | 3.2          | one: 2         | "A gap is recorded in the project record where the [Toolchain] defines one, as the [toolchain specification](TOOLING-SPEC.md) requires it to; only where it does not is the location the project's choice, and then the only requirement is that somebody deciding what to invest in the [Toolchain] would find it."                                                                        |
| The entry point for a bundled defence                                        | 3.5          | one: 2         | "For a [Bundled defence], the project whose entry point demonstrates it is any project the [Toolchain] is genuinely installed into, the [Consuming project] included", and the terms "Bundled defence" and "Consuming project", which occur only in that sentence                                                                                                                           |
| Narrowings enumerable and reported to the owner                              | 3.3, Part B  | one: 5         | "Every [Narrowing] MUST be enumerable by the same means as the project's [Exceptions]" and "a [Narrowing] that excludes more code than the [Rule] still covers MUST be reported to the [Owner] as if it were a [Suppression]" (J6)                                                                                                                                                          |
| The three parts of clause 3.3                                                | 3.3          | one: 5         | "the [Practitioner]'s to decide" (J5, J7)                                                                                                                                                                                                                                                                                                                                                   |
| A defence conforming whilst the sweep is incomplete                          | 7            | one: 1         | "A [Defence] can [Conform] whilst the [Sweep] is incomplete."                                                                                                                                                                                                                                                                                                                               |
| Fix them all                                                                 | 3.4          | one: 1         | "Fix them all" (J5)                                                                                                                                                                                                                                                                                                                                                                         |
| The dividing line, an agent's authority                                      | 4            | one: 1         | "An [Agent] MUST NOT [Baseline], suppress or knowingly leave an [Instance] unfixed" (J5)                                                                                                                                                                                                                                                                                                    |

Readers' accounts of what they could not tell are recorded with the passage they attach to and are
not suggestions; none of the sheets proposes a change.

**Earlier passages (the fourth row).** Run 21 found four passages named by two or more readers,
the open ones. As the paragraphs read in the changed document:

- Clause 3.2's two grounds and the "For the second ground" paragraph (J8): reader 3 names a
  sentence of the paragraph beginning "The language has a [Detector] of the stronger kind", and
  words of the sentence that now states the two grounds. Not cleared.
- Section 4's bullet on leaving the next wider rule unbuilt: named by no reader. Reader 2's 3.1
  passage is in clause 3.1's lower-bound list item, not the bullet. Cleared.
- The fourth column of table row 3.1 in section 3: named by no reader. Cleared.
- Section 4's lead-in, now "**Decisions that MUST go to the [Owner]**, which the [Practitioner]
  never takes alone:": named by no reader. Reader 1's section 4 sentence lies in the paragraph
  beginning "The dividing line", not the lead-in. Cleared.

No sentence kept from one of the three cleared paragraphs is named elsewhere in the document.
Reader 1's "Fix them all" lies in the clause 3.4 paragraph run 19 named and run 21 cleared; it is
not an open passage and is recorded above as one reader's.

## Findings applied

Applied to the text, never to a question, threshold, fixture or key, in b172fd6 and the Owner fix
after its review (key quotations kept verbatim in 296aad5). SPEC.md: clause 3.2's record sentence
names both grounds itself, and its sentence on when the language has a detector of the stronger kind
is plain; clause 3.1's lower-bound item is in short, plain sentences; section 1's Owner entry says
plainly who the default Owner is, the first human up the chain of instructions, and its Narrowing
entry says plainly when a narrowing is a suppression. A fresh cohort follows.

## Process change

Made under a process change before it merged: yes, pull request 13 at commit 204f95b, named
before the readers started.

## Verdict

**FAIL.** Against the criteria in `ACCEPTANCE.md`:

- Load-bearing statements: not met. 2a, 2b and 2c five of five; 2d none of five. Readers 1 and 3
  state neither ground for a weaker kind, only that there are two; readers 1, 2 and 4 name no
  place for the record (J2); reader 5 does not give the order semantic, syntactic, textual (J3).
- Restatement and application: met. Question 1 and every keyed item of question 3 five of five.
- Misses traceable to the text, each a finding: 2d for all five readers, on clause 3.2's
  paragraph beginning "**Qualifying is not the same as being the right host.**" and the record
  sentence "Where that kind is weaker than [Semantic], the [Practitioner] MUST also record, for
  each step down from [Semantic], which of the two grounds above holds and why, naming the
  [Detectors] of the stronger kind that were considered, on the [Rule]'s [Remediation docs] and in
  the description of the commit that adds the [Rule], moves it to another [Detector], or first
  records the grounds.", which every reader quotes.
- Passages found confusing by two or more, each a finding that blocks until the text is changed
  and a fresh cohort no longer names it: clause 3.1's lower-bound list item (three readers); the
  Owner entry in section 1 (two); the Narrowing entry in section 1 (two, on J5). Run 21's clause
  3.2 passage is not cleared: reader 3 names the paragraph beginning "The language has a
  [Detector] of the stronger kind" and the sentence stating the two grounds (J8). Run 21's other
  three passages are cleared.
- Single-reader notes, recorded: the Semantic entry (reader 3); clause 3.2's paragraph on where a
  gap is recorded (reader 2); clause 3.5's bundled defence sentence (reader 2); clause 3.3's
  paragraph on narrowings enumerable and reported to the owner, and its three-parts paragraph
  (reader 5); section 7's conforming defence over an incomplete sweep (reader 1); clause 3.4's
  "Fix them all" (reader 1); section 4's "An [Agent] MUST NOT" sentence (reader 1).

Answer sheets, the reader prompt, the command and the marker's instruction: posted on pull request 14 in [comment 1](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090684297), [comment 2](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090684613), [comment 3](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090684941), [comment 4](https://github.com/Defence-Before-Fix/defence-before-fix.github.io/pull/14#issuecomment-6090685201).
