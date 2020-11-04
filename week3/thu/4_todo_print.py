'''# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected output:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

todoText = " - Buy milk\n"

print(todoText)'''

todoText = "\t- Buy milk\n"
tt2 = todoText + "\t- Download games"
tt3 = "My todo:\n" + tt2[0:]
tt4 = tt3 + "\n\t\t- Diablo"
print(tt4)