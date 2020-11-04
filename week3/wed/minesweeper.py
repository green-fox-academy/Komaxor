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
        print(size * "▢")

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
        x = random.choice(fields)
        if x not in bomb_list:
            bomb_list.append(x)
    return sorted(bomb_list)

def draw_bombs(b, s, v, n):
    for i in range (0, (s * s)):
        if i in v:
            if i in b:
                print("M", end="")
            else:
                print(n[i], end="")
        else:
            print("▢", end="")
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

def count_neighbour_bombs(size, b):
    all_neighbours = []
    for i in range (0, (size * size)):
        neighbours = []
        if i == 0:
            if (i + 1) in b:
                neighbours.append(i)
            if (i + size + 1) in b:
                neighbours.append(i)
            if (i + size) in b:
                neighbours.append(i)
        elif i == size - 1:
            if (i - 1) in b:
                neighbours.append(i)
            if (i + size - 1) in b:
                neighbours.append(i)
            if (i + size) in b:
                neighbours.append(i)
        elif i == ((size - 1) * size):
            if (i + 1) in b:
                neighbours.append(i)
            if (i - size + 1) in b:
                neighbours.append(i)
            if (i - size) in b:
                neighbours.append(i)
        elif i == ((size * size) - 1):
            if (i - 1) in b:
                neighbours.append(i)
            if (i - size - 1) in b:
                neighbours.append(i)
            if (i - size) in b:
                neighbours.append(i)
        elif 0 < i < (size - 1):
            if (i - 1) in b:
                neighbours.append(i)
            if (i + 1) in b:
                neighbours.append(i)
            if (i + size - 1) in b:
                neighbours.append(i)
            if (i + size) in b:
                neighbours.append(i)
            if (i + size + 1) in b:
                neighbours.append(i)
        elif (size * size) > i > (size * (size - 1)):
            if (i - size - 1) in b:
                neighbours.append(i)
            if (i - size) in b:
                neighbours.append(i)
            if (i - size + 1) in b:
                neighbours.append(i)
            if (i - 1) in b:
                neighbours.append(i)
            if (i + 1) in b:
                neighbours.append(i)
        elif (i + 1) % size == 0:
            if (i - size) in b:
                neighbours.append(i)
            if (i - size - 1) in b:
                neighbours.append(i)
            if (i - 1) in b:
                neighbours.append(i)
            if (i + size) in b:
                neighbours.append(i)
            if (i + size - 1) in b:
                neighbours.append(i)
        elif i % size == 0:
            if (i - size + 1) in b:
                neighbours.append(i)
            if (i - size) in b:
                neighbours.append(i)
            if (i + 1) in b:
                neighbours.append(i)
            if (i + size + 1) in b:
                neighbours.append(i)
            if (i + size) in b:
                neighbours.append(i)
        else:
            if (i - size - 1) in b:
                neighbours.append(i)
            if (i - size) in b:
                neighbours.append(i)
            if (i - size + 1) in b:
                neighbours.append(i)
            if (i - 1) in b:
                neighbours.append(i)
            if (i + 1) in b:
                neighbours.append(i)
            if (i + size - 1) in b:
                neighbours.append(i)
            if (i + size) in b:
                neighbours.append(i)
            if (i + size + 1) in b:
                neighbours.append(i)
        all_neighbours.append(len(neighbours))
    #print(b)
    return all_neighbours

def move(s, b, v, n):
    x = x_input(s)
    y = y_input(s)
    place = ((x - 1) * s + y) - 1
    if place not in v:
        v.append(place)
    draw_bombs(b, s, v, n)
    #print(v)
    if place in b:
        print("You died!")
        return False
    return True

while True:
    gameon = True
    print("Mark: Welcome to the Minesweeper game! Let's play!")
    size = map_size()
    bombs = get_bombs(size)
    visible = []
    n = count_neighbour_bombs(size, bombs)
    draw_map(size)
    while gameon:
        gameon = move(size, bombs, visible, n)
        if len(visible) == (size * size) - len(bombs):
            print("Congratulations! You won!")
            gameon = False
    restart = str(input("Play again? "))
    if restart.lower().startswith("y"):
        continue
    else:
        print("Bye")
        break