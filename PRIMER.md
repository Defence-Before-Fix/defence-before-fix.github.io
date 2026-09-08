# Build the net before you land the catch

*An introduction to Defence Before Fix (DBF). The precise version is in
[the specification](SPEC.md); this page is the idea it formalises.*

---

A bug report comes in, you go looking, and within twenty minutes you have found it. It is a
single line, the fix is obvious, and everything in the situation is telling you to change that
line and move on to the next thing.

Hold on a moment, because you are holding something quite valuable and it is about to expire.

What you have in front of you is a confirmed, real, in-production example of a pattern that
actually hurt you. Not a pattern you read about in a style guide, not one you suspect might be a
problem some day, but one that has already cost a customer something and cost you an afternoon.
That is very hard evidence to come by, and it is exactly what you need in order to write a good
detection rule, because the hardest part of writing a rule is usually being sure that the thing
it detects is genuinely worth detecting.

The moment you fix that line, the evidence is gone and the opportunity closes with it.

## So build the net first

Before you touch the bug, ask a different question about it. Not "how do I fix this" but "what
kind of thing is this an instance of". A missing null check is not really a missing null check;
it is an instance of coalescing an absent value into a falsy one, which is a pattern, and
patterns can be detected mechanically.

Then write the rule that detects that pattern. A static analysis rule, a custom lint rule, a
check in whatever tool your project already runs on every commit. Something that reads the code
rather than running it, so it can be pointed at every file you have rather than only the paths
your tests happen to exercise.

That rule is the net.

## The net has to go red

This is the part I would most encourage you not to skip, and it is the part that looks like a
formality.

Run the rule. It must fail, and at minimum it must catch the bug that sent you looking in the
first place. If your brand new rule comes back green, then whatever you have built does not
detect the thing you built it to detect, and the honest reading is that the rule is broken
rather than that the codebase is clean.

It is never the goal to write the rule and be instantly green. Green feels like success and in
this one specific moment it is the opposite. The red run is what proves the net has a hole
shaped like the bug you were chasing.

## Then you find out how many there are

Here is where it stops being a tidy-up exercise and starts being worth the effort.

Run the net across the whole codebase and count. In the worked example in
[the original article](https://ltscommerce.dev/articles/defence-before-fix-static-analysis) the
reported bug turned out to be one of twenty-three, and the other twenty-two were not theoretical.
They were the same bug, sitting in twenty-two other places, waiting to surface in different
contexts, for different customers, at different times, each one arriving as its own separate
support ticket months apart with nothing to connect them.

You fix all of them. Not mechanically, because a rewrite that satisfies the rule whilst keeping
the hazard is not a fix, and suppressing the rule at the call site is not a fix at all. Each one
gets a real decision about what the correct behaviour actually is.

Sometimes the count comes back enormous and you genuinely cannot fix them all today. Most tools
let you baseline what already exists so the rule at least blocks anything new. That is a
judgement call for your project and I would not pretend otherwise, but I would say plainly that
it is a much weaker outcome than finding and fixing, and that a baseline nobody ever shrinks is
just a list of defects you have agreed to keep.

## The net stays, and it has to teach

The rule goes into the gate that blocks the build, for every contributor, permanently. A warning
that does not block is a suggestion, and suggestions do not survive contact with a deadline.

And the message it prints matters more than people expect. Keep the message itself short,
because it is read by somebody who is mid-task and wants to get on, but give it a stable
identifier that leads to real documentation: what this rule is about, why it exists, and how to
do the thing correctly. "Pattern X detected" teaches nobody anything. A rule that explains the
better approach is the closest thing most codebases have to institutional memory that cannot be
forgotten when somebody leaves.

## This does not replace your tests

Worth saying clearly, because the name invites the misunderstanding.

You still reproduce the original bug with a test and you still prove it fixed. That is ordinary
TDD and it is doing an ordinary and necessary job, which is to pin down one specific behaviour
so it stays pinned. Defence Before Fix operates a level above that, on the class rather than the
instance, and the two are complementary rather than alternatives.

The ordering in the name is the whole point. The defence comes before the fix, because after the
fix there is nothing left to build it from.

## Why this has become more important, not less

For a human developer a good failure message is a nice courtesy, and whether it changes anything
depends on how tired they are and how many times they have seen it.

For a coding agent the failure message is the entire correction loop. It gets read, in full,
every single time, with no fatigue and no seniority gradient, and a message that explains the
correct approach does not merely stop the agent, it turns it around and points it the right way.
Hopefully that makes the case on its own: if you intend to have agents writing code in your
codebase, then the rules in your quality gate, and the messages attached to them, are the main
channel you have for teaching them your project's standards at all.

---

**Read [the specification](SPEC.md)** for the normative version: six numbered clauses, what
conformance means for a rule and for a toolchain, and how the method relates to TDD and to the
wider quality pipeline.

If you maintain a linter, a static analyser or a QA pipeline that other people install, the
[toolchain specification](TOOLING-SPEC.md) is the one addressed to you. It states what a tool has
to offer so that the projects using it can follow the method at all, which turns out to be a
different list from the one the method itself gives.

*Defence Before Fix was coined by [Joseph Edmonds](https://ltscommerce.dev) of
[Edmonds Commerce](https://edmondscommerce.co.uk) and first published on
22 February 2026. US spelling: Defense Before Fix. If you want the detail of what is and is not
being claimed, it is in [provenance](PROVENANCE.md).*
