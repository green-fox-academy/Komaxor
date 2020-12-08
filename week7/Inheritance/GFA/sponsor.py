from person import Person

class Sponsor(Person):

    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', company = 'Google'):
        super().__init__(name, age, gender)
        self.hired_students = 0
        self.company = company

    def get_goal(self):
        print("Hire brilliant junior software developers.")

    def introduce(self):
        print(super().common_introduce() + " who represents " + self.company + " and hired " + str(self.hired_students) + " students so far.")

    def hire(self):
        self.hired_students += 1

