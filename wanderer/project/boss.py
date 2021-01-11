from monster import Monster

class Boss(Monster):

    def __init__(self):
        super().__init__()
        self.name = 'Boss'
        self.max_health = 2 * self.level * super().rng() + super().rng()
        self.current_health = self.max_health
        self.def_point = self.level / 2 * super().rng() + super().rng() / 2
        self.strike_point = self.level * super().rng() + self.level
