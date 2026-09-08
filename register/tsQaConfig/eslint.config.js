// Project-specific ESLint additions. This file is merged AFTER ts-qa-ci's
// Tier A core config, never replaces it - any attempt to override a Tier A
// rule's severity here is rejected unless a matching entry exists in
// tier-a-exemptions.json (see resolveEslintConfig.ts). This is the SINGLE home
// for ALL project lint opinion (local plugins, strict-TS preset, per-dir
// overrides) - it is composed for BOTH `npx eslint` and `npx ts-qa`.
export default [];
