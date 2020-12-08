from student import Student
from mentor import Mentor

class Cohort:
    name = ''
    students = []
    mentors = []

    def __init__(self, name):
        self.students = []
        self.mentors = []

    def add_student(self, Student):
        self.students.append(Student)

    def add_mentor(self, Mentor):
        self.mentors.append(Mentor)

    def info(self):
        print("The " + self.name + " cohort has " + str(len(self.students)) + "students and " + str(len(self.mentors)) + "mentors.")
