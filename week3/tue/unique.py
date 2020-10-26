num_list = [10, 30, 20, 30, 20, 40, 40]

def unique(x):
    x.sort()
    for i in range (1, len(x)):
        if i > len(x):
            break
        if x[i] == x[i - 1]:
            x.remove(x[i - 1])
    return x
            

print(unique(num_list))