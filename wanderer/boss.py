from random import randrange
from monster import Monster

class Boss(Monster):

    def __init__(self):
        super().__init__()
        self.level = 1 # = area.number
        self.max_health = 2 * self.level * randrange(6) + randrange(6)
        self.current_health = self.max_health
        self.def_point = self.level / 2 * randrange(6) + randrange(6) / 2
        self.strike_point = self.level * randrange(6) + self.level
        self.on_tile = randrange(1, 100)
