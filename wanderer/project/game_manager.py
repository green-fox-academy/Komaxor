from random import randrange
from area import Area
from hero import Hero
from monster import Monster
from skeleton import Skeleton
from boss import Boss


class GameManager:

    def __init__(self):
        self.area_number = 1
        self.area = Area()
        self.hero = Hero()
        self.characters = self.create_characters()
        self.monsters = self.characters[1:]
        self.kill_count = 0

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
        boss.level = self.area_number
        monsters.append(boss)
        skeletons = []
        number_of_skeletons = randrange(2, 5)
        for i in range(number_of_skeletons):
            skeletons.append(Skeleton('Skeleton_' + str(i + 1)))
        skeletons[0].has_key = True
        for skeleton in skeletons:
            skeleton.level = self.area_number
            monsters.append(skeleton)
        return monsters

    def set_free_tiles(self):
        free_tiles = []
        for tile in self.area.tiles:
            if (tile[0].walkable and not tile[0].has_hero
                and not tile[0].has_monster):
                free_tiles.append(tile)
        return free_tiles

    def spawn_characters(self, canvas):
        self.spawn_hero(canvas)
        self.spawn_monsters(canvas)

    def spawn_hero(self, canvas):
        self.hero.x, self.hero.y = 0, 0
        self.area.draw_character(canvas, self.hero)
        tile = self.area.tiles[0][0]
        tile.has_hero = True

    def spawn_monsters(self, canvas):
        free_tiles = self.set_free_tiles()
        for monster in self.monsters:
            tile = free_tiles[randrange(len(free_tiles))]
            free_tiles.remove(tile)
            monster.x = tile[2][1]
            monster.y = tile[2][0]
            self.area.draw_character(canvas, monster)
            tile[0].has_monster = True

    def get_character_tile(self, character):
        return [i for i in self.area.tiles if [character.x, character.y] in i]

    def set_hero_position(self, canvas, direction):
        self.hero.turn(direction)
        canvas.delete(self.hero.name)
        self.area.draw_character(canvas, self.hero)
        destination_x, destination_y = self.calculate_destination(self.hero,
                                                                  direction)
        is_wall = self.check_walls(destination_x, destination_y)
        if is_wall:
            return
        if self.check_map(destination_x, destination_y):
            self.get_character_tile(self.hero)[0][0].has_hero = False
            self.hero.x, self.hero.y = destination_x, destination_y
            canvas.delete(self.hero.name)
            self.area.draw_character(canvas, self.hero)
            self.get_character_tile(self.hero)[0][0].has_hero = True
        else:
            return
        has_monster = self.check_monsters(destination_x, destination_y)
        if has_monster != False:
            self.fight(canvas, self.hero, has_monster)
            self.hero.level_up()
        self.check_monster_move(canvas)
        self.check_next_area(canvas)

    def check_monster_move(self, canvas):
        if self.area.turn_count % 2 != 0:
            self.move_monsters(canvas)
        self.area.increase_turn_count()

    def move_monsters(self, canvas):
            for monster in self.monsters:
                self.set_monster_position(canvas, monster)

    def set_monster_position(self, canvas, monster):
        directions = self.get_possible_moves(monster)
        direction = directions[randrange(len(directions))]
        destination_x, destination_y = self.calculate_destination(monster,
                                                                direction)
        self.get_character_tile(monster)[0][0].has_monster = False
        canvas.delete(monster.name)
        monster.x, monster.y = destination_x, destination_y
        self.area.draw_character(canvas, monster)
        self.get_character_tile(monster)[0][0].has_monster = True
        if self.get_character_tile(monster)[0][0].has_hero:
            self.fight(canvas, monster, self.hero)
            self.hero.level_up()

    def get_possible_moves(self, monster):
        directions = ['up', 'down', 'left', 'right']
        bad_directions = []
        for direction in directions:
            destination_x, destination_y = self.calculate_destination(monster,
                                                                    direction)
            is_wall = self.check_walls(destination_x, destination_y)
            if is_wall:
                bad_directions.append(direction)
                continue
            if not self.check_map(destination_x, destination_y):
                bad_directions.append(direction)
                continue
            has_monster = self.check_monsters(destination_x, destination_y)
            if has_monster != False:
                bad_directions.append(direction)
                continue
        if len(bad_directions) != 0:
            for item in bad_directions:
                directions.remove(item)
        if len(directions) == 0:
            self.get_character_tile(monster)[0][0].has_monster = False
            return ['stay']
        return directions

    def calculate_destination(self, character, direction):
        if direction == 'up':
            x = character.x
            y = character.y - self.area.tile_size
        elif direction == 'down':
            x = character.x
            y = character.y + self.area.tile_size
        elif direction == 'right':
            y = character.y
            x = character.x + self.area.tile_size
        elif direction == 'left':
            y = character.y
            x = character.x - self.area.tile_size
        else:
            y = character.y
            x = character.x
        return (x, y)

    def check_walls(self, destination_x, destination_y):
        if (((destination_y * self.area.number_of_tiles) / self.area.tile_size)
            + (destination_x / self.area.tile_size) in self.area.walls):
            return True
        return False

    def check_map(self, destination_x, destination_y):
        if (destination_x < 0
            or destination_x > self.area.size - self.area.tile_size
            or destination_y < 0
            or destination_y > self.area.size - self.area.tile_size):
            return False
        return True

    def check_monsters(self, destination_x, destination_y):
        for monster in self.monsters:
            if monster.x == destination_x and monster.y == destination_y:
                return monster
        return False

    def fight(self, canvas, attacker, defender):
        while attacker.current_health > 0 and defender.current_health > 0:
            attacker.strike(attacker, defender)
            if self.check_death(canvas, defender):
                return
            defender.strike(defender, attacker)
            if self.check_death(canvas, attacker):
                return

    def check_death(self, canvas, receiver):
        if receiver.current_health <= 0:
            canvas.delete(receiver.name)
            self.kill_monster(receiver)
            self.area.draw_character(canvas, self.hero)
            return True
        return False

    def kill_monster(self, character):
        self.characters.remove(character)
        if isinstance(character, Monster):
            self.monsters.remove(character)
            self.kill_count += 1

    def check_next_area(self, canvas):
        if not self.check_boss() and not self.check_key():
            self.next_area(canvas)

    def check_boss(self):
        for monster in self.monsters:
            if isinstance(monster, Boss):
                return True
        return False

    def check_key(self):
        for monster in self.monsters:
            if monster.has_key:
                return True
        return False

    def next_area(self, canvas):
        self.area_number += 1
        self.area = Area()
        self.hero.restore_health()
        self.characters = self.create_characters()
        self.monsters = self.characters[1:]
        self.area.draw_map(canvas)
        canvas.delete(self.hero.name)
        self.hero.direction = 'hero-down'
        self.spawn_characters(canvas)
