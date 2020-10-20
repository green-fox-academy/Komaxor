number = int(input("Tell me a number! "))
number2 = int(input("Tell me another number! "))

difference = number2-number

if number2 <= number:
    print("The second number should be bigger")
else:
    for i in range (number, (number + difference)):
        print(i)