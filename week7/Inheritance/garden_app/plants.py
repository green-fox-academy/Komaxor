class Plant:

    def __init__(self, color):
        self.type = ''
        self.color = color
        self.water_level = 0.0
        self.needs_water_at = 0
        self.absorption_rate = 0.0

    def getStatus(self):
        print(self.color + self.type)