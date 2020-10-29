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
        print(size * "O")

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

def draw_bombs(b, s):
    num = count_neighbour_bombs(s, b)
    for i in range (0, (s * s)):
        if i in b:
            print("M", end="")
        else:
            print(num[i], end="")
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
    for i in range (0, (size * size)):
        neighbours = []
        all_neighbours = []
        if i == 0:
            if (i + 1) in b:
                neighbours.append(i)
            if (i + size + 1) in b:
                neighbours.append(i)
            if (i + size) in b:
                neighbours.append(i)        
        elif i == size:
            if (i - 1) in b:
                neighbours.append(i)
            if (i + size - 1) in b:
                neighbours.append(i)
            if (i + size) in b:
                neighbours.append(i)        
        elif i == (size - 1) * size +1:
            if (i + 1) in b:
                neighbours.append(i)
            if (i - size + 1) in b:
                neighbours.append(i)
            if (i - size) in b:
                neighbours.append(i)        
        elif i == size * size:
            if (i - 1) in b:
                neighbours.append(i)
            if (i - size - 1) in b:
                neighbours.append(i)
            if (i - size) in b:
                neighbours.append(i)        
        elif i % (size + 1) == 0:
            if (i - size) in b:
                neighbours.append(i)  
            if (i - size + 1) in b:
                neighbours.append(i)
            if (i + 1) in b:
                neighbours.append(i)
            if (i + size) in b: 
                neighbours.append(i)
            if (i + size + 1) in b:
                neighbours.append(i)    
        elif i % size == 0:
            if (i - size - 1) in b:
                neighbours.append(i)
            if (i - size) in b:
                neighbours.append(i)  
            if (i - 1) in b:
                neighbours.append(i)
            if (i + size - 1) in b:
                neighbours.append(i) 
            if (i + size) in b: 
                neighbours.append(i)
        elif i < size:
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
        elif i > size * (size - 1):
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
        print(len(neighbours))
        all_neighbours.append(len(neighbours)) #TODO why not size^2 long???
    print(all_neighbours)
    return all_neighbours


def move(s, b):
    x = x_input(s)
    y = y_input(s)
    place = ((x - 1) * s + y) - 1
    if place in b:
        print("You died!")
    else:
        print(place + 1)

#TODO def gameover():

while True:
    print("Mark: Welcome to the Minesweeper game! Let's play!")
    size = map_size()
    draw_map(size)
    bombs = get_bombs(size)
    draw_bombs(bombs, size)
    for i in range (0, (size * size - len(bombs))):
        move(size, bombs)
    restart = str(input("Play again? "))
    if restart.lower().startswith("y"):
        continue
    else:
        print("Bye")
        break