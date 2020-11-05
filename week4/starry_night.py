from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300', bg ="black")
canvas.pack()

# Draw the night sky:
#  - The background should be black
#  - The stars should be small squares
for _ in range(0, 150):
    ax = random.randrange(300)
    ay = random.randrange(300)
    colour_value = random.randrange(254)
    colour = '#%02x%02x%02x' % (colour_value, colour_value, colour_value) # TODO i don't understand but it works
    canvas.create_rectangle(ax, ay, ax + 5, ay + 5, fill=colour)

#  - The stars should have random positions on the canvas
#  - The stars should have random color (some shade of grey)

root.mainloop()