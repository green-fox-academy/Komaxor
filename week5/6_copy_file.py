# Write a function that copies the contents of a file into another
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful
origin_file = 'week5/myrenamedfile.txt'
new_file = 'week5/newfile.txt'

def copy_file(origin, new):
    try:
        with open(origin, 'r') as file:
            content = file.read()
        with open(new, 'w') as file:
            file.write(content)
    except NameError:
        return 1
    except FileNotFoundError:
        return 2
    except IOError:
        return str("Unable to read file")

copy_file(origin_file, new_file)