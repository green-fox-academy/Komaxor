from character import Character

class Hero(Character):

    def __init__(self):
        super().__init__()
        self.name = 'Hero'
        self.max_health = 20 + 3 * super().rng()
        self.current_health = self.max_health
        self.def_point = 2 * super().rng()
        self.strike_point = 5 + super().rng()
        self.image_down = "project/assets/hero-down.gif"
        self.image_up = "project/assets/hero-up.gif"
        self.image_left = "project/assets/hero-left.gif"
        self.image_right = "project/assets/hero-right.gif"
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
        self.current_health += self.max_health / 3 #int

    def restore_health_tenth(self):
        self.current_health += self.max_health / 10 #int
