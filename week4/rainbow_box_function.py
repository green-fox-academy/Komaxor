from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a square drawing function that takes 2 parameters:
# The square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# Create a loop that fills the canvas with rainbow colored squares (red, orange, yellow, green, blue, indigo, violet).

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
    a = ((300 - length) / 2) + (i * length / len(rainbow) / 2)
    d = 300 - ((300 - length) / 2) - (i * length / len(rainbow) / 2)
    canvas.create_rectangle(a, a, d, d, fill=rainbow[i])

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
size = size_input()

for i in range (0, len(rainbow)):
    drawer(size)

root.mainloop()