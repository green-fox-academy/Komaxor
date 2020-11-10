# Write function that joins the two lists by matching one girl with one boy in a new list
# If someone has no pair, he/she should be the element of the list too
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

girls = ["Eve", "Ashley", "Claire", "Kat", "Jane"]
boys = ["Joe", "Fred", "Tom", "Todd", "Neef", "Jeff"]

def making_matches(girls, boys): #kiirni
    res = []
    for i in range(0, len(girls) + len(boys)):
        if i < len(girls):
            res.append(girls[i])
        if i < len(boys):
            res.append(boys[i])
    return res

print(making_matches(girls, boys))