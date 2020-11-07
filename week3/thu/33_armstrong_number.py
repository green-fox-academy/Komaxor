def number_input():
    while True:
        try:
            num = int(input("Enter a number! "))
        except ValueError:
            print("That is definitely not a number.")
            continue
        else:
            return num

def calculate():
    num = number_input()
    digits = [int(d) for d in str(num)]
    length = len(digits)
    powered_digits = []
    for d in digits:
        powered_d = d ** length
        powered_digits.append(powered_d)
    if sum(powered_digits) == num:
        print(str(num) + " is an Armstrong number")
    else:
        print(str(num) + " is not an Armstrong number")

calculate()