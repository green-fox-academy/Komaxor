number = 8
user_input = 0
while user_input != number:
    user_input = int(input("Guess a number! "))
    if user_input == number:
        print("You found the number: " + str(number))
    elif user_input > number:
        print("The stored number is smaller")
    else:
        print("The stored number is bigger")