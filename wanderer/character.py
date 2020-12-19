from random import randrange
from PIL import Image, ImageTk

class Character:

    def __init__(self):
        self.name = ''
        self.level = 0
        self.max_health = 0
        self.current_health = 0
        self.def_point = 0
        self.strike_point = 0
        self.x = 0
        self.y = 0
        self.image_path = ''

    def rng(self, min, max):
        return randrange(min, max)

    def introduce(self):
        return (self.__class__.__name__ + " (Level " + str(self.level) + ") HP: " +
            str(self.current_health) + "/" + str(self.max_health) +
            " | DP: " + str(self.def_point) + " | SP: " + str(self.strike_point))

    def get_image(self):
        return ImageTk.PhotoImage(Image.open(self.image_path))

    def step(self, direction):
        if direction == 'down' and self.y < 9:
            self.y += 1
        if direction == 'up' and self.y > 0:
            self.y -= 1
        if direction == 'right' and self.x < 9:
            self.x += 1
        if direction == 'left' and self.x > 0:
            self.x -= 1
        return (self.y, self.x)

    def hit(self, defender):
        defender.current_health -= self.strike_point
        defender.check_death()

    def check_death(self):
        if self.current_health <= 0:
            if self.__class__() == 'Monster':
                return "Monster successfully destroyed!"
            if self.__class__() == 'Hero':
                return "You died!"
