class Person:

    def __init__(self, name = 'Jane Doe', age = 30, gender = 'female'):
        self.name = name
        self.age = age
        self.gender = gender

    def common_introduce(self):
        return ("Hi, I'm " + self.name + ", a " + str(self.age) + " age old " + self.gender)

    def introduce(self):
        print(self.common_introduce() + ".")

    def get_goal(self):
        print("My goal is: Live for the moment!")

