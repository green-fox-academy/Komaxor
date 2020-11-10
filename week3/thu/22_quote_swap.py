# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.
# Create a function called quote_swap()

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]

def quote_swap(words): #kiirni
    do = words.index("do")
    cannot = words.index("cannot")
    words[do] = "cannot"
    words[cannot] = "do"
    return words

print(quote_swap(words))
# Expected output: "What I cannot create I do not understand."