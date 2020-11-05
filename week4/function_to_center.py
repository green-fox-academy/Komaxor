from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# Create a function that draws a single line and takes 2 parameters:
# The x and y coordinates of the line's starting point
def x_input():
        while True:
            try:
                x = int(input("How wide away do you want the line? "))
            except ValueError:
                print("Enter a number!")
                continue
            if 300 < x or x < 0:
                print("Number must be between 0 and 300")
                continue
            else:
                return x

def y_input():
        while True:
            try:
                y = int(input("How high away do you want the line? "))
            except ValueError:
                print("Enter a number!")
                continue
            if 300 < y or y < 0:
                print("Number must be between 0 and 300")
                continue
            else:
                return y

x = x_input()
y = y_input()

# and draws a line from that point to the center of the canvas.
def drawer(x, y):
    canvas.create_line(x, y, 150, 150)

drawer(x, y)

edge = []

for i in range(0, 301, 20):
    edge.append(i)

for i in range(0, len(edge)):
    canvas.create_line(0, edge[i], 150, 150)
    canvas.create_line(300, edge[i], 150, 150)
    canvas.create_line(edge[i], 0, 150, 150)
    canvas.create_line(edge[i], 300, 150, 150)

'''
for i in range(0, 301, 20):
    for j in range(0, 301, 20):
        if i == 0 or i == 300:
            canvas.create_line(i, j, 150, 150)
        if j == 0 or j == 300:
            canvas.create_line(i, j, 150, 150)
'''
# Fill the canvas with lines from the edges, every 20 px, to the center.
root.mainloop()

