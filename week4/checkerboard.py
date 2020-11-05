from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Fill the canvas with a checkerboard pattern.
for i in range (0, 30):
    for j in range (0, 30):
        if j % 2 != 0 and i % 2 == 0:
            canvas.create_rectangle(i * 10, j * 10, i * 10 + 10, j * 10 + 10, fill="black") #NOTE nem kozepen kezdodik
        elif j % 2 == 0 and i % 2 != 0:
            canvas.create_rectangle(i * 10, j * 10, i * 10 + 10, j * 10 + 10, fill="black")
root.mainloop()