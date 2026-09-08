import { gradeColumnLabel } from "../register/filter";
import {
  GRADE_COLUMNS,
  type Sort,
  type SortKey,
  type Tool,
} from "../register/types";
import { GradeMark } from "./GradeMark";

interface RegisterTableProps {
  tools: Tool[];
  sort: Sort;
  onSort: (key: SortKey) => void;
}

interface Column {
  key: Exclude<SortKey, "default">;
  label: string;
}

const COLUMNS: Column[] = [
  { key: "name", label: "Tool" },
  { key: "language", label: "Language" },
  { key: "kind", label: "Kind" },
  ...GRADE_COLUMNS.map((key) => ({ key, label: gradeColumnLabel(key) })),
  { key: "checked", label: "Checked" },
];

function ariaSort(
  column: Column,
  sort: Sort,
): "ascending" | "descending" | "none" {
  if (sort.key !== column.key) {
    return "none";
  }
  return sort.direction === "asc" ? "ascending" : "descending";
}

function Notes({ tool }: { tool: Tool }) {
  return (
    <>
      {tool.notes.map((segment, index) =>
        segment.href === undefined ? (
          <span key={index}>{segment.text}</span>
        ) : (
          <a key={index} href={segment.href}>
            {segment.text}
          </a>
        ),
      )}
    </>
  );
}

function Row({ tool }: { tool: Tool }) {
  return (
    <tr data-kind={tool.kind}>
      <td className="register-name">
        <a href={tool.page}>{tool.name}</a>
      </td>
      <td>{tool.language}</td>
      <td>{tool.kind}</td>
      {GRADE_COLUMNS.map((column) => (
        <td key={column} className="register-grade-cell">
          <GradeMark grade={tool[column]} column={column} />
        </td>
      ))}
      <td className="register-checked">{tool.checked}</td>
      <td className="register-notes">
        <Notes tool={tool} />
      </td>
    </tr>
  );
}

export function RegisterTable({ tools, sort, onSort }: RegisterTableProps) {
  return (
    <div className="register-scroll">
      <table className="register-table">
        <thead>
          <tr>
            {COLUMNS.map((column) => (
              <th
                key={column.key}
                scope="col"
                aria-sort={ariaSort(column, sort)}
              >
                <button
                  type="button"
                  className="register-sort"
                  onClick={() => onSort(column.key)}
                >
                  {column.label}
                  <span className="register-sort-mark" aria-hidden="true">
                    {sort.key === column.key
                      ? sort.direction === "asc"
                        ? " ▲"
                        : " ▼"
                      : ""}
                  </span>
                </button>
              </th>
            ))}
            <th scope="col">Notes</th>
          </tr>
        </thead>
        <tbody>
          {tools.length === 0 ? (
            <tr>
              <td colSpan={COLUMNS.length + 1} className="register-empty">
                No tools match these filters.
              </td>
            </tr>
          ) : (
            tools.map((tool) => <Row key={tool.slug} tool={tool} />)
          )}
        </tbody>
      </table>
    </div>
  );
}
