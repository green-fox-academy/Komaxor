from random import randrange

class Character:

    def __init__(self):
        self.level = 0
        self.max_health = 0
        self.current_health = 0
        self.def_point = 0
        self.strike_point = 0
        self.on_tile = 0
        self.x_axis = 0
        self.y_axis = 0

    def rng(self):
        return randrange(1, 6)

    def introduce(self):
        return (self.__class__.__name__ + " (Level " + str(self.level) + ") HP: " +
            str(self.current_health) + "/" + str(self.max_health) +
            " | DP: " + str(self.def_point) + " | SP: " + str(self.strike_point))


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

    def hit(self, defender):
        defender.current_health -= self.strike_point
        defender.check_death()

    def check_death(self):
        if self.current_health <= 0:
            if self.__class__() == 'Monster':
                return ("Monster successfully destroyed!")
            if self.__class__() == 'Hero':
                return ("You died!")