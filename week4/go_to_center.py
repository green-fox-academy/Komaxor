from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws a single line and takes 2 parameters:
# the x and y coordinates of the line's starting point
def x_input():
        while True:
            try:
                x = int(input("How wide away do you want the line? "))
            except ValueError:
                print("Enter a number!")
                continue
            if 300 < x or x < 0:
                print("Number must be between 0 and 300")
                continue
            else:
                return x

def y_input():
        while True:
            try:
                y = int(input("How high away do you want the line? "))
            except ValueError:
                print("Enter a number!")
                continue
            if 300 < y or y < 0:
                print("Number must be between 0 and 300")
                continue
            else:
                return y

# and draws a line from that point to the center of the canvas.
def drawer(x, y):
    canvas.create_line(x, y, 150, 150)

# Draw at least 3 lines with that function using a loop.
for _ in range (0, 3):
    x = x_input()
    y = y_input()
    drawer(x, y)

root.mainloop()