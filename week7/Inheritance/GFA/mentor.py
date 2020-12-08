from person import Person

class Mentor(Person):

    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female', level = 'intermediate'):
        super().__init__(name, age, gender)
        self.level = level

    def get_goal(self):
        print("Educate brilliant junior software developers.")

    def introduce(self):
        print(super().common_introduce() + " " + self.level + " mentor.")
