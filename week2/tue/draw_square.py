height = int(input("Enter a positive number! "))

for i in range (0 , height):
    if i == 0 or i == height - 1:
        print(6 * "%")
    else:
        print("%" + 4 * " " + "%")