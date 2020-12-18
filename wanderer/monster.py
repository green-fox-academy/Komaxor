from character import Character
from random import randrange


class Monster(Character):

    def __init__(self):
        super().__init__()
        self.level = 1 # = area.number
        self.x = self.monster_spawn_tile()
        self.y = self.monster_spawn_tile()

    def monster_spawn_tile(self):
        return randrange(72, 720 - 72, 72)
