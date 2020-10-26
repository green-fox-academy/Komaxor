num = 5
num_list = [1234, 2345, 45, 76, 98, 41, 52, 63, 79, 86, 50, 4028]

def subint(x, y):
    res = []
    for i in range (0, len(y)):
        z = str(y[i])
        for j in range (0, len(z)):
            a = z[0]
            if a == str(x):
                res.append(str(y[i]))
            z = z[1:]
    return res


print(subint(num, num_list))