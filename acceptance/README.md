# Acceptance question sets

The question sets and answer keys that [ACCEPTANCE.md](../ACCEPTANCE.md) requires. One directory per
specification document, each holding the fixed questions a cold reader answers and the key an
editor marks against. The fixture cases the application question uses live in `fixtures/`.

| Document           | Questions                                        | Key                                  |
| ------------------ | ------------------------------------------------ | ------------------------------------ |
| `SPEC.md`          | [method/QUESTIONS.md](method/QUESTIONS.md)       | [method/KEY.md](method/KEY.md)       |
| `DETECTOR-SPEC.md` | [detector/QUESTIONS.md](detector/QUESTIONS.md)   | [detector/KEY.md](detector/KEY.md)   |
| `TOOLING-SPEC.md`  | [toolchain/QUESTIONS.md](toolchain/QUESTIONS.md) | [toolchain/KEY.md](toolchain/KEY.md) |

## How a run works

1. The editor identifies which documents the change touched. Only those are tested.
2. For each, five or more fresh low-strength readers each receive the document's current text,
   its `QUESTIONS.md`, and the fixture the questions name. Nothing else: no key, no changelog, no
   critique findings, no other reader's answers.
3. The editor marks each answer sheet against `KEY.md` and applies the pass criteria in
   `ACCEPTANCE.md`.
4. The result is recorded in the changelog entry for the version, with cohort size, model, run
   count and the findings applied. A run that fails is followed by a change to the text, never to
   the questions, and a fresh cohort.

## Keeping the keys honest

A key quotes the document. When a clause is reworded, the key line that quotes it is updated in
the same commit, and the change is one the acceptance run itself then tests. A key that no longer
matches the document is a defect in this directory, not a reason to mark a reader wrong.

Questions are fixed so that runs can be compared across versions. Adding a keyed question is
allowed when a new clause is load-bearing; removing or softening one to make a run pass is not.
Every question has a key. The reader is never asked to rate the document, name what it found
hard, or say what would make it clearer: the cohort confirms comprehension and does not design
the text.
