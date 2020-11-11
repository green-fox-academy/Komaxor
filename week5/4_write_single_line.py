# Write a function that is able to manipulate a file
# By writing your name into it as a single line
# The file should be named "my-file.txt"
# In case the program is unable to write the file,
# It should print the following error message: "Unable to write file: my-file.txt"
import os

myfile = 'week5/myrenamedfile.txt'

def add_name(myfile):
    try:
        with open(myfile, 'a') as file:
            file.write("\nMark Ambrus")
            os.rename(r'week5/myrenamedfile',r'week5/myrenamedfile.txt')
    except NameError:
        return 1
    except FileNotFoundError:
        return 2
    except IOError: #error valtozo
        return str("Unable to write file: " + myfile)

add_name(myfile)