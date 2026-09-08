import {
  defaultFilters,
  encode,
  gradeColumnLabel,
  toggle,
} from "../register/filter";
import {
  GRADE_COLUMNS,
  type Filters,
  type GradeColumn,
  type Kind,
  type Level,
} from "../register/types";

interface FilterBarProps {
  filters: Filters;
  languages: string[];
  shown: number;
  total: number;
  onChange: (filters: Filters) => void;
}

const KINDS: { value: Kind; label: string }[] = [
  { value: "tool", label: "Tool" },
  { value: "toolchain", label: "Toolchain" },
];

const LEVELS: { value: Level; mark: string }[] = [
  { value: "green", mark: "🟢" },
  { value: "amber", mark: "🟡" },
  { value: "red", mark: "🔴" },
];

interface GradeGroupProps {
  column: GradeColumn;
  selected: Level[];
  onToggle: (level: Level) => void;
}

function GradeGroup({ column, selected, onToggle }: GradeGroupProps) {
  const label = gradeColumnLabel(column);
  return (
    <fieldset className="register-filter-group">
      <legend>{label}</legend>
      {LEVELS.map((level) => (
        <label key={level.value} className="register-filter-option">
          <input
            type="checkbox"
            checked={selected.includes(level.value)}
            onChange={() => onToggle(level.value)}
            aria-label={`${label}: ${level.value}`}
          />
          <span aria-hidden="true">{level.mark}</span>
        </label>
      ))}
    </fieldset>
  );
}

export function FilterBar({
  filters,
  languages,
  shown,
  total,
  onChange,
}: FilterBarProps) {
  const filtered = encode(filters) !== "";
  return (
    <form
      className="register-filters"
      onSubmit={(event) => event.preventDefault()}
    >
      <label className="register-search">
        <span>Search</span>
        <input
          type="search"
          value={filters.query}
          placeholder="Name, language, note…"
          onChange={(event) =>
            onChange({ ...filters, query: event.target.value })
          }
        />
      </label>
      <fieldset className="register-filter-group">
        <legend>Language</legend>
        {languages.map((language) => (
          <label key={language} className="register-filter-option">
            <input
              type="checkbox"
              checked={filters.languages.includes(language)}
              onChange={() =>
                onChange({
                  ...filters,
                  languages: toggle(filters.languages, language),
                })
              }
            />
            <span>{language}</span>
          </label>
        ))}
      </fieldset>
      <fieldset className="register-filter-group">
        <legend>Kind</legend>
        {KINDS.map((kind) => (
          <label key={kind.value} className="register-filter-option">
            <input
              type="checkbox"
              checked={filters.kinds.includes(kind.value)}
              onChange={() =>
                onChange({
                  ...filters,
                  kinds: toggle(filters.kinds, kind.value),
                })
              }
            />
            <span>{kind.label}</span>
          </label>
        ))}
      </fieldset>
      {GRADE_COLUMNS.map((column) => (
        <GradeGroup
          key={column}
          column={column}
          selected={filters.grades[column]}
          onToggle={(level) =>
            onChange({
              ...filters,
              grades: {
                ...filters.grades,
                [column]: toggle(filters.grades[column], level),
              },
            })
          }
        />
      ))}
      <p className="register-count" role="status">
        {shown} of {total} tools
        {filtered ? (
          <>
            {" "}
            <button
              type="button"
              className="register-reset"
              onClick={() => onChange(defaultFilters())}
            >
              Reset filters
            </button>
          </>
        ) : null}
      </p>
    </form>
  );
}
