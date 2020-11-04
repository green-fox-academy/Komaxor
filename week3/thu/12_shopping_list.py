'''
We are going to represent a shopping list in a list containing strings.

Create a list with the following items.
Eggs, milk, fish, apples, bread and chicken
Create an application which solves the following problems.
Do we have milk on the list?
Do we have bananas on the list?
'''

shopping = ['eggs', 'milk', 'fish', 'apples', 'bread', 'chicken']

def onlist():
    if "milk" in shopping:
        print("Yes!")
    else:
        print("No")
    if "banans" in shopping:
        print("Yes!")
    else:
        print("No")


onlist()