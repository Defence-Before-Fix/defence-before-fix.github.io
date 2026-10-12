# Acceptance question sets

The question sets and answer keys that [ACCEPTANCE.md](../ACCEPTANCE.md) requires. One directory per
specification document, each holding the fixed questions a cold reader answers and the key an
editor marks against. The fixture cases the application question uses live in `fixtures/`, the
record of every run lives in `runs/`, findings routed out of a run to a change of their own are
listed in [ROUTED.md](ROUTED.md), and changes to the acceptance process itself are recorded
in [CHANGES.md](CHANGES.md).

| Document           | Questions                                        | Key                                  |
| ------------------ | ------------------------------------------------ | ------------------------------------ |
| `SPEC.md`          | [method/QUESTIONS.md](method/QUESTIONS.md)       | [method/KEY.md](method/KEY.md)       |
| `DETECTOR-SPEC.md` | [detector/QUESTIONS.md](detector/QUESTIONS.md)   | [detector/KEY.md](detector/KEY.md)   |
| `TOOLING-SPEC.md`  | [toolchain/QUESTIONS.md](toolchain/QUESTIONS.md) | [toolchain/KEY.md](toolchain/KEY.md) |

## How a run works

1. The editor identifies which documents the change touched. Only those are tested.
2. For each, an odd number of fresh low-strength readers, at least five, each isolated as
   `ACCEPTANCE.md` describes, receive the document's current text, its `QUESTIONS.md`, and the
   fixture the questions name. Nothing else: no key, no changelog, no critique findings, no other
   reader's answers.
3. The editor, or a separate marker the editor delegates to, marks each answer sheet against
   `KEY.md` under the marking rules in `ACCEPTANCE.md` and applies its pass criteria.
4. The result is recorded as a file under [runs/](runs/), stating what `ACCEPTANCE.md` lists,
   with the answer sheets posted on the pull request and linked from it, and the change's
   `Unreleased` changelog line names that file. A run that fails is followed by a change to the
   text the findings name and a fresh cohort; a finding on text the change did not write or
   alter is added to [ROUTED.md](ROUTED.md) instead.

## How a key is written

A key says, for each keyed item, exactly what is marked and nothing a marker has to guess:

- **Question 1**: the obligations a bullet may name, and the assertions that make a bullet wrong.
- **Question 2**: for each item, the elements an answer is required to state, numbered, one for
  each part of the question; the assertions that make an answer wrong; and the sentence or
  sentences of the document the answer rests on, quoted verbatim. The required elements are
  what the question asks for, no more: an element the question does not ask for is not
  required, however load-bearing, until the question is reworded to ask for it.
- **Question 3**: for each item, the grade or grades accepted, any condition on the reasoning,
  and the wrong readings the text invites, which count against the document when one reader
  takes them.

Everything else in a key is explanation for the marker and never marks an answer down.

## Keeping the keys honest

A key quotes the document. When a clause is reworded, the key line that quotes it is updated in
the same commit, and the change is one the acceptance run itself then tests. A key that no longer
matches the document is a defect in this directory, not a reason to mark a reader wrong. A key
update under step 4 of `CONTRIBUTING.md` changes a quotation to follow the text, or adds a keyed
item for a new load-bearing obligation; it does not change what an existing item requires. A
change to what an item requires, or to a question, is a change to the process and is recorded in
[CHANGES.md](CHANGES.md) with its reason, before the readers of the next run start.

Questions are fixed so that runs can be compared across versions. Adding a keyed question is
allowed when a new clause is load-bearing; removing or softening one to make a run pass is not;
rewording one is allowed so that it asks for what its key requires, and for no other reason.
The reader may quote a passage it found confusing; it is never asked to rate the document, say
what would make a passage clearer, or propose a change: the cohort confirms comprehension and
does not design the text.
