import type { Grade, GradeColumn } from "../register/types";
import { gradeColumnLabel } from "../register/filter";

interface GradeMarkProps {
  grade: Grade;
  column: GradeColumn;
}

function describe(grade: Grade): string {
  return grade.level === "none" ? "not applicable" : grade.level;
}

// The grade is drawn as a coloured disc from the level, so it does not depend on a colour
// emoji font; the emoji itself is kept for copy and paste but hidden from view.
export function GradeMark({ grade, column }: GradeMarkProps) {
  const label = `${gradeColumnLabel(column)}: ${describe(grade)}`;
  return (
    <span
      className="register-grade"
      data-level={grade.level}
      role="img"
      aria-label={label}
      title={label}
    >
      <span className="register-dot" aria-hidden="true"></span>
      <span className="register-grade-text">{grade.mark}</span>
    </span>
  );
}
