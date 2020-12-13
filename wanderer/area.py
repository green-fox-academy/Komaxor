from tiles import *

class Area:

    def __init__(self):
        self.number = 0
        self.size = 10
        self.tiles = []

    def create_floor(self):
        for _ in range(0, 100):
            self.tiles.append(Floor)
        return self.tiles

    def create_walls(self):
        self.create_floor()
        walls = [5, 12, 13, 15, 23, 24, 25, 60]
        return self.tiles

