class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of subject scores

    def average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0

    def __str__(self):
        return f"{self.name} — average: {self.average():.2f}"


class GraduateStudent(Student):
    """Inherits from Student, adds thesis-specific data."""

    def __init__(self, name, marks, thesis_title):
        super().__init__(name, marks)
        self.thesis_title = thesis_title

    def __str__(self):
        base = super().__str__()
        return f"{base} | Thesis: {self.thesis_title}"


class Course:
    """Holds a list of Student objects and reports on the group."""

    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0
        total = sum(s.average() for s in self.students)
        return total / len(self.students)

    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.average())


if __name__ == "__main__":
    s1 = Student("Asha", [78, 82, 91])
    s2 = Student("Ravi", [65, 70, 68])
    g1 = GraduateStudent("Meera", [88, 94, 90], "Numerical Methods for PDEs")

    course = Course("Computational Mathematics")
    course.add_student(s1)
    course.add_student(s2)
    course.add_student(g1)

    for student in course.students:
        print(student)

    print(f"\nClass average: {course.class_average():.2f}")
    print(f"Top student: {course.top_student()}")