class Person:
    name = ''
    age = 0
    gender = ''

    def introduce(self):
        print("Hi, I'm " + self.name + ", a " + str(self.age) + " age old " + self.gender + ".")

    def get_goal(self):
        print("My goal is: Live for the moment!")

    def __init__(self, name, age, gender):
        self.name = 'Jane Doe'
        self.age = 30
        self.gender = 'female'