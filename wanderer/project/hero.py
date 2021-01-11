from character import Character

class Hero(Character):

    def __init__(self):
        super().__init__()
        self.name = 'Hero'
        self.max_health = 20 + 3 * super().rng()
        self.current_health = self.max_health
        self.def_point = 2 * super().rng()
        self.strike_point = 5 + super().rng()
        self.direction = 'hero-down'

    def turn(self, direction):
        if direction == 'down':
            self.direction = 'hero-down'
        if direction == 'up':
            self.direction = 'hero-up'
        if direction == 'left':
            self.direction = 'hero-left'
        if direction == 'right':
            self.direction = 'hero-right'

    def level_up(self):
        self.level += 1
        self.max_health += super().rng()
        #self.current_health += super().rng()
        self.def_point += super().rng()
        self.strike_point += super().rng()

    def restore_health(self):
        random = super().rng(max=11)
        if random == 1:
            self.restore_health_full()
        elif random > 5:
            self.restore_health_tenth()
        else:
            self.restore_health_third()
        if self.current_health > self.max_health:
            self.restore_health_full()

    def restore_health_full(self):
        self.current_health = self.max_health

    def restore_health_third(self):
        self.current_health += int(self.max_health / 3)

    def restore_health_tenth(self):
        self.current_health += int(self.max_health / 10)
