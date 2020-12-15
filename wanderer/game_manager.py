from random import randrange
from area import CreateArea
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

    def kill(self, character):
        del character

    def check_fight(self, attacker, defender):
        if attacker.on_tile == defender.on_tile:
            self.fight(attacker, defender)

    def fight(self, attacker, defender):
        while attacker.current_health > 0 and defender.current_health > 0:
            attacker.hit(defender)
            attacker.check_death()
            #prevent defender to hit after it died
            defender.hit(attacker)
            defender.check_death()
        if attacker.current_health <= 0:
            self.kill(attacker)
        else:
            self.kill(defender)
        #self.check_next_area(characters)

    def spawn_characters(self, area, hero, monsters):
        self.spawn_hero(area, hero)
        self.spawn_monsters(area, monsters)

    def spawn_hero(self, area, hero):
        area.paste_character(hero)

    def spawn_monsters(self, area, monsters):
        for monster in monsters:
            area.paste_character(monster)

    def check_next_area(self, area, characters):
        for monster in characters[1:]:
            if monster.__class__() == "Boss":
                break
        for skeleton in characters[2:]:
            if skeleton.has_key == True:
                break
        else:
            self.next_area(area, characters)

    def clear_area(self, monsters):
        for monster in monsters:
            del monster

    def next_area(self, area, characters):
        hero = self.hero
        monsters = characters[1:]
        self.clear_area(monsters)
        area.number += 1
        self.create_characters()
        new_monsters = characters[1:]
        self.spawn_characters(area, hero, new_monsters)
'''
    def move_hero(self, hero, direction):
        destination = '' #get tile
        hero.turn(direction)
        if destination.walkable == True:
            hero.x_axis = destination.x_axis
            hero.y_axis = destination.y_axis
            '''