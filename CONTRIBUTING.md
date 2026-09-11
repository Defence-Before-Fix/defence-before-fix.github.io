# Contributing

Pull requests are welcome, and the process here is heavier than most because the documents are
normative: an agent meeting the method in a failing pipeline will act on the words as written.
Every step below exists to keep that reader able to follow the text. Read SCOPE.md before
proposing an obligation; most proposals that fail do so there, and it is cheaper to find out
first.

## Branches

| Branch      | What it is                                                         | Who merges into it                           |
| ----------- | ------------------------------------------------------------------ | -------------------------------------------- |
| `next`      | The editor's draft. Every pull request targets it.                 | The editor, after the checks below           |
| `release/*` | A release candidate cut from `next`, prepared for publication      | Nobody; it is merged into `main` and deleted |
| `main`      | The published site and the tagged releases. Deploys on every push. | Only a release branch, by merge commit       |

Direct pushes to `main` and `next` are refused by branch protection, with one exception: the
editor's back-merge of `main` into `next` at release, described in PUBLISHING.md. Merges are merge commits,
never squashes or rebases, so that every commit keeps its ancestry and a branch can be deleted
cleanly afterwards.

## Two kinds of change

**A clarity edit** changes no obligation: a rewording, a correction, an example, an appendix
change, a table. It needs a changelog line under `Unreleased`, an acceptance run, and the editor's
review. It is a patch version when released.

**A new, removed or changed obligation** is any change to the set of sentences carrying a MUST,
SHOULD or MAY in a numbered section or appendix. It needs everything a clarity edit needs, plus
the five tests in SCOPE.md answered in the pull request, and it is at least a minor version when
released. `tools/changes.py` tells the two apart mechanically and CI runs it on every pull
request.

## What a pull request contains

- The change to the document, and nothing about versions: no version line, no changelog entry
  beyond the `Unreleased` line, no key update. The editor does those.
- For an obligation, the five SCOPE.md tests, each answered in a sentence or two. The pull
  request template lays them out.
- The observed case that prompted it, for either kind. A clarity edit still has a reason: a
  reader who took the passage the wrong way.
- `python3 spec-qa.py` clean and the unit tests passing, which CI checks for you.

Wording is a proposal. The editor rewrites accepted changes to fit the document, and a rewrite is
the normal outcome, not a criticism. If the substance survives, the change is yours.

## What happens next, in order

1. **Mechanical checks in CI.** Terminology and link discipline, house style, version agreement,
   key quotations, and the change discipline in `tools/changes.py`. A red check blocks review.
2. **Scope.** For an obligation, the editor confirms each SCOPE.md test. A failed test closes the
   pull request with a row in `DECLINED.md`.
3. **Review and rewrite.** An independent review of the diff against the document, then the
   editor's rewrite, pushed to the pull request branch where the contributor allows it or to an
   editor's branch that supersedes it.
4. **Keys.** Where the change touches a sentence an acceptance key quotes, or adds a load-bearing
   obligation, the editor updates the key before the cohort runs, never after.
5. **The cohort.** The acceptance test in ACCEPTANCE.md runs on the final text. Its record is
   committed under `acceptance/runs/` and named from the `Unreleased` changelog line, and CI
   refuses a specification change that lacks one. A wording change after the run means a fresh
   run.
6. **Merge** into `next` by merge commit, and the branch is deleted.

Steps 2 to 5 are done by a person with a Claude Code session, not by CI, and they happen in
batches. A quiet pull request is not a declined one; a declined one says so.

## Versions and releases

Versions are bumped at release, not per change. Whilst `next` carries unreleased changes to a
document, that document's header reads `<next version>-dev, unpublished` and CHANGELOG.md has an
`Unreleased` entry for it. At release a `release/<version>` branch is cut from `next`, the
version and date are set, the `Unreleased` entry becomes the version's entry with its cohort
records, the branch is merged into `main` by merge commit and tagged, and `main` is merged back
into `next`. PUBLISHING.md has the steps.

## Licence

The documents are under Creative Commons Attribution 4.0 International, and a contribution is
made under the same licence.
