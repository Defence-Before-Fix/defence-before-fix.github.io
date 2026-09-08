// Project-root ESLint config — the SSoT delegator.
//
// It exists ONLY so `npx eslint` and your editor run the EXACT same rule set as
// `npx ts-qa`. Keep it a thin delegator: ALL project-specific lint opinion (local
// plugins, strict-TS, per-dir overrides) belongs in tsQaConfig/eslint.config.js,
// which ts-qa composes for BOTH entrypoints. The eslintConfigParity phase-0 check
// fails the pipeline if this file ever stops delegating.
//
// A root config is optional — delete this file to lint solely through ts-qa — but
// if it exists it MUST delegate.
import { projectEslintConfig } from "@longtermsupport/ts-qa-ci";

export default await projectEslintConfig(import.meta.url);
