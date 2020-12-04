from person import Person

class Student(Person):
    previous_organization = ''
    skipped_days = 0

    def get_goal(self):
        print("Be a junior software developer.")

    def introduce(self):
        super().introduce()
        print(" from " + self.previous_organization + " who skipped " + str(self.skipped_days) + " days from the course already.")

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days

    def __init__(self, name, age, gender, previous_organization):
        super().__init__(name, age, gender)
        previous_organization = 'The School of Life'
        self.skipped_days = 0

#person = Person()
student = Student('Joe', 20, 'male', 'The School of Life')
student.introduce()