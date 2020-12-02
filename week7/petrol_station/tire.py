class Tire:
    wear = 0

    def __init__(self):
        self.wear = 0

    def is_usable(self):
        return self.wear < 10

    def drive(self):
        self.wear += 1