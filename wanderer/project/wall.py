from tiles import Tile

class Wall(Tile):

    def __init__(self):
        super().__init__()
        self.image_path = "project/assets/wall.gif"