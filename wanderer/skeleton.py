from monster import Monster
from PIL import Image

class Skeleton(Monster):

    def __init__(self):
        super().__init__()
        self.has_key = False
        self.max_health = 2 * self.level * super().rng()
        self.current_health = self.max_health
        self.def_point = self.level / 2 * super().rng()
        self.strike_point = self.level * super().rng()
        self.image = Image.open("assets/skeleton.png")
