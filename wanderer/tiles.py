from PIL import Image

class Tile:

    def __init__(self):
        self.position = 0
        self.has_monster = False
        self.has_hero = False

class Floor(Tile):

    def __init__(self):
        super().__init__()
        self.image = Image.open("assets/floor.png")

class Wall(Tile):

    def __init__(self):
        super().__init__()
        self.image = Image.open("assets/wall.png")