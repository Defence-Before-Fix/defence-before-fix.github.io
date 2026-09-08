# Publishing

## The custom domain

The site is served by GitHub Pages at <https://longtermsupport.github.io/defence-before-fix/>,
which is the canonical URL the toolchains print. Moving it to `defencebeforefix.ltscommerce.dev`
is Joseph's, because it needs DNS:

1. Add a `CNAME` record for `defencebeforefix` pointing at `longtermsupport.github.io`.
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
