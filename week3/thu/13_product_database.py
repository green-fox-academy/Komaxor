'''
We are going to represent our products in a map where the keys are strings representing the product's name and the values are numbers representing the product's price.

Create a map with the following key-value pairs.

Product name (key)	Price (value)
Eggs	200
Milk	200
Fish	400
Apples	150
Bread	50
Chicken	550
Create an application which solves the following problems.

How much is the fish?
What is the most expensive product?
What is the average price?
How many products' price is below 300?
Is there anything we can buy for exactly 125?
What is the cheapest product?
'''
products = {"eggs": 200, "milk": 200, "fish": 400, "apples": 150, "bread": 50, "checken": 550}

def forshop():
    fish_price = products["fish"]
    print(fish_price)
    avg_price = round((sum(products.values()) / len(products)), 2)
    print(avg_price)
    cheap = []
    for v in products.values():
        if v < 300:
            cheap.append(v)
    print(len(cheap))
    is_125 = "No"
    for v in products.values():
        if v == 125:
            is_125 = "Yes"
    print(is_125)
    cheapest = products.keys()[products.values()[min(products.values())]]
    print(cheapest)

forshop()