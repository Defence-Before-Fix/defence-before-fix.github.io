import type { Grade, GradeColumn } from "../register/types";
import { gradeColumnLabel } from "../register/filter";

interface GradeMarkProps {
  grade: Grade;
  column: GradeColumn;
}

function describe(grade: Grade): string {
  return grade.level === "none" ? "not applicable" : grade.level;
}

export function GradeMark({ grade, column }: GradeMarkProps) {
  return (
    <span
      className="register-grade"
      data-level={grade.level}
      role="img"
      aria-label={`${gradeColumnLabel(column)}: ${describe(grade)}`}
    >
      {grade.mark}
    </span>
  );
}
