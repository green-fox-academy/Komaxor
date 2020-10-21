number = int(input("Tell me a number! "))
number2 = int(input("Tell me another number! "))

if number2 <= number:
    print("The second number should be bigger")
else:
    for i in range (number, number2):
        print(i)