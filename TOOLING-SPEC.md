# Defence Before Fix: Toolchain Specification

**Version**: 0.1.0, published 2026-09-08
**Companion to**: [the method specification](SPEC.md), version 1.0.0
**Author**: [Joseph Edmonds](https://ltscommerce.dev), [Edmonds Commerce](https://edmondscommerce.co.uk)
**Coined**: 22 February 2026, in [the original article](https://ltscommerce.dev/articles/defence-before-fix-static-analysis)

## 1. What this document is for

The key words MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT and MAY are to be interpreted as
described in RFC 2119.

[The method specification](SPEC.md) states what a [Practitioner](SPEC.md#practitioner) does when a [Defect](SPEC.md#defect) is found. This
document states what a [Toolchain](SPEC.md#toolchain) must offer so that they can do it.

The two are separable because they fail separately, and both failures have been observed. A project
can follow the method faithfully on a [Toolchain](SPEC.md#toolchain) that gives it nowhere to record what it decided, and
a [Toolchain](SPEC.md#toolchain) can offer every mechanism the method needs whilst the project using it writes no [Rules](SPEC.md#rule)
at all. Conflating the two produces a specification that blames a project for a gap in its [Toolchain](SPEC.md#toolchain), or
credits a [Toolchain](SPEC.md#toolchain) for discipline the project supplied itself.

**The governing principle**: where the method specification requires a [Practitioner](SPEC.md#practitioner) to do something,
a [Conforming](SPEC.md#conform) [Toolchain](SPEC.md#toolchain) MUST make that possible without the project building the mechanism first. A
tool that leaves the project to construct the means has moved the obligation rather than met it.

## 2. Terminology

Terms from the method specification carry over unchanged. These are additional.

#### Rule author

Whoever writes a [Defence](SPEC.md#defence). May be the [Toolchain](SPEC.md#toolchain)'s maintainer or the [Consuming project](#consuming-project).

#### Consuming project

A codebase that installs the [Toolchain](SPEC.md#toolchain). The [Toolchain](SPEC.md#toolchain)'s maintainer does not control it and cannot inspect it.

#### Bundled defence

A [Defence](SPEC.md#defence) the [Toolchain](SPEC.md#toolchain) ships and enables by default.

#### Project record

The place a [Consuming project](#consuming-project) writes down the judgements the method specification delegates to it: [Calibrations](SPEC.md#calibration), [Exceptions](SPEC.md#exception) and conventions.

The distinction between a [Bundled defence](#bundled-defence) and a project's own is significant throughout. A bundled
[Defence](SPEC.md#defence) is authored once and runs in codebases its author will never see, so everything a
[Practitioner](SPEC.md#practitioner) needs in order to act on it has to travel with it.

## 3. The division of responsibility

Almost every requirement in section 8 of the method specification has two halves. Stating only one
of them is what produces a tool that is *nearly* usable.

| Requirement                                 | The [Toolchain](SPEC.md#toolchain) MUST provide         | The project supplies                           |
| ------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------- |
| Bespoke [Defences](SPEC.md#defence)         | The authoring and registration route                    | The [Rules](SPEC.md#rule)                      |
| The red proof                               | A harness that runs a [Rule](SPEC.md#rule) in isolation | The [Fixture](SPEC.md#fixture) and the red run |
| Running the [Defence](SPEC.md#defence)      | A local invocation, including subsets                   | Running it                                     |
| [Identifier](SPEC.md#identifier) resolution | The lookup mechanism                                    | The documentation content                      |
| Correct construction                        | A place for it to live                                  | The remediation text                           |
| Enumeration                                 | The listing                                             | The [Defences](SPEC.md#defence) listed         |
| [Agent](SPEC.md#agent)-context summary      | Generation and delivery                                 | The terse lines                                |
| Recorded decisions                          | A location it reads itself                              | The decisions                                  |

Read down the first column and the shape of a [Conforming](SPEC.md#conform) [Toolchain](SPEC.md#toolchain) is already visible. Read across
any row and the failure mode is visible too: either half alone leaves the [Practitioner](SPEC.md#practitioner) stuck.

## 4. Authoring defences

### 4.1 The toolchain MUST support bespoke rules written by the consuming project

Configuration of an existing [Rule](SPEC.md#rule) set is not sufficient. The project must be able to express a
pattern its authors have never anticipated.

**Why**: the method turns a specific [Defect](SPEC.md#defect) into a [Class](SPEC.md#class) [Defence](SPEC.md#defence), and the [Classes](SPEC.md#class) that matter most
to a project are the ones peculiar to it. A [Toolchain](SPEC.md#toolchain) offering only a fixed catalogue can defend
against the industry's known [Hazards](SPEC.md#hazard) and none of the project's own, which is the half that carries
its institutional knowledge.

### 4.2 The toolchain MUST provide a harness that runs a single rule against supplied code

Without executing the project's own test suite, and reporting for a given input whether the [Rule](SPEC.md#rule)
fired.

**Why**: clause 3.3 of the method specification requires the [Rule](SPEC.md#rule) to be proven by making it go red.
A [Practitioner](SPEC.md#practitioner) who can only observe a [Rule](SPEC.md#rule)'s behaviour by running every [Detector](SPEC.md#detector) over the whole
codebase cannot demonstrate that a [Rule](SPEC.md#rule) fires on the pattern rather than on something incidental.

### 4.3 The toolchain MUST allow a defence to carry a stable identifier, and MUST print it

The [Identifier](SPEC.md#identifier) MUST be stable across releases and MUST NOT be derived from the [Rule](SPEC.md#rule)'s file path,
[Class](SPEC.md#class) name or position in a configuration file. The [Rule author](#rule-author) chooses it once.

**Why**: the [Identifier](SPEC.md#identifier) is the only string that reaches the [Practitioner](SPEC.md#practitioner) and the only key their
lookup can use. An [Identifier](SPEC.md#identifier) that changes when a [Rule](SPEC.md#rule) is renamed silently breaks every reference to
it, including references written down by people who have left.

### 4.4 The toolchain SHOULD enforce 4.3 with a defence of its own

A [Rule](SPEC.md#rule) over the [Rules](SPEC.md#rule), failing any [Defence](SPEC.md#defence) that reports without a stable [Identifier](SPEC.md#identifier).

**Why**: this is the method applied to the [Toolchain](SPEC.md#toolchain) itself, and it is cheap. `php-qa-ci`'s
`RequireRuleIdentifierConstantRule` is the worked example: it rejects a magic-string [Identifier](SPEC.md#identifier) and
names the constant to declare instead.

## 5. Reporting

### 5.1 The toolchain MUST be invocable by the practitioner, locally, with no infrastructure

**Why**: method specification clause 8.1. An [Agent](SPEC.md#agent) that cannot check its own work cannot iterate
against a [Defence](SPEC.md#defence), so the loop never closes in the turn where it is cheap to close.

### 5.2 The toolchain MUST support invocation over a subset, at minimum a single file

**Why**: 5.1 is satisfied in principle by a whole-codebase run and defeated in practice by one.
Checking a single edited file has to be fast enough to do on every edit, or it will not be done on
any.

### 5.3 The result MUST reach the practitioner in the output of the command they ran

Where the [Toolchain](SPEC.md#toolchain) writes fuller detail elsewhere, the invoked command's own output MUST carry both
a usable summary and the location of the remainder.

**Why**: method specification clause 8.2. A report the [Practitioner](SPEC.md#practitioner) has to go and find is a report
that arrives after the decision it was meant to inform.

### 5.4 A defence MUST NOT be reportable only through a mode the practitioner cannot run

**Why**: a [Rule](SPEC.md#rule) that fires only in an environment the [Practitioner](SPEC.md#practitioner) has no access to teaches nobody
anything and blocks them anyway, which is the worst combination available.

## 6. Resolving an identifier

### 6.1 The toolchain MUST provide a mechanism that resolves a printed identifier to its documentation

Keyed on **the [Identifier](SPEC.md#identifier) exactly as printed**. A command, an index file or a URL are all
acceptable.

A [Message](SPEC.md#message) that carries its own documentation path resolves that [Message](SPEC.md#message), not the
[Identifier](SPEC.md#identifier). The mechanism MUST resolve an [Identifier](SPEC.md#identifier) presented alone, because the reader
who needs it most has the [Identifier](SPEC.md#identifier) from a log, a ticket or a colleague and not the [Message](SPEC.md#message).
Where the [Identifier](SPEC.md#identifier) is itself a URL, as method clause 3.6 allows, printing it is printing the
[Identifier](SPEC.md#identifier); what this clause forbids is a path supplied in addition to a shorter [Identifier](SPEC.md#identifier)
that cannot be looked up on its own.

Where one page documents a family of [Identifiers](SPEC.md#identifier) under a shared prefix, every full
[Identifier](SPEC.md#identifier) in the family MUST appear on it verbatim, in the installed artefact clause 6.2
requires resolution to work from and not only in rendered output, or the page MUST carry a pattern the
audit under clause 10.1 can execute, a glob or a regular expression rather than prose, that matches every
member and no [Identifier](SPEC.md#identifier) outside the family. A prefix alone is neither. That audit MUST apply the
pattern to every [Identifier](SPEC.md#identifier) printed and confirm it lands on this page, so that a member added to
the [Rule](SPEC.md#rule) and not to the page fails the release.

**Why**: method specification clause 8.3 requires the [Identifier](SPEC.md#identifier) to resolve without a human. An index
keyed on anything else does not resolve it. This is the most commonly failed clause in this document
and it fails in a specific way: documentation exists, is genuinely good, and is keyed on the [Rule](SPEC.md#rule)'s
[Class](SPEC.md#class) or file name, which is a string the [Practitioner](SPEC.md#practitioner) was never given. The lookup they can actually
perform is the only one that counts.

### 6.2 Resolution MUST work from the installed copy, without network access

**Why**: an [Agent](SPEC.md#agent) working offline, behind a proxy, or against a URL that has since moved needs the
answer to be on disk. A dependency the project already installed is on disk by definition.

### 6.3 A bundled defence's documentation MUST ship with the defence, at a version tracked together

**Why**: method specification clause 3.6. A [Bundled defence](#bundled-defence) travels into codebases its author will
never see. If its documentation lives only in the [Toolchain](SPEC.md#toolchain)'s repository or on its website, then
every [Consuming project](#consuming-project) is one link rot away from a [Rule](SPEC.md#rule) that blocks without explaining.

The failure to guard against is not the absent document but the **dangling one**: a reference to
documentation that was planned and never written is worse than no reference, because it consumes
the [Practitioner](SPEC.md#practitioner)'s attention before failing them.

## 7. Enumeration

### 7.1 The toolchain MUST be able to list the defences active in a project, without triggering them

The listing MUST include each [Defence](SPEC.md#defence)'s [Identifier](SPEC.md#identifier) and a terse statement of what it forbids or
requires, and MUST provide the route to its full documentation.

**Why**: method specification clause 8.5. An [Agent](SPEC.md#agent) arriving at a codebase has no colleague to ask.
Without a listing, a project's standards can only be learned by violating them one at a time.

### 7.2 The listing MUST be derived from the active configuration

It MUST NOT be a hand-maintained document that happens to describe the configuration.

**Why**: a hand-maintained list drifts, and it drifts silently and in the dangerous direction. The
observed failure is a [Rule](SPEC.md#rule) that is registered, active, [Blocking](SPEC.md#blocking), and absent from
the list of [Rules](SPEC.md#rule), whilst the list states its own count with confidence. A derived listing cannot
diverge from what is enforced, because the thing enforced is what produced it.

### 7.3 A project's own defences MUST appear in the listing alongside bundled ones

A [Toolchain](SPEC.md#toolchain)'s [Defences](SPEC.md#defence) against its own source, the ones only its contributors can
trigger, are that project's own [Defences](SPEC.md#defence) for this purpose, and MUST appear in the same listing
clause 7.1 requires, meeting its content requirements in full, when the [Toolchain](SPEC.md#toolchain) is run on itself,
however they are enabled. Where such a [Defence](SPEC.md#defence) is not expressible in the [Toolchain](SPEC.md#toolchain)'s own
[Detectors](SPEC.md#detector), its entry MAY be sourced from wherever it is enabled, provided the listing stays derived
under clause 7.2 rather than hand-maintained.

**Why**: the [Practitioner](SPEC.md#practitioner) does not care which package a [Rule](SPEC.md#rule) came from. They care what defends the
code in front of them, and a listing that covers only what the [Toolchain](SPEC.md#toolchain) ships describes somebody
else's project.

## 8. The project record

This section exists because of a gap found by cold readers of the method specification, repeatedly
and independently: the method delegates several judgements to project level, and a [Practitioner](SPEC.md#practitioner)
arriving at a project that has recorded none of them has no legal move. That is a [Toolchain](SPEC.md#toolchain)
obligation. The method specification cannot fix it, because the method specification does not own a
file in the [Consuming project](#consuming-project).

### 8.1 The toolchain MUST define a location for the project record, and MUST read it itself

Not a documentation convention. A path the [Toolchain](SPEC.md#toolchain) loads.

**Why**: a [Project record](#project-record) the [Toolchain](SPEC.md#toolchain) does not read can be wrong without anything noticing.
When the [Toolchain](SPEC.md#toolchain) reads it, the written decision and the enforced decision are the same object, and
neither can drift from the other.

### 8.2 Every exception in the project record MUST carry a written justification

The [Toolchain](SPEC.md#toolchain) MUST require the justification, MUST NOT supply a default, and MUST reject an
[Exception](SPEC.md#exception) that omits it.

**Why**: an [Exception](SPEC.md#exception) without a reason is indistinguishable from an [Exception](SPEC.md#exception) nobody would defend,
and the person who could tell them apart is usually gone. Requiring the sentence is the whole
mechanism: it costs the author a minute at the moment they have the reason in mind, and it is the
only thing that makes an [Exception](SPEC.md#exception) reviewable later.

`ts-qa-ci`'s `tier-a-exceptions.json` is the reference implementation, and its own two entries
demonstrate the standard: both explain the scope limit as well as the reason.

The justification MUST name the [Hazard](SPEC.md#hazard) being accepted and the scope of the [Exception](SPEC.md#exception),
and the [Toolchain](SPEC.md#toolchain) MUST reject a justification that could be pasted onto any [Exception](SPEC.md#exception)
unchanged: "needed for now", "legacy", "TODO" and their like, by a check it documents. That check
cannot verify truth, and a [Toolchain](SPEC.md#toolchain)'s [Conformance](SPEC.md#conform) MUST NOT be read as having verified
it; whether the sentence is true is the [Owner](SPEC.md#owner)'s judgement under clause 3.3 of the method
specification, which is why clause 8.4 puts every justification in one listing where a vacuous
one is seen next to its neighbours.

### 8.3 The toolchain MUST NOT offer a suppression route that bypasses the project record

Inline [Suppression](SPEC.md#suppression) comments, per-line ignores and silent [Baselines](SPEC.md#baseline) all bypass it. Where the
underlying [Detector](SPEC.md#detector) provides such a mechanism, a [Conforming](SPEC.md#conform) [Toolchain](SPEC.md#toolchain) MUST defend against it.

**Why**: a governance mechanism whose escape hatch is an unreviewed comment is not a governance
mechanism. This is the one place the [Toolchain](SPEC.md#toolchain) specification is stricter than the [Detectors](SPEC.md#detector) it describes
usually are by default, and it is deliberate: the method specification's position is that
[Suppression](SPEC.md#suppression) is an [Owner](SPEC.md#owner) decision, and an [Owner](SPEC.md#owner) cannot decide something they are never shown.

The reference implementations both do this. `ts-qa-ci` bans every `eslint-disable` and
`@ts-expect-error` form outright; `php-qa-ci`'s `ForbidInlinePhpstanIgnoreRule` bans inline
`@phpstan-ignore` and directs irreducible cases to the configuration file, where they are visible.

### 8.4 The project record MUST be enumerable by the same means as the defences

Listing the [Defences](SPEC.md#defence) and listing the [Project record](#project-record) MUST be the same kind of operation.

**Why**: method specification clause 8.7. A decision nobody can find will be re-opened by every
[Practitioner](SPEC.md#practitioner) who arrives after it, which converts a settled question into a recurring one.

### 8.5 The toolchain SHOULD state its own defaults for anything the method leaves to the project

Where the method specification delegates a judgement and the project has recorded nothing, a
documented [Toolchain](SPEC.md#toolchain) default is what the [Practitioner](SPEC.md#practitioner) falls back to.

**Why**: this is the deadlock this section exists to break. "The project decides" combined with "the
project has decided nothing" leaves an [Agent](SPEC.md#agent) choosing between guessing and stopping. A default
turns the first project-level decision from a prerequisite into a refinement, and the project's
first day is exactly when it has recorded least and can afford the interruption least.

## 9. Agent context

### 9.1 The toolchain SHOULD generate a summary of the active defences suitable for an agent's context

One terse line per [Defence](SPEC.md#defence), phrased as a standing instruction rather than as a failure report, each
carrying its [Identifier](SPEC.md#identifier) and the route to its documentation. Generated from the active configuration,
per clause 7.2.

### 9.2 The toolchain SHOULD deliver that summary into the consuming project automatically

Into the file the project's [Agents](SPEC.md#agent) already load, refreshed on install and update, in a delimited
region marked as generated.

**Why**: 9.1 and 9.2 are separate clauses because they are separately missed, and the two reference
implementations miss opposite halves. `php-qa-ci` writes an auto-generated, auto-refreshed block
into every [Consuming project](#consuming-project)'s [Agent](SPEC.md#agent) instructions and does not put a [Rule](SPEC.md#rule) table in it; `ts-qa-ci`
maintains an excellent [Rule](SPEC.md#rule) catalogue and has no mechanism to deliver it. Each has built the half
the other lacks. A summary that exists but is never loaded and a delivery channel carrying
everything except the [Rules](SPEC.md#rule) are the same outcome from opposite directions.

Together these are the only clauses in either specification that operate **before** the mistake
rather than after it, which is why they are worth stating even as SHOULDs.

## 10. Self-audit

### 10.1 The toolchain MUST fail its own release if a bundled defence lacks resolvable documentation

An automated check, over every [Identifier](SPEC.md#identifier) printed by a [Rule](SPEC.md#rule) the [Toolchain](SPEC.md#toolchain) authors or
bundles as its own [Defence](SPEC.md#defence), whatever kind of [Detector](SPEC.md#detector) carries it, that blocks its own release. A
third-party [Detector](SPEC.md#detector)'s native catalogue, which the [Toolchain](SPEC.md#toolchain) orchestrates without claiming as its
own, is outside this audit and inside clause 6.1's resolution all the same. Clause 6.3 names the
dangling reference as the failure to guard against above all others; this is the guard, and a
[Toolchain](SPEC.md#toolchain) is not held to less than it holds its [Practitioners](SPEC.md#practitioner) to.

**Why**: clause 6.1 is the clause most easily believed to be satisfied whilst being broken, because
the documentation is written by the same person who wrote the [Rule](SPEC.md#rule) and its absence is invisible from
the inside. A check that blocks the release is the difference between honouring the clause and asserting it, and it
is the method applied to the [Toolchain](SPEC.md#toolchain): the [Class](SPEC.md#class) of [Defect](SPEC.md#defect) is "a [Rule](SPEC.md#rule) that blocks without
explaining", and it is detectable mechanically.

### 10.2 The toolchain MUST run its own bundled defences on its own source

Every [Rule](SPEC.md#rule) the [Toolchain](SPEC.md#toolchain) ships to [Consuming projects](#consuming-project) MUST also be
active when the [Toolchain](SPEC.md#toolchain) analyses itself, and a [Toolchain](SPEC.md#toolchain) release MUST fail when
they are not.

**Why**: a mechanism that delivers [Rules](SPEC.md#rule) to installed packages and not to the root package
leaves the [Toolchain](SPEC.md#toolchain) as the one project in which its own [Defences](SPEC.md#defence) never run. A
[Defect](SPEC.md#defect) in a [Rule](SPEC.md#rule)'s own code then goes unseen by every [Rule](SPEC.md#rule) built to see it, and a
self-check that reports clean is believed, by the [Rule author](#rule-author) and by anyone checking their
work, because nobody expects a clean run to have run nothing. This clause was found by an execution
test in which both the [Practitioner](SPEC.md#practitioner) and the reviewer cited exactly such a run as evidence.

## 11. Conformance

**A [Toolchain](SPEC.md#toolchain) [Conforms](SPEC.md#conform)** if it satisfies every MUST in sections 4 to 8 and clauses 10.1 and 10.2.

**A [Toolchain](SPEC.md#toolchain) [Conforms](SPEC.md#conform) with [Agent](SPEC.md#agent) support** if it additionally satisfies section 9.

Partial [Conformance](SPEC.md#conform) MUST NOT be described as [Conformance](SPEC.md#conform). A [Toolchain](SPEC.md#toolchain) that satisfies most of this
document is in a normal and respectable condition; it is not [Conforming](SPEC.md#conform), and describing it as such
removes the only value the word has.

### 11.1 A conforming toolchain MUST declare the version of the method specification it implements

Machine-readably, in whatever form its ecosystem uses to record dependencies.

The same declaration is where a gap against this document is recorded once it is known. A
[Toolchain](SPEC.md#toolchain) that has learnt, from its own self-audit under section 10 or from a
[Practitioner](SPEC.md#practitioner)'s report under the method's clause 3.2, that it fails a MUST in sections 4 to 8 or
section 10 MUST record that gap alongside the version it declares, in the same file or one it names,
and MUST NOT claim [Conformance](SPEC.md#conform) whilst the record is non-empty. A mechanism gap is by its
nature one the [Toolchain](SPEC.md#toolchain) could not detect for itself, so the record is the only place its
[Owner](SPEC.md#owner) and its consumers can learn of it.

**Why**: a [Conformance](SPEC.md#conform) claim in a README is a sentence; a [Conformance](SPEC.md#conform) claim in a lock file is a fact
about a specific installed artefact, checkable by anyone, including mechanically. It also fixes what
"[Conforming](SPEC.md#conform)" meant at the point the claim was made, which a claim against a moving document cannot.

## 12. Relationship to the method specification

This document adds no obligations to a [Practitioner](SPEC.md#practitioner) and relaxes none. Every clause here exists to
make a clause of the method specification achievable.

Where the two disagree, the method specification governs. It describes the method, which is the
thing being specified; this describes the equipment.

Nothing here requires a project to use a [Conforming](SPEC.md#conform) [Toolchain](SPEC.md#toolchain). A project can [Conform](SPEC.md#conform) to the method
specification on a [Toolchain](SPEC.md#toolchain) that [Conforms](SPEC.md#conform) to none of this, at the cost of building the missing
mechanisms itself. This document exists so that it does not have to.
