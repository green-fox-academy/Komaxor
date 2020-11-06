shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list.
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)
# Create a function called sweets() which takes the list as a parameter.
def sweets(items):
    _2 = items.index(2)
    _False = items.index(False)
    items[_2] = "Croissant"
    items[_False] = "Ice cream"
    return items

print(sweets(shop_items))
# Expected output: "Cupcake", "Croissant", "Brownie", "Ice cream"