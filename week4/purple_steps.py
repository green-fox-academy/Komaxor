from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Reproduce this:
# [https://github.com/green-fox-academy/teaching-materials/blob/master/workshop/drawing/assets/r3.png]

def steps():
        while True:
            try:
                number_of_boxes = int(input("How many steps do you want? "))
            except ValueError:
                print("Enter a number!")
                continue
            if 30 <= number_of_boxes or number_of_boxes <= 0:
                print("Number must be between 1 and 29")
                continue
            else:
                return number_of_boxes

def drawer(num):
    a = length * i
    d = length + length * i
    canvas.create_rectangle(a, a, d, d, fill="purple")

length = 10
num = steps()
for i in range (1, num + 1):
    drawer(length)


root.mainloop()