from monster import Monster

class Boss(Monster):

    def __init__(self):
        super().__init__()
        self.name = 'Boss'
        self.max_health = (2 * self.level * super().rng(1, 6)) + super().rng(1, 6)
        self.current_health = self.max_health
        self.def_point = (self.level / 2 * super().rng(1, 6)) + (super().rng(1, 6) / 2)
        self.strike_point = (self.level * super().rng(1, 6)) + self.level
        self.image_path = "project/assets/boss.gif"
