from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
#canvas.create_rectangle(10, 10, 150, 150, outline="red")
canvas.create_line(150, 10, 150, 150, fill="red")
canvas.create_line(10, 150, 150, 150, fill="green")
canvas.create_line(150, 10, 10, 10, fill="blue")
canvas.create_line(10, 150, 10, 10, fill="purple")

root.mainloop()