a = 24
out = 0

if (a % 2) == 0:
    out += 1

print(out)

b = 13
out2 = ""

if b < 10:
    out2 = "Less!"
elif b > 20:
    out2 = "More!"
else:
    out2 = "Sweet!"

print(out2)

c = 123
credits = 100
is_bonus = False

if credits >= 50 and not is_bonus: #not = is False
    c -= 2
elif credits < 50 and not is_bonus:
    c -=1

print(c)

d = 8
time = 120
out3 = ""

if (d % 4) == 0 and time <= 200:
    out3 = "check"
elif time > 200:
    out3 = "Time out"
else:
    out3 = "Run Forest Run"

print(out3)