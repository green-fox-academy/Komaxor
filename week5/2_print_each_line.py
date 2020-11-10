#Write a program that opens a file called "my-file.txt", then prints
# each line from the file.
# If the program is unable to read the file (for example it does not exist),
# then it should print the following error message: "Unable to read file: my-file.txt"
file = open('myfile.txt', 'r') #TODO does not find file
print(file.read())

while True:
    try:
        print(file.readlines())
        break
    except FileNotFoundError: #TODO does not work
        print("Unable to read file: ", file)