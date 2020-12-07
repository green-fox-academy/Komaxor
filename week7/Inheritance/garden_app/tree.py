from plants import Plant

class Tree(Plant):

    def __init__(self, color):
        super().__init__(color)
        self.type = 'tree'
        self.needs_water_at = 10
        self.absorption_rate = 0.4