x = input("Sth pls ")
y = input('sth pls ')

def is_anagram(x, y):
    x = sorted(x)
    y = sorted(y)
    if x == y:
        return True
    else:
        return False

print(is_anagram(x, y))