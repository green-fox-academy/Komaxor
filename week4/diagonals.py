from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Draw the canvas' diagonals.
# If it starts from the upper-left corner it should be green, otherwise it should be red.
canvas.create_line(0, 0, 300, 300, fill="green")
canvas.create_line(0, 300, 300, 0, fill="red")

root.mainloop()