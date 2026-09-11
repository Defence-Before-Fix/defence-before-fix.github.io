# Scope: what the specifications cover, and the tests a new obligation must pass

The three specifications describe a defence: a rule that reads code, the proof that it fires,
the sweep and the fix, the permanence of the rule in the project's own checks, the message and
documentation it prints, and who decides what along the way. They do not describe how a project
runs its checks, ships, reviews, plans or manages its work, however sensible the advice would be.
SPEC.md says so in section [8](SPEC.md#8-operating-a-defence-under-ai-assisted-development), under "Scope: this specifies a defence, not a pipeline", and this
page exists so that the boundary is applied to every proposal the same way, before the wording is
argued over.

A specification grows by a paragraph at a time, and every paragraph is another thing the weakest
reader who will meet it can misread. The cohort in ACCEPTANCE.md is one brake on that. This page
is the other: an obligation that fails any test below is declined, whatever its merits as advice.

## The five tests

A proposed obligation, a MUST, SHOULD or MAY in any of the three documents, enters only when all
five hold. The proposer states each in the pull request; the editor confirms each before any
wording is discussed.

1. **Observed, not imagined.** The proposal names a case where the absence of this obligation
   let a practitioner or an agent route around the method, with enough detail that a reader can
   see it happened, or a contradiction or gap in the text itself that a reading shows. A
   hypothetical about what someone might do, however plausible, does not qualify. Section [4](SPEC.md#4-authority-which-decisions-belong-to-whom) of
   SPEC.md records obligations added after cold readings of an earlier draft, and new ones are
   added the same way.

2. **Not already covered.** A correct reading of an existing clause does not already forbid the
   behaviour or require the action. Where it does, the change is a clarity edit to the existing
   clause, a patch version, and never a new obligation. The proposer says which clauses were
   read and why they fall short.

3. **About the defence.** The obligation concerns the rule, its class, its proof, its sweep, its
   permanence, its message, its documentation, its record, or who decides. Anything about how a
   project runs its quality checks, what happens when they fail, how work is planned, reviewed,
   deployed or paid for, is outside the documents, per section [8](SPEC.md#8-operating-a-defence-under-ai-assisted-development) of SPEC.md, and stays outside
   however useful it would be.

4. **Verifiable from the record.** For a MUST or a SHOULD, an owner can tell from the project
   record alone, without asking the practitioner, whether the obligation was met. A MUST nobody
   can check is advice, and advice does not go in a normative document. The proposer says what
   an owner would look at. A MAY is not verified; it names the obligation it relaxes instead.

5. **Costed.** The proposal states, in a sentence each, what the obligation costs the
   practitioner to meet and what it leaves that an owner can read. An obligation with a cost and
   nothing an owner can read is declined; one an owner can read that costs the practitioner
   nothing is suspicious and gets a second look.

## Where an obligation goes

An accepted obligation names the section or clause it extends. Nothing is added as a free-standing
paragraph. If no existing section is its home, that is evidence for test 3 failing, not a reason
to open a new section.

## What the tests are not

They do not judge wording; the editor rewrites every accepted proposal, and the contributor's
phrasing is a starting point. They do not judge clarity; the cohort does that, after the editor's
rewrite. They do not apply to clarity edits, corrections, examples or the appendix, which change
no obligation and follow the lighter path in CONTRIBUTING.md.

## Declined proposals

A proposal declined under these tests is recorded in `DECLINED.md` with the test it failed and
one sentence of reasoning, so that the same idea, arriving again, meets the earlier answer rather
than a fresh debate. A declined proposal can be reopened only with new evidence against the test
it failed.
