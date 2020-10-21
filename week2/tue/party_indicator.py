girls = int(input("How many girls are coming to the party? "))
boys = int(input("How many boys are coming to the party? "))

people = girls + boys

if people > 20 and girls > 0:
    if girls == boys:
        print("The party is excellent!")
    else:
        print("Quite cool party!")
elif girls == 0:
    print("Sausage party!")
else:
    print("Average party!")