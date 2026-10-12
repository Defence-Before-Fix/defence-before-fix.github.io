# Run 35: SPEC.md, defined terms, second run

- **Document**: SPEC.md
- **Pull request**: not yet opened; branch `editor/defined-terms` at b1e7145, the commit the
  readers were given. The change is be546ea and 35f42bf (Remediation defined, Harness renamed
  Rule harness); the revision after [run 31](031-defined-terms-method-run-1.md) is df016ab
  (section 2's steps in order, clause 3.1's bounds and lower bound, a clause 3.3 Part B paragraph
  on an ignore placed on one instance)
- **Cohort**: five readers, none reused from run 31, model alias `haiku`; every reader reported
  `claude-haiku-5-5` in its JSON output
- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked that the prompt is byte for byte the question set, the document and the
  fixture at b1e7145, in that order, each preceded by one `===== FILE: <name> =====` line, and
  that each sheet is the `result` of its reader's JSON output (one turn, `is_error` false)
- **Run within the pull request**: 2
- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/method/KEY.md` at
  b1e7145, with the judgements of run 31
- **Verdict**: FAIL on a miss traceable to the text under 3.3, in the clause 3.3 Part B text the
  revision added to, and on one passage found confusing by two readers, in untouched base text

## Marks

| Reader | Q1 restatement | 2a  | 2b  | 2c  | 3.1     | 3.2 | 3.3             | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 | Q4 passages |
| ------ | -------------- | --- | --- | --- | ------- | --- | --------------- | --- | --- | --- | ----------- | ------- | --------- | ----------- |
| 1      | correct        | ok  | ok  | ok  | Partial | Yes | Yes             | No  | No  | No  | ok          | ok      | ok        | three       |
| 2      | correct        | ok  | ok  | ok  | Partial | Yes | Yes             | No  | No  | No  | ok          | ok      | ok        | three       |
| 3      | correct        | ok  | ok  | ok  | No      | Yes | Yes             | No  | No  | No  | ok          | ok      | ok        | two         |
| 4      | correct        | ok  | ok  | ok  | Partial | Yes | Yes             | No  | No  | No  | ok          | ok      | ok        | one         |
| 5      | correct        | ok  | ok  | ok  | Partial | Yes | Partial, miss T | No  | No  | No  | ok          | ok      | ok        | three       |

`T` marks a miss whose reasoning quotes or states what the document requires. Every grade under
3.1, 3.2 and 3.4 to 3.6 is one the key accepts, and every 3.1 grade of Partial or No notes that no
independent search technique is recorded.

### Question 1

Five of five correct, each with at least four bullets the key lists and none it marks wrong.

### Question 2

- **2a**, five of five. Readers 1 to 4 quote section 2's new sentence, "In order, the steps are
  section 3's: ...", and state the four steps in order. Reader 5 states the four steps in order
  and quotes section 2's MUST sentence. Run 31 had three of five.
- **2b**, five of five, each naming the owner and quoting section 4's sentence on what an agent
  MUST NOT do.
- **2c**, five of five, each quoting section 7's conforming-remediation sentence with
  reproduction.

### Question 3

- **3.3**, four of five. Reader 5 grades Partial because "the inline ignore in commit C is an
  exclusion with no written sentence, so it is a suppression under Part B, not a narrowing", and
  also fails 3.4 on it. The key's excuse covers attributing the suppression to 3.3 rather than
  3.4, not to both (run 31's judgement J3, kept). The reasoning states what Part B requires, so
  the miss is traceable and a finding whatever the count. It traces to clause 3.3 Part B, where
  the revision added the paragraph saying an ignore placed on one instance is not an exclusion
  but a call-site Suppression governed by 3.4 and section 4. This reader did not apply that
  paragraph. The other four grade 3.3 Yes, and readers 3 and 5 cite clause 3.4's "suppressing the
  [Rule] at the call site, which is not a fix at all" for 3.4.
- **Remediation**: five of five say it does not conform. **Defence**: five of five say it does
  not conform, each naming 3.6. **Section 4**: five of five name the inline ignore.

### Judgements made in marking

Run 31's judgements J1 to J4 are applied unchanged. None affects a mark here except J3, above.
Under J4 (the same passage is the same sentence), the Owner entry is three single-reader notes.
Read by paragraph, it would be one passage named by three readers and would also block. The
verdict is FAIL either way.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                               | Clause           | Readers   | Text                      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------- | ------------------------- |
| "This does not reopen a [Class] whose bounds a [Hazard] sentence has settled, and it reaches no further than the one wider [Rule] already on the record."                                                             | 4                | two: 1, 5 | Untouched base            |
| "the default exists so work is not blocked, not to certify that a second judgement was applied", set against "SHOULD be revisited by someone not under that deadline"                                                 | 1, Owner         | one: 1    | Untouched base            |
| "a decision they take under section 4 to keep an [Instance] unfixed, [Suppress], [Baseline] or remove a [Rule] MUST be recorded in the project record with its justification"                                         | 1, Owner         | one: 3    | Untouched base            |
| "that record MUST mark the decision as taken by a default [Owner] and state why nobody better placed was reachable, where the next reader can see who decided and why"                                                | 1, Owner         | one: 5    | Untouched base            |
| "...the scale at which that becomes true is tremendous."                                                                                                                                                              | 3.4              | one: 1    | Untouched base            |
| "The two bounds settle how wide the [Class] is drawn, not at which level of abstraction.", with the next paragraph's "usually sits one level below that behaviour"                                                    | 3.1              | one: 2    | Rewritten by the revision |
| "The attempt that separates the first from the second is complete when ..."                                                                                                                                           | 2                | one: 2    | Untouched base            |
| "The absence of an [Instance] is the [Practitioner]'s reason not to widen unasked; it is not authority to exclude the extension."                                                                                     | 4                | one: 2    | Untouched base            |
| "the [detector specification](DETECTOR-SPEC.md)'s clause 8.1 for a [Detector]", beside this document's own clause 8.1                                                                                                 | 3.2              | one: 3    | Untouched base            |
| "Where the only thing pending is whether one matched case carries the [Hazard], the [Rule] MAY merge at full width ...", set against "provided the [Rule] does not become [Blocking] until every [Instance] is fixed" | 4                | one: 4    | Untouched base            |
| "Keeping the narrower [Rule] excludes what that wider [Rule] would add, so the rejection is tested as a [Narrowing] is under clause 3.3."                                                                             | 3.1, lower bound | one: 5    | Rewritten by the revision |

Of run 31's blocking passages, no reader quotes the old wording, which no longer exists. One reader
each quotes the rewritten level sentence and the rewritten lower-bound sentence. The section 4
"This does not reopen" sentence was named by one reader in run 31 and two in this run. No reader
quotes the new section 2 sentence (four quote it as their 2a answer), the new Part B paragraph,
the Remediation entry or any sentence the original change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met. 2a, 2b and 2c five of five.
- Restatement and application, at least four of five on each keyed item: met. 3.3 four of five,
  every other item five of five.
- A wrong answer traceable to the text, none: not met. Reader 5's 3.3, which traces to clause 3.3
  Part B, the passage the revision added to.
- A passage found confusing by two or more, none outstanding: not met. Section 4's "This does not
  reopen" sentence, two readers, untouched base text.
- From one reader only, recorded: the ten other passages above.

**FAIL.** Neither failure is in text the change made. The 3.3 miss traces to a passage the
revision rewrote, and the blocking passage is untouched base text.
