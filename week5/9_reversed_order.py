# Create a method that decrypts reversed-order.txt
reversed_file = 'week5/reversed_order.txt'

def decrypt(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in reversed(lines):
            print(line, end="")

decrypt(reversed_file)