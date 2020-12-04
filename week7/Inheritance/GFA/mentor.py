from person import Person

class Mentor(Person):
    level = ''

    def get_goal(self):
        print("Educate brilliant junior software developers.")

    def introduce(self):
        super().introduce()
        print(self.level + "mentor.")

    def __init__(self, name, age, gender, level):
        super().__init__(name, age, gender)
        level = 'intermediate'
