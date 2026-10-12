# Answer key for SPEC.md

Marked against the document at the commit the readers read, with this key, its question set and
fixture at that same commit. Quotations below are from the document; when a clause is reworded,
update the quotation here in the same commit. `ACCEPTANCE.md` says how each item is marked;
`acceptance/README.md` says what each part of this key is for.

## 1. Restatement

A bullet is correct when it names one of these obligations. Four or more correct bullets, and no
bullet asserting one the list of wrong assertions below marks wrong, is a correct restatement.

- Attribute the defect to a class, bounded on both sides, with the hazard stated ([3.1](../../SPEC.md#31-attribute-the-defect-to-a-class)).
- Express the class as a rule in a detector that reads code, never a test ([3.2](../../SPEC.md#32-build-the-net)).
- Prove the rule fires, against the instance or a fixture, in a commit of its own ([3.3](../../SPEC.md#33-prove-the-net-by-making-the-rule-fire)).
- Sweep the whole codebase, record the count, then fix every instance ([3.4](../../SPEC.md#34-sweep-the-codebase-then-fix-every-instance)).
- Make the rule permanent and blocking in the project's checks ([3.5](../../SPEC.md#35-enforce-permanently-and-block)).
- Make the failure message terse, with a stable identifier resolving to documentation versioned
  with the rule ([3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation)).
- Record a defect whose fix is deferred where the project's other decisions are enumerable, rather
  than only mentioning it (section [2](../../SPEC.md#2-when-the-method-applies)).
- Take a baseline, a suppression or an instance left unfixed to the owner, never on the
  practitioner's own authority (section [4](../../SPEC.md#4-authority-which-decisions-belong-to-whom)).

Wrong if it asserts: the practitioner fixes the reported instance first and defends afterwards;
a test may serve as the detector; an agent may baseline the remaining instances.

Wrong readings the text invites, which count against the document on one reader: none named.

## 2. Load-bearing statements

- **2a.** Required: (1) the four steps before the fix: attribute the defect to a class, express
  the class as a rule in a detector, prove the rule fires, and sweep the codebase; (2) in that
  order, with the fix after the sweep. Wrong if it has the fix before the rule, or the sweep
  before the proof, or a test as the detector. Key quotations, section [3](../../SPEC.md#3-the-method): "Six clauses, in
  order."; [3.4](../../SPEC.md#34-sweep-the-codebase-then-fix-every-instance): "The Practitioner MUST run the Rule across the entire codebase and record the
  total Instance count before fixing anything, and MUST then fix every Instance found rather
  than only the one". An answer that names the steps by their clause numbers in order states
  both elements.
- **2b.** Required: (1) the owner of the codebase, the human who holds that authority; (2) no,
  an agent may not do so on its own authority. Wrong if it lets the practitioner or an agent
  decide because the count was small, because the project recorded no owner, or at all. Key
  quotation, section [4](../../SPEC.md#4-authority-which-decisions-belong-to-whom): "An Agent MUST NOT Baseline, suppress or knowingly leave an Instance
  unfixed on its own authority, whatever the Instance count turns out to be." "The owner" names
  the defined term and states that the decision is a human's; an answer need not add "a human"
  to be correct. The default-owner sentences of the terminology entry for Owner still require a
  recorded decision, so an answer naming whoever instructed the practitioner, for a project that
  has recorded nobody, names the owner and is correct.
- **2c.** Required: (1) all six clauses of section [3](../../SPEC.md#3-the-method) were followed for that defect; (2) the verdict
  rests on reproduction, the reviewer rerunning the defence, not on the report. Wrong if it
  accepts the pull request description or the practitioner's report as the verdict, or says
  that most clauses suffice. Key quotations, section [7](../../SPEC.md#7-conformance): "A remediation Conforms if all six clauses
  of section [3](../../SPEC.md#3-the-method) were followed for that Defect, and the verdict that they were rests on
  reproduction"; "A verdict on a remediation or a Defence MUST rest on reproduction, not on the
  report". "Reproduction" or "reproducing the runs" states element (2); the red and green runs
  need not be named.

## 3. Application: the ledger remediation

| Clause                                                                                    | Accepted grades    | Condition on the reasoning                                                                | What the fixture supports                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [3.1](../../SPEC.md#31-attribute-the-defect-to-a-class)                                   | Yes, Partial or No | None                                                                                      | Class, hazard and the next wider rule are named; Partial or No is the reading that no independent search technique is recorded, which step 2 and the record [3.1](../../SPEC.md#31-attribute-the-defect-to-a-class) requires both call for  |
| [3.2](../../SPEC.md#32-build-the-net)                                                     | Yes                | None                                                                                      | A rule in the project's static analyser, reading code, not a test                                                                                                                                                                           |
| [3.3](../../SPEC.md#33-prove-the-net-by-making-the-rule-fire)                             | Yes, Partial or No | For Partial or No: attributes the inline ignore to this clause, a fair reading of Part B  | Commit B is red on the fixture and the originating instance and survives as its own commit                                                                                                                                                  |
| [3.4](../../SPEC.md#34-sweep-the-codebase-then-fix-every-instance)                        | No or Partial      | Mentions the instance left unfixed, the inline ignore, or `Report::render()`              | Five findings were recorded, but one instance was left unfixed behind an inline ignore on the agent's own authority                                                                                                                         |
| [3.5](../../SPEC.md#35-enforce-permanently-and-block)                                     | Partial or No      | Mentions the suppression, the inline ignore, or that no recorded decision covers it       | The rule is permanent and blocking, but the suppression was not a recorded decision. [3.5](../../SPEC.md#35-enforce-permanently-and-block): "neither does a Rule whose green run depends on a Suppression that no recorded decision covers" |
| [3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation) | No or Partial      | Mentions the wiki, or that the documentation is not versioned or co-located with the rule | The message is terse and carries an identifier, but the documentation lives on a wiki, not versioned with the rule                                                                                                                          |

The three answers the question then asks for, each with the condition its reason must meet:

- **The remediation under section [7](../../SPEC.md#7-conformance).** Accepted answer: does not conform. Condition: the reason
  names [3.4](../../SPEC.md#34-sweep-the-codebase-then-fix-every-instance) or [3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation) among the clauses not followed; other clauses named alongside are not marked.
- **The defence alone.** Accepted answer: does not conform. Condition: the reason names [3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation), or
  [3.5](../../SPEC.md#35-enforce-permanently-and-block)'s unrecorded suppression, which section [7](../../SPEC.md#7-conformance)'s definition of a conforming defence also
  requires to be absent; other clauses named alongside are not marked.
- **The decision section [4](../../SPEC.md#4-authority-which-decisions-belong-to-whom) says was not the practitioner's.** Accepted answer: the inline ignore on
  `Report::render()`, which was the owner's decision. Condition: none; any other decision named
  alongside it is not marked. An answer naming only the decision to leave the wider rule unbuilt,
  or naming none, is wrong.

Wrong readings the text invites, which count against the document on one reader:

- [3.5](../../SPEC.md#35-enforce-permanently-and-block) graded Yes with reasoning that says the rule blocks, or is permanent, and does not mention
  the suppression.
- [3.6](../../SPEC.md#36-make-the-failure-message-terse-and-point-it-at-real-documentation) graded Yes with reasoning that says the identifier resolves, or the URL works, and does not
  mention versioning or co-location.
- The defence graded as conforming with reasoning that says only the sweep failed and that
  quotes section [7](../../SPEC.md#7-conformance)'s definition of a conforming defence.

A reader who grades [3.4](../../SPEC.md#34-sweep-the-codebase-then-fix-every-instance) Yes has misread the fixture, which is the reader's miss, whether or not
the inline ignore was attributed to [3.3](../../SPEC.md#33-prove-the-net-by-making-the-rule-fire) instead.

## 4. Confusion

No keyed answer. Record every passage named, as `ACCEPTANCE.md` defines naming and the same
passage. A passage named by two or more readers of the run is a finding: it blocks the change
where it lies in text the change wrote or altered, and is routed to `acceptance/ROUTED.md`
otherwise. What to change is the editor's decision; the reader is not asked and any suggestion
it volunteers is discarded unread.
