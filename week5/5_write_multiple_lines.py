# Create a function that takes 3 parameters: a path, a word and a number
# and is able to write into a file.
# The path parameter should be a string that describes the location of the file you wish to modify
# The word parameter should also be a string that will be written to the file as individual lines
# The number parameter should describe how many lines the file should have.
# If the word is "apple" and the number is 5, it should write 5 lines
# into the file and each line should read "apple"
# The function should not raise any errors if it could not write the file.

myfile = 'week5/myrenamedfile.txt'
word = "hello"
number = 3

def add_words(myfile, word, num):
    try:
        with open(myfile, 'a') as file:
            for _ in range(num):
                file.write("\n" + word)
    except NameError:
        return 1
    except FileNotFoundError:
        return 2
    except IOError:
        return 3

add_words(myfile, word, number)