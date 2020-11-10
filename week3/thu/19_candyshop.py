shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list.
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)
# Create a function called sweets() which takes the list as a parameter.
def sweets(items):
    items[items.index(2)] = "Croissant"
    items[items.index(False)] = "Ice cream"
    return items

print(sweets(shop_items))
# Expected output: "Cupcake", "Croissant", "Brownie", "Ice cream"