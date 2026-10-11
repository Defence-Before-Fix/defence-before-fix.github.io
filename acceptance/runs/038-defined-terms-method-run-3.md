# Run 38: SPEC.md, defined terms, third run

- **Document**: SPEC.md

- **Pull request**: not yet opened; branch `editor/defined-terms` at 8517aa4, the commit the
  readers were given. The change is be546ea and 35f42bf (Remediation defined, Harness renamed
  Rule harness). Revision 1, after [run 31](031-defined-terms-method-run-1.md), is df016ab. The
  revision after [run 35](035-defined-terms-method-run-2.md) is 0fd02ef:

  - clause 3.3 Part B's paragraph on an ignore placed on one instance moves to the Part's
    opening, under the sentence "This Part is about the [Rule]'s own scope.";
  - in section 4's bullet on the next wider rule, two sentences replace "This does not reopen a
    [Class] ...".

  The question set and key are as at b1e7145.

- **Cohort**: five readers, none reused from runs 31 or 35, model alias `haiku`; every reader
  reported `claude-haiku-5-5` in its JSON output

- **Isolation**, as the editor supplied it: each reader a separate `claude -p` process started
  through the `ccy-claude` wrapper, in a fresh empty directory made by `mktemp -d` outside the
  repository, with the packet on standard input; no tools, no settings, no project context and no
  saved session. Command:
  `ccy-claude -p --model haiku --safe-mode --tools '' --setting-sources '' --strict-mcp-config --no-session-persistence --output-format json < prompt.txt`.
  The marker checked two things:

  - the prompt is byte for byte the question set, the document and the fixture at 8517aa4, in
    that order. Each is preceded by one `===== FILE: <name> =====` line, and one blank line
    separates each file from the next;
  - each sheet is the `result` of its reader's JSON output (one turn, `is_error` false).

- **Run within the pull request**: 3

- **Marked by**: a delegated marker that saw neither the drafting nor the review, against
  `ACCEPTANCE.md` as it stands at this branch's base, 9e914fe, and `acceptance/method/KEY.md` at
  8517aa4, with the judgements of run 31

- **Verdict**: FAIL on two passages found confusing by two readers each. One is untouched base
  text in section 2. The other is the clause 3.1 lower-bound sentence that revision 1 rewrote.
  Every keyed item is five of five, and no miss is traceable to the text.

## Marks

| Reader | Q1 restatement | 2a  | 2b  | 2c  | 3.1     | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | Remediation | Defence | Section 4 | Q4 passages |
| ------ | -------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | ----------- | ------- | --------- | ----------- |
| 1      | correct        | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | two         |
| 2      | correct        | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | one         |
| 3      | correct        | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | two         |
| 4      | correct        | ok  | ok  | ok  | Partial | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | three       |
| 5      | correct        | ok  | ok  | ok  | No      | Yes | Yes | No  | No  | No  | ok          | ok      | ok        | three       |

Every grade under question 3 is one the key accepts. Every 3.1 grade of Partial or No notes that
no independent search technique is recorded.

### Question 1

Five of five correct, each with at least four bullets the key lists and none it marks wrong.
Readers 4 and 5 add fixing the original defect with a reproduction test, which section 7 states.

### Question 2

- **2a**, five of five, each quoting section 2's "In order, the steps are section 3's: ..." and
  stating the four steps in order.
- **2b**, five of five, each naming the owner and quoting section 4's sentence on what an agent
  MUST NOT do. Readers 1 and 4 also quote "Always a human."
- **2c**, five of five, each quoting section 7's conforming-remediation sentence with
  reproduction.

### Question 3

- **3.3**, five of five Yes, against four of five in run 35. Reader 2 applies the moved Part B
  paragraph: "The inline ignore is a suppression at the call site, not a narrowing, so it does not
  touch this proof." No reader attributes the inline ignore to 3.3.
- **3.4**, **3.5** and **3.6**, five of five No. Each 3.4 names the inline ignore, and each 3.6
  names the wiki documentation, not versioned with the rule.
- **Remediation**: five of five say it does not conform. **Defence**: five of five say it does
  not conform, each naming 3.6 or the unversioned documentation. **Section 4**: five of five name
  the inline ignore on `Report::render()`, and readers 1 and 3 also name leaving the wider rule
  unbuilt, which the key accepts.

### Judgements made in marking

Run 31's judgements J1 to J4 are applied unchanged. None affects a mark here except J4 (the same
passage is the same sentence), below. Readers 3, 4 and 5 each quote a different sentence of
section 4's bullet on leaving the next wider rule unbuilt. Under J4 these are three single-reader
notes. Read by paragraph, they would be one passage named by three readers and would also block.
Two of the three sentences are the ones revision 2 added. The verdict is FAIL either way.

## Passages quoted as confusing

| Passage                                                                                                                                                                                                        | Clause           | Readers   | Text                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------- | --------------------------------------------------------------------------- |
| "naming at least two independent techniques tried at expressing the [Rule], in the vocabulary clause 3.1 uses for a search"                                                                                    | 2                | two: 1, 3 | Untouched base                                                              |
| "Keeping the narrower [Rule] excludes what that wider [Rule] would add, so the rejection is tested as a [Narrowing] is under clause 3.3."                                                                      | 3.1, lower bound | two: 4, 5 | Rewritten by revision 1                                                     |
| "Only that one wider [Rule], the one the record names, comes to the [Owner] this way, and only when it was rejected for want of an [Instance]."                                                                | 4                | one: 5    | Added by revision 2                                                         |
| "Where it was rejected because a [Hazard] sentence shows the [Hazard] cannot arise in what that [Rule] would add, the [Class]'s bounds are settled and remain the [Practitioner]'s decision under clause 3.1." | 4                | one: 4    | Added by revision 2                                                         |
| "The absence of an [Instance] is the [Practitioner]'s reason not to widen unasked; it is not authority to exclude the extension, and recording it as a known gap does not change whose decision it is."        | 4                | one: 3    | Untouched base, in the bullet revision 2 rewrote                            |
| "The two bounds settle how wide the [Class] is drawn, not at which level of abstraction.", with the next paragraph's "usually sits one level below that behaviour"                                             | 3.1              | one: 1    | Rewritten by revision 1                                                     |
| "Where the project has recorded nobody, the [Owner] is whoever instructed the [Practitioner], and [Escalation] goes there."                                                                                    | 1, Owner         | one: 2    | Untouched base                                                              |
| "The attempt that separates the first from the second is complete when ..."                                                                                                                                    | 2                | one: 5    | Untouched base                                                              |
| "naming the [Rule] and the [Identifier], with no [Rule] build of their own to attach it to."                                                                                                                   | 3.6              | one: 4    | Untouched base; the next sentence was changed by the change ([Remediation]) |

Notes on the two blocking passages:

- **Section 2, "techniques tried at expressing the [Rule]".** Reader 1 reads the techniques as
  both expressing the rule and searching for instances. Reader 3 sets the sentence against clause
  3.1, which it says excludes the rule itself as a technique. It was named by one reader in run 31
  and by none in run 35.
- **Clause 3.1, the lower-bound rejection "tested as a [Narrowing] is".** Reader 4 could not work
  out what it required of the record, and reader 5 did not follow what testing a rejection "as a
  [Narrowing] is" means. Reader 5 of run 35 quoted the same sentence.

Run 35's two failures are clear in this run. No reader quotes section 4's "This does not reopen"
sentence, which revision 2 removed. 3.3 is five of five, and no reader quotes the moved Part B
paragraph. No reader quotes the Remediation entry or any other sentence the original change made.

## Findings applied

None at the time of marking; what to change is the editor's decision.

## Against the criteria

- Load-bearing statements, five of five on every one: met.
- Restatement and application, at least four of five on each keyed item: met, five of five
  throughout.
- A wrong answer traceable to the text, none: met.
- A passage found confusing by two or more, none outstanding: not met. Section 2's "techniques
  tried at expressing the [Rule]" sentence (two readers), untouched base text. Clause 3.1's
  lower-bound "tested as a [Narrowing] is" sentence (two readers), rewritten by revision 1.
- From one reader only, recorded: the seven other passages above.

**FAIL**, on question 4 alone. One blocking passage is untouched base text (section 2). The other
is a sentence revision 1 rewrote (3.1). Neither is in text the change made.
