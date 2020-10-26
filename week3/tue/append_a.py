animals = ["koal", "pand", "zebr"]
def append_a(x):
    x = [item + "a" for item in x]
    return x
print(append_a(animals))