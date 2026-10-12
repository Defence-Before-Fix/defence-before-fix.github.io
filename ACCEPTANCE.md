# Acceptance test for changes to the specifications

Every change to `SPEC.md`, `DETECTOR-SPEC.md` or `TOOLING-SPEC.md` MUST pass this test before it
is merged to `next`, and so before it is published. It is the specifications' own defence: a
document that only a strong reader can follow is not a specification, and the readers that
matter most, coding agents meeting the method in a failing pipeline, are often the weakest. The
test is run with a low-strength model so that clarity is measured at the floor, not the ceiling.

The test proves one thing: that a capable reader, reading the document cold and once, takes from
it what the document exists to say, and is not confused by the text the change put there. The
keyed questions prove the document; the confusion question proves the change. Everything below
serves that, and a rule that stops it proving that is a defect in this file, fixed as
[Changes to this process](#changes-to-this-process) describes.

## The cohort

- **An odd number of independent readers, at least five**, each a fresh instance of a
  low-strength model (the smallest current model in its family, for example Haiku), with no
  shared context and no access to the change history, the critique findings or each other.

- **Each reader is a separate process with no tools and no project context, only its packet**:
  started from an empty directory outside any repository, with no user, project or local settings
  files, no `CLAUDE.md`, skills, plugins, hooks or MCP servers, and no saved session, so that no
  project instruction reaches it. The model tool's own fixed system prompt is not project
  context. For example, with the packet on standard input:

  ```
  claude -p --safe-mode --model haiku --tools "" --setting-sources "" --strict-mcp-config --no-session-persistence --output-format json < packet.md
  ```

  A reader is set aside, and its answers do not count, when its answer text is empty, when its
  process reports an error, or when the model version it reports is not the cohort's model, the
  one version the editor names for the run before its readers start. A run
  with a reader set aside is void: it takes a run number and has a record, and a fresh cohort
  runs. No reader is set aside for any other cause.

- Each reader receives **only its packet**: the document's question set, the changed document
  and the fixture the questions name, each in full in the reader's prompt, the question set
  first. Each file is preceded by exactly one line, `===== FILE: <name> =====`, where `<name>` is
  the name the question set gives the file (so `fixtures/remediation-ledger.md`, and
  `QUESTIONS.md` for the question set itself). The question set carries the instruction to the
  reader, and nothing else is added. Every reader in a run receives the same packet.

- Readers are run **after** every stronger review has been applied. They are the last gate, not
  the first draft.

## The question set

Written before the run, with an **answer key** for every keyed question, so that marking is
mechanical. The key states, for each keyed item, exactly what an answer must contain and what
makes it wrong; the question asks for exactly that and nothing the key does not expect. A key
asks for nothing the question does not. Each reader answers all of them.

1. **Restatement.** In their own words, what the document asks of its subject, in at most six
   bullets. Keyed against the key's list of the document's obligations: a bullet is correct when
   it names one of them.

2. **Load-bearing statements.** Three or more questions, fixed per document and listed in its
   question set under `acceptance/`, each asking for a short answer and the sentence or
   sentences of the document it rests on, quoted. Each has one or more parts, and the key lists
   the element an answer must state for each part. An obligation is load-bearing, and gets a
   question, when a reader who misreads it would act against the method; the editor decides, and
   the pull request that adds the question says why.

3. **Application.** A fixture case supplied with the questions, graded clause by clause with
   Yes, Partial or No and one line of reasoning, then the verdicts the question set asks for,
   each with its reason. Keyed against the accepted grades and answers, with the readings the
   key names as ones the text invites counting against the document.

4. **Confusion.** Any passage the reader found confusing on its one reading, quoted with its
   clause number, and nothing else: not what would make it clearer, not a proposed change.

## What the cohort is not asked

The cohort may point at what it found confusing. It is never asked to rate the document, to say
what would make a passage clearer, or to suggest any change, and a suggestion it volunteers is
discarded unread. A low-strength reader is there to show whether the text can be followed; it is
not there to design the text, and a document shaped by what its weakest reader says it wants is
a document designed by that reader. The signals this test takes from the cohort are a keyed
answer missed, a wrong verdict reasoned from the document, and a passage pointed at; what to do
about any of them is the editor's decision. An earlier version of this test asked the reader
what would make a clause clearer and for a clarity rating; both were removed on the editor's
instruction for that reason, and neither is reinstated.

## Marking

The editor marks each answer sheet against the document's key, or delegates the marking to a
separate marker that has seen neither the drafting nor the review. A delegated marker receives
the document, its question set, fixture and key at the commit the readers read, this file, the
answer sheets, and the facts the record needs that the sheets cannot show. Its marks are final
unless the editor shows that a rule here was misapplied, and a re-mark says which rule and why.

Every mark is given by a rule in this file or in the key, as follows. Where neither settles a
mark, the marker records the point in the run record and marks it as the open-point rule below
says, and the editor settles it in this file or in the key, as
[Changing the test](#changing-the-test) allows, before the next run. A run record states no
judgement that is not written here or in the key; a judgement an earlier run recorded is not a
rule.

- **Keyed items.** Question 1 as a whole is one keyed item, and so is each item of question 2
  and each answer of question 3 for which the key gives an accepted grade or answer.
- **Reading an answer.** An answer is read for its sense, not its wording: a paraphrase, a
  synonym, or a defined term used in its defined sense states what it means. A reader quotes the
  document when it gives, in quotation marks or a block quote, a run of six or more consecutive
  words of the document in the document's order, verbatim apart from letter case, quotation-mark
  or apostrophe style, and markdown link or emphasis markup; a quotation that drops or changes a
  word quotes the document by its longest such run.
- **Question 1** is correct when at least four bullets each name an obligation the key lists and
  no bullet asserts one the key marks wrong. Only the first six bullets are marked. Several
  bullets that name different clauses of one line of the key's list each count; two that name
  the same clause count once. A bullet asserting an obligation that is in neither list is not
  counted either way, and is recorded as an open point for the key.
- **Question 2.** An answer is the reader's sentences and its quotation read together. It is
  correct when it states every element the key lists as required for that item, in the
  document's words or the reader's own, asserts nothing the key marks wrong, and quotes the
  document. An element stated only in the quotation is stated. Anything in the key beyond the
  required elements and the wrong assertions is explanation for the marker, and an answer is
  never marked down for leaving it out.
- **Question 3.** Each item is correct when its grade or answer is one the key accepts and,
  where the key sets a condition on the reasoning for it, the reasoning meets it. A grade or
  answer the key accepts with no condition is correct whatever the reasoning. A grade given on a
  stated condition is read as the grade for the case the fixture presents, where the key says
  which case that is; otherwise the item is unanswered.
- **A miss that counts against the document.** The key names, for question 1 and for each item
  of question 3, the wrong readings the text invites, each as a grade or answer together with
  what the reasoning states or leaves out. A miss that matches one blocks whatever the count,
  since one reader in five taking that reading means one agent in five acting on it, and it
  blocks wherever the text lies, because the keyed questions are what prove the document. Every
  other single miss under questions 1 and 3 is the reader's and is tolerated by the threshold
  below; a second miss on the same item fails the threshold, and no judgement is needed.
- **An unanswered question.** Each keyed item left unanswered is a miss. Question 4 left
  unanswered counts as no passage named.
- **Question 4.** A reader names a passage when it quotes the document, as defined above, or
  gives a clause number with a description or a shorter quotation that identifies a sentence or
  paragraph. A quotation whose words occur in more than one paragraph, given with no clause
  number, names the paragraph where they first occur. A remark that is not about a passage of
  the document, such as that another document was not supplied, is recorded as a note and is
  not a passage. Two readers name the same passage when the words or sentences they name lie in
  the same paragraph; a heading, a list item, a table row and a terminology entry are each a
  paragraph of their own. A passage named by two or more readers of the run is a finding.
- **Where a finding lies.** The record says, for each finding, whether it lies in text the change
  wrote or altered: a paragraph in which the pull request, read against its merge base with the
  branch it targets, adds, rewords, moves or deletes a sentence, or changes a word, a term or a
  link; or a paragraph that any reader naming the finding sets against such a paragraph. A
  finding there blocks the change. A finding anywhere else is a finding against the document, not
  against the change: it is recorded in [acceptance/ROUTED.md](acceptance/ROUTED.md), routed to a
  change of its own, and does not block. The change is judged on what it changed; the document
  is proved by the keyed questions, which every run answers over the whole of it.
- **Open points.** An open point in marking an answer is marked for the reader, except that a
  question 1 bullet on neither list is not counted, as above. An open point on whether a reader
  named a passage, or whether two readers named the same one, counts the passage. An open point
  on where a finding lies treats it as the change's own text.

## Pass criteria

The change passes when all of the following hold on a single run. The thresholds apply to the
readers whose answers count; with five readers, "every reader" is five of five and "all but one"
is four of five.

| Criterion                                                                             | Threshold                                                      |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Load-bearing statements (question 2)                                                  | **Every** reader correct on every item                         |
| Restatement and application (questions 1 and 3)                                       | **All but one** reader correct on each keyed item              |
| A miss the key says counts against the document                                       | **None**, whatever the count                                   |
| A passage found confusing by two or more readers, in text the change wrote or altered | **None.** It is a finding and blocks until the text is changed |
| A passage found confusing by two or more readers, elsewhere                           | Recorded in `acceptance/ROUTED.md` and routed; does not block  |
| Anything else from one reader only                                                    | Recorded; applied at the editor's discretion; does not block   |

The asymmetry is deliberate. A load-bearing statement is the sentence the whole document exists
to make, and one reader in five getting it wrong means one agent in five will act on the wrong
reading; unanimity is the only acceptable result there. Everywhere else a single divergent reader
is more likely to be the reader than the text, so one such reader is tolerated, unless the key
says the text invites that reading. A finding is settled run by run: a passage two readers named
in one run has no standing in the next, which is judged on its own readers, and a passage the
fresh cohort names by fewer than two is clear.

## Changing the test

Nothing in this test is changed to let a particular run through. A threshold, a question, a
key, a fixture or a rule here is changed only before a run's readers start, never changes a mark
already given, and is changed by one of two routes, each recorded with its reason:

- In the specification pull request that changes the text, under step 4 of `CONTRIBUTING.md`:
  a key's quotation follows the text it quotes; a key gains an item, with the question that asks
  for it, for a new load-bearing obligation; and where the change alters or removes the
  obligation an existing item tests, the item and its question follow the text, since that is
  the text changing and not the test. `acceptance/README.md` says what that may and may not do.
- By a change to this process, with its own pull request: a threshold, a fixture, a rule here,
  what an existing key item requires of an unchanged obligation, or the wording of a question.

An open point a run recorded is settled by whichever route it needs, before the next run of the
pull request whose run recorded it; a run of another pull request is not held up by it.

A question is reworded only so that it asks for what its key requires, and a key's required
elements are never more than its question asks for. A run made after such a change is a fresh
run under the new rules, not a re-mark of an old one. The test for a change to a rule is what
the rule measured: a rule that measured something other than whether a cold reader could follow
the text is a defect in this file and is corrected, and the correction says what the rule
measured instead; a rule that measured that, and found the text wanting, is not touched, and the
text is fixed. The one time a threshold was relaxed to let a change through, after three runs,
the relaxation was reversed on the editor's instruction and is recorded here so that it is not
tried again. Removing the clarity rating and the request for suggestions was not that: it
changed what the cohort is asked, not how strictly an answer is marked.

## After a failure

Fix the text the run's misses and findings name and run a fresh cohort; readers are never reused.
A failed keyed item is fixed in the text that carries the obligation, wherever it lies, since the
keyed questions prove the document as a whole, whoever wrote the sentence; where that fix would
change an obligation, it is routed to a change of its own, and this change waits for it. A
finding on text the change wrote or altered is fixed there. A finding elsewhere goes to
`acceptance/ROUTED.md` and is not fixed in this change. The number of runs it took is recorded;
a document that needed three runs is telling its editor something.

## When it runs

On the final text of each pull request, after the editor's rewrite and any key update, one cohort
per changed document. It is the last gate before the merge to `next`, so that every change on
`next` is one the cohort has accepted, and the release branch needs no cohort of its own unless it
changes specification text. A fresh cohort runs after every change to the changed document's
text that follows a run, and after every void run; a text that failed is never run again
unchanged, and a commit that adds the run record or the changelog line changes no document. A version number or date that `PUBLISHING.md` or step 5 of `CONTRIBUTING.md` has the
editor set is not such a change, and neither is a merge of `next` into the branch that brings in
text another cohort accepted and alters no sentence this change wrote.

## The record

Each run has a file under `acceptance/runs/`, named `NNN-<slug>-run-<k>.md` with `NNN` the next
number in the one sequence shared by the three documents and `<k>` the run number within the pull
request, stating: the document; the pull request and the commit read; the cohort size and model,
with the model version each reader reported; how the readers were isolated and the command they
were started with; any reader set aside and why; who marked and, for a delegated marker, how it
was started; the marks per reader per keyed item, with each miss and the reader's reasoning in
brief; every passage named under question 4, with the words quoted or the description given, its
clause and the readers naming it; each finding and whether it lies in text the change wrote or
altered; any point the rules did not settle; whether the run was made under a process change
before it merged and, if so, at which commit; the findings applied afterwards; the verdict; and
a link to the answer sheets.

The answer sheets are not kept in this repository. Every reader's whole output as its process
returned it, the exact prompt every reader received, the command the readers were started with,
and the instruction a delegated marker was given are posted in one or more comments on the pull
request, linked from the record and never edited, hidden or deleted after posting.

The changelog line for the change names every run made on it, the passing run last. CI refuses a
specification change whose pull request adds no run file; it checks for at least one, and a pull
request that changes two documents adds a run for each. Each published version's changelog entry
carries the lines of the changes it contains, so a version's cohort record is the set of runs
those lines name. A version with no such line has not been accepted and MUST NOT be described as
published. The question sets and answer keys live under `acceptance/` in this repository so that
a run can be repeated and compared.

`acceptance/ROUTED.md` lists every finding routed from a run, open until a change that fixes
its passage passes a cohort, or until the editor closes it with a recorded reason. The editor
reads that list before cutting a release.

## Changes to this process

The process files are this file, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md` and the checks that enforce them: `tools/changes.py`, the key-quotation checks
in `spec-qa.py`, the CI workflow and the pull request template. A change to any of them is a
change to this process, and so is a change to a threshold, a fixture, the wording of a question
or what a key item requires, as [Changing the test](#changing-the-test) says. They are not
specifications, and a change to them is not tested by a cohort: the cohort measures whether a
low-strength reader can follow a specification, and the process is followed by the editor. Such
a change names the runs or the case that showed the need for it, and goes through steps 1, 3 and
6 of `CONTRIBUTING.md`, with no scope, key or cohort step; its review reads every process file it
changes. It applies to every run whose readers start after it merges; a run made before then may
be made under it, following all of it at a commit named in the record before the readers start.
It is recorded by a line added at the top of [acceptance/CHANGES.md](acceptance/CHANGES.md),
naming its pull request, not in the changelog, which is for the three specifications.
`acceptance/ROUTED.md` and `acceptance/runs/` are records, not process files: a specification
pull request writes to them.
