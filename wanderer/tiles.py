from PIL import Image

class Tile:

    def __init__(self):
        self.x_axis = 0
        self.y_axis = 0
        self.has_monster = False
        self.has_hero = False
        self.walkable = False

class Floor(Tile):

    def __init__(self):
        super().__init__()
        self.image = Image.open("assets/floor.png")
        self.walkable = True

class Wall(Tile):

    def __init__(self):
        super().__init__()
        self.image = Image.open("assets/wall.png")