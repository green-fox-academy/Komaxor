# Create a method that decrypts the duplicated-chars.txt
file_name = 'week5/thezenofpython.txt'

def decrypt(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        newcontent = ""
        print(content)
        for i in range(0, len(content)):
            if i % 2 != 0:
                newcontent = newcontent + content[i]
        print(newcontent)

decrypt(file_name)

# TODO first linebreak missing