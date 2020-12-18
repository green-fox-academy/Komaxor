from tiles import Wall, Floor
from PIL import Image
from tkinter import *

class Area:

    def __init__(self):
        self.number = 0
        self.number_of_tiles = 10
        self.tile_size = 72
        self.tiles = {}
        self.walls = [13, 15, 17, 18, 21, 22, 23, 25, 28, 35, 41, 42, 43, 45,
                      47, 51, 61, 63, 65, 66, 68, 75, 78, 81, 82, 83, 88, 95]
        self.map_images = []
        self.area_size = self.tile_size * self.number_of_tiles
        self.info_size = 200
        self.app_x = self.area_size + self.info_size
        self.app_y = self.area_size
        self.tile_x = 0
        self.tile_y = 0

    def create_map(self):
        for i in range(self.number_of_tiles ** 2):
            if i in self.walls:
                self.tiles[i] = Wall()
            else:
                self.tiles[i] = Floor()

    def draw(self, canvas):
        self.create_map()
        for i in range(self.number_of_tiles):
            for j in range(self.number_of_tiles):
                y = self.tile_size * j
                x = self.tile_size * i
                img = self.tiles[i * 10 + j].get_image()
                self.map_images.append(img)
                canvas.create_image(y, x, anchor=NW, image=img)