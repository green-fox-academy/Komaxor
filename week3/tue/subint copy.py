num = 5
num_list = [1234, 2345, 45, 76, 98, 41, 52, 63, 79, 86, 50, 4028]

def subint(x, y):
    res = []
    for number in y:
        for character in str(number):
            if character == str(x):
                res.append(str(number))
    return res

print(subint(num, num_list))