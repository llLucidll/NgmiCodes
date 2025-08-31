from __future__ import annotations
from dataclasses import dataclass, field
from typing import Set

@dataclass(eq=True, frozen=True, slots=True)
class StudentId:
    value: int

@dataclass(eq=True, frozen=True, slots=True)
class CourseId:
    value: int

class Student:
    """Student with identity, name, email, and enrolled courses."""
    __slots__ = ("id", "name", "email", "_courses")

    def __init__(self, id: StudentId, name: str, email: str):
        if not name.strip():
            raise ValueError("name required")
        if "@" not in email:
            raise ValueError("invalid email")
        self.id: StudentId = id
        self.name: str = name
        self.email: str = email
        self._courses: Set[Course] = set()

    def courses(self) -> Set["Course"]:
        # return a snapshot to avoid external mutation
        return set(self._courses)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Student) and self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"Student(id={self.id.value}, name={self.name!r})"

class Course:
    """Course with identity, name, and enrolled students."""
    __slots__ = ("id", "name", "_students")

    def __init__(self, id: CourseId, name: str):
        if not name.strip():
            raise ValueError("name required")
        self.id: CourseId = id
        self.name: str = name
        self._students: Set[Student] = set()

    # --- Single source of truth for enrollment operations ---
    def enroll(self, student: Student) -> None:
        if student in self._students:
            raise ValueError("student already enrolled")
        # mutate both sides atomically
        self._students.add(student)
        try:
            student._courses.add(self)  # internal update
        except Exception:               # rollback on failure (paranoia)
            self._students.remove(student)
            raise

    def drop(self, student: Student) -> None:
        if student not in self._students:
            raise ValueError("student not enrolled")
        self._students.remove(student)
        student._courses.remove(self)

    def students(self) -> Set[Student]:
        return set(self._students)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Course) and self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f"Course(id={self.id.value}, name={self.name!r})"

# Optional façade methods on Student that delegate to Course:
def enroll_student(student: Student, course: Course) -> None:
    course.enroll(student)

def drop_student(student: Student, course: Course) -> None:
    course.drop(student)
