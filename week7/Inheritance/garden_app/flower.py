from plants import Plant

class Flower(Plant):

    def __init__(self, color):
        super().__init__(color)
        self.type = 'Flower'
        self.needs_water_at = 5
        self.absorption_rate = 0.75