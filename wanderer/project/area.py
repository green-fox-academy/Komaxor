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
        self.walls = [] #[13, 15, 17, 18, 21, 22, 23, 25, 28, 35, 41, 42, 43, 45,
                      #47, 51, 61, 63, 65, 66, 68, 75, 78, 81, 82, 83, 88, 95]
        self.floors = []
        self.size = self.tile_size * self.number_of_tiles

    def create_map(self):
        self.create_walls()
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

    def create_walls(self):
        self.random_map()
        self.connect_map()

    def random_map(self):
        self.floors.append(0)
        for i in range(1, self.number_of_tiles ** 2):
            random = randrange(0, 10)
            if random < randrange(3, 7):
                self.walls.append(i)
            else:
                self.floors.append(i)
        if len(self.floors) < 6:
            self.floors = []
            self.walls = []
            self.random_map()

    def connect_map(self):
        unseen = self.floors + self.walls
        seen = [0]
        been = [0]
        unseen.remove(0)
        #print('floors ' + str(self.floors))
        #print(len(self.floors))
        #print('walls ' + str(self.walls))
        #print(len(self.walls))
        #while len(self.floors) != len(been):
        for _ in range(1):
            #print('start')
            self.see_neighbours(0, unseen, seen)
            #self.print_all(unseen, seen, been)
            self.check_seen(unseen, seen, been)
            #self.print_all(unseen, seen, been)
            #for _ in range(3):
            while len(set(self.floors)) != len(set(been)):
                #print('floors' + str(len(set(self.floors))) + 'been' + str(len(set(been))))
                self.check_over_walls(unseen, seen, been)
                #self.print_all(unseen, seen, been)
                self.check_seen(unseen, seen, been)

    def print_all(self, unseen, seen, been):
        print('been on ' + str(been))
        print(len(been))
        print('seen ' + str(seen))
        print(len(seen))
        print('unseen ' + str(unseen))
        print(len(unseen))


    def see_neighbours(self, tile, unseen, seen):
        #print('see neighbours of ' + str(tile))
        if tile - 1 in unseen and tile % self.number_of_tiles != 0:
            self.see(tile - 1, unseen, seen)
        if tile + 1 in unseen and (tile + 1) % self.number_of_tiles != 0:
            self.see(tile + 1, unseen, seen)
        if tile - self.number_of_tiles in unseen:
            self.see(tile - self.number_of_tiles, unseen, seen)
        if tile + self.number_of_tiles in unseen:
            self.see(tile + self.number_of_tiles, unseen, seen)

    def see(self, tile, unseen, seen):
        #print('seeing ' +str(tile))
        seen.append(tile)
        unseen.remove(tile)

    def check_seen(self, unseen, seen, been):
        for tile in seen:
            #print('checking seen ' + str(tile))
            if tile in self.floors and tile not in been:
                been.append(tile)
                self.see_neighbours(tile, unseen, seen)
        #seen_as_set = set(seen)
        #common = seen_as_set.intersection(self.floors)
        #print('common ' + str(len(common)) + 'been_len ' + str(len(been)))
        #if len(been) < len(common):
            #print('hello there')
            #self.check_seen(unseen, seen, been)

    def check_over_walls(self, unseen, seen, been):
        #print('checking over walls')
        for tile in unseen:
            if tile in self.floors:
                if tile - 2 in been and tile - 1 in self.walls:
                    self.break_wall(tile, tile - 1, unseen, seen, been)
                    #print('break ' + str(tile - 1))
                    return
                elif tile - (2 * self.number_of_tiles) in been and tile - self.number_of_tiles in self.walls:
                    self.break_wall(tile, tile - self.number_of_tiles, unseen, seen, been)
                    #print('break ' + str(tile - self.number_of_tiles))
                    return
                elif tile + 2 in been and tile + 1 in self.walls:
                    self.break_wall(tile, tile + 1, unseen, seen, been)
                    #print('break ' + str(tile + 1))
                    return
                elif tile + (2 * self.number_of_tiles) in been and tile + self.number_of_tiles in self.walls:
                    self.break_wall(tile, tile + self.number_of_tiles, unseen, seen, been)
                    #print('break ' + str(tile + self.number_of_tiles))
                    return
                else:
                    print(str(tile) + 'and' + str(unseen[len(unseen) - 1]))
                    if tile == unseen[len(unseen) - 1]:
                        self.make_wall(tile)
                        #print('wall ' + str(tile))
                    else:
                        continue

    def break_wall(self, tile, tile_between, unseen, seen, been):
        self.walls.remove(tile_between)
        self.floors.append(tile_between)

    def make_wall(self, tile):
        self.walls.append(tile)
        self.floors.remove(tile)