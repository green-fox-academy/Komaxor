x = input("Enter sth: " )

def palindrome_builder(x):
    x = x + x[::-1]
    print(x)

palindrome_builder(x)