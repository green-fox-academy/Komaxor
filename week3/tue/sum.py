max = int(input("How much numbers do you want to add together? "))
def sum(max):
    total = 0
    for i in range (1, max + 1):
        total = i + total
    return total

print(sum(max))