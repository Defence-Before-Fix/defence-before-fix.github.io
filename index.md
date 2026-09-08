---
title: Defence Before Fix
description: A phase that runs before a defect is fixed. The method and toolchain specifications, the tools that implement them, and the article in which the term was first published.
permalink: /
---

# Defence Before Fix

> **Defence Before Fix** is a phase that runs *before* a defect is fixed. Rather than dropping
> straight into remediating the specific instance in front of you, you first treat that instance
> as evidence of a class, and you build the automated defence that detects every occurrence of
> that class across the whole codebase. The defence is only trusted once it has been seen to fire.

A bug you have just found is a confirmed, in-production example of a pattern that actually hurt
you, and that is exactly the evidence you need in order to write a good detection rule. The
moment you fix the line, the evidence is gone. This method asks you to hold on for a moment and
build the net first, then go red on the bug that sent you looking, then sweep the codebase and
find out how many more there are, and only then fix them all. The
[primer](PRIMER.md) tells that story at reading pace; the specification below is the precise
version.

## The method, in six clauses

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

## The specifications

| Document                                       | What it is                                                    | Version |
| ---------------------------------------------- | ------------------------------------------------------------- | ------- |
| [The method specification](SPEC.md)            | Normative. What a practitioner does when a defect is found.   | 1.0.0   |
| [The toolchain specification](TOOLING-SPEC.md) | What a toolchain must offer so that a practitioner can do it. | 0.1.0   |
| [Primer](PRIMER.md)                            | The short introduction.                                       |         |
| [Provenance](PROVENANCE.md)                    | Who coined the term, when, and what is and is not claimed.    |         |
| [Changelog](CHANGELOG.md)                      | Changes to each document, versioned independently.            |         |

The method specification is the source of truth for what the method is. Where anything else
describing Defence Before Fix disagrees with it, including the article in which the term was first
published, the specification is correct. The two documents are versioned independently, so a
toolchain clause can be added without reissuing the method.

If you maintain a linter, a static analyser or a QA pipeline that other people install, the
toolchain specification is the one addressed to you. It states what a tool has to offer so that
the projects using it can follow the method at all, which turns out to be a different list from
the one the method itself gives.

## Tools that implement it

- [php-qa-ci](https://github.com/LongTermSupport/php-qa-ci), the PHP toolchain
- [ts-qa-ci](https://github.com/LongTermSupport/ts-qa-ci), the TypeScript toolchain

Each records the toolchain specification version it conforms to, in its own manifest, and each
was audited against every clause through its own commands before the claim was made. Both were
also the subjects of the execution tests that hardened the method specification before it was
published: real defects, found in the tools themselves, taken through all six clauses.

## The article

The term was first published on 22 February 2026 in
[Defence Before Fix: Preventing Bug Classes with Static Analysis](https://ltscommerce.dev/articles/defence-before-fix-static-analysis),
which walks through a worked example in which the reported defect turned out to be one of
twenty-three. The article's date is what establishes priority on the coinage; the specification
here is what the method now is.

## Source and licence

The documents live at
[github.com/Defence-Before-Fix](https://github.com/Defence-Before-Fix/defence-before-fix.github.io),
with their full history, and are checked in CI by the repository's own defence, `spec-qa.py`.
They are licensed under
[Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

Coined by [Joseph Edmonds](https://ltscommerce.dev) of
[Edmonds Commerce](https://edmondscommerce.co.uk). US spelling: Defense Before Fix.
