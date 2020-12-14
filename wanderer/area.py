from tiles import Floor, Wall
from PIL import Image

class CreateArea:

    def __init__(self, tile_size, area_size):
        self.number = 0
        self.tiles = {}
        self.tile_size = tile_size
        self.area_size = area_size
        self.bg = Image.new("RGBA", (self.area_size, self.area_size), (0,0,0,0))
        self.tile_x = 0
        self.tile_y = 0

    def get_current_position(self):
        self.x_axis = (self.tile_size * self.tile_x)
        self.y_axis = (self.tile_size * self.tile_y)
        if (self.x_axis + self.tile_size > self.area_size):
            self.tile_x = 0
            self.tile_y += 1
            self.get_current_position()

    def paste_image(self, image):
        self.get_current_position()
        place = (self.x_axis, self.y_axis, self.x_axis + image.size[0], self.y_axis + image.size[1])
        self.bg.paste(image, place)
        self.tile_x += 1

    def show(self):
        self.bg.show()

    def get_walls(self):
        walls = [13, 15, 17, 18, 21, 22, 23, 25, 27, 28, 35, 41, 42, 43, 45, 47, 51, 61, 63, 65, 66, 68, 75, 76, 78, 81, 82, 83, 88, 96, 97]
        for i in range(int((self.area_size / self.tile_size) ** 2)):
            if i in walls:
                self.tiles[i] = "Wall"
            else:
                self.tiles[i] = "Floor"

    def paste_character(self, character):
        image = character.image
        place = (character.x_axis, character.y_axis, character.x_axis + image.size[0], character.y_axis + image.size[1])
        self.bg.paste(image, place)
