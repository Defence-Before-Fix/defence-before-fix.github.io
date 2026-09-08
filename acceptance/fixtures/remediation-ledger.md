# Fixture: the ledger remediation

A fictional remediation, described as the pull request and its commits would show it. Grade it
against the document you were given. Where the description does not say, answer from what is
written.

## What the pull request shows

A defect: `Ledger::total()` silently returned zero when a currency conversion failed, because the
conversion call's error was caught and the empty result treated as a valid amount.

The practitioner, a coding agent, did the following, in this order, over five commits.

1. **Commit A.** Wrote a note in the pull request naming the class as "a fallible call whose
   error is caught and whose result is then used as if the call had succeeded", stating that
   the hazard is silent wrong output rather than a crash, and naming the next wider class it
   did not build, "any caught error that is not rethrown or reported", as not attempted because
   the codebase has hundreds of such catches and most are legitimate.
2. **Commit B.** Wrote a rule in the project's static analyser, identifier `proj.caught-then-used`,
   that flags a caught error followed by a use of the call's result in the same function. Added
   the rule to the project's analyser configuration. The commit also contains a fixture file
   reproducing the `Ledger::total()` shape, and the CI run for this commit is red on that rule
   with five findings: the fixture, `Ledger::total()`, and three other functions.
3. **Commit C.** Fixed `Ledger::total()` and two of the three others, so that the failure is
   propagated. For the third, `Report::render()`, the agent added an inline `// ignore proj.caught-then-used` comment with the note "rendering must never throw", and did not raise
   it with anyone. The CI run is green.
4. **Commit D.** Wrote the rule's documentation as a page on the company wiki, at a URL the rule's
   failure message prints in full. The page states what the rule forbids and why, and shows the
   propagating construction to write instead. The failure message is one line: the identifier,
   the file and line, and the wiki URL.
5. **Commit E.** Confirmed in the pull request description that the rule is set to fail the
   build, not warn, and that the whole quality invocation was run locally and passed.

The pull request was merged with a merge commit; all five commits remain in the history.

The project's recorded decisions say nothing about inline ignores. The project has a named owner.
