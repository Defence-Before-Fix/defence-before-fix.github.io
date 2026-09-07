# Defence Before Fix

> **Defence Before Fix** is a phase that runs *before* a defect is fixed. Rather than dropping
> straight into remediating the specific instance in front of you, you first treat that instance
> as evidence of a class, and you build the automated defence that detects every occurrence of
> that class across the whole codebase. The defence is only trusted once it has been seen to fire.

Six clauses, in order:

1. **Attribute the defect to a class.** Not "what went wrong here" but "what kind of thing is
   this an instance of", within a lower bound and an upper bound that are both checkable.
2. **Build the net.** A rule that reads code, in whatever detector the toolchain offers, bespoke
   where nothing off the shelf will take it.
3. **Prove the net by making the rule fire.** Red before green, on the originating instance,
   committed before the fix.
4. **Sweep the codebase, then fix every instance.** The count is the finding; the fix addresses
   the hazard, not the rule.
5. **Enforce permanently, and block.** Through the project's own entry point for accepting
   changes, failing rather than warning.
6. **Make the failure message terse, and point it at real documentation.** Versioned with the
   rule, resolvable from the identifier as printed.

## The documents

| Document                             | What it is                                                                          | Version         |
| ------------------------------------ | ----------------------------------------------------------------------------------- | --------------- |
| [SPEC.md](SPEC.md)                   | The method. Normative. What a practitioner does when a defect is found.             | 1.0.0           |
| [TOOLING-SPEC.md](TOOLING-SPEC.md)   | The toolchain. What a toolchain must offer so that a practitioner can do it.        | 0.1.0, draft    |
| [PRIMER.md](PRIMER.md)               | The short introduction.                                                             |                 |
| [PROVENANCE.md](PROVENANCE.md)       | Who coined the term, when, and what is and is not claimed.                          |                 |
| [CHANGELOG.md](CHANGELOG.md)         | Changes to each document, versioned independently.                                  |                 |

The method specification is the source of truth for what the method is. Where anything else
describing Defence Before Fix disagrees with it, including the article in which the term was first
published, the specification is correct.

## Tools that implement it

- [php-qa-ci](https://github.com/LongTermSupport/php-qa-ci), the PHP toolchain
- [ts-qa-ci](https://github.com/LongTermSupport/ts-qa-ci), the TypeScript toolchain

Each records the toolchain specification version it conforms to.

## Checking the documents

`spec-qa.py` is the repository's own defence: every defined term is a heading in the terminology
section, every use in the body is a capitalised link to it, and a bare occurrence of a defined
word is a finding. It runs in CI on every push.

```
python3 spec-qa.py
```

## Attribution

Coined by [Joseph Edmonds](https://ltscommerce.dev) of
[Edmonds Commerce](https://edmondscommerce.co.uk). First published 22 February 2026 in
[Defence Before Fix: Preventing Bug Classes with Static Analysis](https://ltscommerce.dev/articles/defence-before-fix-static-analysis).
US spelling: Defense Before Fix.

The documents are licensed under
[Creative Commons Attribution 4.0 International](LICENSE). `spec-qa.py` is under the same
licence.
