#Create Counter class
#which has an integer field value
#when creating it should have a default value 0 or we can specify it when creating
#we can add(number) to this counter another whole number
#or we can add() without parameters just increasing the counter's value by one
#and we can get() the current value
#also we can reset() the value to the initial value
#Check if everything is working fine with the proper test
#Download test_counter.py and place it next to your solution
#Run the test file as a usual python program

class Counter:
    field = 0

    def add(self, number = None):
        if number != None:
            self.field += number
        else:
            self.field += 1

    def get(self):
        return self.field

    def reset(self):
        self.field = self.number

    def __init__(self, number = 0):
        self.number = number
        self.field = number
