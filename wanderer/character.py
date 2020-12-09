from area import Area

class Character:

    def __init__(self):
        self.level = 0
        self.max_health = 0
        self.current_health = 0
        self.def_point = 0
        self.strike_point = 0
        self.on_tile = 0

    def move(self, direction):
        self.turn(direction)
        tile = self.step(direction)
        if tile.has_hero == tile.has_monster == True:
            self.fight(defender)


    def turn(self, direction):
        if direction == 'down':
            pass
        if direction == 'up':
            pass
        if direction == 'right':
            pass
        if direction == 'left':
            pass

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
        while True:
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
            del self