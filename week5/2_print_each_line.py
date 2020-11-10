#Write a program that opens a file called "my-file.txt", then prints
# each line from the file.
# If the program is unable to read the file (for example it does not exist),
# then it should print the following error message: "Unable to read file: my-file.txt"
import os

file = open('my-file.txt', 'r') #TODO does not file file

while True:
    try:
        print(file.readlines())
    except FileNotFoundError: #TODO does not work porbably same reason as previous
        print("Unable to read file: ", file)