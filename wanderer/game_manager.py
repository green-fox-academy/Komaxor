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
        for character in characters:
            print(character.introduce())

    def spawn_characters(self, area, hero, monsters):
        self.spawn_hero(area, hero)
        self.spawn_monsters(area, monsters)

    def spawn_hero(self, area, hero):
        area.paste_character(hero)

    def spawn_monsters(self, area, monsters):
        for monster in monsters:
            area.paste_character(monster)

    def move(self, character, direction):
        x, y = self.get_position(character)
        print(x, y)
        if character.__class__.__name__ == 'Hero':
            character.turn(direction)
        destination_x, destination_y = self.calculate_destination(direction, x, y)
        character.x_axis, character.y_axis = destination_x, destination_y

    def get_position(self, item):
        x = item.x_axis
        y = item.y_axis
        return (x, y)

    def calculate_destination(self, direction, x, y):
        if direction == 'up':
            y -= 72
        elif direction == 'down':
            y += 72
        elif direction == 'right':
            x += 72
        elif direction == 'left':
            x -= 72
        return (x, y)

        #check for walls
        #print(direction)
        #check for other characters
        #character.step(direction)
        #if hero x monster -> fight

    def check_fight(self, attacker, defender):
        if attacker.on_tile == defender.on_tile:
            self.fight(attacker, defender)

    def fight(self, attacker, defender):
        while attacker.current_health > 0 and defender.current_health > 0:
            attacker.hit(defender)
            defender.check_death()
            #prevent defender to hit after it died
            defender.hit(attacker)
            attacker.check_death()
        if attacker.current_health <= 0:
            self.kill(attacker)
        else:
            self.kill(defender)

    def kill(self, character):
        del character

    def check_next_area(self, area, characters):
        for monster in characters[1:]:
            if monster.__class__() == "Boss":
                break
        for skeleton in characters[2:]:
            if skeleton.has_key == True:
                break
        else:
            self.next_area(area, characters)

    def next_area(self, area, characters):
        hero = self.hero
        monsters = characters[1:]
        self.clear_area(monsters)
        area.number += 1
        self.create_characters()
        new_monsters = characters[1:]
        self.spawn_characters(area, hero, new_monsters)

    def clear_area(self, monsters):
        for monster in monsters:
            del monster
    '''
    def move_hero(self, hero, direction):
        destination = '' #get tile
        hero.turn(direction)
        if destination.walkable == True:
            hero.x_axis = destination.x_axis
            hero.y_axis = destination.y_axis


    def player_input(self):
        directions = ['w', 'a', 's', 'd']
        while True:
            try:
                x = input("Which direction do you want to go? ")
            except ValueError:
                print("Use WASD for movement!")
                continue
            if x not in directions:
                print("Use WASD for movement!")
                continue
            else:
                if x == 'w' or x == 'W':
                    return 'up'
                if x == 's' or x == 'S':
                    return 'down'
                if x == 'a' or x == 'A':
                    return 'left'
                if x == 'd' or x == 'D':
                    return 'right'
    '''