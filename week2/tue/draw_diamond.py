size = int(input("Enter a positive number! "))
max = size // 2

for i in range (0 , size):
    if i < max:
        if size % 2 == 0:
            print((max - i - 1) * " " + i * "**" + "*")
        else:
            print((max - i) * " " + i * "**" + "*")
    else:
        print((i - max) * " " + (size - i - 1) * "**" + "*")

'''
this also worked bud was not nice
for i in range (0 , size):
    while i < size / 2:
        print((size // 2 - i) * " " + i * "**" + "*")
        break
    while i >= size / 2:
        if size % 2 == 0:
            print((i - size // 2) * " " + (size - i) * "**" + "*")
        else:
            print(((i - size // 2) - 1) * " " + (size - i) * "**" + "*")
        break
print(size // 2 * " " + "*")
'''