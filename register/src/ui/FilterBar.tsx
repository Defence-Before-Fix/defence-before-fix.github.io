import { defaultFilters, encode } from "../register/filter";
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

interface Choice<T extends string> {
  value: T;
  label: string;
}

const KINDS: Choice<Kind>[] = [
  { value: "tool", label: "Tool" },
  { value: "toolchain", label: "Toolchain" },
];

const LEVELS: Choice<Level>[] = [
  { value: "green", label: "🟢 Green" },
  { value: "amber", label: "🟡 Amber" },
  { value: "red", label: "🔴 Red" },
];

const GRADE_LABELS: Record<GradeColumn, string> = {
  readiness: "Readiness",
  detector: "Detector conformance",
  toolchain: "Toolchain conformance",
  project: "Project conformance",
};

interface ChoiceSelectProps<T extends string> {
  label: string;
  any: string;
  choices: Choice<T>[];
  selected: T[];
  onSelect: (value: T | undefined) => void;
}

// One select per facet: the first option means no restriction. The filter model allows
// several values per facet, from a hand-written address; the select shows the first.
function ChoiceSelect<T extends string>({
  label,
  any,
  choices,
  selected,
  onSelect,
}: ChoiceSelectProps<T>) {
  const current = selected[0] ?? "";
  return (
    <label className="register-facet">
      <span>{label}</span>
      <select
        value={current}
        onChange={(event) => {
          const chosen = choices.find((c) => c.value === event.target.value);
          onSelect(chosen?.value);
        }}
      >
        <option value="">{any}</option>
        {choices.map((choice) => (
          <option key={choice.value} value={choice.value}>
            {choice.label}
          </option>
        ))}
      </select>
    </label>
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
  const languageChoices: Choice<string>[] = languages.map((language) => ({
    value: language,
    label: language,
  }));
  return (
    <form
      className="register-filters"
      onSubmit={(event) => event.preventDefault()}
    >
      <div className="register-filter-row">
        <label className="register-search">
          <span>Search</span>
          <input
            type="search"
            value={filters.query}
            placeholder="Tool name, language or note"
            onChange={(event) =>
              onChange({ ...filters, query: event.target.value })
            }
          />
        </label>
        <ChoiceSelect
          label="Language"
          any="Any language"
          choices={languageChoices}
          selected={filters.languages}
          onSelect={(value) =>
            onChange({
              ...filters,
              languages: value === undefined ? [] : [value],
            })
          }
        />
        <ChoiceSelect
          label="Kind"
          any="Tools and toolchains"
          choices={KINDS}
          selected={filters.kinds}
          onSelect={(value) =>
            onChange({ ...filters, kinds: value === undefined ? [] : [value] })
          }
        />
      </div>
      <div className="register-filter-row">
        {GRADE_COLUMNS.map((column) => (
          <ChoiceSelect
            key={column}
            label={GRADE_LABELS[column]}
            any="Any grade"
            choices={LEVELS}
            selected={filters.grades[column]}
            onSelect={(value) =>
              onChange({
                ...filters,
                grades: {
                  ...filters.grades,
                  [column]: value === undefined ? [] : [value],
                },
              })
            }
          />
        ))}
      </div>
      <p className="register-count" role="status">
        <span>
          {shown} of {total} tools
        </span>
        {filtered ? (
          <button
            type="button"
            className="register-reset"
            onClick={() => onChange(defaultFilters())}
          >
            Reset filters
          </button>
        ) : null}
      </p>
    </form>
  );
}
