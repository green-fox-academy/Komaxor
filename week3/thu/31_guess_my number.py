#Write a program where the program chooses a number between 1 and 100.
#The player is then asked to enter a guess.
#If the player guesses wrong, then the program gives feedback and ask to enter an other guess until the guess is correct.

#Make the range customizable (ask for it before starting the guessing).
#You can add lives.
#I've the number between 1-100. You have 5 lives.
#> 20
#Too high. You have 4 lives left.
#> 10
#Too low. You have 3 lives left.
#> 15
#Congratulations. You won!

import random

def highest():
    while True:
        try:
            num = int(input("I want the range between 1 and "))
        except ValueError:
            print("That is definitely not a number.")
            continue
        if num < 2:
            print("The highest number must be at least 2!")
        else:
            print("Mark: Guess the correct number between 0 and " + str(num) + " to win!")
            secret = random.randrange(1, num)
            return secret

def guessing_game(life):
    secret = highest()
    guess = -1
    while guess != secret:
        if life == 0:
            print("Mark: You are out of lives! You lost.\nThe correct number was " + str(secret) + ".")
            break
        while True:
            try:
                guess = int(input("Mark: What is your guess?\nMe: My guess is "))
            except ValueError:
                print("That is definitely not a number.")
                continue
            if guess < 0:
                print("The guess must be a positive number!")
            else:
                break
        if guess < secret:
            life -= 1
            print("Mark: Try bigger! You have " + str(life) + " lives left")
        elif guess > secret:
            life -= 1
            print("Mark: Try smaller! You have " + str(life) + " lives left")
        else:
            print("Mark: You won!")

print("Mark: Welcome to my guessing game!")
restart = True
while restart:
    while True:
        try:
            life = int(input("How many lives do you want?\nMe: "))
        except ValueError:
            print("That is definitely not a number.")
            continue
        if life < 1:
            print("You must have at least 1 life!")
        else:
            break
    guessing_game(life)
    ans = input("Mark: Can you beat me faster (yes/no)?\nMe: ")
    if not ans.lower().startswith("y"):
        restart = False
    if restart:
        print("Mark: Looks like it wasn't enough... Here we go again!")
input("Mark: I knew you are week. Hit enter and run to Mommy!\n")