from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that takes 1 parameter:

def connect(xy):
    for i in range(0, len(xy) - 1):
        canvas.create_line(xy[i], xy[i], xy[i + 1], xy[i + 1], fill="green")
# and connects them with green lines.
# Connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
box = [[10, 10], [290,  10], [290, 290], [10, 290], [10, 10]]
# A list of [x, y] points
# Connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]
points = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]

connect(box)
connect(points)

root.mainloop()