orders = ["first", "second", "third"]
a = orders.index("first")
b = orders.index("third")

orders[a], orders[b] = orders[b], orders[a]

print(orders)