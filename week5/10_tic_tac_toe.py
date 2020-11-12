# Write a function that takes a filename as a parameter
# The file contains an ended Tic-Tac-Toe match
# We have provided you some example files (draw.txt, win-x.txt, win-o.txt)
# Return "X", "O" or "Draw" based on the input file

#source_file = 'week5/draw.txt'
source_file = 'week5/win-x.txt'
#source_file = 'week5/win-o.txt'

def tic_tac_result(filename):
    ch_list = []
    ch_sublist = []
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
        for ch in content:
            if ch == "X" or ch == "O":
                ch_sublist.append(ch)
            else:
                ch_list.append(ch_sublist)
                ch_sublist = []
        ch_list.append(ch_sublist)
        for i in range(0, len(ch_list)):
            is_same = True
            left = ch_list[i][0]
            for j in range(0, len(ch_list)):
                #print(left, ch_list[i][j])
                if ch_list[i][j] != left:
                    is_same = False
            if is_same:
                return left
            is_same = True
        for i in range(0, len(ch_list)):
            is_same = True
            top = ch_list[0][j]
            for j in range(0, len(ch_list)):
                #print(top, ch_list[j][i])
                if ch_list[j][i] != top:
                    is_same = False
            if is_same:
                return top
            is_same = True
        return "Draw"
'''            for j in range(0, len(ch_list)):
                corner = ch_list[0][j]
                #print(top)
                if ch_list[j][j] != corner:
                    is_same = False
            if is_same:
                return corner
'''


'''
        if ch[0] == ch[1] == ch[2] == "X" or ch[4] == ch[5] == ch[6] == "X" or ch[8] == ch[9] == ch[10] == "X" or ch[0] == ch[4] == ch[8] == "X" or ch[1] == ch[5] == ch[9] == "X" or ch[2] == ch[6] == ch[10] == "X" or ch[0] == ch[5] == ch[10] == "X" or ch[2] == ch[5] == ch[8]:
            return "X"
        elif ch[0] == ch[1] == ch[2] == "O" or ch[4] == ch[5] == ch[6] == "O" or ch[8] == ch[9] == ch[10] == "O" or ch[0] == ch[4] == ch[8] == "O" or ch[1] == ch[5] == ch[9] == "O" or ch[2] == ch[6] == ch[10] == "O" or ch[0] == ch[5] == ch[10] == "O" or ch[2] == ch[5] == ch[8]:
            return "O"
        else:
            return "Draw"

'''

print(tic_tac_result(source_file))