**Student Course**



🎓 Student Class – Features



Attributes (fields):

1. id → unique identifier (e.g., student number)
2. name → full name
3. email → (optional, good for realism)
4. courses → list/set of courses the student is enrolled in



Methods:

1. enroll(course) → add this student to a course

2. drop(course) → remove this student from a course

3. list_courses() → return all courses the student is taking

4. __repr__/toString() → display student details nicely





📘 Course Class – Features

Attributes (fields):

1. id → unique course code (e.g., "CS101")

2. name → course title

3. students → list/set of students enrolled

Methods:

1. add_student(student) → enroll a student

2. remove_student(student) → drop a student

3. list_students() → return all students in the course

__repr__/toString() → display course details nicely