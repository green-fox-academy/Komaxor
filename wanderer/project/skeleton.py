from monster import Monster


class Skeleton(Monster):

    def __init__(self, name='Skeleton_#'):
        super().__init__()
        self.name = name
        self.max_health = 2 * self.level * super().rng()
        self.current_health = self.max_health
        self.def_point = self.level / 2 * super().rng()
        self.strike_point = self.level * super().rng()
