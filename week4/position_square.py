from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws one square and takes 2 parameters:
# The x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# Draw 3 squares with that function.
# Avoid code duplication.
def x_input():
        while True:
            try:
                x = int(input("How far aside away do you want the box? "))
            except ValueError:
                print("Enter a number!")
                continue
            if 250 <= x or x <= 0:
                print("Number must be between 0 and 250")
                continue
            else:
                return x

def y_input():
        while True:
            try:
                y = int(input("How high do you want the box? "))
            except ValueError:
                print("Enter a number!")
                continue
            if 250 <= y or y <= 0:
                print("Number must be between 0 and 250")
                continue
            else:
                return y

def drawer(x, y):
    canvas.create_rectangle(x, y, x + 50, y + 50)

for _ in range (0, 3):
    x = x_input()
    y = y_input()
    drawer(x, y)

root.mainloop()