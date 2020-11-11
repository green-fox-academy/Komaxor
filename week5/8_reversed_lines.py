# Create a method that decrypts reversed-lines.txt
reversed_file = 'week5/reversed_lines.txt'

def decrypt(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line[::-1])

decrypt(reversed_file)

#TODO why double linebreaks?