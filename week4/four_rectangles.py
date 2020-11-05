from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Draw four different size and color rectangles.
# Avoid code duplication.
colours = ['black', 'green', 'blue', 'purple', 'yellow', 'orange']
for _ in range(0, 4):
    select = random.randrange(len(colours)) - 1
    canvas.create_rectangle(random.randrange(300), random.randrange(300), random.randrange(300), random.randrange(300), fill=colours[select])
    colours.remove(colours[select])
root.mainloop()