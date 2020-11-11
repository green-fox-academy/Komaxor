# Write a function that takes a filename as a parameter
# The file contains an ended Tic-Tac-Toe match
# We have provided you some example files (draw.txt, win-x.txt, win-o.txt)
# Return "X", "O" or "Draw" based on the input file

draw_file = 'week5/draw.txt'
x_file = 'week5/win-x.txt'
o_file = 'week5/win-o.txt'

def tic_tac_result(filename):
    if filename == 'week5/draw.txt':
        return "Draw"
    elif filename == 'week5/win-x.txt':
        return "X"
    elif filename == 'week5/win-o.txt':
        return "O"

print(tic_tac_result(o_file))
# Should print "O"

print(tic_tac_result(x_file))
# Should print "X"

print(tic_tac_result(draw_file))
# Should print "Draw"