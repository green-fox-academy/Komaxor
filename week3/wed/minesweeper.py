import random

def map_size():
    minimum_board_size = 3
    while True:
        try:
            size = int(input("How big do you want the board? "))
        except ValueError:
            print("Enter a number!")
            continue
        if size < minimum_board_size:
            print("The board must be bigger than " + str(minimum_board_size - 1) + "!")
            continue
        else:
            break
    return size

def draw_map(size):
    for _ in range (0, size):
        print(size * "0")

def num_bombs(size):
    allowed_difficulty = (1,2)
    while True:
        try:
            difficulty = int(input("Enter the difficulty! "))
        except ValueError:
            print("Enter a number!")
            continue
        if difficulty not in allowed_difficulty:
            print("The difficulty must be 1 or 2!")
            continue
        else:
            break
    bombs = round(size * size * difficulty / 10)
    return bombs


def get_bombs(s):
    number_of_bombs = num_bombs(size)
    bomb_list = []
    fields = []
    for i in range (0, (s * s)):
        fields.append(i)
    while len(bomb_list) < number_of_bombs:
        bomb_list.append(random.choice(fields)) #TODO prevent duplicates!
    return sorted(bomb_list)

def draw_bombs(b, s):
    for i in range (0, (s * s)):
        if i in b:
            print("X", end="")
        else:
            print("0", end="")
        if (i + 1) % s == 0:
            print()

def x_input(size):
    while True:
        try:
            x = int(input("Which row do you want to mine? "))
        except ValueError:
            print("Enter a number!")
            continue
        if x > size:
            print("The value must be between 1 and " + str(size))
            continue
        else:
            return x
def y_input(size):
    while True:
        try:
            y = int(input("Which column do you want to mine? "))
        except ValueError:
            print("Enter a number!")
            continue
        if y > size:
            print("The value must be between 1 and " + str(size))
            continue
        else:
            return y

size = map_size()
draw_map(size)
bombs = get_bombs(size)
draw_bombs(bombs, size)