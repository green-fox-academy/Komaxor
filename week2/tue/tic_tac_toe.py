import sys

#coordinates
x = 0
y = 0

#availability
available = True
p1 = True
p2 = True
p3 = True
p4 = True
p5 = True
p6 = True
p7 = True
p8 = True
p9 = True

#places filled
if p1 and p2 and p3 and p4 and p5 and p6 and p7 and p8 and p9:
    available = False

empty_row = "     |     |    "

# draws empty map
for i in range (0, 9):
    if i == 2 or i == 5:
        print("_____|_____|_____")
    else:
        print(empty_row)

# first player input
while True:
    try:
        x = int(input("Which column do you want to place your figure: 1, 2 or 3? "))
    except ValueError:
        print("That is definitely not 1, 2 or 3!")
        continue
    if x > 3:
        print("1, 2 or 3?")
        continue
    if available is False:
        sys.exit("No more places! It is a tie!")
    else:
        break

if x == 1:
    print("Great!")
    x = 3
elif x == 2:
    print("Awesome!")
    x = 9
elif x == 3:
    print("Cool!")
    x = 15

while True:
    try:
        y = int(input("Which row do you want to place your figure: 1, 2 or 3? "))
    except ValueError:
        print("That is definitely not 1, 2 or 3!")
        continue
    if y > 3:
        print("1, 2 or 3?")
        continue
    else:
        break

if y == 1:
    print("Excellent!")
    y = 2
elif y == 2:
    print("You rock!")
    y = 5
elif y == 3:
    print("Superb!")
    y = 8


#control
print(x)
print(y)

empty_row = empty_row[:x - 1] + "X" + empty_row[x:]
#empty_row = empty_row[:x - 1] + "O" + empty_row[x:]

# draws map with 1 mark
for i in range (0, 9):
    if i == 2 or i == 5:
        print("_____|_____|_____")
    elif i + 1 == y:
        print(empty_row)
    else:
        print("     |     |    ")

