def number_input():
    while True:
        try:
            num = int(input("Enter a number! "))
        except ValueError:
            print("That is definitely not a number.")
            continue
        else:
            return num

def kill():
    #creates list
    pos = []
    num = number_input() + 1
    for i in range(1, num):
        pos.append(i)
    #removes every second until 1 remains
    while len(pos) != 1:
        for i in range(0, (len(pos) - 1)):
            if i == len(pos) - 1:
                pos.remove(pos[0])
                break
            elif i < len(pos):
                pos.remove(pos[i + 1])
    print(pos)
kill()