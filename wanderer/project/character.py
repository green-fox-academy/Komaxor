from random import randrange
from PIL import Image, ImageTk

class Character:

    def __init__(self):
        self.name = ''
        self.level = 1
        self.max_health = 0
        self.current_health = self.max_health
        self.def_point = 0
        self.strike_point = 0
        self.x = 0
        self.y = 0
        self.image_path = ''

    def rng(self, min=1, max=6):
        return randrange(min, max)

    def introduce(self):
        return (self.__class__.__name__ + " (Level " + str(self.level) +
                ") HP: " + str(int(self.current_health)) + "/" +
                str(self.max_health) +" | DP: " + str(self.def_point) +
                " | SP: " + str(self.strike_point))

    def get_image(self):
        return ImageTk.PhotoImage(Image.open(self.image_path))

    def strike(self, attacker, defender):
        strike_value = attacker.strike_point + 2 * self.rng()
        if 2 * self.rng() + attacker.strike_point > defender.def_point:
            defender.current_health -= (strike_value - defender.def_point)
