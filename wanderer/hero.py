from random import randrange
from character import Character

class Hero(Character):

    def __init__(self):
        super().__init__()
        self.direction = ''
        self.level = 1
        self.max_health = 20 + 3 * super().rng(1, 6)
        self.current_health = self.max_health
        self.def_point = 2 * super().rng(1, 6)
        self.strike_point = 5 + super().rng(1, 6)
        self.image_down = "assets/hero-down.png"
        self.image_up = "assets/hero-up.png"
        self.image_left = "assets/hero-left.png"
        self.image_right = "assets/hero-right.png"
        self.image_path = self.image_down

    def turn(self, direction):
        if direction == 'down':
            self.image_path = self.image_down
        if direction == 'up':
            self.image_path = self.image_up
        if direction == 'left':
            self.image_path = self.image_left
        if direction == 'right':
            self.image_path = self.image_right

    def level_up(self):
        self.max_health += super().rng(1, 6)
        #self.current_health += super().rng()
        self.def_point += super().rng(1, 6)
        self.strike_point += super().rng(1, 6)

    def restore_health(self):
        random = randrange(1, 11)
        if random == 1:
            self.restore_health_full
        if random > 5:
            self.restore_health_tenth
        else:
            self.restore_health_third

    def restore_health_full(self):
        self.current_health = self.max_health

    def restore_health_third(self):
        self.current_health += self.max_health / 3

    def restore_health_tenth(self):
        self.current_health += self.max_health / 10
