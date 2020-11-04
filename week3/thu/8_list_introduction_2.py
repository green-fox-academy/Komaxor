'''
Create a list ('List A') which contains the following values
Apple, Avocado, Blueberries, Durian, Lychee
Create a new list ('List B') with the values of List A
Print out whether List A contains Durian or not
Remove Durian from List B
Add Kiwifruit to List A after the 4th element
Compare the size of List A and List B
Get the index of Avocado from List A
Get the index of Durian from List B
Add Passion Fruit and Pomelo to List B in a single statement
Print out the 3rd element from List A
'''

list_A = ['Apple', 'Avocado', 'Blueberries', 'Durian', 'Lychee']
list_B = list_A[::]

if "Durian" in list_A:
    print("Yes")
else:
    print("No")

list_B.remove("Durian")

list_A.insert(3, "Kiwifruit")

if len(list_A) > len(list_B):
    print("A is longer")
elif len(list_B) > len(list_A):
    print("B is longer")
else:
    print("They are equally long")

print(list_A.index("Avocado"))

if "Durian" in list_B:
    print(list_B.index("Durian"))
else: print("Nope")

list_B.extend(("Passion Fruit", "Pomelo"))

print(list_A[2])

print(list_A, list_B)