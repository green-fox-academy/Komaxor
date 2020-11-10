# Create a function that takes a number,
# divides ten with it,
# and prints the result.
# It should print "fail" if the parameter is 0
def divider():
    while True:
        try:
            num = int(input("Enter a number! "))
            res = 10 / num
            return res
        except ValueError:
            print("You must enter a number")
            continue
        except ZeroDivisionError:
            print("fail if the parameter is 0")

res = divider()
print(res)