#Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]

def table_printer():
    #length of first column
    char = 12
    chars = []
    for item in ingredients:
        length = len(item['name'])
        chars.append(length)
        if max(chars) > 10:
            char = max(chars)

#print table
    print("+" + char * "-" + "--" + "+" + 15 * "-" + "+" + 10 * "-" + "+")
    print("| Ingredient "  + (char - 10) * " " + "| Needs cooling | In stock |")
    print("+" + char * "-" + "--" + "+" + 15 * "-" + "+" + 10 * "-" + "+")
    for item in ingredients:
        if item['needs_cooling']:
            cooling = "Yes"
        else:
            cooling = "No"
        if item['in_stock'] == 0:
            stock = "-"
        else:
            stock = str(item['in_stock'])
        print("| " + item['name'] + (char - len(item['name'])) * " " + " | " + cooling + (15 - len(cooling) - 1) * " " + "| " + stock + (10 - len(stock) - 1) * " " + "|")
    print("+" + char * "-" + "--" + "+" + 15 * "-" + "+" + 10 * "-" + "+")

table_printer()