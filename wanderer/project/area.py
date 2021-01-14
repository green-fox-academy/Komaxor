from random import randrange

from floor import Floor
from wall import Wall
from PIL import Image
from tkinter.constants import NW
from resources import Resources
from monster import Monster


class Area:

    def __init__(self):
        self.turn_count = 0
        self.resources = Resources()
        self.number_of_tiles = 10
        self.tile_size = self.resources.floor_size
        self.tiles = []
        self.walls = []
        self.floors = []
        self.size = self.tile_size * self.number_of_tiles

    def create_map(self):
        self.random_map()
        for i in range(self.number_of_tiles):
            for j in range(self.number_of_tiles):
                tile = []
                position = j * self.number_of_tiles + i
                if position in self.walls:
                    tile.append(Wall())
                else:
                    tile.append(Floor())
                tile.append(position)
                x = self.tile_size * j
                y = self.tile_size * i
                tile[0].x = x
                tile[0].y = y
                tile.append([x, y])
                self.tiles.append(tile)

    def draw_map(self, canvas):
        self.create_map()
        for tile in self.tiles:
            if isinstance(tile[0], Floor):
                img = self.resources.get_image('floor')
            elif isinstance(tile[0], Wall):
                img = self.resources.get_image('wall')
            canvas.create_image(tile[2][1], tile[2][0], anchor=NW, image=img)

    def draw_character(self, canvas, character):
        if isinstance(character, Monster):
            img = self.resources.get_image(character.__class__.__name__)
        else:
            img = self.resources.get_image(character.direction)
        y = character.y
        x = character.x
        canvas.create_image(x, y, anchor=NW, image=img, tag=character.name)

    def increase_turn_count(self):
        self.turn_count += 1

    def random_map(self):
        self.floors = []
        self.walls = []
        self.floors.append(0)
        for i in range(1, self.number_of_tiles ** 2):
            random = randrange(0, 10)
            if random < randrange(3, 7):
                self.walls.append(i)
            else:
                self.floors.append(i)
        if len(self.floors) < 6:  # max characters
            self.random_map()
        start_block = [0, 1, 2, self.number_of_tiles, 2 *
                       self.number_of_tiles, self.number_of_tiles + 1]
        if all(tiles in self.walls for tiles in start_block):
            self.random_map()
        self.connect_map()

    def connect_map(self):
        unseen = self.walls + self.floors
        seen = [0]
        been = [0]
        unseen.remove(0)
        self.see_neighbours(0, unseen, seen)
        self.check_seen(unseen, seen, been)
        while len(set(self.floors)) != len(set(been)):
            self.check_over_walls(unseen, seen, been)
            self.check_seen(unseen, seen, been)
        if len(self.floors) < 6:  # max characters
            self.random_map()

    def see_neighbours(self, tile, unseen, seen):
        if tile - 1 in unseen and tile % self.number_of_tiles != 0:
            self.see(tile - 1, unseen, seen)
        if tile + 1 in unseen and (tile + 1) % self.number_of_tiles != 0:
            self.see(tile + 1, unseen, seen)
        if tile - self.number_of_tiles in unseen:
            self.see(tile - self.number_of_tiles, unseen, seen)
        if tile + self.number_of_tiles in unseen:
            self.see(tile + self.number_of_tiles, unseen, seen)

    def see(self, tile, unseen, seen):
        seen.append(tile)
        unseen.remove(tile)

    def check_seen(self, unseen, seen, been):
        for tile in seen:
            if tile in self.floors and tile not in been:
                been.append(tile)
                self.see_neighbours(tile, unseen, seen)

    def check_over_walls(self, unseen, seen, been):
        unseen_floors = list(set(unseen).intersection(set(self.floors)))
        counter = 1
        for tile in unseen_floors:
            # connect isolated floors with 1 break
            if (tile - 2 in been and tile - 1 in self.walls and
                    tile - 1 in seen):
                self.break_wall(tile - 1)
                return
            elif (tile - (2 * self.number_of_tiles) in been and
                  tile - self.number_of_tiles in self.walls and
                  tile - self.number_of_tiles in seen):
                self.break_wall(tile - self.number_of_tiles)
                return
            elif (tile + 2 in been and tile + 1 in self.walls and
                  tile + 1 in seen):
                self.break_wall(tile + 1)
                return
            elif (tile + (2 * self.number_of_tiles) in been and
                  tile + self.number_of_tiles in self.walls and
                  tile + self.number_of_tiles in seen):
                self.break_wall(tile + self.number_of_tiles)
                return
            elif (tile - 1 - self.number_of_tiles in been and
                  tile - 1 in self.walls and
                  tile - self.number_of_tiles in self.walls and
                  tile - 1 in seen):
                self.break_wall(tile - 1)
                return
            elif (tile - 1 + self.number_of_tiles in been and
                  tile - 1 in self.walls and
                  tile + self.number_of_tiles in self.walls and
                  tile - 1 in seen):
                self.break_wall(tile - 1)
                return
            elif (tile + 1 - self.number_of_tiles in been and
                  tile + 1 in self.walls and
                  tile - self.number_of_tiles in self.walls and
                  tile + 1 in seen):
                self.break_wall(tile + 1)
                return
            elif (tile + 1 + self.number_of_tiles in been and
                  tile + 1 in self.walls and
                  tile + self.number_of_tiles in self.walls and
                  tile + 1 in seen):
                self.break_wall(tile + 1)
                return
            # wall isolated block that cannot be connected with 1 break
            else:
                print('else')
                print(counter, len(unseen_floors))
                if counter == len(unseen_floors):
                    self.make_wall(tile)
                    print('wall made')
                    return
                else:
                    counter += 1
                    print('counter increased')
                    continue

    def break_wall(self, tile_between):
        self.walls.remove(tile_between)
        self.floors.append(tile_between)

    def make_wall(self, tile):
        self.walls.append(tile)
        self.floors.remove(tile)
