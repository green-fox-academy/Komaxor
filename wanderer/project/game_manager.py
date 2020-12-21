from random import randrange
from area import Area
from hero import Hero
from skeleton import Skeleton
from boss import Boss

class GameManager:

    def __init__(self):
        self.area_number = 1

    def create_characters(self, hero):
        characters = []
        characters.append(hero)
        monsters = self.create_monsters()
        for i in range(0, len(monsters)):
            characters.append(monsters[i])
        return characters

    def create_monsters(self):
        monsters = []
        boss = Boss()
        boss.level = self.area_number
        monsters.append(boss)
        skeletons = []
        skeleton_number = randrange(2, 5)
        for i in range(skeleton_number):
            skeletons.append(Skeleton('Skeleton ' + str(i + 1)))
        skeletons[0].has_key == True
        for skeleton in skeletons:
            skeleton.level = self.area_number
            monsters.append(skeleton)
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
        for tile in area.tiles:
            #self.get_tile_stats(tile)
            if tile[0].walkable == True and tile[0].has_hero == False and tile[0].has_monster == False:
                area.free_tiles.append((tile[0], (tile[0].x, tile[0].y)))

    def spawn_characters(self, area, canvas, characters):
        hero = characters[0]
        monsters = characters[1:]
        area.character_images = {}
        self.spawn_hero(area, canvas, hero)
        self.spawn_monsters(area, canvas, monsters)

    def spawn_hero(self, area, canvas, hero):
        self.set_free_tiles(area)
        hero.image_path = hero.image_down
        area.draw_character(canvas, hero)
        tile = area.tiles[0][0]
        tile.has_hero = True

    def spawn_monsters(self, area, canvas, monsters):
        for monster in monsters:
            self.set_free_tiles(area)
            tile = area.free_tiles[randrange(len(area.free_tiles))]
            monster.y = tile[1][0]
            monster.x = tile[1][1]
            area.draw_character(canvas, monster)
            tile[0].has_monster = True

    def get_tile(self, area, character, x=None, y=None):
        return [i for i in area.tiles if [character.x, character.y] in i]

    def set_hero_position(self, area, canvas, hero, direction, monsters):
        hero.turn(direction)
        area.draw_character(canvas, hero)
        destination_x, destination_y = self.calculate_destination(hero, direction)
        is_wall = self.check_walls(area, destination_x, destination_y)
        if is_wall == True:
            print('Ouch! Watch where you are going!')
            return
        if (destination_x >= 0 and destination_x < area.size
            and destination_y >= 0 and destination_y < area.size):
            self.get_tile(area, hero)[0][0].has_hero = False
            hero.x, hero.y = destination_x, destination_y
            area.draw_character(canvas, hero)
            self.get_tile(area, hero)[0][0].has_hero = True
        else:
            print('The edge has been reached!')
            return
        has_monster = self.check_monsters(monsters, destination_x, destination_y)
        if has_monster != False:
            self.fight(area, hero, has_monster)
        self.check_monster_move(area, canvas, hero, monsters)

    def check_monster_move(self, area, canvas, hero, monsters):
        if area.turn_count % 2 != 0:
            for monster in monsters:
                self.set_monster_position(area, canvas, hero, monster, monsters)
        area.increase_turn_count()

    def set_monster_position(self, area, canvas, hero, monster, monsters):
        directions = self.get_possible_moves(area, monster, monsters)
        #print(monster.name, directions)
        direction = directions[randrange(len(directions))]
        destination_x, destination_y = self.calculate_destination(monster, direction)
        self.get_tile(area, monster)[0][0].has_monster = False
        monster.x, monster.y = destination_x, destination_y
        area.draw_character(canvas, monster)
        self.get_tile(area, monster)[0][0].has_monster = True
        if self.get_tile(area, monster)[0][0].has_hero == True:
            self.fight(area, monster, hero)
            hero.level_up()
        #print('turn done ' + monster.name, direction, destination_x / area.tile_size, destination_y / area.tile_size)

    def get_possible_moves(self, area, monster, monsters):
        directions = ['up', 'down', 'left', 'right']
        bad_directions = []
        for direction in directions:
            #print(direction)
            destination_x, destination_y = self.calculate_destination(monster, direction)
            is_wall = self.check_walls(area, destination_x, destination_y)
            if is_wall == True:
                #print('nope wall ' + monster.name, direction, destination_x / area.tile_size, destination_y / area.tile_size)
                bad_directions.append(direction)
                continue
            has_monster = self.check_monsters(monsters, destination_x, destination_y)
            if has_monster != False:
                #print('nope another monster ' + monster.name, direction, destination_x / area.tile_size, destination_y / area.tile_size)
                bad_directions.append(direction)
                continue
            if (destination_x < 0 or destination_x > area.size - area.tile_size
                or destination_y < 0 or destination_y > area.size - area.tile_size):
                #print('nope edge ' + monster.name, direction, destination_x / area.tile_size, destination_y / area.tile_size)
                bad_directions.append(direction)
                continue
        if len(bad_directions) != 0:
            for item in bad_directions:
                directions.remove(item)
                #print(item)
                #print(directions)
        if len(directions) == 0:
            #print(monster.x, monster.y)
            monster.x, monster.y = area.free_tiles[0][0].x, area.free_tiles[0][0].y
            #print(monster.x, monster.y)
            print('monster is trapped') #NOTE does not get out
            self.get_possible_moves(area, monster, monsters)
        return directions

    def calculate_destination(self, character, direction):
        if direction == 'up':
            x = character.x
            y = character.y - 72
        elif direction == 'down':
            x = character.x
            y = character.y + 72
        elif direction == 'right':
            y = character.y
            x = character.x + 72
        elif direction == 'left':
            y = character.y
            x = character.x -72
        else:
            y = character.y
            x = character.x
        return (x, y)

    def check_walls(self, area, destination_x, destination_y):
        if (((destination_y * area.number_of_tiles) / area.tile_size) +
            (destination_x / area.tile_size) in area.walls):
            return True
        else:
            return False

    def check_monsters(self, monsters, destination_x, destination_y):
        for monster in monsters:
            if monster.x == destination_x and monster.y == destination_y:
                return monster
        else:
            return False

    def fight(self, area, attacker, defender):
        while attacker.current_health > 0 and defender.current_health > 0:
            attacker.strike(attacker, defender)
            #print(attacker.name + ' has striked')
            if self.check_death(area, defender) == True:
                return
            defender.strike(defender, attacker)
            #print(defender.name + ' has striked back')
            self.check_death(area, attacker)

    def check_death(self, area, receiver):
        if receiver.current_health <= 0:
            print(receiver.name + " died")
            #print(area.character_images)
            del area.character_images[receiver.name] #NOTE does not work
            #print(area.character_images)
            self.kill(receiver)
            return True
        else:
            return False

    def kill(self, character):
        del character #NOTE does not work

    def check_next_area(self, area, canvas, characters):
        print(characters)
        print(characters[1].__class__.__name__)
        if characters[1].__class__() == "Boss":
            print('boss alive')
            #return
        print(characters[2:])
        for skeleton in characters[2:]:
            if skeleton.has_key == True:
                print(skeleton.name + ' has key')
                #return
        print('next area triggered')
        #self.next_area(area, canvas, characters)

    def next_area(self, area, canvas, characters):
        monsters = characters[1:]
        self.clear_area(area, monsters)
        self.area_number += 1
        characters = self.create_characters(characters[0])
        self.spawn_characters(area, canvas, characters)

    def clear_area(self, area, monsters):
        for monster in monsters:
            del monster
            area.character_images = {}
