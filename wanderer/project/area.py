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
        self.walls = [13, 15, 17, 18, 21, 22, 23, 25, 28, 35, 41, 42, 43, 45,
                      47, 51, 61, 63, 65, 66, 68, 75, 78, 81, 82, 83, 88, 95]
        self.size = self.tile_size * self.number_of_tiles

    def create_map(self):
        for i in range(self.number_of_tiles):
            for j in range(self.number_of_tiles):
                tile = []
                position = j * 10 + i
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
