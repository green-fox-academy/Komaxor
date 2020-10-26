nums = [1312, 231, 21, 12, 535]
desc = True

def sort(x, bool):
    if bool:
        x.sort()
        x = x[::-1]
    else:
        x.sort()
    return x

print(sort(nums, desc))