from typing import List, Optional
from .student import Student


class S_Class:
    def __init__(self, name: str, students: Optional[List[Student]] = None):
        self.name = name
        self.students = students or []

    def add_student(self, student: Student):
        student._class = self
        self.students.append(student)

    def remove_student(self, student: Student):
        student._class = None
        self.students.remove(student)
