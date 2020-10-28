text = input(str("Enter text: " ))
def palindrome_builder(x):
    for i in range (2, len(x)):
        res = x[:(len(x) - i + 2)]
        print_palindrome(res)
        for j in range (3, len(res)):
            res = res[1:]
            print_palindrome(res)

def print_palindrome(fin):
    if fin == fin[::-1]:
        print(fin)

palindrome_builder(text)