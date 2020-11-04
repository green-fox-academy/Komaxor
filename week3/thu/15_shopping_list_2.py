'''
Represent the following products with their prices

Product	Amount
Milk	1.07
Rice	1.59
Eggs	3.14
Cheese	12.60
Chicken Breasts	9.40
Apples	2.31
Tomato	2.58
Potato	1.75
Onion	1.10
Represent Bob's shopping list

Product	Amount
Milk	3
Rice	2
Eggs	2
Cheese	1
Chicken Breasts	4
Apples	1
Tomato	2
Potato	1
Represent Alice's shopping list

Product	Amount
Rice	1
Eggs	5
Chicken Breasts	2
Apples	1
Tomato	10
Create an application which solves the following problems.

How much does Bob pay?
How much does Alice pay?
Who buys more Rice?
Who buys more Potato?
Who buys more different products?
Who buys more products? (piece)
'''
prices = {"milk": 1.07, "rice": 1.59, "eggs": 3.14, "cheese": 12.60, "chicken breasts": 9.40, "apples": 2.31, "tomato": 2.58, "potato": 1.75, "onion": 1.10, }
alice_sl = {"rice": 1, "eggs": 5, "chicken breasts": 2, "apples": 1, "tomato": 10}
bob_sl = {"milk": 3, "rice": 2, "eggs": 2, "cheese": 1, "chicken breasts": 4, "apples": 1, "tomato": 2, "potato": 1}

def buyers():
    alice_pays = 0
    for k, v in prices.items():
        for k2, v2 in alice_sl.items():
            if k == k2:
                alice_pays = alice_pays + (v * v2)
    print(alice_pays)
    bob_pays = 0
    for k, v in prices.items():
        for k2, v2 in bob_sl.items():
            if k == k2:
                bob_pays = bob_pays + (v * v2)
    print(bob_pays)

    if alice_sl["rice"] > bob_sl["rice"]:
        print("Alice buys more rice")
    elif alice_sl["rice"] == bob_sl["rice"]:
        print("They buy the same amount")
    else:
        print("Bob buys more rice")

    if alice_sl.get("potato", 0) > bob_sl.get("potato", 0):
        print("Alice buys more potato")
    elif alice_sl.get("potato", 0) == bob_sl.get("potato", 0):
        print("They buy the same amount")
    else:
        print("Bob buys more potato")

    if len(alice_sl) > len(bob_sl):
        print("Alice buys more different products")
    elif len(alice_sl) == len(bob_sl):
        print("They buy the same different products")
    else:
        print("Bob buys more different products")

    if sum(alice_sl.values()) > sum(bob_sl.values()):
        print("Alice buys more products")
    elif sum(alice_sl.values()) == sum(bob_sl.values()):
        print("They buy the same amount of products")
    else:
        print("Bob buys more products")

buyers ()