from tile import Tile

class Floor(Tile):

    def __init__(self):
        super().__init__()
        self.walkable = True