# Defence Before Fix: Method Specification

**Version**: 1.0.1, published 2026-09-08
**Companion to**: [the detector specification](DETECTOR-SPEC.md), version 1.0.0, and [the toolchain specification](TOOLING-SPEC.md), version 0.2.0
**Author**: [Joseph Edmonds](https://ltscommerce.dev), [Edmonds Commerce](https://edmondscommerce.co.uk)
**Coined**: 22 February 2026, in [the original article](https://ltscommerce.dev/articles/defence-before-fix-static-analysis)

> **Defence Before Fix** ([DBF](#dbf)) is a phase that runs *before* a [Defect](#defect) is fixed. Rather than dropping
> straight into remediating the specific [Instance](#instance) in front of you, you first treat that [Instance](#instance)
> as evidence of a [Class](#class), and you build the automated [Defence](#defence) that detects every occurrence of
> that [Class](#class) across the whole codebase. The [Defence](#defence) is only trusted once it has been seen to
> fire.

The [Defect](#defect) is what makes this possible. It is a real, confirmed, impactful example of a harmful
pattern, which is precisely the raw material a good custom [Rule](#rule) needs and which speculative
[Rules](#rule) never have. Every [Defect](#defect) is therefore an opportunity to extend the codebase's permanent
defensive [Coverage](#coverage), and that opportunity exists only in the window before the fix.

Defence Before Fix does not replace test-driven development. The specific [Defect](#defect) is still
reproduced with a test and proven fixed, exactly as normal. The two operate at different levels:
TDD addresses the [Instance](#instance), Defence Before Fix addresses the [Class](#class).

Not to be confused with *Defence in depth*, which is a security term meaning something else
entirely. The [Defence](#defence) here comes before the fix in time, not in layers.

US spelling: **Defense Before Fix**. Abbreviated [DBF](#dbf) throughout.

---

## Status of this document

This is version 1.0.1 of the specification. It is normative: section 3 defines the method,
section 4 states who decides what, and section 7 defines what [Conformance](#conform) means and who may claim
it.

**This document is the source of truth for what the method is.** Where anything else describing
Defence Before Fix disagrees with it, including the article in which the term was first published,
this document is correct.

Who coined the term, when it was first published, and what is and is not being claimed are recorded
separately in [provenance](PROVENANCE.md), which is meta information about this specification
rather than part of it. A short introduction to the method is in [the primer](PRIMER.md).

Changes are recorded in the changelog at the end.

## 1. Terminology

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY are to be interpreted as described in
RFC 2119.

#### DBF

The acronym for Defence Before Fix, used as shorthand for this method and for anything built under it. A [DBF](#dbf) [Rule](#rule) is a [Rule](#rule) as this specification defines it; a [DBF](#dbf) [Toolchain](#toolchain) is one that [Conforms](#conform) to the [Toolchain](#toolchain) specification; a [DBF](#dbf) project is one that [Conforms](#conform) to section 7.

#### Defect

Any observed problem worth acting on: a bug, a code review finding, a performance observation, an incident, an inconsistency. The method does not care which.

#### Class

The pattern, style, idiom or configuration that permitted the [Defect](#defect), expressed generally enough that other occurrences of it are also [Defects](#defect) or latent [Defects](#defect).

#### Instance

One occurrence of a [Class](#class). The reported [Defect](#defect) is one [Instance](#instance); there are usually others.

#### Hazard

The harm a [Class](#class) causes, which is **not necessarily a failure**. It may be a failure, but it may equally be error hiding, or something merely sloppy that makes the code harder to reason about or to change safely.

#### Detector

A tool that reads code without executing it and reports occurrences of a pattern. A [Detector](#detector) is not a [Runner](#runner). What a [Detector](#detector) must offer so that a [Practitioner](#practitioner) can write, prove, run and resolve a [Rule](#rule) in it is specified in the [detector specification](DETECTOR-SPEC.md).

#### Runner

A tool that **executes** code and reports what happened: a test [Runner](#runner), a compilation, a benchmark, a smoke check. A [Runner](#runner) answers questions about behaviour at one moment, on the paths it happened to exercise; a [Detector](#detector) answers questions about the text of the code, everywhere it exists. Detection under this method MUST come from a [Detector](#detector), for that reason.

#### Rule

One pattern definition within a [Detector](#detector).

#### Defence

A **[Blocking](#blocking)** [Rule](#rule) together with the supporting documentation that clarifies it and clearly signposts best practice. A [Rule](#rule) without its documentation is not a [Defence](#defence), and neither is a [Rule](#rule) that only warns.

#### Coverage

The accumulated set of [Defences](#defence) a project has built. Every [Defect](#defect) handled under this method extends it.

#### Remediation docs

The fuller documentation a failure [Message](#message) points to, explaining what a [Rule](#rule) is about, why it exists and how to fix a violation correctly.

#### Blocking

A [Rule](#rule) is [Blocking](#blocking) when its firing prevents a change from being accepted by whatever the project uses to accept changes. A report that does not block is a **[Warning](#warning)**, and a [Rule](#rule) that only warns is not a [Defence](#defence).

#### Warning

A report that does not block. A [Rule](#rule) that only warns is not a [Defence](#defence).

#### Message

The text a [Rule](#rule) prints when it fires. Terse, and carries the [Rule](#rule)'s [Identifier](#identifier).

#### Identifier

The stable string a [Rule](#rule) reports with, by which its [Remediation docs](#remediation-docs) are found. Survives renames of the [Rule](#rule).

#### False positive

A report on code that does not carry the [Hazard](#hazard).

#### Narrowing

Reducing a [Rule](#rule)'s scope so it stops reporting code that does not carry the [Hazard](#hazard). [Narrowing](#narrowing) that excludes code which does carry the [Hazard](#hazard) is a [Suppression](#suppression).

#### Suppression

Any means of preventing a [Rule](#rule) from reporting an [Instance](#instance) that carries the [Hazard](#hazard): an ignore comment, an ignore entry, a [Baseline](#baseline), or a [Narrowing](#narrowing) that excludes it.

#### Baseline

A recorded set of pre-existing [Instances](#instance) a [Rule](#rule) is configured not to report. A [Suppression](#suppression) in bulk.

#### Exception

A recorded [Owner](#owner) decision that a specific [Instance](#instance) or scope is excluded from a [Defence](#defence). The only legitimate form of [Suppression](#suppression). This document never uses the word in its programming-language sense.

#### Sweep

Running a [Rule](#rule) across the whole codebase to enumerate every [Instance](#instance).

#### Fixture

Code written to carry the [Hazard](#hazard) deliberately, so a [Rule](#rule) can be proven to fire when the codebase has no [Instance](#instance) to prove it on.

#### Calibration

A project-level ruling on a threshold or parameter this document leaves open.

#### Practitioner

Whoever is doing the work of this method on a given [Defect](#defect), human or [Agent](#agent). Decides how the [Defence](#defence) is built. Has no authority over [Exceptions](#exception).

#### Agent

A [Practitioner](#practitioner) that is an automated system. Everything said of a [Practitioner](#practitioner) applies to an [Agent](#agent); section 8 exists because of what is additionally true of one.

#### Owner

Whoever holds authority over a project's [Exceptions](#exception) and [Calibrations](#calibration). Always a human. The project decides who, and clause 8.7 requires the answer to be findable. Where the project has recorded nobody, the [Owner](#owner) is whoever instructed the [Practitioner](#practitioner), and [Escalation](#escalation) goes there, with one limit: that default [Owner](#owner) is usually the person under the same deadline as the [Practitioner](#practitioner), so a decision they take under section 4 to keep an [Instance](#instance) unfixed, [Suppress](#suppression), [Baseline](#baseline) or remove a [Rule](#rule) MUST be recorded in the project record with its justification, marked as taken by a default [Owner](#owner), and stating why nobody better placed was reachable, where the next reader can see who decided and why; and such a decision SHOULD be revisited by someone not under that deadline before the next release. A project that wants the separation section 4 describes names an [Owner](#owner); the default exists so work is not blocked, not to certify that a second judgement was applied.

#### Escalation

Referring a decision to the [Owner](#owner), whilst continuing with everything that does not depend on it.

#### Toolchain

Whatever a project assembles to run its checks through: its [Detectors](#detector) and [Runners](#runner), and the parts around them that route, list, record and resolve, from third-party, first-party and project-level parts in any combination. It is measured at the project level. What a [Toolchain](#toolchain) must offer beyond what each [Detector](#detector) in it offers is specified in the [toolchain specification](TOOLING-SPEC.md).

#### Conform

To satisfy every MUST of the relevant section 7 level, or of the companion specification being claimed. Partial satisfaction is not [Conformance](#conform).

## 2. When the method applies

Defence Before Fix applies to a [Defect](#defect) when that [Defect](#defect) can be attributed to a pattern, style,
idiom or configuration that a [Detector](#detector) can be made to recognise.

When it can, building the [Defence](#defence) is not optional and MUST be attempted before the [Defect](#defect) is
fixed. This is the substance of the method rather than a preliminary to it.

When it cannot, the [Defect](#defect) is outside the method's scope and is fixed conventionally. Not every
[Defect](#defect) is an [Instance](#instance) of a detectable pattern, and forcing a [Rule](#rule) where no pattern exists
produces [Detectors](#detector) that fire on innocent code, which is worse than having no [Detector](#detector).

**Attempt rather than pre-judge.** The [Practitioner](#practitioner) MUST attempt to express the [Class](#class) as a [Rule](#rule)
rather than deciding in advance whether it is expressible. Failing to write a [Rule](#rule) that satisfies
clause 3.1's bounds is itself the evidence that the [Defect](#defect) is out of scope, and it is cheaper and
more reliable than a judgement made before trying. The conclusion that no pattern exists MUST be
stated in one sentence, naming at least two independent techniques tried at expressing the
[Rule](#rule), in the vocabulary clause 3.1 uses for a search, and recorded where the project's
other decisions are enumerable under clause 8.7, not only with the fix. It is the cheapest way
out of the method and the only one that would otherwise leave no trace; enumerating it is how an
[Owner](#owner) sees an [Agent](#agent) routing around the method, and naming the techniques is what lets
them judge whether the attempt was one.

There are three ways out of the method and they are recorded differently. No pattern exists: the
[Defect](#defect) is out of scope under this section, and only the sentence above is recorded. A pattern exists but the
language has no extensible [Detector](#detector) and a bespoke one is not practical: a [Toolchain](#toolchain) gap
under clause 3.2. A pattern exists, a
[Detector](#detector) exists, but the [Toolchain](#toolchain) lacks a mechanism the [toolchain specification](TOOLING-SPEC.md) requires: a
mechanism gap under clause 3.2, and the [Rule](#rule) is still built. The attempt that separates the first
from the second is complete when the [Practitioner](#practitioner) has checked the [Detectors](#detector) the project already
runs and the language's own [Detector](#detector) ecosystem for an extension point, and found none.

## 3. The method

Six clauses, in order.

**Three of them turn on a judgement this specification deliberately does not close**: whether code
carries the [Hazard](#hazard) (3.1, 3.3), whether a search was comprehensive (3.1, 3.4), and how broadly to
draw the [Class](#class) (3.1). Any threshold given here would be calibrated to one codebase, one team and
one generation of [Toolchain](#toolchain), and would be wrong everywhere else.

**Those judgements are settled at project level, not in this document.** A project fixes its own
thresholds and parameters, in its configuration or in its [Toolchain](#toolchain)'s defaults, and where a case is
genuinely ambiguous it is raised, discussed and written down so the next person inherits the answer
rather than the argument. A project's accumulated decisions become part of its [Coverage](#coverage) in the same
way its [Rules](#rule) do.

**A project MUST make those decisions discoverable**, by the same means as its [Defences](#defence), so that a
[Practitioner](#practitioner) arriving cold can find what has already been settled instead of guessing at it or
re-opening it. The burden is the project's, not the reader's: a decision that cannot be found by the
means clause 8.7 requires is, for the [Practitioner](#practitioner)'s purposes, a decision the project has not
recorded, and the paragraph below applies. The search is therefore bounded: enumerate the project's
[Defences](#defence) as clause 8.5 requires them to be enumerable, and whatever is reachable from there is the
record. Nothing further is owed before concluding that nothing is recorded.

**Where the project has recorded nothing, the [Practitioner](#practitioner) is not blocked.** Proceed on the
examples below, **state the [Calibration](#calibration) assumed**, and record it with the [Remediation docs](#remediation-docs)
for the [Defence](#defence) being built, which clause 3.6 already requires to exist, to ship with the project
and to be reachable by a stable [Identifier](#identifier). That statement becomes the project's first recorded
decision on the point, and the next [Practitioner](#practitioner) inherits it.

A project MAY of course keep these decisions somewhere else and say so. **The default above exists
so that a [Practitioner](#practitioner) who finds no project convention still has one**, because "the project
decides" and "the project has decided nothing" would otherwise combine into a deadlock. What is
never acceptable is assuming silently, since a [Calibration](#calibration) nobody knows was chosen cannot be
corrected.

Worked examples of the three, to calibrate against:

| Judgement             | Too little                                                                                                  | Too much                                                                                          |
| --------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **[Hazard](#hazard)** | Only counting things that crash. Error hiding and code nobody can safely change are [Hazards](#hazard) too. | Counting every stylistic preference, so the [Rule](#rule) defends taste rather than the codebase. |
| **Comprehensive**     | One text search for the exact token from the reported [Defect](#defect), then stopping.                     | Auditing the whole system by hand before writing a [Rule](#rule) at all.                          |
| **[Class](#class)**   | A [Rule](#rule) matching the variable name in the original bug report.                                      | A [Rule](#rule) matching every use of the language feature the bug happened to involve.           |

### 3.1 Attribute the defect to a class

The [Practitioner](#practitioner) MUST first establish what [Class](#class) the [Defect](#defect) belongs to. The question is not
"what went wrong here" but "what kind of thing is this an [Instance](#instance) of".

A [Defect](#defect) usually belongs to several overlapping [Classes](#class) at different levels of abstraction, and
choosing between them determines the [Rule](#rule), the [Instance](#instance) count and the scope of the remediation.
Two bounds apply, and both are checkable during the work rather than matters of taste:

- **Lower bound.** If the [Rule](#rule) catches only the originating [Instance](#instance), the [Class](#class) is probably drawn
  too narrowly and MUST be widened, unless the independent search below has found no other
  [Instance](#instance) and the [Practitioner](#practitioner) records that the [Class](#class) is genuinely singular today. A
  [Rule](#rule) that matches exactly one thing is an [Instance](#instance) [Detector](#detector) wearing a [Rule](#rule)'s clothes.
  A [Rule](#rule) drawn to the exact value or name found in the [Defect](#defect) is the same [Narrowing](#narrowing) however
  it is spelt, and where it stays because the search found nothing wider, the record MUST also name the next
  wider [Rule](#rule), the one with the [Instance](#instance)'s distinguishing detail dropped, and state why it was
  rejected. That rejection is tested as a [Narrowing](#narrowing) is under clause 3.3: a sentence stating why the
  [Hazard](#hazard) cannot arise in the code the wider [Rule](#rule) would add, confirmed by search, with uncertainty
  routed upwards under section 4.
- **Upper bound.** If the [Rule](#rule) matches code that does not carry the [Hazard](#hazard), the [Class](#class) is drawn
  too broadly and MUST be narrowed. [False positives](#false-positive) destroy a [Defence](#defence)'s credibility faster than a
  missing [Rule](#rule) does. One report on code that does not carry the [Hazard](#hazard) is enough; there is no
  tolerated rate.

**Both bounds measure breadth within one level; the level itself is a separate question, answered
against the report.**
Where the [Defect](#defect) was reported as a behaviour, a check that reported clean having run nothing, a
process that stopped before its work, the [Class](#class) a [Detector](#detector) can read usually sits one level
below that [Hazard](#hazard): the mechanism of this [Instance](#instance), not the failure the report opens with.
That [Class](#class) is the right one to build, because no [Detector](#detector) reads "this check still produces
its signal". It is not the whole answer. The record MUST state whether the reported behaviour is also
pinned by a check a [Runner](#runner) executes, under section 6, either one added with this remediation or
an existing one named, and where neither is offered, why not. A [Class](#class) drawn at the mechanism with
the behaviour left unpinned defends the [Instance](#instance) thoroughly and the report not at all.

**Resolve the lower bound by searching independently, not by judgement.** The [Rule](#rule) is not the only
way to find [Instances](#instance), and it is the least trustworthy one whilst it is still unproven. Search for
other [Instances](#instance) by other means, whether that is a text search, reading the code, or asking someone
who knows the system, and, once the [Rule](#rule) exists under clause 3.2, confirm it catches what those
searches found. That confirmation is not one of the techniques.

That search MUST be a comprehensive one, carried out by a person, model or [Agent](#agent) competent to
carry it out. No fixed technique is prescribed, because what is comprehensive depends entirely on
the [Class](#class) and the codebase. What is not acceptable is a cursory look that exists to discharge the
requirement, since this search is what the single-[Instance](#instance) conclusion and the [Sweep](#sweep) count both
rest on, and a bad search validates a bad [Rule](#rule) silently.

**The stopping criterion is saturation, not effort.** Use at least two independent techniques, and
the search is complete when the last technique added found nothing the earlier ones had missed. A
second technique that turns up new [Instances](#instance) means a third is owed; a second that turns up nothing
new means the search is done. That is a test the [Practitioner](#practitioner) can apply and record without a
threshold, and it is the standard clause 3.4 refers back to.

Two techniques are independent when they would miss different things. A text search for the token
and a reading of the code paths that consume the value are independent; two text searches for two
spellings of the same token are one technique; asking someone who knows the system is a third. For a
[Class](#class) defined by how code is spelt, writing the idiom the other ways it is commonly spelt and searching
the codebase for each of them is a technique, because a search for one spelling misses every other;
whether the [Rule](#rule) catches those spellings is the confirmation step, not the technique. The
[Rule](#rule) itself is never one of the techniques, because the search exists to check the [Rule](#rule).
A clean run of the [Rule](#rule) is therefore not evidence of saturation either: "the [Rule](#rule) found nothing
the reading had missed" is one technique and a [Rule](#rule) run, not two techniques, and the stopping
criterion cannot be applied to it.
The record MUST name both techniques, chosen before the [Rule](#rule) is run against the codebase, and
MUST state what each found that the other could not have checked. A technique counts only if it does
not invoke the [Detector](#detector) under proof in any configuration and would exist unchanged had the
[Rule](#rule) never been written; a [Sweep](#sweep)-shaped run of the [Rule](#rule), however comprehensive it looks, is
never one of the two. Where a later technique shows that two earlier checks shared a blind spot, they
were one technique, and a third is owed.

That turns the single-[Instance](#instance) case into something checkable rather than a matter of taste. If an
independent search finds [Instances](#instance) the [Rule](#rule) missed, the [Class](#class) was drawn too narrowly and the [Rule](#rule)
MUST be widened until it catches them. Fixing those [Instances](#instance) by hand does not discharge the
widening: they are still [Instances](#instance) the [Rule](#rule) missed, and where the [Practitioner](#practitioner) leaves the
[Rule](#rule) unwidened because the wider check is harder to build without [False positives](#false-positive), that is
the [Owner](#owner)'s decision under section 4 and is recorded as one. If an independent search finds nothing
the [Rule](#rule) did not already have, then one [Instance](#instance) is a reasonable conclusion rather than an
assumption, and the [Rule](#rule) is correct as written.

**What this clause leaves on the record**, before clause 3.2 begins: the [Class](#class), spelt as a
pattern; the [Hazard](#hazard) sentence; the two search techniques and what each found; and the next
wider [Rule](#rule) that was not built, with the reason. A record missing any of the four has not
finished this clause.

**Why**: the [Class](#class) is the unit of work. Everything downstream operates on it, so an error here
wastes all the effort that follows.

### 3.2 Build the net

The [Practitioner](#practitioner) MUST express the [Class](#class) as a [Rule](#rule) in a [Detector](#detector), and the [Detector](#detector) MUST read code
rather than execute it.

A test MUST NOT serve as the [Detector](#detector). A test proves that one input produces one wrong output; a
[Rule](#rule) finds the pattern wherever it occurs, including in code nobody thought to test.

Where an off-the-shelf [Rule](#rule) or a tightening of existing configuration genuinely detects the
[Class](#class), using it [Conforms](#conform). However, a [Toolchain](#toolchain) that supports only its own built-in [Rules](#rule) cannot
support the method in general, so **a [Conforming](#conform) [Toolchain](#toolchain) MUST allow bespoke custom [Rules](#rule)**.
The [Rules](#rule) that matter most are tightly coupled to the project and carry project-specific
knowledge, both in the pattern they match and, importantly, in the [Message](#message) they emit.

Any tool that reads code and reports pattern matches qualifies, whatever its category. Static
[Detectors](#detector) such as PHPStan, ESLint, mypy and Clippy are the usual instruments; so are custom AST
walkers, architectural fitness checks, and [Detectors](#detector) that inspect a change before it lands. These
are examples rather than a permitted list, and a [Detector](#detector) is not disqualified for being unfamiliar.

Where the affected language has no extensible [Detector](#detector) available, the [Practitioner](#practitioner) MAY build a
bespoke one: a program of the project's own that reads code and reports matches of the [Class](#class), run
through the project's own entry point like any other [Detector](#detector). This is a last resort rather than
a default, because a [Detector](#detector) the ecosystem maintains is cheaper to keep and easier for the next
[Practitioner](#practitioner) to find, but a bespoke [Detector](#detector) is far better than none: the [Class](#class) is defended,
and every clause of this method applies to the bespoke [Detector](#detector) unchanged, including the proof in
3.3, the enforcement in 3.5 and the [Identifier](#identifier) and documentation in 3.6.

Only where a bespoke [Detector](#detector) is not practical either is the [Class](#class) undefended. That is a
**[Toolchain](#toolchain) gap and MUST be recorded as one**, with the reason a bespoke [Detector](#detector) was not
practical, rather than treated as the [Defect](#defect) being out of scope. The distinction matters, because
the first is a decision somebody can revisit and the second quietly disappears.

A gap is recorded in the project record where the [Toolchain](#toolchain) defines one, as the
[toolchain specification](TOOLING-SPEC.md) requires it to; only where it does not is the location the project's choice, and
then the only requirement is that somebody deciding what to invest in the [Toolchain](#toolchain) would find
it. A gap recorded where nobody looks has been forgotten with extra steps.

There are two kinds of gap and they lead to different work. The language having no extensible
[Detector](#detector) and no practical bespoke one is the gap above, and the [Class](#class) waits for one. The project's [Toolchain](#toolchain)
lacking a mechanism the [toolchain specification](TOOLING-SPEC.md) requires, such as a proving harness or an
[Identifier](#identifier) resolver, is a mechanism gap, and it does not put the [Class](#class) out of reach: the
[Practitioner](#practitioner) builds the [Rule](#rule), uses the substitutes clauses 3.3 and 3.6 already allow, and records
the mechanism gap alongside it. A mechanism gap that is also a breach of the [toolchain specification](TOOLING-SPEC.md)'s
own obligations, such as a [Toolchain](#toolchain) that cannot run its [Defences](#defence) on its own source, is recorded
against the [Toolchain](#toolchain)'s claim under section 7 as well, because that is the fact its [Owner](#owner) needs.
Where that record lives is the [Toolchain](#toolchain)'s own [Conformance](#conform) declaration, under the
[toolchain specification](TOOLING-SPEC.md)'s clause 9.2, or the [detector specification](DETECTOR-SPEC.md)'s clause 8.1 for a [Detector](#detector); a [Practitioner](#practitioner) who cannot write there reports it by the channel
section 4 names, as a blocked decision.

**What happens next is not waiting.** Once the gap is recorded, the [Defect](#defect) is fixed conventionally
under section 2, with its reproduction test, and the work moves on. What the record changes is the
[Class](#class), not the [Defect](#defect): the [Class](#class) is known to be undefended, and the next person to see an
[Instance](#instance) of it finds a decision to revisit rather than nothing.

**Why**: this clause is what distinguishes the method. Detection happens at the level of the
[Class](#class), using an artefact that can be pointed at the whole codebase, and it happens before
anything is fixed.

### 3.3 Prove the net by making the rule fire

A new [Rule](#rule) MUST be proven to fire before it is trusted. It is never the goal to write a [Rule](#rule) and
be instantly green.

**Proving and sweeping are two questions, not necessarily two runs.** Proving asks "does this [Rule](#rule)
work at all", and the answer is pass or fail. Sweeping, in clause 3.4, asks "how much of this [Class](#class)
is present", and the answer is a count. A single execution of the [Rule](#rule) answers both, and no second
run is required. What matters is that the two answers are not confused with one another: a large
count does not make a [Rule](#rule) more proven, and a [Rule](#rule) that fired does not tell you the [Sweep](#sweep) is
complete.

**The proof MUST survive as a commit of its own.** The [Defence](#defence) is committed with the originating
[Instance](#instance) still present, and the fix is committed after it. That first commit is the red run: it is
what a reviewer under section 7 checks out to reproduce the proof, and it is the only record that the
[Rule](#rule) fired on real code rather than on a [Fixture](#fixture) alone. Where the [Defence](#defence) and the fix share a
commit, the red run can only be reconstructed by hand-reverting lines the reviewer has to guess at,
and the proof rests on that guess.
Surviving as a commit means a fresh checkout of that commit, followed by the project's own declared
setup, reproduces the proof. Dependency installation and generation driven by files the commit does
carry, a manifest, a lockfile, are that setup. Anything else the proof depends on that version control
does not carry, an empty directory, an ignored file, an artefact placed by hand, is state the commit
does not contain, and a reviewer under section 7
reproduces from a fresh checkout rather than from the [Practitioner](#practitioner)'s working tree, so a
proof that passes only there does not survive.
Both commits MUST remain individually reachable in the history the reviewer inspects. A merge that
flattens them into one destroys the proof, so a project whose merge policy does that MUST keep the
[Defence](#defence) commit reachable by another recorded reference, a tag or the retained branch, or MUST NOT
claim the remediation [Conforms](#conform). How the project merges is its own business under section 8;
what must survive the merge is not.

**A [Narrowing](#narrowing) is proven the other way round, and both ways.** Where the change under proof is
that the [Rule](#rule) should stop firing on code that does not carry the [Hazard](#hazard), three things are shown:
the [Rule](#rule) firing on that code before the change, from a commit still reachable in history and to the
same standard as a new [Rule](#rule)'s red run; the [Rule](#rule) not firing on it afterwards; and a retained
[Fixture](#fixture) on which it still fires afterwards, the case that motivated the [Rule](#rule). Where the narrower
shape was chosen from the outset and no wider [Rule](#rule) was ever built, the before state is a [Fixture](#fixture)
of the wider pattern the [Rule](#rule) does not catch, retained as the record of what was left out.

**Firing on more than the originating [Defect](#defect) is success.** A [Rule](#rule) that catches the reported
[Instance](#instance) and forty-nine others has done exactly what it was built to do, and the forty-nine are
the reason the method exists.

**The test for whether [Narrowing](#narrowing) is legitimate is the [Hazard](#hazard), never the count.** The
test has two halves, and the rest of this passage says how each is checked:

- **[Narrowing](#narrowing)**, which the [Practitioner](#practitioner) decides: they can write down why
  the [Hazard](#hazard) cannot arise in the code being excluded, and they record that sentence.
- **[Suppression](#suppression)**, which the [Owner](#owner) decides under section 4: the sentence
  cannot be written, so the exclusion is not the [Practitioner](#practitioner)'s to make. Doubt is
  [Suppression](#suppression); [Narrowing](#narrowing) needs confidence backed by the sentence.

Ask what the [Narrowing](#narrowing) would exclude:

- If the excluded code **carries the [Hazard](#hazard)**, the [Narrowing](#narrowing) is [Suppression](#suppression) and is forbidden,
  however many or few [Instances](#instance) it removes.
- If the excluded code **does not carry the [Hazard](#hazard)**, the [Narrowing](#narrowing) is precision and is required
  by clause 3.1's upper bound.

A [Rule](#rule) MUST NOT be narrowed because its [Instance](#instance) count is uncomfortably high. A high count is a
finding about the codebase, not a [Defect](#defect) in the [Rule](#rule).

**If you are not sure whether the excluded code carries the [Hazard](#hazard), you are suppressing.** Treat it
as a [Suppression](#suppression) and refer it upwards under section 4. The [Practitioner](#practitioner) narrows on confidence, not
on the balance of probability.

**"Sure" is not a percentage; it is a sentence.** The [Practitioner](#practitioner) is sure when they can write down,
for the code being excluded, why the [Hazard](#hazard) cannot arise there, and that sentence is recorded with
the [Narrowing](#narrowing) as part of the [Rule](#rule)'s [Remediation docs](#remediation-docs). If the sentence cannot be
written, the exclusion is a [Suppression](#suppression) and goes upwards. Confidence that cannot be stated is not
confidence.

A [Narrowing](#narrowing) reduces the [Practitioner](#practitioner)'s own work, which is why it is not left to self-report
alone. The sentence states the reasoning; the search confirms it. Code a [Narrowing](#narrowing) excludes
MUST be searched to the standard of clause 3.1, and an [Instance](#instance) that search finds there
disproves the sentence and reverses the [Narrowing](#narrowing). Every [Narrowing](#narrowing) MUST be enumerable by the
same means as the project's [Exceptions](#exception), so the [Owner](#owner) sees them in one place, and a
[Narrowing](#narrowing) that excludes more code than the [Rule](#rule) still covers MUST be reported to the [Owner](#owner)
as if it were a [Suppression](#suppression). The sentence remains the test of whether an exclusion is honest;
the search and the listing are what make a fluent dishonest one visible.
Where the [Toolchain](#toolchain)'s own listing shows the [Narrowing](#narrowing) with its sentence, that listing is
the record, and no separate prose is owed for it.

The sentence may turn out to be wrong. The method does not require the [Practitioner](#practitioner) to be
infallible; it requires the reasoning to be written down where the next reader, or the next
[Defect](#defect), can test it. A [Narrowing](#narrowing) with a recorded reason is correctable. One without is
indistinguishable from a [Suppression](#suppression), which is why the sentence is the test and a percentage is
not.

**Where the pattern is present, prove the [Rule](#rule) against it.** At minimum the [Rule](#rule) MUST detect the
originating [Defect](#defect). Where the [Defect](#defect) was found in code review rather than in production, the
pattern exists in the branch under review, so the [Rule](#rule) is written and proven there before the fix
lands.

**Where the pattern is genuinely absent, prove the [Rule](#rule) another way.** A [Rule](#rule) may legitimately be
green against the codebase: the branch that carried the pattern may have been rejected and
orphaned, the [Instance](#instance) may already have been fixed, or the [Rule](#rule) may be a purely proactive [Defence](#defence)
against a pattern that might occur but does not yet. In each of these cases the [Rule](#rule) MUST still be
proven, using [Fixture](#fixture) code that demonstrates the pattern the [Rule](#rule) is meant to catch. That [Fixture](#fixture)
SHOULD be kept as the [Rule](#rule)'s own test rather than deleted, so the proof re-runs whenever the [Rule](#rule) runs
instead of expiring the moment it succeeds.

**A green run proves nothing unless the [Rule](#rule) was loaded.** Before treating any run as evidence,
confirm the [Rule](#rule) was active in it, by enumerating the [Defences](#defence) that run was configured with or by
seeing it fire on a [Fixture](#fixture) in the same run. A [Toolchain](#toolchain) analysing its own source with a
configuration that omits its own bundled [Rules](#rule) reports clean on every one of them, and both the
[Practitioner](#practitioner) and a reviewer have taken that for a pass.

**A [Rule](#rule) about how code is written may match its own source.** A [Rule](#rule) that forbids a construct in
[Rule](#rule) code will contain that construct, because it has to look for it. That match is not an
[Instance](#instance): the construct there is the [Rule](#rule)'s subject, not its use, so the [Hazard](#hazard) is absent and
clause 3.1's upper bound requires the [Narrowing](#narrowing). Exclude it as precisely as possible, write the
sentence, and keep a test that proves the exclusion reaches nothing else.

**[Rules](#rule) are software, and SHOULD be built test-first like any other software.** How practical
that is varies considerably between [Detectors](#detector), some of which offer purpose-built [Rule](#rule)-testing harnesses
and some of which offer nothing, so this is a best-effort requirement rather than an absolute one.
Where a [Detector](#detector) makes [Fixture](#fixture)-based testing impractical, an acceptance or smoke check that
demonstrates the [Rule](#rule) firing is an acceptable substitute.

[Fixtures](#fixture) are part of the [Rule](#rule) and are versioned with it, under the co-location requirement in
clause 3.6. A [Fixture](#fixture) is input to the [Rule](#rule)'s test, not part of the code the [Defence](#defence) enforces:
the [Sweep](#sweep) excludes it under clause 3.4, and the enforced run does not report it, so there is no
circularity in a [Fixture](#fixture) that deliberately fails the [Rule](#rule) it proves. Writing the [Fixture](#fixture) is the [Practitioner](#practitioner)'s own decision under section 4, not something
to refer upwards.

Where they sit within the repository is the project's business. **Absent a convention, put them
where the project's existing tests live, and where there are none, alongside the [Rule](#rule)** - then say
which was chosen, as with any other [Calibration](#calibration) under section 3.

**Why**: proving is the [Rule](#rule)'s own validation. A [Rule](#rule) that does not catch the [Instance](#instance) that
prompted it does not detect the [Class](#class) it claims to, and shipping it would add a [Defence](#defence) that defends nothing
whilst defending nothing. This is the clause most easily skipped, because a green run feels like
success and looks like a clean codebase.

### 3.4 Sweep the codebase, then fix every instance

The [Practitioner](#practitioner) MUST run the [Rule](#rule) across the entire codebase and record the total [Instance](#instance)
count before fixing anything, and MUST then fix every [Instance](#instance) found rather than only the one
that was reported.

**"Entire codebase" means everywhere the pattern can occur, and nowhere it cannot.** For most
[Classes](#class) that is a single language, because the pattern is a feature of that language, and sweeping
unrelated languages would be theatre. What the clause forbids is stopping at the package,
component or service that happened to report the [Defect](#defect) when the pattern plainly reaches further.
The question is where the pattern can exist, never where the bug was found.

Whether vendored dependencies, generated code and test [Fixtures](#fixture) are in scope is the project's
decision, and it SHOULD be a recorded one rather than an implicit one, because a [Class](#class) that is
excluded silently is indistinguishable from a [Class](#class) that was never swept. **Where a project has
recorded no such decision, [Sweep](#sweep) all first-party source in every language where the pattern can
occur, and exclude generated code and vendored dependencies**, then record that as the decision.
First-party source is code the project maintains in its own repository; generated code is what a
build step produces from other source; vendored code is a dependency copied in rather than
installed. Modified vendored code is first-party, because the project now maintains it. The two
exclusions are not a judgement that such code carries no [Hazard](#hazard). Unmodified vendored code is
somebody else's project, and an [Instance](#instance) found in it is reported upstream rather than fixed
in place; generated code carries an [Instance](#instance) only because its generator does, and the generator
is the first-party source the [Sweep](#sweep) covers. An [Instance](#instance) the [Practitioner](#practitioner) notices in either
is recorded as a known [Instance](#instance) under section 4, not ignored.
A [Rule](#rule)'s own [Fixtures](#fixture) under clause 3.3 are never [Instances](#instance): they carry the pattern
deliberately, as the proof, and the [Sweep](#sweep) count excludes them.

**The count MUST be corroborated independently**, to the standard set out in clause 3.1: a
comprehensive search by someone competent to make it. A [Rule](#rule) that is too narrow produces a small
count and a clean-looking [Sweep](#sweep), and nothing inside the [Rule](#rule) can reveal that.

Where the independent search finds [Instances](#instance) the [Rule](#rule) did not, **clause 3.1 governs: the [Rule](#rule) was
drawn too narrowly and MUST be widened until it catches them.** The two are not permitted to
disagree, and the search is the authority, not the [Rule](#rule).

**Each fix MUST address the [Hazard](#hazard) rather than the [Rule](#rule).** Throw on the absent case, or propagate
the absence explicitly so the caller decides: whatever the correct behaviour turns out to be. What is
forbidden is a change that turns the [Rule](#rule) green whilst leaving the failure mode intact, and
suppressing the [Rule](#rule) at the call site, which is not a fix at all.

**Supplying a default is usually the [Hazard](#hazard) in another form**, not a fix. A default makes the absent
case look present, and the failure moves downstream to where nobody expects it and nothing names it.
A default is a fix only where absence is a legitimate state whose meaning the code defines, and then
the default states that meaning rather than filling the gap with a placeholder. This is the same
test as clause 3.3's [Narrowing](#narrowing) sentence and carries the same discipline: the [Practitioner](#practitioner)
MUST write down, with the fix, what the absence means and why the default is that meaning, and
where the sentence cannot be written the absence is an error and MUST be treated as one.

**Repetition is not the problem.** Where every [Instance](#instance) genuinely has the same correct answer,
applying that answer to all of them is right, and the fact that it looks mechanical is not an
objection. The requirement is that each [Instance](#instance) was actually examined and the same answer was
genuinely correct for it, rather than assumed correct because it was correct elsewhere. Where one
change is applied across many [Instances](#instance), the [Practitioner](#practitioner) MUST record which were examined
individually and which received the change by pattern, and MUST examine a sample of the latter
large enough, given how much the surrounding code varies, that a wrong answer there would have
been seen. "All examined" with nothing behind it is a claim, not a record.

**Fix them all.** There is no count at which a [Practitioner](#practitioner) stops fixing. A [Practitioner](#practitioner)
stops only when the next [Instance](#instance) needs a decision they lack the authority to make, and section 4
says which decisions those are; a hundred [Instances](#instance), or a thousand, is work rather than a
decision. A [Baseline](#baseline) of the existing [Instances](#instance), so that the [Rule](#rule) blocks only new ones, MAY
be adopted where fixing every [Instance](#instance) is genuinely unfeasible, and the scale at which that
becomes true is tremendous. **No threshold is given here deliberately.** Any figure would be
calibrated to the [Toolchain](#toolchain) of the moment rather than to anything durable, and the honest measure is
the size of the change rather than the hours it would take, since the hours depend entirely on what
is doing the work.

**Under AI-assisted development a [Baseline](#baseline) is almost never the right answer.** The historical case
for baselining was the cost of human hours, and that cost has largely collapsed: an [Agent](#agent) can work
through hundreds of [Instances](#instance) at a price that made a [Baseline](#baseline) unavoidable a few years ago. Reaching
for one now is usually a habit rather than a judgement. This specification stops short of
forbidding [Baselines](#baseline) outright, and only just.

Adopting one is a decision for whoever owns the codebase, taken after fixing has genuinely been
attempted rather than on the strength of the [Instance](#instance) count alone. "Attempted" is the
[Owner](#owner)'s judgement on the [Practitioner](#practitioner)'s report, not a threshold the [Practitioner](#practitioner) applies:
the [Practitioner](#practitioner) fixes until stopped by a decision they cannot make, and reports what was fixed and
what remains. That report MUST state the count fixed, the count remaining, what stopped the fixing,
and what would have to be tried next, so the [Owner](#owner) judges a record and not an adjective. **A
[Practitioner](#practitioner) executing this method does not have that authority** - see section 4. A baselined project SHOULD reduce the
[Baseline](#baseline) over time and MUST NOT allow it to grow.

**Why**: consistency across a codebase is fundamental, and the [Sweep](#sweep) is where this method
delivers most of its value. In the published worked example the reported [Defect](#defect) was one of
twenty-three; the other twenty-two were bugs waiting to surface in different contexts, reported
by different customers, at different times. A project that knows about twenty-three [Instances](#instance)
and fixes one has produced a documented list of [Defects](#defect) it has chosen to keep.

### 3.5 Enforce permanently, and block

The [Rule](#rule) MUST become a permanent part of the project's quality checks, and it MUST **fail** rather
than warn. A [Rule](#rule) that reports a violation without failing does not [Conform](#conform).

**Where those checks run, and what the project does when they fail, is out of scope.** Continuous
integration, git hooks, branch policy and release process are the project's own business; see
section 8. What this clause requires is that the [Defence](#defence) is permanent, applies to everyone rather
than to whoever remembers it, and produces a failure rather than a remark.

Removing a [Rule](#rule), or adding a [Suppression](#suppression) for an [Instance](#instance), MUST be a recorded decision rather
than a silent edit, and belongs to the [Owner](#owner) under section 4, which governs.

**Enforcement is demonstrated through the project's own entry point.** Running the [Detector](#detector)
directly shows that the [Rule](#rule) can fire; it does not show that the project's checks will run it.
The [Practitioner](#practitioner) MUST run the invocation the project uses to accept changes, over everything
that invocation covers, and see the [Rule](#rule) reported there. A [Toolchain](#toolchain) that wraps its
[Detectors](#detector) in its own command is asking for that command to be used, and a [Practitioner](#practitioner)
who bypasses it has proven the [Rule](#rule) and not the [Defence](#defence).

For a [Bundled defence](TOOLING-SPEC.md#bundled-defence), the project whose entry point demonstrates it is any project the
[Toolchain](#toolchain) is genuinely installed into, the [Consuming project](TOOLING-SPEC.md#consuming-project) included, since that is
where the [Rule](#rule) will be enforced. A mechanism gap that stops the [Toolchain](#toolchain) running its own entry
point on its own source moves the demonstration to such a project; it does not weaken it. The
substitutes clause 3.2 allows, for proving under clause 3.3 and for resolution under clause 3.6, do
not extend to this clause: the demonstration here is through an entry point or it is not made. A
project created for the purpose, with the [Toolchain](#toolchain) installed into it from the source under
test, is such a project, so a [Toolchain](#toolchain) with no consumer yet is not excused.

**Why**: the purpose is that the mistakes of the past become structurally impossible to repeat, and
a [Warning](#warning) is not structure. A [Warning](#warning) is a suggestion, and suggestions decay under deadline
pressure, which is the condition under which the original [Defect](#defect) was written.

### 3.6 Make the failure message terse, and point it at real documentation

The failure [Message](#message) MUST be terse, and it MUST carry a stable [Identifier](#identifier) that resolves to
[Remediation docs](#remediation-docs) shipped with the project.

That documentation MUST state three things: what the [Rule](#rule) is about, why it exists, and how to
fix a violation correctly using the project's preferred approach.

A [Practitioner](#practitioner) who finds that an existing [Rule](#rule)'s printed [Identifier](#identifier) does not resolve records
it where clause 3.2's gaps are recorded, naming the [Rule](#rule) and the [Identifier](#identifier), with no [Rule](#rule) build of
their own to attach it to. It does not block the remediation. Where the mechanism cannot resolve
[Identifiers](#identifier) at all, it is a [Toolchain](#toolchain) gap and blocks the [Toolchain](#toolchain)'s claim under section 7
until fixed; where the mechanism resolves others and only this [Rule](#rule)'s documentation is missing, it is a
fault in that [Rule](#rule)'s [Remediation docs](#remediation-docs), owned by whoever wrote the [Rule](#rule), and bears on
the project's claim rather than the [Toolchain](#toolchain)'s.

**The split between the two is by job, not by length.** The [Message](#message) carries what was detected,
where, and the [Identifier](#identifier); it is read under interruption by somebody trying to get on with
something else. The documentation carries the reasoning and the remedy; it is read once, by
somebody who has decided to understand the [Rule](#rule), and it is maintained as the project's thinking
develops. Anything that would grow over time belongs in the documentation.

**A [Rule](#rule) and its documentation are one artefact and MUST be versioned as one.** They live in the
same repository and are committed together, or in a library the project depends on at a clearly
tracked version. A [Rule](#rule) carries knowledge specific to the project it defends, and its
documentation is where most of that knowledge actually sits, so anything that lets the two drift
apart destroys the value of both. The same applies to a [Rule](#rule)'s [Fixtures](#fixture) under clause 3.3.

An external URL [Conforms](#conform) only where the project controls it and versions it alongside the [Rule](#rule). A
link into a third-party wiki or a general article does not, because neither can be relied upon to
still describe this [Rule](#rule).

**Repository structure is left to the project.** Where these artefacts sit, how they are foldered,
whether [Rules](#rule) are vendored or depended upon: none of that is this specification's business. What
is required is that they move together.

The [Identifier](#identifier) MAY be a [Rule](#rule) ID resolved by a command, an anchor in a documentation file, or a
URL. It MUST continue to resolve for as long as any released version can emit it, which is a
stronger requirement than surviving the current release. Where a [Rule](#rule) is redesigned such that its
meaning materially changes, a new [Identifier](#identifier) SHOULD be issued and the old one SHOULD keep
resolving to an explanation of what became of it.

A [Message](#message) that names a pattern without leading anywhere does not [Conform](#conform). "Pattern X detected"
teaches nothing.

**Why**: the [Message](#message) is read at the moment of failure, by someone who wants to get on with their
work, so it has to be short enough to read and specific enough to act on, whilst the reasoning
has to live somewhere it can be maintained and can grow. Splitting it this way keeps the [Message](#message)
terse without losing the teaching, and the documentation becomes the project's accumulated
engineering knowledge rather than a comment nobody revisits. The best custom [Rules](#rule) are
opinionated documentation encoded as automation.

## 4. Authority: which decisions belong to whom

The method is frequently executed by somebody who does not own the codebase, including an [Agent](#agent)
acting under instruction. This section states which decisions that person takes alone and which
they do not.

**Decisions the [Practitioner](#practitioner) takes alone**, without seeking approval:

- What [Class](#class) the [Defect](#defect) belongs to, and where its bounds sit (clause 3.1).
- Which [Detector](#detector) to use and how to express the [Rule](#rule) in it (clause 3.2).
- How to prove the [Rule](#rule), and what [Fixture](#fixture) to prove it against (clause 3.3).
- What the correct behaviour is at each [Instance](#instance), and therefore what each fix should be (clause
  3.4).
- The wording of the failure [Message](#message) and the [Remediation docs](#remediation-docs) (clause 3.6).

**Decisions that MUST go to whoever owns the codebase:**

- Adopting a [Baseline](#baseline), in whole or in part (clause 3.4).
- Suppressing an [Instance](#instance), or removing or disabling an existing [Rule](#rule) (clauses 3.4 and 3.5).
- Accepting a known [Instance](#instance) as unfixed for any reason.
- Deciding that a [Class](#class) will not be defended at all, where a [Rule](#rule) for it is achievable.
- Leaving unbuilt the next wider [Rule](#rule) that clause 3.1 required the [Practitioner](#practitioner) to name, where
  it was rejected because no [Instance](#instance) of it exists today rather than because the [Hazard](#hazard) cannot
  arise there. The absence of an [Instance](#instance) is the [Practitioner](#practitioner)'s reason not to widen unasked; it
  is not authority to exclude the extension, and recording it as a known gap does not change whose
  decision it is. This does not reopen a [Class](#class) whose bounds a [Hazard](#hazard) sentence has settled, and
  it reaches no further than the one wider [Rule](#rule) already on the record.
- Leaving a [Rule](#rule) narrower than an independent search under clause 3.1 showed it should be, where
  the reason is that the wider check is harder to build without [False positives](#false-positive) rather
  than that the [Hazard](#hazard) is absent from what it would add. The [Instances](#instance) the search found are
  fixed regardless; what stays with the [Owner](#owner) is the [Class](#class) left partly undefended.

The dividing line is that the [Practitioner](#practitioner) decides **how the [Defence](#defence) is built** and the [Owner](#owner)
decides **what the codebase is permitted to keep**. An [Agent](#agent) MUST NOT [Baseline](#baseline), suppress or
knowingly leave an [Instance](#instance) unfixed on its own authority, whatever the [Instance](#instance) count turns out to
be.

**The default position is that none of these are permitted at all.** [Suppressions](#suppression), [Baselines](#baseline) and
every other means of evading a [Defence](#defence) are not techniques with a threshold governing their use; they are
[Exceptions](#exception) to the method, and the standing answer is no. An [Exception](#exception) exists only where a human has
discussed it, agreed it and documented it for that project. Nothing an [Agent](#agent) concludes on its own
creates one.

**Uncertainty is itself an [Escalation](#escalation) trigger.** Where the [Practitioner](#practitioner) is not confident that code
they are about to exclude is free of the [Hazard](#hazard), that exclusion is a [Suppression](#suppression) and belongs to the
[Owner](#owner), whatever it is called. This is deliberately asymmetric: [Narrowing](#narrowing) is the [Practitioner](#practitioner)'s
decision only whilst they are sure, and doubt routes it upwards. Without this, the [Hazard](#hazard) judgement
in clause 3.3 would let a [Practitioner](#practitioner) suppress an [Instance](#instance) whilst never touching the clause that
would have escalated it.

**Where the work is entirely [Agent](#agent)-driven, do the work.** Fixing [Instances](#instance) is cheap now, and an
[Agent](#agent) that reaches for an [Exception](#exception) has almost always found a shortcut rather than a genuine
obstacle.

**What to do whilst waiting.** A decision awaiting the [Owner](#owner) MUST NOT stall the rest of the work.
The [Practitioner](#practitioner) completes everything within their own authority, reports the blocked decision
with the [Instance](#instance) count and what it would cost to fix, and leaves the [Rule](#rule) unmerged rather than
merged in a weakened form. Where the only thing pending is whether one matched case carries the
[Hazard](#hazard), the [Rule](#rule) MAY merge at full width with that case recorded as a known [Instance](#instance)
awaiting the [Owner](#owner), enumerable under clause 8.7: the [Rule](#rule) is not weakened, the case is not
hidden, and the [Practitioner](#practitioner) is not pushed towards declaring that no pattern exists. Reporting a
[Sweep](#sweep) of four hundred [Instances](#instance) and stopping is a useful outcome; quietly baselining them is not.

Report by whatever channel carries the rest of the [Practitioner](#practitioner)'s work: for an [Agent](#agent), its
output to whoever instructed it. An [Instance](#instance) in code the [Practitioner](#practitioner) is not permitted to
change is reported the same way, as a blocked decision with its count, and is never a reason to
narrow the [Rule](#rule) so that it stops seeing it.

**The [Instance](#instance) count alone never triggers [Escalation](#escalation).** A large [Sweep](#sweep) is work, not a blocked
decision. Stopping to report is what the [Practitioner](#practitioner) does when an [Owner](#owner) decision is genuinely
required, which means an [Exception](#exception) is being contemplated, or when they are uncertain whether an
exclusion carries the [Hazard](#hazard). It is not what they do because the number is uncomfortable. Five
hundred [Instances](#instance) with no [Exception](#exception) needed is five hundred [Instances](#instance) to fix.

A remediation MAY be delivered across several changes where the volume warrants it, **provided the
[Rule](#rule) does not become [Blocking](#blocking) until every [Instance](#instance) is fixed**, since a [Blocking](#blocking) [Rule](#rule) merged over a
codebase that still violates it either fails continuously or has been weakened to avoid doing so.
No [Instance](#instance) may be knowingly left unfixed at the end without the [Owner](#owner)'s decision.

**Why**: without this, an executing [Agent](#agent) either stalls at the first judgement call it cannot
authorise or takes the decision unilaterally, and the second failure is much harder to notice than
the first. Both were observed in cold readings of an earlier draft of this specification.

## 5. Ordering the quality checks

Defence Before Fix presumes quality checks ordered as follows, and the ordering is enforcing rather
than advisory:

1. [Detectors](#detector) - type checking, linting, custom [Rules](#rule)
2. Automated tests - unit, integration, functional
3. Build verification - services start, dependencies resolve
4. Human acceptance testing - visual review, workflow validation

[Detectors](#detector) MUST run first, and a failure at that level MUST stop the levels below it from
being treated as meaningful.

This constrains the **sequence of checks**, not the infrastructure that runs them. How the project
expresses that sequence is out of scope, per section 8. It is a property of the project, not a step
in any one remediation: a [Practitioner](#practitioner) handling a [Defect](#defect) is not required to reorder the
project's checks, and a project whose checks run in another order is a project that does not
[Conform](#conform), which is a finding to record, not work to do on the way to a fix.

**Why**: a [Detector](#detector) is preventive and a test is diagnostic. A [Detector](#detector) reads every file, every
time it runs, so it cannot miss a file merely because nobody thought to write a test for it.
Failures at a lower level also produce confusing results at the levels above, so any other order
costs time diagnosing symptoms of a problem the first level would have named directly.

## 6. Relationship to test-driven development

Defence Before Fix neither replaces nor competes with TDD. They operate at different levels, and
a full remediation uses both: a test, executed by a [Runner](#runner), pins the [Instance](#instance); a [Rule](#rule), evaluated by
a [Detector](#detector), catches the [Class](#class).

| Concern            | TDD                                | Defence Before Fix                                   |
| ------------------ | ---------------------------------- | ---------------------------------------------------- |
| Operates on        | The specific [Defect](#defect)     | The [Class](#class) the [Defect](#defect) belongs to |
| Artefact           | A test                             | A [Rule](#rule) in a [Detector](#detector)           |
| Proves correctness | For one behaviour, by executing it | For a pattern, by reading the code                   |
| Answers            | "Is this bug fixed?"               | "Can this kind of bug still exist anywhere?"         |

The specific [Defect](#defect) is still reproduced with a test and proven fixed, exactly as normal. What
this method adds is the phase before that work begins, in which the codebase's permanent [Defence](#defence)
[Coverage](#coverage) is extended using the evidence the [Defect](#defect) has just supplied.

The name records the ordering. The [Defence](#defence) comes first, because once the fix has landed the
evidence is gone and the opportunity closes with it.

## 7. Conformance

[Conformance](#conform) is claimed at one of four levels. Partial [Conformance](#conform) MUST NOT be described as
[Conformance](#conform).

**A remediation [Conforms](#conform)** if all six clauses of section 3 were followed for that [Defect](#defect).

**A [Defence](#defence) [Conforms](#conform)** if it satisfies clauses 3.1, 3.2, 3.3, 3.5 and 3.6: it is drawn to a
[Class](#class) within both bounds and not to the reported [Instance](#instance), it is evaluated by reading code, it
was proven to fire against either the originating [Instance](#instance) or [Fixture](#fixture) code, it fails rather
than warns, and its [Message](#message) is terse and resolves to [Remediation docs](#remediation-docs) versioned alongside
it. A [Defence](#defence) can [Conform](#conform) whilst the [Sweep](#sweep) is incomplete; what that describes is a
[Conforming](#conform) [Defence](#defence) over a codebase with known [Instances](#instance), which section 4 requires to be
recorded, not a [Conforming](#conform) remediation.

**A [Toolchain](#toolchain) [Conforms](#conform)** if it permits bespoke custom [Rules](#rule), supports the ordering in section 5,
and satisfies clauses 8.1 to 8.5 and 8.7: the [Practitioner](#practitioner) can run it, the result reaches them in
the output they are reading, [Identifiers](#identifier) resolve mechanically, documentation states the correct
construction, and both the [Defences](#defence) and the project's recorded decisions can be enumerated. Clause
8.6 is a SHOULD and does not bear on [Conformance](#conform), deliberately: it is the one clause that acts
before a mistake rather than after, so no failing run can prove it absent, and [Conformance](#conform) is
claimed only over what a run can prove. The [toolchain specification](TOOLING-SPEC.md) names a
[Toolchain](#toolchain) that also satisfies it as [Conforming](#conform) with [Agent](#agent) support, which is the claim to
make when it is true. Those obligations fall in two documents: what each [Detector](#detector) the
[Toolchain](#toolchain) routes a [Defence](#defence) through must offer is stated in the
[detector specification](DETECTOR-SPEC.md), and what the assembled [Toolchain](#toolchain) must add is stated
in the [toolchain specification](TOOLING-SPEC.md), which requires the first as its own opening clause,
carries the ordering in section 5 and the correct construction of clause 8.4 as clauses of its own,
and states the listing and the project record that clauses 8.5 and 8.7 require.

**A project [Conforms](#conform)** if its [Defences](#defence) and [Remediation docs](#remediation-docs) [Conform](#conform), and if its recorded
decisions under section 3 are discoverable. Nothing here constrains how the project runs its checks
or what it does when they fail.

[Toolchain](#toolchain) [Conformance](#conform) is stated in full in the [detector specification](DETECTOR-SPEC.md)
and the [toolchain specification](TOOLING-SPEC.md) together, which give each of the obligations above as a
clause with its own reasoning, and add what a [Detector](#detector) and a [Toolchain](#toolchain) must provide so
that a project can meet its own. The summary here is normative and sufficient to judge a
[Toolchain](#toolchain) by; the companion documents are where a [Detector](#detector) maintainer and a
[Toolchain](#toolchain) author should work from.

A verdict on a remediation or a [Defence](#defence) MUST rest on reproduction, not on the report: the reviewer
reruns the [Defence](#defence) red at the commit that introduced it and green at the final commit, through the
project's own entry point for accepting changes, and reruns the originating symptom against the fix.
Where the [Rule](#rule) was proven against a [Fixture](#fixture) under clause 3.3, the red run is against the
retained [Fixture](#fixture). Where the originating symptom cannot be reproduced through the entry point,
an incident or an observation at production scale, the reviewer says so and verifies the red and green
runs alone. A verdict on a [Toolchain](#toolchain) or a project rests on the reviewer exercising the clauses
named above, not on the claimant's report of having done so. A report that reads as [Conforming](#conform)
has not been shown to be.

A [Toolchain](#toolchain) MAY additionally audit its own [Rules](#rule) against clause 3.6, failing its own release if any
[Rule](#rule) fails something without resolving to [Remediation docs](#remediation-docs). This is the strongest
available demonstration that the clause is honoured rather than asserted.

## 8. Operating a defence under AI-assisted development

*This section is normative.*

### The argument these clauses rest on

For a human developer, a failure [Message](#message) that teaches is good practice. They may read it, may
internalise it, may ignore it, and which of those happens depends on their seniority, their
workload and how many times they have seen the [Message](#message) before.

For an [Agent](#agent), the failure [Message](#message) is the entire remediation loop. It is consumed as instruction,
in the same turn, every time, with no fatigue and no seniority gradient. A [Message](#message) that resolves
to documentation explaining the correct approach does not simply block the [Agent](#agent), it redirects it,
and it does so identically on the thousandth occurrence as on the first.

That reframes the usual complaint about AI-written code. The difficulty was never that [Agents](#agent) make
mistakes, since people do too. The difficulty is that nobody built the channel to correct them at
the level of the [Class](#class) rather than the [Instance](#instance).

If the value of the method depends on that loop closing, then what closing it requires has to be
stated rather than assumed. The clauses below are what a [Defence](#defence) must do to be usable by an [Agent](#agent)
at all.

### Scope: this specifies a defence, not a pipeline

**Continuous integration, git hooks, branch policy, review process and release management are out
of scope.** How a project chooses to run its quality checks, and what it does when they fail, is
the project's own business and no part of this specification.

What is in scope is the [Defence](#defence) itself: a [Rule](#rule) that reads code, the documentation that explains it,
and the requirement that the [Practitioner](#practitioner) can run it and act on the result. A specification that
told projects how to run their checks would be overreaching, and would be ignored for it.

### 8.1 The practitioner MUST be able to run the defence themselves

A [Rule](#rule) that only reports through infrastructure the [Practitioner](#practitioner) cannot invoke is not usable by
them, whatever it does for anyone else.

**Why**: an [Agent](#agent) that cannot check its own work against a [Defence](#defence) cannot iterate against it, so
the loop never closes in the turn where the mistake was made, which is the only moment it is cheap
to fix.

### 8.2 The result MUST reach the practitioner in the output they are already reading

The [Detector](#detector)'s own output, at the point of the work. Not exclusively a dashboard, a report artefact or
a summary elsewhere.

**Why**: a [Message](#message) that teaches nobody, because nobody sees it, is the same as no [Message](#message).

### 8.3 The identifier MUST resolve without a human

By a command the [Practitioner](#practitioner) can run, a file they can read, or a URL they can fetch.

**Why**: clause 3.6 requires the [Identifier](#identifier) to resolve. This requires it to resolve *for the
reader*, which for an [Agent](#agent) means mechanically. An explanation that lives in a colleague's head
resolves for nobody at three in the morning either.

### 8.4 Documentation MUST state the correct construction, not only the prohibition

Explaining why the pattern is dangerous is not sufficient. The documentation has to show what to do
instead, specifically enough to act on.

**Why**: this is the difference between [Blocking](#blocking) an [Agent](#agent) and redirecting it. A prohibition alone
leaves it to guess at the replacement, and it will guess.

### 8.5 A project's defences MUST be enumerable

A [Practitioner](#practitioner) MUST be able to list what defends this codebase, and read each [Defence](#defence)'s
documentation, without triggering it first.

**Why**: an [Agent](#agent) arriving at a codebase has no colleague to ask and no memory of last time.
Without this, a project's standards can only be learned by violating them one at a time.

### 8.6 A project SHOULD publish a summary of its defences suitable for an agent's context

One terse line per [Defence](#defence), stating the [Rule](#rule) as a standing instruction rather than as a failure
report, each linked to its full documentation. *"Error hiding is forbidden"* is the shape.

**Why**: everything else in this method operates after the mistake. This operates before it. A
summary small enough to sit in an [Agent](#agent)'s working context turns the accumulated [Defences](#defence) from a
series of ambushes into a description of how this project expects code to be written, and it costs
one table.

### 8.7 Recorded project decisions MUST be discoverable by the same means

The judgements section 3 delegates to project level, once agreed and written down, MUST be
reachable exactly as the [Defences](#defence) are.

**Why**: section 3 says a project's accumulated decisions become part of its [Coverage](#coverage). [Coverage](#coverage)
nobody can find is not [Coverage](#coverage), and every [Practitioner](#practitioner) who arrives after a decision will otherwise
re-open it.

## 9. Citation

> Edmonds, Joseph. *Defence Before Fix*, version 1.0.1. First published 22 February 2026.
> <https://ltscommerce.dev>

## Appendix A: Instructing an agent

Where an [Agent](#agent) is expected to follow this method, give it the clauses rather than the article.
This appendix restates sections 3 and 4; where the two differ, the sections govern.

> When you find a [Defect](#defect) of any kind, do not fix it yet.
>
> First work out what [Class](#class) it belongs to: the pattern, style, idiom or configuration that allowed
> it. Do not decide in advance whether that is possible, attempt it. If you cannot write a [Rule](#rule)
> for it, say so and fix the [Defect](#defect) conventionally.
>
> Write a custom [Rule](#rule) that detects the [Class](#class), in a tool that reads code rather than running it.
> Draw it so that it catches more than the single [Instance](#instance) you started from, but never so broadly
> that it matches code which does not carry the [Hazard](#hazard).
>
> Do not trust the [Rule](#rule) as your only way of finding [Instances](#instance). Search independently as well, by
> text search and by reading the code, and check the [Rule](#rule) catches what you found by hand. Make that
> search a thorough one rather than a gesture, because everything downstream rests on it. If your
> own search turns up [Instances](#instance) the [Rule](#rule) missed, widen the [Rule](#rule) until it catches them; the search
> wins, not the [Rule](#rule). If it turns up nothing new, then one [Instance](#instance) is a supported conclusion rather
> than a guess.
>
> The [Hazard](#hazard) is whatever harm the [Class](#class) does, and it need not be a failure. Error hiding counts.
> So does something merely sloppy that makes the code harder to reason about safely.
>
> Prove the [Rule](#rule) fires before you trust it. It must catch the originating [Defect](#defect). If the pattern
> is not present in the codebase, because it was already fixed or because you are defending
> against it pre-emptively, prove the [Rule](#rule) against [Fixture](#fixture) code that demonstrates the pattern and
> keep that [Fixture](#fixture) as the [Rule](#rule)'s test.
>
> Then run the [Rule](#rule) everywhere the pattern can occur, which usually means one language but never
> just the component the bug was reported in, and report the [Instance](#instance) count. Catching far more
> [Instances](#instance) than you expected is success, not evidence the [Rule](#rule) is too broad. Only ever narrow a
> [Rule](#rule) to exclude code that does not carry the [Hazard](#hazard); never to make the number smaller.
>
> Fix every [Instance](#instance). Examine each one; where the same answer is genuinely right for all of them,
> applying it to all of them is correct. Never satisfy the [Rule](#rule) whilst leaving the [Hazard](#hazard) in place,
> and never suppress the [Rule](#rule) at the call site.
>
> You do not have the authority to [Baseline](#baseline), to suppress an [Instance](#instance), or to leave a known [Instance](#instance)
> unfixed, however large the count turns out to be. Those belong to whoever owns the codebase, and
> the standing answer is no unless a human has already agreed and documented an [Exception](#exception) for this
> project. If you hit one, finish everything else, then report the count and what fixing it would
> take, and leave the [Rule](#rule) unmerged rather than merging it weakened.
>
> If you are unsure whether code you want to exclude carries the [Hazard](#hazard), you are suppressing it, so
> refer it upwards rather than deciding. Narrow only where you are confident.
>
> Otherwise, just do the work. Fixing [Instances](#instance) is cheap for you, and reaching for an [Exception](#exception) is
> almost always a shortcut rather than a real obstacle.
>
> Make the [Rule](#rule) a permanent part of the project's quality checks, failing rather than [Warning](#warning). Write
> its failure [Message](#message) terse, carrying a stable [Identifier](#identifier) that resolves to documentation shipped
> with the project saying what the [Rule](#rule) is about, why it exists and how to fix a violation
> correctly. Check you can run the [Rule](#rule) yourself and read its output, because if you cannot, nor can
> the next [Agent](#agent).
>
> Only then fix the original [Defect](#defect) in the normal way, with a test that reproduces it.

## Changelog

| Version | Date       | Change                                                                                                                                                                                                                                                                      |
| ------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0.0   | 2026-09-08 | Initial specification, formalising the method published on 22 February 2026. Revised before publication after three independent cold readers understood the method correctly and still could not execute its judgement calls.                                               |
| 1.0.0   | 2026-09-08 | Editorial, no version change: two terminology entries and two section 7 paragraphs name the [detector specification](DETECTOR-SPEC.md) 1.0.0 alongside the [toolchain specification](TOOLING-SPEC.md) 0.2.0. No clause changed.                                             |
| 1.0.1   | 2026-09-08 | Clarity, no obligation changed: clause 3.1 closes with the four things it leaves on the record, and clause 3.3 opens its [Narrowing](#narrowing) passage with the two-halves test the passage then checks. Both were named by two or more readers of the acceptance cohort. |
