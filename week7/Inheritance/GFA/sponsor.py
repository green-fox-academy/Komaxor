from person import Person

class Sponsor(Person):
    company = ''
    hired_students = 0

    def get_goal(self):
        print("Hire brilliant junior software developers.")

    def introduce(self):
        super().introduce()
        print("who represents " + self.company + " and hired " + self.hired_students + " students so far.")

    def hire(self):
        self.hired_students += 1

    def __init__(self, name, age, gender, company):
        super().__init__(name, age, gender)
        self.hired_students = 0
        company = "Google"