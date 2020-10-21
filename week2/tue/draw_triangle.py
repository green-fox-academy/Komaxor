length = int(input("Enter a positive number! "))

for i in range (0, length):
        print((length - i - 1) * " " + i * "**" + "*")