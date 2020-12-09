from tile import Tile

class Area:

    def __init__(self):
        self.number = 0
        self.tiles = []

    def create_floor(self):
        for _ in range(0, 100):
            self.tiles.append(Tile('floor'))
        return self.tiles

    def create_walls(self):
        self.create_floor()
        walls = [5, 12, 13, 15, 23, 24, 25, 60]
        for tile in walls:
            self.tiles[tile - 1].type = 'wall'
        return self.tiles