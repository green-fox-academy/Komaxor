from random import randint

def guessing_game():
    secret = 102
    guess = 103
    biggest = 101
    smallest = -1
    while guess != secret:
        g = input("Mark: What is your guess?\nYou: My guess is ")
        guess = int(g)
        if biggest > guess and smallest < guess:
            if biggest - smallest == 2:
                secret = smallest + 1
            if guess - smallest < biggest - guess:
                smallest = guess
                print("Mark: Try bigger!")
            elif guess - smallest > biggest - guess:
                biggest = guess
                print("Mark: Try smaller!")
            else:
                choice = randint(0,1)
                if choice == 1:
                    biggest = guess
                    if secret > 100:
                        print("Mark: Try smaller!")
                else:
                    smallest = guess
                    if secret > 100:
                        print("Mark: Try bigger!")
        else:
            print("Mark: What? I try to help and... Ah! You are hopeless...")
    print("Mark: You finally got it... Huh. WOW! You are as fast as walk of snails!")

print("Mark: Welcome to my guessing game! Guess the correct number between 0 and 100 to win!")
smallest = 0
biggest = 100
restart = True
while restart:
    guessing_game()
    ans = input("Mark: Can you beat me faster (yes/no)?\nYou:")
    if not ans.lower().startswith("y"):
        restart = False
    if restart:
        print("Mark: Looks like it wasn't enough... Here we go again!")
input("Mark: I knew you are week. Hit enter and run to Mommy!\n")