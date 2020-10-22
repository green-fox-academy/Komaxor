p1 = " "
p2 = " "
p3 = " "
p4 = " "
p5 = " "
p6 = " "
p7 = " "
p8 = " "
p9 = " "
mark = " "

# draws map
def draw_map(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    for i in range (0, 9):
        if i == 1:
            print("  " + p1 + "  |  " + p2 + "  |  " + p3 + "  ")
        elif i == 4:
            print("  " + p4 + "  |  " + p5 + "  |  " + p6 + "  ")
        elif i == 7:
            print("  " + p7 + "  |  " + p8 + "  |  " + p9 + "  ")
        elif i == 2 or i == 5:
            print("_____|_____|_____")
        else:
            print("     |     |    ")

#player input
def x_input(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    while True:
        try:
            x = int(input("Which row do you want to place your figure: 1, 2 or 3? "))
        except ValueError:
            print("That is definitely not 1, 2 or 3!")
            continue
        if x > 3:
            print("1, 2 or 3?")
            continue
        else:
            return x
def x_validate():
    x = x_input(p1, p2, p3, p4, p5, p6, p7, p8, p9)
    if x == 1:
        print("Great!")
        x = 3
    elif x == 2:
        print("Awesome!")
        x = 9
    elif x == 3:
        print("Cool!")
        x = 15
    return x
def y_input(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    while True:
        try:
            y = int(input("Which column do you want to place your figure: 1, 2 or 3? "))
        except ValueError:
            print("That is definitely not 1, 2 or 3!")
            continue
        if y > 3:
            print("1, 2 or 3?")
            continue
        else:
            return y
def y_validate():
    y = y_input(p1, p2, p3, p4, p5, p6, p7, p8, p9)
    if y == 1:
        print("Excellent!")
        y = 2
    elif y == 2:
        print("You rock!")
        y = 5
    elif y == 3:
        print("Superb!")
        y = 8
    return y

#switch players
def change_turn(player1_turn):
    player1_turn = not player1_turn
    return player1_turn
def change_mark(player1_turn):
    if player1_turn:
        mark = "X"
    else:
        mark = "O"
    return mark

#place mark
def place_mark(p1, p2, p3, p4, p5, p6, p7, p8, p9, mark):
    mark = change_mark(player1_turn)
    while True:
        x = x_validate()
        y = y_validate()
        if x == 3 and y == 2:
            if p1 != " ":
                print("That is already taken! Try again!")
                continue
            else:
                p1 = mark
                break
        elif x == 3 and y == 5:
            if p2 != " ":
                print("That is already taken! Try again!")
                continue
            else:
                p2 = mark
                break
        elif x == 3 and y == 8:
            if p3 != " ":
                print("That is already taken! Try again!")
                continue
            else:
                p3 = mark
                break
        elif x == 9 and y == 2:
            if p4 != " ":
                print("That is already taken! Try again!")
                continue
            else:
                p4 = mark
                break
        elif x == 9 and y == 5:
            if p5 != " ":
                print("That is already taken! Try again!")
                continue
            else:
                p5 = mark
                break
        elif x == 9 and y == 8:
            if p6 != " ":
                print("That is already taken! Try again!")
                continue
            else:
                p6 = mark
                break
        elif x == 15 and y == 2:
            if p7 != " ":
                print("That is already taken! Try again!")
                continue
            else:
                p7 = mark
                break
        elif x == 15 and y == 5:
            if p8 != " ":
                print("That is already taken! Try again!")
                continue
            else:
                p8 = mark
                break
        elif x == 15 and y == 8:
            if p9 != " ":
                print("That is already taken! Try again!")
                continue
            else:
                p9 = mark
                break
    return(p1, p2, p3, p4, p5, p6, p7, p8, p9)

#check for win
def win(p1, p2, p3, p4, p5, p6, p7, p8, p9, game_over):
    if p1 == p2 == p3 != " " or p4 == p5 == p6 != " " or p7 == p8 == p9 != " " or p1 == p4 == p7 != " " or p2 == p5 == p8 != " " or p3 == p6 == p9 != " " or p1 == p5 == p9 != " " or p3 == p5 == p7 != " ":
        if player1_turn:
            game_over = True
            print("Player 1 won! YAAAY")
        else:
            game_over = True
            print("Player 2 won! Congratulations!")
    return game_over

#the game
while True:
    print("Mark: Welcome to the Tic-Tac-Toe game! Let's play!")
    player1_turn = True
    game_over = False
    draw_map(p1, p2, p3, p4, p5, p6, p7, p8, p9)
    for i in range (0,9):
        if i % 2 == 0:
            print("Player 1's turn!")
        else:
            print("Player 2's turn!")
        (p1, p2, p3, p4, p5, p6, p7, p8, p9) = place_mark(p1, p2, p3, p4, p5, p6, p7, p8, p9, mark)
        draw_map(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        game_over = win(p1, p2, p3, p4, p5, p6, p7, p8, p9, game_over)
        if game_over == True:
            break
        if i == 8:
            print("No more places! It is a tie!")
            break
        player1_turn = change_turn(player1_turn)
    restart = str(input("Play again? "))
    if restart.lower().startswith("y"):
        p1 = " "
        p2 = " "
        p3 = " "
        p4 = " "
        p5 = " "
        p6 = " "
        p7 = " "
        p8 = " "
        p9 = " "
        mark = " "
        continue
    else:
        print("Bye")
        break
