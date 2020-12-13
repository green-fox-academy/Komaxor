from area import Area
from random import randrange

class Character:

    def __init__(self):
        self.level = 0
        self.max_health = 0
        self.current_health = 0
        self.def_point = 0
        self.strike_point = 0
        self.on_tile = 0

    def rng(self):
        return randrange(1, 6)

    def spawn(self):
        return randrange(2, 100)

    def move(self, character, direction):
        character.turn(direction)
        self.on_tile = self.step(direction)

    def step(self, direction):
        if direction == 'down' and self.on_tile < 91:
            self.on_tile += 10
        if direction == 'up' and self.on_tile > 10:
            self.on_tile -= 10
        if direction == 'right' and self.on_tile - 1 == 0:
            self.on_tile += 1
        if direction == 'left' and self.on_tile % 10 == 0:
            self.on_tile -= 1
        return self.on_tile

    def fight(self, defender):
        defender.current_health -= self.strike_point
        defender.check_death()
        self.current_health -= defender.strike_point
        self.check_death()

    def check_death(self):
        if self.current_health <= 0:
            if self.__class__() == 'Monster':
                print("Monster successfully destroyed!")
            if self.__class__() == 'Hero':
                print("You died!")
            #area.kill()