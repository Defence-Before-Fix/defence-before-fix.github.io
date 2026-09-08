# Defence Before Fix: provenance

*Meta information about the specification rather than part of it. Who coined the term, when, what
is claimed and what is not. Most readers do not need this page. It exists so that the claim can be
checked by anyone who wants to check it.*

The method itself is in [the specification](SPEC.md). The short introduction is in
[the primer](PRIMER.md).

---

## The term

**Defence Before Fix** was coined by **[Joseph Edmonds](https://ltscommerce.dev)** of
[Edmonds Commerce](https://edmondscommerce.co.uk) and first
published on **22 February 2026**, in the article
[*Defence Before Fix: Preventing Bug Classes with Static Analysis*](https://ltscommerce.dev/articles/defence-before-fix-static-analysis)
at [ltscommerce.dev](https://ltscommerce.dev).

The method was developed in commercial practice at
[Edmonds Commerce](https://edmondscommerce.co.uk), and the quality tooling that implements it is
published from there.

That publication date is what establishes priority on the coinage. The article remains at its
original URL for that reason and will not be moved or re-slugged.

US spelling: **Defense Before Fix**. The British spelling is canonical, because the author is
British and it is the spelling that carries the publication date. The American spelling resolves
to the same page.

## What is claimed, and what is not

The territory adjacent to this method is well populated. The claim is scoped accordingly, and the
scoping matters more than the claim: a claim that collapses on the first challenge takes
everything near it down as well.

| Claim                                                                    | Status                                                                                      |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| The term *Defence Before Fix*                                            | **Claimed.** No prior use as a named practice was found at the time of publication.         |
| The defence phase preceding the fix, and preceding the reproduction test | **Claimed.** The conventional sequence is reproduce, then fix.                              |
| Requiring the rule to be proven by firing before it is trusted           | **Claimed** as a formulation.                                                               |
| Defensive programming                                                    | Not claimed. Decades old.                                                                   |
| Preventing classes of bug rather than instances                          | Not claimed. *The Pragmatic Programmer*, shift-left testing and poka-yoke all precede this. |
| Static analysis, custom lint rules, or blocking quality gates            | Not claimed. All long-established practice.                                                 |

Everyone agrees that preventing classes of defect is better than fixing instances of them. What
this specification contributes is a name, a placement of the work before the fix, and a
conformance standard for what the resulting defence has to do.

**No adoption is claimed.** The accurate sentence is "a method I named and published". Anything
stronger invites one question, *"says who?"*, and loses the whole position.

## Relationship to the article

The article came first and holds the date. The specification is now the source of truth for what
the method is, and where the two differ the specification is correct.

The article will be reworked to agree with it. It predates several things the specification
settles, most obviously the requirement that a rule be proven by firing, which the article does not
mention at all, and its framing of the method as inverting the usual order, which is not what the
method does.

**The specification is the product. The article is something written about it.**

There is deliberately no `rel=canonical` between the two and no redirect. Pointing the article at
the specification would deindex the page carrying the publication date, which is the one asset here
that cannot be recreated.

## How this specification was developed

Version 1.0.0 was written from a structured interview with the author, then tested against
independent readers who were given the document and nothing else, in successive rounds, and revised
after each. Each round was asked the same question: could you follow this faithfully with no
further input?

That process found, among other things, a contradiction between two clauses about narrowing a rule,
and a reading under which a rule catching fifty legitimate instances might be narrowed until it
caught only one. Neither was visible to the author.

It is recorded here because a specification's claim to be followable is worth more when somebody
has actually tried to follow it.

## Versioning

The specification carries a version number and a changelog. Changes to normative content are
versioned; corrections to wording that do not change what conforms are not.

## Citation

> Edmonds, Joseph. *Defence Before Fix*, version 1.0.1. First published 22 February 2026.
> <https://ltscommerce.dev>
