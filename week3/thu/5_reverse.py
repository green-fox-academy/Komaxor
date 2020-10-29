'''# Create a function called 'reverse' which takes a string as a parameter
# The function reverses it and returns with the reversed string


toBeReversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"
print(reverse(toBeReversed))'''

x = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"

def reverse(s):
    ns = s[::-1]
    return ns

print(reverse(x))