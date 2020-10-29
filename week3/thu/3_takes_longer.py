'''# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

print(quote)'''

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
new = quote[:21] + 'always takes longer than ' + quote[21:]

print(new)