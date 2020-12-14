from character import Character
from random import randrange


class Monster(Character):

    def __init__(self):
        super().__init__()
        self.level = 1 # = area.number
        self.x_axis = self.monster_spawn_tile()
        self.y_axis = self.monster_spawn_tile()
        self.on_tile = self.y_axis * 10 + self.x_axis

    def monster_spawn_tile(self):
        return randrange(72, 720 - 72, 72)
