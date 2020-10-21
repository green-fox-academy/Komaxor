height = int(input("Enter a positive number! "))

for i in range (0 , height):
    if i == 0 or i == height - 1:
        print(height * "%")
    else:
        print("%" + (i - 1) * " " + "%" + (height - 2 - i) * " " + "%")

'''for i in range(0, height):
  for j in range(0, height):
    if i == 0 or j == 0 or i == j:
      print('%')'''