from tiles import Floor, Wall
from PIL import Image

#wall = Wall()
floor = Floor()
class CreateArea:

    def __init__(self):
        self.number = 0
        self.number_of_tiles = 10
        self.tiles = {}
        self.tile_size = floor.image.size[0]
        self.area_size = self.number_of_tiles * self.tile_size
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

    def paste_tile(self, image):
        self.get_current_position()
        place = (self.x_axis, self.y_axis, self.x_axis + image.size[0], self.y_axis + image.size[1])
        self.bg.paste(image, place)
        self.tile_x += 1

    def display(self):
        self.bg.show()

    def draw_map(self):
        walls = [13, 15, 17, 18, 21, 22, 23, 25, 28, 35, 41, 42, 43, 45, 47,
                 51, 61, 63, 65, 66, 68, 75, 78, 81, 82, 83, 88, 95, 96]
        for i in range(self.number_of_tiles ** 2):
            if i in walls:
                self.tiles[i] = Wall()
            else:
                self.tiles[i] = Floor()
            image = self.tiles[i].image
            self.paste_tile(image)

    def paste_character(self, character):
        image = character.image
        place = (character.x_axis, character.y_axis, character.x_axis + image.size[0], character.y_axis + image.size[1])
        self.bg.paste(image, place)
