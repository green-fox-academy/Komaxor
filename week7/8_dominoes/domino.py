class Domino(object):
    def __init__(self, value_a, value_b):
        self.values = [value_a, value_b]

    def __repr__(self):
        return '[{}, {}]'.format(self.values[0], self.values[1])