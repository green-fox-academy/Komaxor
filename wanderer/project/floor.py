from tiles import Tile

class Floor(Tile):

    def __init__(self):
        super().__init__()
        self.walkable = True
        self.image_path = "project/assets/floor.gif"