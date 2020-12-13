from random import randrange
from area import Area
from hero import Hero
from skeleton import Skeleton
from boss import Boss

class Game:

    def __init__(self):
        self.hero = Hero()

    def create_characters(self):
        characters = []
        characters.append(self.hero)
        monsters = self.create_monsters()
        for i in range(0, len(monsters)):
            characters.append(monsters[i])
        return characters

    def create_monsters(self):
        monsters = []
        boss = Boss()
        monsters.append(boss)
        skeletons = []
        skeleton_number = randrange(2, 5)
        for i in range(skeleton_number):
            skeletons.append(Skeleton())
        skeletons[0].has_key == True
        for i in range(0, len(skeletons)):
            monsters.append(skeletons[i])
        return monsters

    def get_stats(self, characters):
        for i in range(0, len(characters)):
            print(characters[i].__class__.__name__ + " (Level " + str(characters[i].level) + ") HP: " +
                str(characters[i].current_health) + "/" + str(characters[i].max_health) +
                " | DP: " + str(characters[i].def_point) + " | SP: " + str(characters[i].strike_point))

    def fight(self, characters):
        for i in range(1, len(characters)):
            if characters[0].on_tile == characters[i].on_tile:
                #create loop until one has lower health than 0
                characters[0].fight(characters[i])
                characters[0].check_death()
                characters[i].check_death()

    #def check_square(self):


    def start_area(self):
        area = Area()
        tiles = area.create_walls()
        characters = self.create_characters()

    def start_turn(self):
        pass

    def end_turn(self):
        pass

    def end_area(self):
        pass