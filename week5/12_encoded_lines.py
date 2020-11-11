# Create a method that decrypts encoded-lines.txt
encoded_file = 'week5/encoded-lines.txt'

def decrypt(file_name):
    cipherText = ""
    with open(file_name, 'r') as file:
        content = file.read()
        for ch in content:
            if ch.isalpha:
                new_ch = ord(ch) - 1
                current_ch = chr(new_ch)
                cipherText += current_ch
        print(cipherText)

decrypt(encoded_file)

