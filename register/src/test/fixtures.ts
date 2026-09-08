import type { Register, Tool } from "../register/types";

export const phpstan: Tool = {
  slug: "phpstan",
  name: "PHPStan",
  page: "/tools/phpstan.html",
  language: "PHP",
  kind: "tool",
  readiness: { mark: "🟢", level: "green" },
  detector: { mark: "🟡", level: "amber" },
  toolchain: { mark: "·", level: "none" },
  project: { mark: "·", level: "none" },
  notes: [
    { text: "Bundled documentation online only fails " },
    { text: "6.2", href: "/DETECTOR-SPEC.html#62-resolution" },
    { text: " and " },
    { text: "6.3", href: "/DETECTOR-SPEC.html#63-a-bundled" },
    { text: "." },
  ],
  checked: "2026-09-08, version 2.2.13",
};

export const phpQaCi: Tool = {
  slug: "php-qa-ci",
  name: "php-qa-ci",
  page: "/tools/php-qa-ci.html",
  language: "PHP",
  kind: "toolchain",
  readiness: { mark: "🟢", level: "green" },
  detector: { mark: "🟡", level: "amber" },
  toolchain: { mark: "🟡", level: "amber" },
  project: { mark: "🟡", level: "amber" },
  notes: [
    {
      text: "Harness, resolver, derived listing and justified record verified by running them.",
    },
  ],
  checked: "2026-09-08, branch php8.4 at commit e25aba4",
};

export const biome: Tool = {
  slug: "biome",
  name: "Biome",
  page: "/tools/biome.html",
  language: "JavaScript and TypeScript",
  kind: "tool",
  readiness: { mark: "🔴", level: "red" },
  detector: { mark: "🔴", level: "red" },
  toolchain: { mark: "·", level: "none" },
  project: { mark: "·", level: "none" },
  notes: [{ text: "GritQL plugin diagnostics carry no identifier." }],
  checked: "2026-09-08, version 2.5.12",
};

export const ruff: Tool = {
  slug: "ruff",
  name: "Ruff",
  page: "/tools/ruff.html",
  language: "Python",
  kind: "tool",
  readiness: { mark: "🟡", level: "amber" },
  detector: { mark: "🟡", level: "amber" },
  toolchain: { mark: "·", level: "none" },
  project: { mark: "·", level: "none" },
  notes: [{ text: "No plugin mechanism yet." }],
  checked: "2026-09-08, version 0.15.0",
};

export const register: Register = {
  languages: [
    "PHP",
    "JavaScript and TypeScript",
    "Python",
    "Go",
    "Rust",
    "Multi-language",
  ],
  tools: [phpQaCi, phpstan, biome, ruff],
};
