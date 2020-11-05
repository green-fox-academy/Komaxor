from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that takes 1 parameter:
# A list of [x, y] points
# and connects them with green lines.
# Connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# Connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]

root.mainloop()