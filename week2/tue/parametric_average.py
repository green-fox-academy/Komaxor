number = int(input("Enter a positive number! "))
d = {}
for i in range (0, number):
    d["string{0}".format(i)] = int(input("Enter a number! "))

total = sum(d.values())
avg = total/number

print("Sum: " + str(total) + ", Average: " + str(avg))
