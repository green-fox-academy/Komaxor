height = int(input("Enter a positive number! "))

for i in range (0 , height):
    if i == 0 or i == height - 1:
        print(height * "%")
    else:
        print("%" + (height - 2) * " " + "%")