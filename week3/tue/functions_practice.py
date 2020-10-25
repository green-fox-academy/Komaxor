def greet_fox():
    print("Hello Green Fox!")

greet_fox()
greet_fox()

def greet_by_name(name):
    print("Well hi there,", name)

greet_by_name("Tojas")
greet_by_name("Barbi")

def greet(greet="Hi", name="pal"):
    print(greet, name)

greet("Hello", "Tojas")
greet("Howdy", "Barbi")
greet("Hey")
greet(name="Everyone")

def make_green(name):
    new_name = "Green " + name
    return new_name

name = make_green("Tojas")
greet_by_name(name)