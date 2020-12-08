from person import Person

class Student(Person):

    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', previous_organization = 'The School of Life'):
        super().__init__(name, age, gender)
        self.previous_organization = previous_organization
        self.skipped_days = 0

    def get_goal(self):
        print("Be a junior software developer.")

    def introduce(self):
        print(super().common_introduce() + " from " + self.previous_organization + " who skipped " + str(self.skipped_days) + " days from the course already.")

    def skip_days(self, number_of_days):
        self.skipped_days += number_of_days
