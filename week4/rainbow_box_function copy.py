from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a square drawing function that takes 2 parameters:
# The square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# Create a loop that fills the canvas with rainbow colored squares (red, orange, yellow, green, blue, indigo, violet).
#NOTE it even asks the user for inputs

def size_input():
        while True:
            try:
                size = int(input("How big do you want the box? "))
            except ValueError:
                print("Enter a number!")
                continue
            if 300 < size or size <= 0:
                print("Number must be between 1 and 300")
                continue
            else:
                return size

def color_input_r():
    while True:
        try:
            r = int(input("What color do you want the box? Enter the red value! "))
        except ValueError:
            print("Enter a number!")
            continue
        if 255 < r or r < 0:
            print("Number must be between 0 and 255")
            continue
        else:
            return r

def color_input_g():
    while True:
        try:
            g = int(input("What color do you want the box? Enter the green value! "))
        except ValueError:
            print("Enter a number!")
            continue
        if 255 < g or g < 0:
            print("Number must be between 0 and 255")
            continue
        else:
            return g

def color_input_b():
    while True:
        try:
            b = int(input("What color do you want the box? Enter the blue value! "))
        except ValueError:
            print("Enter a number!")
            continue
        if 255 < b or b < 0:
            print("Number must be between 0 and 255")
            continue
        else:
            return b

def drawer(length, red, green, blue):
    a = (300 - length) / 2
    d = 300 - ((300 - length) / 2)
    colour = '#%02x%02x%02x' % (red, green, blue) # TODO i don't understand but it works
    canvas.create_rectangle(a, a, d, d, fill=colour)

for _ in range (0, 3):
    r = color_input_r()
    g = color_input_g()
    b = color_input_b()
    size = size_input()
    drawer(size, r, g, b)

root.mainloop()