girls = int(input("How many girls are coming to the party? "))
boys = int(input("How many boys are coming to the party? "))

people = girls + boys

if girls == boys and people >= 20: #because 10g and 10b would result in no print
    print("The party is excellent!")
elif girls != boys and people > 20:
    print("Quite cool party!")
elif people < 20:
    print("Average party!")
if girls == 0:
    print("Sausage party!")