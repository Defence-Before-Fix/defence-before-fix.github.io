# Defence Before Fix: Toolchain Specification

**Version**: 0.2.0, published 2026-09-08
**Companion to**: [the method specification](SPEC.md), version 1.0.0, and [the detector specification](DETECTOR-SPEC.md), version 1.0.0
**Author**: [Joseph Edmonds](https://ltscommerce.dev), [Edmonds Commerce](https://edmondscommerce.co.uk)
**Coined**: 22 February 2026, in [the original article](https://ltscommerce.dev/articles/defence-before-fix-static-analysis)

## 1. What this document is for

The key words MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT and MAY are to be interpreted as
described in RFC 2119.

[The method specification](SPEC.md) states what a [Practitioner](SPEC.md#practitioner) does when a [Defect](SPEC.md#defect) is found.
[The detector specification](DETECTOR-SPEC.md) states what each [Detector](SPEC.md#detector) must offer so that they
can write, prove, run and resolve a [Rule](SPEC.md#rule) in it. This document states what a project's
[Toolchain](SPEC.md#toolchain) must offer beyond that, so that the [Rules](SPEC.md#rule) become [Defences](SPEC.md#defence)
the project governs.

**A [Toolchain](SPEC.md#toolchain) is measured at the project level.** It is whatever the project assembles to
run its checks through: the [Detectors](SPEC.md#detector) and [Runners](SPEC.md#runner), and the parts around them
that route, list, record and resolve, from third-party, first-party and project-level parts in any
combination. A third-party [Toolchain](SPEC.md#toolchain) such as `php-qa-ci` can supply all of it. A project
can also meet this document with its own scripts around a bare [Detector](SPEC.md#detector). [Conformance](SPEC.md#conform)
is a property of the assembled whole, because that is where it counts: a [Practitioner](SPEC.md#practitioner)
arriving at the project cannot tell which package a mechanism came from, and does not need to.

The three documents are separable because they fail separately, and all three failures have been
observed. A project can follow the method faithfully on a [Toolchain](SPEC.md#toolchain) that gives it nowhere to
record what it decided; a [Toolchain](SPEC.md#toolchain) can offer every mechanism the method needs whilst the
project using it writes no [Rules](SPEC.md#rule) at all; and a [Detector](SPEC.md#detector) can be the best host for
a [Rule](SPEC.md#rule) in its language whilst shipping an inline ignore that the project has never decided
whether to allow. Conflating them produces a specification that blames a project for a gap in its
[Toolchain](SPEC.md#toolchain), credits a [Toolchain](SPEC.md#toolchain) for discipline the project supplied itself, or
fails a [Detector](SPEC.md#detector) for governance that was never its to decide.

**The governing principle**: where the method specification requires a [Practitioner](SPEC.md#practitioner) to do
something, a [Conforming](SPEC.md#conform) [Toolchain](SPEC.md#toolchain) MUST make that possible without the project
building the mechanism first. A [Toolchain](SPEC.md#toolchain) that leaves the project to construct the means has
moved the obligation rather than met it. Where the project builds the means itself, those scripts are
part of its [Toolchain](SPEC.md#toolchain) and are judged as such.

## 2. Terminology

Terms from the method specification and the [detector specification](DETECTOR-SPEC.md) carry over unchanged. Every
capitalised term links to its definition; the ones this document leans on most are, in short:

| Term                                          | In one line                                                                                                         |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| [Detector](SPEC.md#detector)                  | A tool that reads code without executing it and reports what it finds                                               |
| [Runner](SPEC.md#runner)                      | A tool that executes code, a test suite or a compilation, and reports what happened                                 |
| [Rule](SPEC.md#rule)                          | One check a [Detector](SPEC.md#detector) evaluates                                                                  |
| [Defence](SPEC.md#defence)                    | A [Rule](SPEC.md#rule) with its documentation, in force and [Blocking](SPEC.md#blocking)                            |
| [Identifier](SPEC.md#identifier)              | The stable name printed with a finding that leads to its documentation                                              |
| [Blocking](SPEC.md#blocking)                  | Fails the run rather than issuing a [Warning](SPEC.md#warning)                                                      |
| [Exception](SPEC.md#exception)                | A recorded, justified decision to leave an [Instance](SPEC.md#instance) unfixed or a [Rule](SPEC.md#rule) unapplied |
| [Practitioner](SPEC.md#practitioner)          | Whoever is doing the work, a person or an [Agent](SPEC.md#agent)                                                    |
| [Owner](SPEC.md#owner)                        | The human who decides what the codebase may keep                                                                    |
| [Bundled rule](DETECTOR-SPEC.md#bundled-rule) | A [Rule](SPEC.md#rule) a [Detector](SPEC.md#detector) ships rather than one the project wrote                       |
| [Harness](DETECTOR-SPEC.md#harness)           | The route by which one [Rule](SPEC.md#rule) is run against supplied code on its own                                 |

These are additional.

#### Consuming project

A codebase that installs a [Detector](SPEC.md#detector) or a [Toolchain](SPEC.md#toolchain) shipped by somebody else. The maintainer of what is installed does not control it and cannot inspect it.

#### Bundled defence

A [Defence](SPEC.md#defence) a shipped [Toolchain](SPEC.md#toolchain) carries and enables by default in every [Consuming project](#consuming-project). A [Bundled rule](DETECTOR-SPEC.md#bundled-rule) is the [Detector](SPEC.md#detector)-level counterpart; a [Bundled defence](#bundled-defence) is one with its documentation, [Blocking](SPEC.md#blocking), and routed through the [Toolchain](SPEC.md#toolchain)'s own entry point.

#### Project record

The place a project writes down the judgements the method specification delegates to it: [Calibrations](SPEC.md#calibration), [Exceptions](SPEC.md#exception) and conventions.

The distinction between a [Bundled defence](#bundled-defence) and a project's own is significant throughout. A bundled
[Defence](SPEC.md#defence) is authored once and runs in codebases its author will never see, so everything a
[Practitioner](SPEC.md#practitioner) needs in order to act on it has to travel with it.

## 3. The division of responsibility

Almost every requirement in section 8 of the method specification has two halves. Stating only one
of them is what produces a [Toolchain](SPEC.md#toolchain) that is *nearly* usable. The middle column says which
document states the mechanism half; the assembled [Toolchain](SPEC.md#toolchain) MUST provide every row, whichever
part of it does so.

| Requirement                                 | The mechanism, and where it is stated                                                                                                     | The project supplies                           |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Bespoke [Defences](SPEC.md#defence)         | The authoring and registration route, [detector specification](DETECTOR-SPEC.md) 4.1                                                      | The [Rules](SPEC.md#rule)                      |
| The red proof                               | A [Harness](DETECTOR-SPEC.md#harness), [detector specification](DETECTOR-SPEC.md) 4.2                                                     | The [Fixture](SPEC.md#fixture) and the red run |
| Running the [Defence](SPEC.md#defence)      | A local invocation, including subsets, [detector specification](DETECTOR-SPEC.md) 5                                                       | Running it                                     |
| [Identifier](SPEC.md#identifier) resolution | The lookup, [detector specification](DETECTOR-SPEC.md) 6 for [Bundled rules](DETECTOR-SPEC.md#bundled-rule), clause 4.2 here for the rest | The documentation content                      |
| Correct construction                        | A place for it to live, clause 4.2 here                                                                                                   | The remediation text                           |
| Enumeration                                 | The listing, section 5 here                                                                                                               | The [Defences](SPEC.md#defence) listed         |
| [Agent](SPEC.md#agent)-context summary      | Generation and delivery, section 7 here                                                                                                   | The terse lines                                |
| Recorded decisions                          | A location it reads itself, section 6 here                                                                                                | The decisions                                  |
| [Suppression](SPEC.md#suppression)          | A route that can be forbidden, [detector specification](DETECTOR-SPEC.md) 7; forbidding it, clause 4.3 here                               | The decision, under method section 4           |

Read down the middle column and the shape of a [Conforming](SPEC.md#conform) [Toolchain](SPEC.md#toolchain) is already visible. Read across
any row and the failure mode is visible too: either half alone leaves the [Practitioner](SPEC.md#practitioner) stuck.

## 4. The detectors a toolchain routes defences through

### 4.1 Every detector the toolchain routes a defence through MUST conform to the [detector specification](DETECTOR-SPEC.md)

A [Toolchain](SPEC.md#toolchain) MUST NOT route a [Defence](SPEC.md#defence) through a [Detector](SPEC.md#detector) that does not
[Conform](SPEC.md#conform) to [the detector specification](DETECTOR-SPEC.md). Three points govern how that is met.

1. **Wrapping is permitted.** Where a [Detector](SPEC.md#detector) lacks a mechanism that specification
   requires, the [Toolchain](SPEC.md#toolchain) MAY supply it around the [Detector](SPEC.md#detector), a
   [Harness](DETECTOR-SPEC.md#harness) script or a resolver of its own, and the [Detector](SPEC.md#detector)
   together with that wrapping is then what the [Practitioner](SPEC.md#practitioner) uses and what is judged.
2. **How the wrapped pair is judged.** This clause holds when the [Detector](SPEC.md#detector) and the
   [Toolchain](SPEC.md#toolchain)'s wrapping together satisfy every MUST of sections 4 to 7 of the
   [detector specification](DETECTOR-SPEC.md), exercised as its clause 8.1 describes. The
   [Detector](SPEC.md#detector)'s own verdict under that document is unchanged by the wrapping. A gap
   in the [Detector](SPEC.md#detector) that the wrapping leaves open, a [Bundled rule](DETECTOR-SPEC.md#bundled-rule)
   with no documentation for example, fails this clause, whether or not a clause below names the
   same gap again; satisfying most of that document is not [Conformance](SPEC.md#conform) to it, any
   more than satisfying most of this one is.
3. **What cannot be wrapped.** A [Detector](SPEC.md#detector) that cannot host a bespoke [Rule](SPEC.md#rule) at all
   cannot be wrapped into [Conformance](SPEC.md#conform), and no [Defence](SPEC.md#defence) is routed through it.
   It MAY still run as one of the [Toolchain](SPEC.md#toolchain)'s checks, as a formatter or a
   [Runner](SPEC.md#runner) does.

**Why**: the six clauses of the method are carried out in a [Detector](SPEC.md#detector), and everything this
document adds presumes those clauses can be followed there. A [Toolchain](SPEC.md#toolchain) that lists, records
and resolves beautifully around a [Detector](SPEC.md#detector) in which no [Rule](SPEC.md#rule) can be written or proven
has governed nothing. The wrapping is permitted because a [Practitioner](SPEC.md#practitioner) cannot tell where a
mechanism lives and the method does not care; it is bounded because a mechanism the [Detector](SPEC.md#detector)
does not offer and the [Toolchain](SPEC.md#toolchain) does not add is a gap the project writes down under method
clause 3.2, and a gap recorded is not a gap closed.

### 4.2 The toolchain MUST resolve every identifier a defence it routes can print, from the installed copy, without network access

The [detector specification](DETECTOR-SPEC.md) holds a [Detector](SPEC.md#detector) to on-disk resolution of its own
[Bundled rules](DETECTOR-SPEC.md#bundled-rule) and no further, because it cannot know a project's
documentation. The [Toolchain](SPEC.md#toolchain) can, and MUST close the remainder: a mechanism, keyed on the
[Identifier](SPEC.md#identifier) exactly as printed, that resolves the project's own [Rules](SPEC.md#rule) and every
[Bundled defence](#bundled-defence) to [Remediation docs](SPEC.md#remediation-docs) shipped with the project or with the
[Toolchain](SPEC.md#toolchain), at a version tracked together, and a place for that documentation to live so that
a [Rule author](DETECTOR-SPEC.md#rule-author) adding a [Rule](SPEC.md#rule) knows where its documentation goes.
The documentation an [Identifier](SPEC.md#identifier) resolves to MUST state the correct construction, not
only the prohibition, specifically enough to act on, as method clause 8.4 requires; the
[Toolchain](SPEC.md#toolchain) supplies the place and the [Rule author](DETECTOR-SPEC.md#rule-author) the text.
A third-party [Detector](SPEC.md#detector)'s native catalogue, which the [Toolchain](SPEC.md#toolchain) orchestrates
without claiming as its own, is resolved under the [detector specification](DETECTOR-SPEC.md)'s clause 6 and is not
re-shipped here.

**Why**: method specification clauses 3.6 and 8.3. The [Identifier](SPEC.md#identifier) has to resolve for the
reader, which for an [Agent](SPEC.md#agent) means mechanically and on disk, and the project's own
[Rules](SPEC.md#rule) are the ones that carry its knowledge. A [Detector](SPEC.md#detector) that prints the
[Identifier](SPEC.md#identifier) faithfully has done its half; a project in which that string then leads nowhere
has a [Message](SPEC.md#message) that names a pattern without leading anywhere, which method clause 3.6 says
does not [Conform](SPEC.md#conform).

### 4.3 The toolchain MUST forbid, through a defence of its own, every suppression route that bypasses the project record

Inline [Suppression](SPEC.md#suppression) comments, per-line ignores and silent [Baselines](SPEC.md#baseline) all bypass
the [Project record](#project-record). The [detector specification](DETECTOR-SPEC.md) permits a [Detector](SPEC.md#detector) to ship such a
route provided it can be detected or disabled; this clause is where the project's decision is made
and enforced, and the decision is no. For every such route in every [Detector](SPEC.md#detector) it routes a
[Defence](SPEC.md#defence) through that is not itself the [Project record](#project-record), or does not pass
through it, a [Conforming](SPEC.md#conform) [Toolchain](SPEC.md#toolchain) MUST disable the route, or MUST run a
[Blocking](SPEC.md#blocking) [Defence](SPEC.md#defence) that fails on its use, and MUST direct irreducible cases to the
[Project record](#project-record) where clause 6.2 requires a justification. A [Baseline](SPEC.md#baseline) an
[Owner](SPEC.md#owner) has adopted under method section 4 is therefore kept in the [Project record](#project-record),
or read from a file the record names, and never as a file the [Detector](SPEC.md#detector) generates unseen.

**Why**: a governance mechanism whose escape hatch is an unreviewed comment is not a governance
mechanism. This is the one place this document is stricter than the [Detectors](SPEC.md#detector) it assembles
are by default, and it is deliberate: the method specification's position is that
[Suppression](SPEC.md#suppression) is an [Owner](SPEC.md#owner) decision, and an [Owner](SPEC.md#owner) cannot decide something
they are never shown. The [Detector](SPEC.md#detector) is not asked to forbid the route because the
[Detector](SPEC.md#detector) is not the project; the [Toolchain](SPEC.md#toolchain) is the project's, so it is.

The reference implementations both do this. `ts-qa-ci` bans every `eslint-disable` and
`@ts-expect-error` form outright; `php-qa-ci`'s `ForbidInlinePhpstanIgnoreRule` bans inline
`@phpstan-ignore` and directs irreducible cases to the configuration file, where they are visible.

### 4.4 The toolchain's own invocation MUST satisfy the detector specification's reporting clauses for every defence it routes

Where the [Toolchain](SPEC.md#toolchain) wraps its [Detectors](SPEC.md#detector) in an entry point of its own, that entry
point MUST itself meet clauses 5.1 to 5.4 of the [detector specification](DETECTOR-SPEC.md) for every
[Defence](SPEC.md#defence) it routes: invocable locally with no infrastructure, over a subset down to one
file, with the result in the output of the command the [Practitioner](SPEC.md#practitioner) ran, and with no
[Defence](SPEC.md#defence) reportable only through a mode they cannot run. The entry point MUST also print
every [Identifier](SPEC.md#identifier) its [Detectors](SPEC.md#detector) print, unaltered, so that clause 4.3 of the
[detector specification](DETECTOR-SPEC.md) holds through the wrapping; the [Detector](SPEC.md#detector)'s verdict
under that clause is on its own output, and the [Toolchain](SPEC.md#toolchain)'s is on what reaches the
[Practitioner](SPEC.md#practitioner).

**Why**: method clause 3.5 asks the [Practitioner](SPEC.md#practitioner) to demonstrate enforcement through the
project's own entry point, not through the [Detector](SPEC.md#detector) directly. A [Detector](SPEC.md#detector) that
[Conforms](SPEC.md#conform) on its own, wrapped in a command that runs only the whole codebase or only
elsewhere, has had its reporting clauses undone by the wrapping, and the [Practitioner](SPEC.md#practitioner)
is back to a loop that does not close.

### 4.5 The toolchain's entry point MUST run detectors before runners, and MUST stop on a detector failure

The invocation the project uses to accept changes MUST evaluate its [Detectors](SPEC.md#detector) before its
[Runners](SPEC.md#runner), and a [Blocking](SPEC.md#blocking) failure at the [Detector](SPEC.md#detector) level MUST stop the
levels below it from being treated as meaningful, in the order method section 5 states. How the
project expresses that sequence, and where it runs, remain out of scope under method section 8.

**Why**: method section 5. A [Detector](SPEC.md#detector) is preventive and a test is diagnostic, and a failure
at the [Detector](SPEC.md#detector) level produces confusing results at every level above it. The method makes
the ordering a property of the project rather than of any one remediation, which is exactly the
kind of property that lives in the [Toolchain](SPEC.md#toolchain) and nowhere else.

## 5. Enumeration

### 5.1 The toolchain MUST be able to list the defences active in a project, without triggering them

The listing MUST include each [Defence](SPEC.md#defence)'s [Identifier](SPEC.md#identifier) and a terse statement of what it forbids or
requires, and MUST provide the route to its full documentation.

**Why**: method specification clause 8.5. An [Agent](SPEC.md#agent) arriving at a codebase has no colleague to ask.
Without a listing, a project's standards can only be learned by violating them one at a time.

### 5.2 The listing MUST be derived from the active configuration

It MUST NOT be a hand-maintained document that happens to describe the configuration.

**Why**: a hand-maintained list drifts, and it drifts silently and in the dangerous direction. The
observed failure is a [Rule](SPEC.md#rule) that is registered, active, [Blocking](SPEC.md#blocking), and absent from
the list of [Rules](SPEC.md#rule), whilst the list states its own count with confidence. A derived listing cannot
diverge from what is enforced, because the thing enforced is what produced it.

### 5.3 A project's own defences MUST appear in the listing alongside bundled ones

Every [Defence](SPEC.md#defence) the project has written itself MUST appear in the listing clause 5.1
requires, meeting its content requirements in full, alongside every [Bundled defence](#bundled-defence).

For a shipped [Toolchain](SPEC.md#toolchain), the case is the same and worth spelling out. Its [Defences](SPEC.md#defence) against its own source, the ones only its contributors can
trigger, are that project's own [Defences](SPEC.md#defence) for this purpose, and MUST appear in the same listing
clause 5.1 requires, meeting its content requirements in full, when the [Toolchain](SPEC.md#toolchain) is run on itself,
however they are enabled. Where such a [Defence](SPEC.md#defence) is not expressible in the [Toolchain](SPEC.md#toolchain)'s own
[Detectors](SPEC.md#detector), its entry MAY be sourced from wherever it is enabled, provided the listing stays derived
under clause 5.2 rather than hand-maintained.

**Why**: the [Practitioner](SPEC.md#practitioner) does not care which package a [Rule](SPEC.md#rule) came from. They care what defends the
code in front of them, and a listing that covers only what a shipped [Toolchain](SPEC.md#toolchain) carries describes somebody
else's project.

## 6. The project record

This section exists because of a gap found by cold readers of the method specification, repeatedly
and independently: the method delegates several judgements to project level, and a [Practitioner](SPEC.md#practitioner)
arriving at a project that has recorded none of them has no legal move. That is a [Toolchain](SPEC.md#toolchain)
obligation. The method specification cannot fix it, because the method specification does not own a
file in the project.

### 6.1 The toolchain MUST define a location for the project record, and MUST read it itself

Not a documentation convention. A path the [Toolchain](SPEC.md#toolchain) loads.

**Why**: a [Project record](#project-record) the [Toolchain](SPEC.md#toolchain) does not read can be wrong without anything noticing.
When the [Toolchain](SPEC.md#toolchain) reads it, the written decision and the enforced decision are the same object, and
neither can drift from the other.

### 6.2 Every exception in the project record MUST carry a written justification that names the hazard and the scope, and the toolchain MUST reject a generic one

The [Toolchain](SPEC.md#toolchain) MUST require the justification, MUST NOT supply a default, MUST reject an
[Exception](SPEC.md#exception) that omits it, and MUST reject one whose justification could be pasted onto
any [Exception](SPEC.md#exception) unchanged. A field that is merely present and non-empty does not satisfy
this clause.

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
specification, which is why clause 6.3 puts every justification in one listing where a vacuous
one is seen next to its neighbours.

### 6.3 The project record MUST be enumerable by the same means as the defences

Listing the [Defences](SPEC.md#defence) and listing the [Project record](#project-record) MUST be the same kind of operation.

**Why**: method specification clause 8.7. A decision nobody can find will be re-opened by every
[Practitioner](SPEC.md#practitioner) who arrives after it, which converts a settled question into a recurring one.

### 6.4 The toolchain SHOULD state its own defaults for anything the method leaves to the project

Where the method specification delegates a judgement and the project has recorded nothing, a
documented [Toolchain](SPEC.md#toolchain) default is what the [Practitioner](SPEC.md#practitioner) falls back to.

**Why**: this is the deadlock this section exists to break. "The project decides" combined with "the
project has decided nothing" leaves an [Agent](SPEC.md#agent) choosing between guessing and stopping. A default
turns the first project-level decision from a prerequisite into a refinement, and the project's
first day is exactly when it has recorded least and can afford the interruption least.

## 7. Agent context

### 7.1 The toolchain SHOULD generate a summary of the active defences suitable for an agent's context

One terse line per [Defence](SPEC.md#defence), phrased as a standing instruction rather than as a failure report, each
carrying its [Identifier](SPEC.md#identifier) and the route to its documentation. Generated from the active configuration,
per clause 5.2.

### 7.2 The toolchain SHOULD deliver that summary into the project automatically

Into the file the project's [Agents](SPEC.md#agent) already load, refreshed on install and update, in a delimited
region marked as generated.

**Why**: 7.1 and 7.2 are separate clauses because they are separately missed, and the two reference
implementations miss opposite halves. `php-qa-ci` writes an auto-generated, auto-refreshed block
into every [Consuming project](#consuming-project)'s [Agent](SPEC.md#agent) instructions and does not put a [Rule](SPEC.md#rule) table in it; `ts-qa-ci`
maintains an excellent [Rule](SPEC.md#rule) catalogue and has no mechanism to deliver it. Each has built the half
the other lacks. A summary that exists but is never loaded and a delivery channel carrying
everything except the [Rules](SPEC.md#rule) are the same outcome from opposite directions.

Together these are the only clauses in any of the three specifications that operate **before** the
mistake rather than after it, which is why they are worth stating even as SHOULDs.

## 8. Self-audit

### 8.1 A shipped toolchain MUST fail its own release if a bundled defence lacks resolvable documentation

An automated check, over every [Identifier](SPEC.md#identifier) printed by a [Rule](SPEC.md#rule) the [Toolchain](SPEC.md#toolchain) authors or
bundles as its own [Defence](SPEC.md#defence), whatever kind of [Detector](SPEC.md#detector) carries it, that blocks its own release. Where
a documentation page covers a family of [Identifiers](SPEC.md#identifier) by a pattern, as clause 6.3 of
the [detector specification](DETECTOR-SPEC.md) allows, this audit MUST apply the pattern to every [Identifier](SPEC.md#identifier)
printed and confirm it lands on that page, so that a member added to the [Rule](SPEC.md#rule) and not to the
page fails the release. A third-party [Detector](SPEC.md#detector)'s native catalogue, which the
[Toolchain](SPEC.md#toolchain) orchestrates without claiming as its own, is outside this audit and inside clause
4.2's resolution all the same. The [detector specification](DETECTOR-SPEC.md)'s clause 6.3 names the dangling reference as
the failure to guard against above all others; this is the guard, and a [Toolchain](SPEC.md#toolchain) is not held
to less than it holds its [Practitioners](SPEC.md#practitioner) to.

**Why**: clause 4.2 is the clause most easily believed to be satisfied whilst being broken, because
the documentation is written by the same person who wrote the [Rule](SPEC.md#rule) and its absence is invisible from
the inside. A check that blocks the release is the difference between honouring the clause and asserting it, and it
is the method applied to the [Toolchain](SPEC.md#toolchain): the [Class](SPEC.md#class) of [Defect](SPEC.md#defect) is "a [Rule](SPEC.md#rule) that blocks without
explaining", and it is detectable mechanically.

### 8.2 A shipped toolchain MUST run its own bundled defences on its own source

Every [Rule](SPEC.md#rule) the [Toolchain](SPEC.md#toolchain) ships to [Consuming projects](#consuming-project) MUST also be
active when the [Toolchain](SPEC.md#toolchain) analyses itself, and a [Toolchain](SPEC.md#toolchain) release MUST fail when
they are not.

**Why**: a mechanism that delivers [Rules](SPEC.md#rule) to installed packages and not to the root package
leaves the [Toolchain](SPEC.md#toolchain) as the one project in which its own [Defences](SPEC.md#defence) never run. A
[Defect](SPEC.md#defect) in a [Rule](SPEC.md#rule)'s own code then goes unseen by every [Rule](SPEC.md#rule) built to see it, and a
self-check that reports clean is believed, by the [Rule author](DETECTOR-SPEC.md#rule-author) and by anyone checking their
work, because nobody expects a clean run to have run nothing. This clause was found by an execution
test in which both the [Practitioner](SPEC.md#practitioner) and the reviewer cited exactly such a run as evidence.

A project that assembles its [Toolchain](SPEC.md#toolchain) without shipping it has no release and no
[Consuming project](#consuming-project), so this section does not bear on its [Conformance](SPEC.md#conform); its
own [Defences](SPEC.md#defence) already run on its own source because that is the only source there is.

## 9. Conformance

**A project's [Toolchain](SPEC.md#toolchain) [Conforms](SPEC.md#conform)** if every MUST in sections 4 to 6 holds across the
assembled parts, wherever each part came from, and, where the [Toolchain](SPEC.md#toolchain) is one the project
ships, every MUST in section 8 as well. The project-level verdict is a single grade; which part of the
[Toolchain](SPEC.md#toolchain) satisfied each clause is evidence for that grade, not a second grade.

**A [Toolchain](SPEC.md#toolchain) [Conforms](SPEC.md#conform) with [Agent](SPEC.md#agent) support** if it additionally satisfies section 7.

Partial [Conformance](SPEC.md#conform) MUST NOT be described as [Conformance](SPEC.md#conform). A [Toolchain](SPEC.md#toolchain) that satisfies most of this
document is in a normal and respectable condition; it is not [Conforming](SPEC.md#conform), and describing it as such
removes the only value the word has.

### 9.1 A project that ships a detector or a toolchain has two levels of conformance, graded separately

As a project, it follows the method with its own assembled [Toolchain](SPEC.md#toolchain), like any other
project, and is graded against this document and section 7 of the method specification on that
basis. As an artefact, what it ships is graded for its consumers: a [Detector](SPEC.md#detector) against
[the detector specification](DETECTOR-SPEC.md), a [Toolchain](SPEC.md#toolchain) against this document as it stands
when installed into a [Consuming project](#consuming-project) with nothing else built around it. The two
verdicts MUST be graded and declared separately, and neither implies the other. Section 8 bears on
the artefact grade only; clause 5.3 is its project-level counterpart.

**Why**: the two questions have different readers. A contributor to the artefact wants to know
whether the project practises what it ships; a [Consuming project](#consuming-project) wants to know what it
will get. A single grade answers neither, and the observed failure is a [Toolchain](SPEC.md#toolchain) whose own
source was the one place its [Bundled defences](#bundled-defence) never ran, which a consumer-facing grade
alone would never have shown.

### 9.2 The declaration is the claim and the known-gap record, not a condition of conformance

A project or a shipped artefact MAY declare, machine-readably in whatever form its ecosystem uses to
record dependencies, the version of the method specification it follows and the version of this
document or the [detector specification](DETECTOR-SPEC.md) it [Conforms](SPEC.md#conform) to. A project that ships an artefact
carries both levels of clause 9.1 in that declaration, each named separately.

The same declaration is where a gap is recorded once it is known. A project or artefact that has
learnt, from its own self-audit under section 8 or from a [Practitioner](SPEC.md#practitioner)'s report under the
method's clause 3.2, that it fails a MUST of the document it declares against MUST record that gap
alongside the version, in the same file or one it names. A declaration with a non-empty gap record is
a statement of where the project stands and is not a claim of [Conformance](SPEC.md#conform). A mechanism gap
is by its nature one the [Toolchain](SPEC.md#toolchain) could not detect for itself, so the record is the only
place its [Owner](SPEC.md#owner) and its consumers can learn of it.

The declaration is optional. A [Toolchain](SPEC.md#toolchain) assembled before this document existed, or by a
project that has never read it, MAY be graded [Conforming](SPEC.md#conform) on evidence by anyone who exercises
the clauses above against it, and a verdict on any [Toolchain](SPEC.md#toolchain), declared or not, rests on that
exercise and not on the claim.

**Why**: a [Conformance](SPEC.md#conform) claim in a README is a sentence; a [Conformance](SPEC.md#conform) claim in a manifest is a fact
about a specific installed artefact, checkable by anyone, including mechanically. It also fixes what
"[Conforming](SPEC.md#conform)" meant at the point the claim was made, which a claim against a moving document cannot.
Making the claim a condition, though, would grade the maintainer's reading rather than the
[Toolchain](SPEC.md#toolchain), and would leave every project that met the method before hearing of it unable
to say so.

## 10. Relationship to the method and detector specifications

This document adds no obligations to a [Practitioner](SPEC.md#practitioner) and relaxes none. Every clause here exists to
make a clause of the method specification achievable.

Where this document and the method specification disagree, the method specification governs. It
describes the method, which is the thing being specified; this describes the equipment. Where this
document and the [detector specification](DETECTOR-SPEC.md) disagree about a [Detector](SPEC.md#detector), the [detector specification](DETECTOR-SPEC.md)
governs, because it is the document a [Detector](SPEC.md#detector)'s maintainer works from; what this document
asks of a [Detector](SPEC.md#detector) is that it [Conform](SPEC.md#conform) there.

Nothing here requires a project to use a [Conforming](SPEC.md#conform) [Toolchain](SPEC.md#toolchain) shipped by anyone. A project can [Conform](SPEC.md#conform) to the method
specification on a [Toolchain](SPEC.md#toolchain) that [Conforms](SPEC.md#conform) to none of this, at the cost of building the missing
mechanisms itself, and once built they are its [Toolchain](SPEC.md#toolchain) and are graded here. This document exists so that it
does not have to build them alone.
