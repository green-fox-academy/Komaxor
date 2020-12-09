from random import randrange
from area import Area
from hero import Hero
from skeleton import Skeleton
from boss import Boss

def create_characters():
    characters = []
    hero = Hero()
    boss = Boss()
    skeletons = []
    keyholder = randrange(2, 5)
    for i in range(keyholder):
        if i == keyholder:
            skeletons[i].has_key == True
        skeletons.append(Skeleton())
    characters.append(hero)
    characters.append(boss)
    for i in range(0, len(skeletons)):
        characters.append(skeletons[i])
    return characters

def get_stats(characters):
    for i in range(0, len(characters)):
        print(characters[i].__class__.__name__ + " (Level " + str(characters[i].level) + ") HP: " +
              str(characters[i].current_health) + "/" + str(characters[i].max_health) +
              " | DP: " + str(characters[i].def_point) + " | SP: " + str(characters[i].strike_point))

def start_area():
    area = Area()
    tiles = area.create_walls()
    characters = create_characters()

def start_turn():
    pass

def end_turn():
    pass

def end_area():
    pass