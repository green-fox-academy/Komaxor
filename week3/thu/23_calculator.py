
# Create a simple calculator application which does read the parameters from the prompt
# and prints the result to the prompt.

# It should support the following operations, create a function called calculate():
# +, -, *, /, % and it should support two operands.
# The format of the expressions must be: {operation} {operand} {operand}.
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

def user_input():
    while True:
        x = input("Please type in the expression: ")
        words = x.split()
        if len(words) != 3:
            print("You must enter the operation first then the two operands")
            continue
        if words[0] not in ["+", "-", "*", "/", "%"]:
            print("The first word shuld be your operation sign")
            continue
        if not words[1].isdigit():
            print(words[1])
            print("The second word shuld be a number")
            continue
        if not words[2].isdigit():
            print("The third word shuld be a number")
            continue
        else:
            return words

def calculate():
    words = user_input()
    num1 = int(words[1])
    num2 = int(words[2])
    if words[0] == "+":
        return num1 + num2
    elif words[0] == "-":
        return num1 - num2
    elif words[0] == "*":
        return num1 * num2
    elif words[0] == "/":
        return num1 / num2
    elif words[0] == "%":
        return num1 % num2

print(calculate())