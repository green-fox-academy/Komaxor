from tree import Tree
from flower import Flower
from garden import Garden

garden = Garden()
purple_tree = Tree('purple')
orange_tree = Tree('orange')
blue_flower = Flower('blue')

garden.add(purple_tree)
garden.add(orange_tree)
garden.add(blue_flower)

#print(garden.get_Status())

print(purple_tree.water_level)
print(purple_tree.needs_water_at)

garden.water(40)

print(purple_tree.water_level)
print(purple_tree.needs_water_at)

garden.water(70)

print(purple_tree.water_level)
print(purple_tree.needs_water_at)
