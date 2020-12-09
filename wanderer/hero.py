from random import randrange
from character import Character

class Hero(Character):

    def __init__(self):
        super().__init__()
        self.direction = 'down'
        self.level = 1
        self.max_health = 20 + 3 * randrange(6)
        self.current_health = self.max_health
        self.def_point = 2 * randrange(6)
        self.strike_point = 5 + randrange(6)
        self.on_tile = 0
