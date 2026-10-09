# Acceptance test for changes to the specifications

Every change to `SPEC.md`, `DETECTOR-SPEC.md` or `TOOLING-SPEC.md` MUST pass this test before it
is merged to `next`, and so before it is published. It is the specifications' own defence: a
document that only a strong reader can follow is not a specification, and the readers that
matter most, coding agents meeting the method in a failing pipeline, are often the weakest. The
test is run with a low-strength model so that clarity is measured at the floor, not the ceiling.

## The cohort

- **An odd number of independent readers started, at least five**, each a fresh instance of a
  low-strength model (the smallest current model in its family, for example Haiku), with no
  shared context and no access to the change history, the critique findings or each other. The
  editor chooses the size, and may choose a larger cohort the more obligations the change
  touches.

- **Each reader is a separate process with no tools and no project context, only its packet**,
  started from an empty directory outside any repository, with no settings files, no `CLAUDE.md`,
  skills, plugins, hooks or MCP servers, and no saved session, so that no project instruction or
  settings file reaches it. The model tool's own fixed system prompt is not project context. For
  example, with the packet on standard input:

  ```
  claude -p --safe-mode --model haiku --tools "" --setting-sources "" --strict-mcp-config --no-session-persistence --output-format json < packet.md
  ```

  The JSON output gives the model version each reader reported. A reader isolated in this way is
  a cold reader. A reader whose process failed or returned nothing, or that shared the editor's
  context, such as an agent dispatched from the editor's own session, is set aside and its
  answers do not count; no reader is set aside for any other cause, and the record shows the
  cause. If fewer than five readers' answers count, the run is void and a fresh cohort runs,
  unless the readers whose answers count already fail a criterion, when the run fails. A void run
  takes a run number, has a record and posted sheets like any other, and counts towards the
  number of runs.

- Each reader receives **only its packet**: the document's question set, the changed document
  and the fixture the questions name, each in full in the reader's prompt, the question set
  first. Each file is preceded by exactly one line, `===== FILE: <name> =====`, where `<name>` is
  the name the question set gives the file (so `fixtures/remediation-ledger.md`, and
  `QUESTIONS.md` for the question set itself). The question set carries the instruction to the
  reader, and nothing else is added. Every reader in a run receives the same packet. Nothing else
  is read first.

- Readers are run **after** every stronger review has been applied. They are the last gate, not
  the first draft.

The isolation rule above and the answer sheets posted under [The record](#the-record) apply from
run 19; runs 16 to 18 stand as recorded.

## The question set

Written before the run, with an **answer key** for every keyed question drawn verbatim from the
document, so that marking is mechanical. Each reader answers all of them.

1. **Restatement.** In their own words, what the document asks of its subject, in at most six
   bullets. Keyed against the list of MUST clauses: a bullet is correct when it names an
   obligation the document actually states.

2. **Load-bearing statements.** Three questions, fixed per document, each asking for one
   sentence and a quotation:

   - `SPEC.md`: what a practitioner does before fixing a defect, in order; who may baseline or
     suppress; what "conforms" means for a remediation.
   - `DETECTOR-SPEC.md`: what "conforms" means and whether a tool that predates the document can
     conform; what a detector must do about an inline suppression route; where a bundled rule's
     documentation must live.
   - `TOOLING-SPEC.md`: where conformance is measured; how a grade is assigned when parts come
     from different sources; how many grades a project that ships tooling has.

3. **Application.** A fixture case supplied with the questions, graded clause by clause with
   Yes, Partial or No and one line of reasoning. Keyed against the intended verdicts; whether a
   divergence counts against the document is settled by the rule for a miss traceable to the
   text, under [Marking](#marking).

4. **Confusion.** Any passage the reader found confusing on its one reading, quoted with its
   clause number, and nothing else: not what would make it clearer, not a proposed change.

The cohort settles one thing: is the document clear, coherent and comprehensive. A reader getting
everything right after one reading proves it; a reader getting confused fails it. The document
is designed by its editor to resolve the comprehension failures the cohort shows; the cohort is
the acceptance layer, not the designer.

## What the cohort is not asked

The cohort may point at what it found confusing. It is never asked to rate the document, to say
what would make a passage clearer, or to suggest any change, and a suggestion it volunteers is
discarded unread. A low-strength reader is there to show whether the text can be followed; it is
not there to design the text, and a document shaped by what its weakest reader says it wants is
a document designed by that reader. The signals this test takes from the cohort are a keyed
answer missed, a wrong verdict reasoned from the document, and a passage pointed at; what to do
about any of them is the editor's decision. An earlier version of this test asked the reader
what would make a clause clearer and for a clarity rating; both were removed on the author's
instruction for that reason, and neither is reinstated.

## Marking

The editor marks each answer sheet against the document's key, or delegates the marking to a
separate marker that has seen neither the drafting nor the review. Whoever marks is the marker
in this file. A delegated marker receives only these: the document at the commit the readers
read, its question set, the fixture the questions name and its key; this file and
`acceptance/runs/README.md`, with earlier run records of other pull requests as examples of
style only; the answer sheets; and, from the editor, the facts the record states that the sheets
do not, which are the pull request and the commit, the cohort size and model, how the readers
were isolated and the command they were started with, how the marker was started, and the run
number. The marker writes the record, stating those facts as the editor supplied them, and the
editor adds the findings applied and the link to the posted sheets after marking. A delegated
marker's verdict, its marks and its PASS or FAIL, is final unless the editor shows that a rule
in this file was misapplied; the editor then re-marks what the misapplied rule affected, and the
record says which rule and why. Each sheet is marked question by question, as follows.

- **Keyed items.** Question 1 as a whole is one keyed item, and so is each item of question 2
  and each clause verdict and each summary verdict of question 3.
- **Quoting.** A reader quotes the document when it gives five or more consecutive words of the
  document, verbatim apart from markdown link syntax and emphasis markers, as a quotation, in
  quotation marks or a block quote. Naming a clause number, or paraphrasing, is not quoting.
- **Questions 1 and 3** are marked as the key states for each item.
- **Question 2.** An answer is correct when its sentence states what the key's answer states,
  including anything the key says an answer is wrong to omit, asserts nothing the key says makes
  an answer wrong, and quotes the document in support. The quotation need not be the one the key
  gives.
- **A miss traceable to the text** is a miss whose reasoning quotes the document or states, in
  the reader's own words, what the document says or requires, or a miss the key says counts
  against the document. Such a miss is traceable even where it also misreads the fixture, and
  whatever the key says of it: the key can add to the misses that count against the document,
  never take one away. Only a miss whose reasoning states nothing about the document, such as a
  misread fixture alone, is the reader's. Question 1 has no reasoning, so a miss there is
  traceable only where the key says it counts.
- **An unanswered question.** Each keyed item left unanswered is one miss, not traceable to the
  text, so a sheet that leaves three items of question 3 blank has three misses. Question 4 left
  unanswered counts as no passage quoted. A truncated sheet is marked as it stands; a reader
  whose process failed or returned nothing is set aside, as [The cohort](#the-cohort) says.
- **The same passage.** A quotation under question 4 covers every sentence of the document it
  quotes any part of, in every place the quoted words appear, and a passage named without a
  quotation, by clause number or description, covers every sentence of what it names. A heading,
  list item or table row counts as one sentence. Two passages are the same when they cover a
  sentence in common or lie in the same paragraph, and a list item or table row is its own
  paragraph.

Where a mark needs a judgement these rules do not settle, the marker makes it, taking the stricter
reading, the one that records more misses or findings, and the record states the judgement and
why.

## Pass criteria

The change passes when all of the following hold on a single run. The thresholds apply to the
readers whose answers count; with five such readers, "every reader" is five of five and "all but
one" is four of five.

| Criterion                                              | Threshold                                                                                                                         |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| Load-bearing statements (question 2)                   | **Every** reader correct on every one                                                                                             |
| Restatement and application (questions 1 and 3)        | **All but one** reader correct on each keyed item                                                                                 |
| A miss traceable to the text                           | **None.** Any such miss, as [Marking](#marking) defines it, is a finding, whatever the count                                      |
| A passage found confusing (question 4), by two or more | **None outstanding.** It is a finding and blocks until the text is changed and a fresh cohort on the changed text passes this row |
| Anything else from one reader only                     | Recorded; applied at the editor's discretion; does not block                                                                      |

Every row must hold, and the last covers only what none of the others catches. The first, third
and fourth rows block on what a single reader, or for the fourth two readers, did, and the second
row's tolerance of one reader never excuses a miss under the third.

The asymmetry is deliberate. A load-bearing statement is the sentence the whole document exists
to make, and one reader in five getting it wrong means one agent in five will act on the wrong
reading; unanimity is the only acceptable result there. Everywhere else a single divergent reader
is more likely to be the reader than the text, so one such reader is tolerated, but a miss that
the reader can justify from the document is always the document's fault.

## The bar only moves up

No criterion in this document is ever relaxed to let a change through. If the cohort is confused,
the test is working and the text is wrong; the fix is to the text, never to the threshold, the
question, the fixture or the key. A threshold may be raised, a keyed question may be added, a key
may be corrected where it misquoted the document, and a key's limit on which misses count against
the document may be removed, which raises the bar; none of those makes a failing run pass. The
one time a threshold was relaxed, after three runs, the relaxation was reversed on the author's
instruction and is recorded here so that it is not tried again. Removing the clarity rating and
the request for suggestions was not a relaxation: it changed what the cohort is asked, not how
strictly an answer is marked.

## After a failure

Fix the text, never the questions, and run a fresh cohort. Readers are not reused across runs.
The number of runs it took is recorded; a document that needed three runs is telling its editor
something.

## When it runs

On the final text of each pull request, after the editor's rewrite and any key update, and again
after every failure, void run or wording change. It is the last gate before the merge to `next`,
so that every change on `next` is one the cohort has accepted, and the release branch needs no
cohort of its own unless it changes specification text. A wording change is any change to the
document's text after the readers read it, from any source (a review finding, the editor, or
`next` merged into the branch), except the lines `PUBLISHING.md` and step 5 of `CONTRIBUTING.md`
have the editor set for a version: the header, the status paragraph and the citation. A wording
change means a fresh run; readers are never reused.

## The record

Each run has a file under `acceptance/runs/`, named `NNN-<slug>.md` with `NNN` the next number in
the one sequence shared by the three documents, stating: the document, the pull request and the
commit read, the cohort size and model, with the model version each reader reported, how the
readers were isolated and the command they were started with, the run number in that pull
request, who marked and, for a delegated marker, how it was started, the marks per reader per
question, any judgement made in marking, the passages quoted as confusing and by how many
readers, the findings applied, whether it passed, and a link to the answer sheets. The answer
sheets are not kept in this repository: every reader's sheet, unedited, with a set-aside
reader's marked as set aside, and the instruction a delegated marker was given, which is its
task prompt and the agent definition it ran under, are posted in one or more consecutive
comments on the pull request, each linked from the record, so that an owner can check the marks.
The comments also hold the exact prompt every reader received and the command and the form of
the working directory the readers were started in; a sheet cannot show how its process was
started, so the record says that the editor attests the rest of the isolation. A comment is not
edited after posting, and a record whose comment was edited is void; that is checkable only
through GitHub's edit history, which is the limit of keeping the sheets outside the repository.
The changelog line for the change names the file. CI refuses a specification change whose pull
request adds no run file; it checks for at least one, and a pull request that changes two
documents adds a run for each.

Each published version's changelog entry carries the lines of the changes it contains, so a
version's cohort record is the set of runs those lines name. A version with no such line has not
been accepted and MUST NOT be described as published. The question sets and answer keys live
under `acceptance/` in this repository so that a run can be repeated and compared.

## Changes to this process

The process files are this file, `acceptance/README.md`, `acceptance/runs/README.md`,
`CONTRIBUTING.md` and the checks that enforce them: `tools/changes.py`, the key-quotation checks
in `spec-qa.py`, the CI workflow and the pull request template. A change to any part of them is
a change to this process. They are not specifications, and a change to them is not tested by a
cohort: the cohort measures whether a low-strength reader can follow a specification, and the
process is followed by the editor. Such a change names the runs or the case that showed the need
for it, and goes through steps 1, 3 and 6 of `CONTRIBUTING.md`, with no scope, key or cohort
step; its review reads every process file it changes. It applies from its merge into `next`; a
run made before then may follow it, and its record says so. It is recorded by a line added at
the top of [acceptance/CHANGES.md](acceptance/CHANGES.md), naming its pull request, not in the
changelog, which is for the three specifications. It is bound by
[the section on the bar](#the-bar-only-moves-up): it may raise a criterion, never relax one. A
change to a question set, key or fixture is not a change to this process; `acceptance/README.md`
governs those.
