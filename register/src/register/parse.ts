import type { Grade, Kind, Level, NoteSegment, Register, Tool } from "./types";

const LEVELS: readonly Level[] = ["green", "amber", "red", "none", "ungraded"];
const KINDS: readonly Kind[] = ["tool", "toolchain"];

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function isString(value: unknown): value is string {
  return typeof value === "string";
}

function isLevel(value: unknown): value is Level {
  return LEVELS.some((level) => level === value);
}

function isKind(value: unknown): value is Kind {
  return KINDS.some((kind) => kind === value);
}

function isGrade(value: unknown): value is Grade {
  return isRecord(value) && isString(value["mark"]) && isLevel(value["level"]);
}

function isSegment(value: unknown): value is NoteSegment {
  return (
    isRecord(value) &&
    isString(value["text"]) &&
    (value["href"] === undefined || isString(value["href"]))
  );
}

function isTool(value: unknown): value is Tool {
  return (
    isRecord(value) &&
    isString(value["slug"]) &&
    isString(value["name"]) &&
    isString(value["page"]) &&
    isString(value["language"]) &&
    isKind(value["kind"]) &&
    isGrade(value["readiness"]) &&
    isGrade(value["detector"]) &&
    isGrade(value["toolchain"]) &&
    isGrade(value["project"]) &&
    Array.isArray(value["notes"]) &&
    value["notes"].every(isSegment) &&
    isString(value["checked"])
  );
}

// Validates the JSON that tools/build-register.py wrote, so a malformed file is reported
// rather than rendered as a broken table.
export function parseRegister(value: unknown): Register {
  if (
    !isRecord(value) ||
    !Array.isArray(value["languages"]) ||
    !Array.isArray(value["tools"])
  ) {
    throw new Error("not a register: expected languages and tools arrays");
  }
  const languages: string[] = [];
  for (const language of value["languages"]) {
    if (!isString(language)) {
      throw new Error("not a register: a language is not a string");
    }
    languages.push(language);
  }
  const tools: Tool[] = [];
  value["tools"].forEach((tool: unknown, index: number) => {
    if (!isTool(tool)) {
      throw new Error(`not a register: tool ${index} is malformed`);
    }
    tools.push(tool);
  });
  return { languages, tools };
}
