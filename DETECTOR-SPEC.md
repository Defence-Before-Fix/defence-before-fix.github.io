# Defence Before Fix: Detector Specification

**Version**: 1.0.0, published 2026-09-08
**Companion to**: [the method specification](SPEC.md), version 1.0.0, and [the toolchain specification](TOOLING-SPEC.md), version 0.2.0
**Author**: [Joseph Edmonds](https://ltscommerce.dev), [Edmonds Commerce](https://edmondscommerce.co.uk)
**Coined**: 22 February 2026, in [the original article](https://ltscommerce.dev/articles/defence-before-fix-static-analysis)

## 1. What this document is for

The key words MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT and MAY are to be interpreted as
described in RFC 2119.

[The method specification](SPEC.md) states what a [Practitioner](SPEC.md#practitioner) does when a
[Defect](SPEC.md#defect) is found. This document states what a [Detector](SPEC.md#detector) must offer so that they
can do it: write a [Rule](SPEC.md#rule), prove it, run it and resolve what it prints. It is addressed to
whoever maintains a [Detector](SPEC.md#detector), which the method specification defines as a tool that reads
code without executing it and reports occurrences of a pattern.

A [Detector](SPEC.md#detector) is one part of a project's [Toolchain](SPEC.md#toolchain), and this document judges it
on what it offers alone. What the assembled [Toolchain](SPEC.md#toolchain) of a project must add on top, the
[Project record](TOOLING-SPEC.md#project-record), the listing of active [Defences](SPEC.md#defence) and the
governance of [Suppression](SPEC.md#suppression), is stated in [the toolchain specification](TOOLING-SPEC.md).
The two are separable because they are built by different people: a [Detector](SPEC.md#detector) is authored once
and installed into projects its maintainer will never see, whilst governance is decided by each
project for itself. A document that asked a [Detector](SPEC.md#detector) to enforce a project's governance would
fail every [Detector](SPEC.md#detector) in use and would not make any project better governed.

**The governing principle**: where the method specification requires a [Practitioner](SPEC.md#practitioner) to do
something with a [Rule](SPEC.md#rule), a [Conforming](SPEC.md#conform) [Detector](SPEC.md#detector) MUST make that possible
without the project building the mechanism first. A [Detector](SPEC.md#detector) that leaves the project to
construct the means has moved the obligation rather than met it.

## 2. Terminology

Terms from the method specification carry over unchanged. These are additional.

#### Rule author

Whoever writes a [Rule](SPEC.md#rule). May be the [Detector](SPEC.md#detector)'s maintainer, a [Toolchain](SPEC.md#toolchain)'s maintainer or the project that runs it.

#### Bundled rule

A [Rule](SPEC.md#rule) the [Detector](SPEC.md#detector) ships. Its [Rule author](#rule-author) will never see the codebases it runs in, so everything a [Practitioner](SPEC.md#practitioner) needs in order to act on it has to travel with it.

#### Harness

The route by which one [Rule](SPEC.md#rule) is run against supplied code and its findings observed, without the project's own test suite and without every other [Rule](SPEC.md#rule) running alongside it.

The distinction between a [Bundled rule](#bundled-rule) and a project's own [Rule](SPEC.md#rule) matters throughout.
The [Detector](SPEC.md#detector) owns the documentation of the first and can be held to shipping it; it cannot
know the documentation of the second, and what it owes there is the mechanism that lets the project
attach its own.

## 3. The division of responsibility

Each mechanism the method needs has two halves. Stating only one of them is what produces a
[Detector](SPEC.md#detector) that is *nearly* usable.

| Requirement                                        | The [Detector](SPEC.md#detector) MUST provide           | The [Rule author](#rule-author) supplies                                   |
| -------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------- |
| Bespoke [Rules](SPEC.md#rule)                      | The authoring and registration route                    | The [Rules](SPEC.md#rule)                                                  |
| The red proof                                      | A [Harness](#harness)                                   | The [Fixture](SPEC.md#fixture) and the red run                             |
| Running the [Rule](SPEC.md#rule)                   | A local invocation, including subsets                   | Running it                                                                 |
| The [Identifier](SPEC.md#identifier)               | A place to carry it, and printing it with every finding | Choosing it once                                                           |
| Resolution of a [Bundled rule](#bundled-rule)      | The lookup, and the documentation, on disk              | Nothing                                                                    |
| Resolution of a project's own [Rule](SPEC.md#rule) | The [Identifier](SPEC.md#identifier) printed unaltered  | The documentation and, with the [Toolchain](SPEC.md#toolchain), the lookup |
| Inline [Suppression](SPEC.md#suppression)          | A route the project can detect or disable               | The decision whether to forbid it                                          |

Read down the middle column and the shape of a [Conforming](SPEC.md#conform) [Detector](SPEC.md#detector) is already
visible. Read across any row and the failure mode is visible too: either half alone leaves the
[Practitioner](SPEC.md#practitioner) stuck.

## 4. Authoring rules

### 4.1 The detector MUST support bespoke rules written by the project that runs it

Configuration of an existing [Rule](SPEC.md#rule) set is not sufficient. The project must be able to express a
pattern the [Detector](SPEC.md#detector)'s authors have never anticipated, and register it so that it runs with
the same standing as a [Bundled rule](#bundled-rule).

**Why**: the method turns a specific [Defect](SPEC.md#defect) into a [Class](SPEC.md#class) [Defence](SPEC.md#defence), and the
[Classes](SPEC.md#class) that matter most to a project are the ones peculiar to it. A [Detector](SPEC.md#detector) offering
only a fixed catalogue can defend against the industry's known [Hazards](SPEC.md#hazard) and none of the
project's own, which is the half that carries its institutional knowledge.

### 4.2 The detector MUST provide a harness that runs a single rule against supplied code

A [Harness](#harness) reports, for a given input, whether the [Rule](SPEC.md#rule) fired and what it printed, without
executing the project's own test suite and without the other [Rules](SPEC.md#rule) obscuring the answer.

**Why**: clause 3.3 of the method specification requires the [Rule](SPEC.md#rule) to be proven by making it go
red. A [Practitioner](SPEC.md#practitioner) who can only observe a [Rule](SPEC.md#rule)'s behaviour by running every
[Rule](SPEC.md#rule) over the whole codebase cannot demonstrate that a [Rule](SPEC.md#rule) fires on the pattern rather
than on something incidental.

### 4.3 The detector MUST allow a rule to carry a stable identifier, and MUST print it with every finding

The [Identifier](SPEC.md#identifier) MUST be stable across releases and MUST NOT be derived from the [Rule](SPEC.md#rule)'s
file path, [Class](SPEC.md#class) name or position in a configuration file. The [Rule author](#rule-author) chooses it
once. The [Detector](SPEC.md#detector) MUST print it, unaltered, alongside every finding the [Rule](SPEC.md#rule)
reports, in every output format it offers.

**Why**: the [Identifier](SPEC.md#identifier) is the only string that reaches the [Practitioner](SPEC.md#practitioner) and the
only key their lookup can use. An [Identifier](SPEC.md#identifier) that changes when a [Rule](SPEC.md#rule) is renamed
silently breaks every reference to it, including references written down by people who have left.
An [Identifier](SPEC.md#identifier) the [Detector](SPEC.md#detector) carries but does not print is one the
[Practitioner](SPEC.md#practitioner) was never given.

### 4.4 The detector SHOULD enforce 4.3 with a rule of its own

A [Rule](SPEC.md#rule) over the [Rules](SPEC.md#rule), failing any [Rule](SPEC.md#rule) that reports without a stable
[Identifier](SPEC.md#identifier).

**Why**: this is the method applied to the [Detector](SPEC.md#detector) itself, and it is cheap. The worked
example is `php-qa-ci`'s `RequireRuleIdentifierConstantRule`, a [Rule](SPEC.md#rule) hosted in PHPStan by a
[Toolchain](SPEC.md#toolchain) built on it: it rejects a magic-string [Identifier](SPEC.md#identifier) and names the
constant to declare instead. Nothing about it needed to live outside the [Detector](SPEC.md#detector).

## 5. Reporting

### 5.1 The detector MUST be invocable by the practitioner, locally, with no infrastructure

**Why**: method specification clause 8.1. An [Agent](SPEC.md#agent) that cannot check its own work cannot
iterate against a [Defence](SPEC.md#defence), so the loop never closes in the turn where it is cheap to close.

### 5.2 The detector MUST support invocation over a subset, at minimum a single file

**Why**: 5.1 is satisfied in principle by a whole-codebase run and defeated in practice by one.
Checking a single edited file has to be fast enough to do on every edit, or it will not be done on
any.

### 5.3 The result MUST reach the practitioner in the output of the command they ran

Where the [Detector](SPEC.md#detector) writes fuller detail elsewhere, the invoked command's own output MUST
carry both a usable summary and the location of the remainder.

**Why**: method specification clause 8.2. A report the [Practitioner](SPEC.md#practitioner) has to go and find is a
report that arrives after the decision it was meant to inform.

### 5.4 A finding MUST NOT be reportable only through a mode the practitioner cannot run

**Why**: a [Rule](SPEC.md#rule) that fires only in an environment the [Practitioner](SPEC.md#practitioner) has no access to
teaches nobody anything and blocks them anyway, which is the worst combination available.

## 6. Resolving an identifier

### 6.1 The detector MUST provide a mechanism that resolves a printed identifier to its documentation

Keyed on **the [Identifier](SPEC.md#identifier) exactly as printed**. A command, an index file or a URL are all
acceptable.

For a [Bundled rule](#bundled-rule), the [Detector](SPEC.md#detector) supplies the documentation and the lookup, and
clauses 6.2 and 6.3 say where. For a project's own [Rule](SPEC.md#rule), the [Detector](SPEC.md#detector) cannot know
the documentation, so what it owes is the half it can give: the [Identifier](SPEC.md#identifier) printed
unaltered under clause 4.3, and a form of [Identifier](SPEC.md#identifier) that can be looked up on its own,
which method clause 3.6 allows to be a [Rule](SPEC.md#rule) ID, an anchor or a URL. The lookup for such a
[Rule](SPEC.md#rule) is an obligation on the project's assembled [Toolchain](SPEC.md#toolchain), under clause 4.2 of
the [toolchain specification](TOOLING-SPEC.md), and a [Detector](SPEC.md#detector) that offers it as well has gone further than
this clause asks.

A [Message](SPEC.md#message) that carries its own documentation path resolves that [Message](SPEC.md#message), not the
[Identifier](SPEC.md#identifier). The mechanism MUST resolve an [Identifier](SPEC.md#identifier) presented alone, because
the reader who needs it most has the [Identifier](SPEC.md#identifier) from a log, a ticket or a colleague and not
the [Message](SPEC.md#message). Where the [Identifier](SPEC.md#identifier) is itself a URL, as method clause 3.6 allows,
printing it is printing the [Identifier](SPEC.md#identifier); what this clause forbids is a path supplied in
addition to a shorter [Identifier](SPEC.md#identifier) that cannot be looked up on its own.

**Why**: method specification clause 8.3 requires the [Identifier](SPEC.md#identifier) to resolve without a human.
An index keyed on anything else does not resolve it. This is the most commonly failed clause in this
document and it fails in a specific way: documentation exists, is genuinely good, and is keyed on the
[Rule](SPEC.md#rule)'s [Class](SPEC.md#class) or file name, which is a string the [Practitioner](SPEC.md#practitioner) was never
given. The lookup they can actually perform is the only one that counts.

### 6.2 Resolution of a bundled rule's identifier MUST work from the installed copy, without network access

**Why**: an [Agent](SPEC.md#agent) working offline, behind a proxy, or against a URL that has since moved needs
the answer to be on disk. A dependency the project already installed is on disk by definition. A
catalogue on the [Detector](SPEC.md#detector)'s website, however complete, is the right documentation in the wrong
place.

### 6.3 A bundled rule's documentation MUST ship with the rule, at a version tracked together

Where one page documents a family of [Identifiers](SPEC.md#identifier) under a shared prefix, every full
[Identifier](SPEC.md#identifier) in the family MUST appear on it verbatim, in the installed artefact clause 6.2
requires resolution to work from and not only in rendered output, or the page MUST carry a pattern a
mechanical check can execute, a glob or a regular expression rather than prose, that matches every
member and no [Identifier](SPEC.md#identifier) outside the family. A prefix alone is neither.

**Why**: method specification clause 3.6. A [Bundled rule](#bundled-rule) travels into codebases its author
will never see. If its documentation lives only in the [Detector](SPEC.md#detector)'s repository or on its
website, then every project that installs it is one link rot away from a [Rule](SPEC.md#rule) that blocks
without explaining.

The failure to guard against is not the absent document but the **dangling one**: a reference to
documentation that was planned and never written is worse than no reference, because it consumes
the [Practitioner](SPEC.md#practitioner)'s attention before failing them.

### 6.4 The detector SHOULD fail its own release if a bundled rule lacks resolvable documentation

An automated check over every [Identifier](SPEC.md#identifier) a [Bundled rule](#bundled-rule) can print, applying the
family pattern of clause 6.3 where one is used, that blocks the release when any of them lands on no
page.

**Why**: clause 6.1 is the clause most easily believed to be satisfied whilst being broken, because
the documentation is written by the same person who wrote the [Rule](SPEC.md#rule) and its absence is
invisible from the inside. Where the [Detector](SPEC.md#detector) is shipped inside a [Toolchain](SPEC.md#toolchain),
the [toolchain specification](TOOLING-SPEC.md)'s self-audit makes this check a MUST for the [Toolchain](SPEC.md#toolchain); a
[Detector](SPEC.md#detector) released on its own is asked for it as a SHOULD because the same [Class](SPEC.md#class) of
[Defect](SPEC.md#defect), a [Rule](SPEC.md#rule) that blocks without explaining, is detectable mechanically there too.

## 7. Suppression

### 7.1 A detector MAY offer an inline suppression route, but MUST make it detectable or disableable

An inline ignore comment, a per-line directive and a generated [Baseline](SPEC.md#baseline) are all such
routes. The [Detector](SPEC.md#detector) MAY ship them. It MUST make each one either disableable by
configuration, or detectable by a [Rule](SPEC.md#rule) the project can write in the [Detector](SPEC.md#detector) itself
or by a plain reading of the source, so that a project which decides to forbid the route can enforce
that decision. A route that can be neither switched off nor seen does not [Conform](SPEC.md#conform).

**Why**: the method specification's position is that [Suppression](SPEC.md#suppression) is an [Owner](SPEC.md#owner)
decision under its clause 3.4 and section 4, and an [Owner](SPEC.md#owner) cannot decide something they are
never shown. The [Detector](SPEC.md#detector) is not the [Owner](SPEC.md#owner) and does not know the project's
governance, so it is not asked to enforce it; what it is asked is not to hide the route. Every
[Detector](SPEC.md#detector) in wide use ships an inline ignore, and a clause that forbade them would fail all of
them without governing any project better. Whether the route is forbidden is the project's decision,
enforced through its [Toolchain](SPEC.md#toolchain) under clause 4.3 of the [toolchain specification](TOOLING-SPEC.md).

### 7.2 An inline suppression route SHOULD require a written reason

The [Detector](SPEC.md#detector) SHOULD reject, or be configurable to reject, an inline [Suppression](SPEC.md#suppression)
that carries no reason, and SHOULD NOT supply a default one.

**Why**: a [Suppression](SPEC.md#suppression) without a reason is indistinguishable from one nobody would defend,
and the person who could tell them apart is usually gone. Requiring the sentence costs the author a
minute at the moment they have the reason in mind, and it is the only thing that makes the
[Suppression](SPEC.md#suppression) reviewable later. PHPStan's `reportIgnoresWithoutComments` is the shape of it.

## 8. Conformance

**A [Detector](SPEC.md#detector) [Conforms](SPEC.md#conform)** if it satisfies every MUST in sections 4 to 7.

Partial [Conformance](SPEC.md#conform) MUST NOT be described as [Conformance](SPEC.md#conform). A [Detector](SPEC.md#detector)
that satisfies most of this document is in a normal and respectable condition; it is not
[Conforming](SPEC.md#conform), and describing it as such removes the only value the word has.

This document defines one level. The clauses of the method specification's section 8 that reach
beyond what sections 4 to 6 here already secure, the listing of active [Defences](SPEC.md#defence) and the
summary for an [Agent](SPEC.md#agent)'s context, are obligations on a project's assembled [Toolchain](SPEC.md#toolchain)
and are stated in the [toolchain specification](TOOLING-SPEC.md), so there is no separate [Agent](SPEC.md#agent)-support level
for a [Detector](SPEC.md#detector).

### 8.1 A maintainer MAY declare the version of this document the detector conforms to, and the declaration records known gaps

The declaration is machine-readable, in whatever form the [Detector](SPEC.md#detector)'s ecosystem uses to
record dependencies. The same declaration is where a gap against this document is recorded once it is
known: a [Detector](SPEC.md#detector) that has learnt, from its own checks or from a [Practitioner](SPEC.md#practitioner)'s
report under the method's clause 3.2, that it fails a MUST in sections 4 to 7 MUST record that gap
alongside the version it declares, in the same file or one it names. A declaration with a non-empty
gap record is a statement of where the [Detector](SPEC.md#detector) stands and is not a claim of
[Conformance](SPEC.md#conform).

The declaration is optional. It is how a maintainer claims [Conformance](SPEC.md#conform); it is not a
condition of it. A [Detector](SPEC.md#detector) that predates this document, or whose maintainer has never read
it, MAY be graded [Conforming](SPEC.md#conform) on evidence by anyone who exercises the clauses above against
it, and a verdict on any [Detector](SPEC.md#detector), declared or not, rests on that exercise and not on the
claim. A declaration tells the reader what the maintainer believes and what they know to be missing;
the reader still runs the [Harness](#harness).

**Why**: a [Conformance](SPEC.md#conform) claim in a README is a sentence; a claim in a manifest is a fact about
a specific installed artefact, checkable by anyone, including mechanically, and it fixes what
"[Conforming](SPEC.md#conform)" meant at the point the claim was made. Making the claim a condition of
[Conformance](SPEC.md#conform), though, would mean a [Detector](SPEC.md#detector) with every mechanism in place could
never [Conform](SPEC.md#conform) until its maintainer had heard of this document, which grades the
maintainer's reading rather than the [Detector](SPEC.md#detector).

## 9. Relationship to the other specifications

This document adds no obligations to a [Practitioner](SPEC.md#practitioner) and relaxes none. Every clause here
exists to make a clause of the method specification achievable with a [Detector](SPEC.md#detector) in hand.

Where this document and the method specification disagree, the method specification governs. It
describes the method, which is the thing being specified; this describes one piece of the equipment.

The [toolchain specification](TOOLING-SPEC.md) states what a project's assembled [Toolchain](SPEC.md#toolchain) must offer beyond
what each [Detector](SPEC.md#detector) in it offers, and it requires every [Detector](SPEC.md#detector) a [Defence](SPEC.md#defence)
is routed through to [Conform](SPEC.md#conform) to this one. A [Detector](SPEC.md#detector) shipped inside a
[Toolchain](SPEC.md#toolchain) is measured here as a [Detector](SPEC.md#detector) and there as part of the
[Toolchain](SPEC.md#toolchain); the two verdicts are separate and neither implies the other.

Nothing here requires a project to use a [Conforming](SPEC.md#conform) [Detector](SPEC.md#detector). A project can
[Conform](SPEC.md#conform) to the method specification on a [Detector](SPEC.md#detector) that [Conforms](SPEC.md#conform) to
none of this, at the cost of building the missing mechanisms itself. This document exists so that it
does not have to.
