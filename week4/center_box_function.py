from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def size_input():
        while True:
            try:
                size = int(input("How big do you want the box? "))
            except ValueError:
                print("Enter a number!")
                continue
            if 300 <= size or size <= 0:
                print("Number must be between 0 and 300")
                continue
            else:
                return size

def drawer(length):
    a = (300 - length) / 2
    d = 300 - ((300 - length) / 2)
    canvas.create_rectangle(a, a, d, d)

for _ in range (0, 3):
    size = size_input()
    drawer(size)

# Create a function that draws one square and takes 1 parameters:
# The square size
# and draws a square of that size to the center of the canvas.
# Draw 3 squares with that function.
# Avoid code duplication.

root.mainloop()