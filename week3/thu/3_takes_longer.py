'''# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

print(quote)'''

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
index =  quote.find("you")
print(index)
new = quote[:index] + 'always takes longer than ' + quote[index:]
print(new)