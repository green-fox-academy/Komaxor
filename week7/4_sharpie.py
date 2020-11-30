#Create Sharpie class
#We should know about each sharpie their color (which should be a string), width (which will be a floating point number), ink_amount (another floating point number)
#When creating one, we need to specify the color and the width
#Every sharpie is created with a default 100 as ink_amount
#We can use() the sharpie objects
#which decreases inkAmount

class Sharpie(object):
    color = ''
    width = 0.0
    ink_amount = 0.0

    def __init__(self, color, width, ink_amount = 100):
        self.color = color
        self.width = width

    def use(self, ink_amount):
        self.ink_amount -= 1

