from random import randrange
from area2 import Area
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

    def get_tile_stats(self, tile):
        print(tile.walkable)
        print(tile.has_hero)
        print(tile.has_monster)

    def set_free_tiles(self, area):
        area.free_tiles = []
        for tile in area.tiles.values():
            #self.get_tile_stats(tile)
            if tile.walkable == True and tile.has_hero == False and tile.has_monster == False:
                area.free_tiles.append((tile, tile.y, tile.x))

    def spawn_characters(self, area, canvas, hero, monsters):
        self.set_free_tiles(area)
        self.spawn_hero(area, canvas, hero)
        self.spawn_monsters(area, canvas, monsters)

    def spawn_hero(self, area, canvas, hero):
        self.set_free_tiles(area)
        area.draw_character(canvas, hero)
        tile = area.free_tiles[0][0]
        tile.has_hero = True

    def spawn_monsters(self, area, canvas, monsters):
        for monster in monsters:
            self.set_free_tiles(area)
            tile = area.free_tiles[randrange(len(area.free_tiles))]
            monster.y = tile[1]
            monster.x = tile[2]
            area.draw_character(canvas, monster)
            tile[0].has_monster = True

    def move(self, area, canvas, character, direction):
        if character.__class__.__name__ == 'Hero':
            character.turn(direction)
        destination_x, destination_y = self.calculate_destination(character, direction)
        if not self.check_walls (area, destination_x, destination_y):
            return 'Ouch! Whatch where you are going!'
        character.x_axis, character.y_axis = destination_x, destination_y

    def get_position(self, item):
        x = item.x_axis
        y = item.y_axis
        return (x, y)

    def calculate_destination(self, character, direction):
        x, y = self.get_position(character)
        if direction == 'up':
            y -= 72
        elif direction == 'down':
            y += 72
        elif direction == 'right':
            x += 72
        elif direction == 'left':
            x -= 72
        return (x, y)

    def check_walls(self, area, x, y):
        if y * 10 + x in area.walls:
            return False

    def check_other_characters(self, character, characters):
        for char in characters:
            pass
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

    def check_next_area(self, area, canvas, characters):
        for monster in characters[1:]:
            if monster.__class__() == "Boss":
                break
        for skeleton in characters[2:]:
            if skeleton.has_key == True:
                break
        else:
            self.next_area(area, canvas, characters)

    def next_area(self, area, canvas, characters):
        hero = self.hero
        monsters = characters[1:]
        self.clear_area(monsters)
        area.number += 1
        self.create_characters()
        new_monsters = characters[1:]
        self.spawn_characters(area, canvas, hero, new_monsters)

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