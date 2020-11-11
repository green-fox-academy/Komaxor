# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

myfile = 'week5/myfile.txt'

def line_counter(myfile):
    try:
        file = open(myfile, 'r')
        num_lines = len(file.readlines())
        return num_lines
    except NameError:
        return 0
    except FileNotFoundError:
        return 0
    except IOError:
        return 0

print(line_counter(myfile))