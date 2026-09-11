# Publishing

## The custom domain

The site is served by GitHub Pages at <https://defence-before-fix.github.io/>, the organisation
site of `Defence-Before-Fix`, which is the canonical URL the toolchains print. Moving it to
`defencebeforefix.ltscommerce.dev` is Joseph's, because it needs DNS:

1. Add a `CNAME` record for `defencebeforefix` pointing at `defence-before-fix.github.io`.
2. Commit a file named `CNAME` at the repository root containing `defencebeforefix.ltscommerce.dev`,
   or set the custom domain under Settings, Pages, which commits the same file.
3. Once the certificate is issued, tick "Enforce HTTPS" on the same settings page.
4. Update the URL in `_config.yml` if one is set, then in the toolchains' failure output and
   conformance documents, in `head-custom.html` and in the README, since the old address will
   redirect but the printed line should name the canonical one.

## The packages

Two docs-only packages, one per registry, so that a toolchain can depend on the specification it
conforms to and a lock file records the version. Both are published by Joseph; nothing here runs
without his credentials.

## Branches and releases

`next` is the editor's draft and takes every pull request, each already accepted by the cohort as
`ACCEPTANCE.md` and `CONTRIBUTING.md` describe. `main` is what the site serves and what the
registries see, and only a release branch is merged into it. Versions are set at release, not per
change: whilst `next` carries unreleased changes to a document, that document's header reads
`<next version>-dev, unpublished` and `CHANGELOG.md` has an `Unreleased` entry for it.
`tools/versions.py` holds every version line to that.

A release, in order:

1. Cut `release/<version>` from `next`. No specification text changes on it; if one is needed, it
   goes through `next` as a pull request with its own cohort.
2. Set the version and date in each changed document's header, status paragraph, citation and
   closing table, and in `package.json` for the method specification. The `Unreleased` heading
   becomes `### <version>, <date>` and its lines stay as the version's cohort record. A version
   is patch for clarity only, minor for a new or changed obligation, major for a change that
   makes a conforming remediation non-conforming.
3. Run `python3 spec-qa.py` and the unit tests; both must be clean.
4. Open a pull request from the release branch to `main`, since direct pushes are refused; CI
   sees the run files that arrived on `next` and passes. Merge it by merge commit, tag
   `v<version>` on `main`, and delete the release branch.
5. Merge `main` back into `next` and push it directly, so the version lines and changelog land
   there. This is the one push to `next` that does not go through a pull request; branch
   protection exempts administrators for it, and a pull request would fail the run-record check
   since the merge adds no run of its own.
6. Publish the packages as below.

## Versions in the packages

The npm package version tracks the method specification (`SPEC.md`). The toolchain specification
carries its own version inside the document and in `CHANGELOG.md`; it is not a separate package.
A change to either document is a new package release with the changelog updated first.

## Packagist

1. Sign in at packagist.org as the LongTermSupport account and submit
   `https://github.com/Defence-Before-Fix/defence-before-fix.github.io`.
2. Enable the GitHub hook so tags publish automatically.
3. Tag: `git tag -a v1.0.0 -m 'Method specification 1.0.0' && git push origin v1.0.0`.

## npm

1. `npm login` as a member of the `@longtermsupport` organisation.
2. From a clean checkout of the tag: `npm publish`.

## After publication

Add the dependency to both toolchains, `require-dev` in php-qa-ci's `composer.json` and
`devDependencies` in ts-qa-ci's `package.json`, pinned to the version each conforms to, and
record that version where each toolchain states its conformance. Not before: an unpublished
dependency breaks every consumer's install.
