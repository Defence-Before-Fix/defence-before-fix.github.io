# Publishing

Two docs-only packages, one per registry, so that a toolchain can depend on the specification it
conforms to and a lock file records the version. Both are published by Joseph; nothing here runs
without his credentials.

## Versions

The npm package version tracks the method specification (`SPEC.md`). The toolchain specification
carries its own version inside the document and in `CHANGELOG.md`; it is not a separate package.
A change to either document is a new package release with the changelog updated first.

## Packagist

1. Sign in at packagist.org as the LongTermSupport account and submit
   `https://github.com/LongTermSupport/defence-before-fix`.
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
