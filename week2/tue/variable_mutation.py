a = 3
a += 10

print(a)

b = 100
b -= 7

print(b)

c = 44
c *= c

print(c)

d = 125
d /= 5

print(d)

e = 8
e *= e*e

print(e)

f1 = 123
f2 = 345

print(f1>f2)

h = 1357988018575474

yes = 1357988018575474 % 11
if yes == 0:
    print("yes")
else:
    print("no")

i1 = 10
i2 = 3

first = 10>3**2
second = 10<3**3

if first == second == True:
    print("Yes")

j = 1521

c_one = j % 5
c_two = j % 3
if c_one or c_two == 0:
    print("yes")