import {
  GRADE_COLUMNS,
  type Filters,
  type GradeColumn,
  type Kind,
  type Level,
  type Register,
  type Sort,
  type SortDirection,
  type SortKey,
  type Tool,
} from "./types";

const LEVELS: Level[] = ["green", "amber", "red", "none", "ungraded"];
const KINDS: Kind[] = ["tool", "toolchain"];
const SORT_KEYS: SortKey[] = [
  "default",
  "name",
  "language",
  "kind",
  ...GRADE_COLUMNS,
  "checked",
];
const LEVEL_ORDER: Record<Level, number> = {
  green: 0,
  amber: 1,
  red: 2,
  ungraded: 3,
  none: 4,
};

export function defaultFilters(): Filters {
  return {
    query: "",
    languages: [],
    kinds: [],
    grades: { readiness: [], detector: [], toolchain: [], project: [] },
    sort: { key: "default", direction: "asc" },
  };
}

export function noteText(tool: Tool): string {
  return tool.notes.map((segment) => segment.text).join("");
}

function matchesQuery(tool: Tool, query: string): boolean {
  const q = query.trim().toLowerCase();
  if (q === "") {
    return true;
  }
  const haystack = [
    tool.name,
    tool.language,
    tool.kind,
    noteText(tool),
    tool.checked,
  ]
    .join(" ")
    .toLowerCase();
  return q.split(/\s+/).every((word) => haystack.includes(word));
}

function matchesGrades(tool: Tool, grades: Filters["grades"]): boolean {
  return GRADE_COLUMNS.every((column) => {
    const wanted = grades[column];
    return wanted.length === 0 || wanted.includes(tool[column].level);
  });
}

export function apply(register: Register, filters: Filters): Tool[] {
  const kept = register.tools.filter(
    (tool) =>
      matchesQuery(tool, filters.query) &&
      (filters.languages.length === 0 ||
        filters.languages.includes(tool.language)) &&
      (filters.kinds.length === 0 || filters.kinds.includes(tool.kind)) &&
      matchesGrades(tool, filters.grades),
  );
  return sortTools(kept, register.languages, filters.sort);
}

function languageRank(language: string, order: string[]): number {
  const index = order.indexOf(language);
  return index === -1 ? order.length : index;
}

function compareDefault(a: Tool, b: Tool, order: string[]): number {
  return (
    languageRank(a.language, order) - languageRank(b.language, order) ||
    Number(a.kind !== "toolchain") - Number(b.kind !== "toolchain") ||
    a.name.localeCompare(b.name, "en", { sensitivity: "base" })
  );
}

function compareBy(
  key: Exclude<SortKey, "default">,
  a: Tool,
  b: Tool,
  order: string[],
): number {
  switch (key) {
    case "name":
      return a.name.localeCompare(b.name, "en", { sensitivity: "base" });
    case "language":
      return languageRank(a.language, order) - languageRank(b.language, order);
    case "kind":
      return Number(a.kind !== "toolchain") - Number(b.kind !== "toolchain");
    case "checked":
      return a.checked.localeCompare(b.checked, "en");
    default:
      return LEVEL_ORDER[a[key].level] - LEVEL_ORDER[b[key].level];
  }
}

export function sortTools(tools: Tool[], order: string[], sort: Sort): Tool[] {
  const sign = sort.direction === "desc" ? -1 : 1;
  return [...tools].sort((a, b) => {
    const primary =
      sort.key === "default"
        ? compareDefault(a, b, order)
        : compareBy(sort.key, a, b, order);
    return sign * primary || compareDefault(a, b, order);
  });
}

function isKind(value: string): value is Kind {
  return KINDS.some((kind) => kind === value);
}

function isLevel(value: string): value is Level {
  return LEVELS.some((level) => level === value);
}

function isSortKey(value: string): value is SortKey {
  return SORT_KEYS.some((key) => key === value);
}

function isDirection(value: string): value is SortDirection {
  return value === "asc" || value === "desc";
}

function list(params: URLSearchParams, name: string): string[] {
  const raw = params.get(name);
  return raw === null || raw === "" ? [] : raw.split(",");
}

export function encode(filters: Filters): string {
  const params = new URLSearchParams();
  if (filters.query !== "") {
    params.set("q", filters.query);
  }
  if (filters.languages.length > 0) {
    params.set("lang", filters.languages.join(","));
  }
  if (filters.kinds.length > 0) {
    params.set("kind", filters.kinds.join(","));
  }
  for (const column of GRADE_COLUMNS) {
    if (filters.grades[column].length > 0) {
      params.set(column, filters.grades[column].join(","));
    }
  }
  if (filters.sort.key !== "default" || filters.sort.direction !== "asc") {
    params.set("sort", `${filters.sort.key}:${filters.sort.direction}`);
  }
  return params.toString();
}

export function decode(hash: string): Filters {
  const params = new URLSearchParams(hash.replace(/^#/, ""));
  const filters = defaultFilters();
  filters.query = params.get("q") ?? "";
  filters.languages = list(params, "lang");
  filters.kinds = list(params, "kind").filter(isKind);
  for (const column of GRADE_COLUMNS) {
    filters.grades[column] = list(params, column).filter(isLevel);
  }
  const [key = "", direction = ""] = (params.get("sort") ?? "").split(":");
  if (isSortKey(key) && isDirection(direction)) {
    filters.sort = { key, direction };
  }
  return filters;
}

export function toggle<T>(values: T[], value: T): T[] {
  return values.includes(value)
    ? values.filter((v) => v !== value)
    : [...values, value];
}

export function gradeColumnLabel(column: GradeColumn): string {
  switch (column) {
    case "readiness":
      return "Readiness";
    case "detector":
      return "Detector";
    case "toolchain":
      return "Toolchain";
    case "project":
      return "Project";
  }
}
