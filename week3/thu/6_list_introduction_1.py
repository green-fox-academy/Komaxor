'''We are going to play with lists. Feel free to use the built-in methods where possible.

Create an empty list which will contain names (strings)
Print out the number of elements in the list
Add William to the list
Print out whether the list is empty or not
Add John to the list
Add Amanda to the list
Print out the number of elements in the list
Print out the 3rd element
Iterate through the list and print out each name
William
John
Amanda
Iterate through the list and print
1. William
2. John
3. Amanda
Remove the 2nd element
Iterate through the list in a reversed order and print out each name
Amanda
William
Remove all elements'''

names = []
print(len(names))
names.append('William')
if len(names) == 0:
    print('The list is empty!')
else:
    print("Something's there")
names.append('John')
names.append('Amanda')
print(len(names))
print(names[2])
for item in names:
    print(item)
    print(str(names.index(item)) + ".", item)
names.remove(names[1])
for item in reversed(names):
    print(item)

