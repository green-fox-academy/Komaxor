class Plant:

    def __init__(self, color):
        self.type = ''
        self.color = color
        self.water_level = 0.0
        self.needs_water_at = 0
        self.absorption_rate = 0.0

    def getStatus(self):
        if self.water_level <= self.needs_water_at:
            print("The " + self.color + " " + self.type + " needs water")
        else:
            print("The " + self.color + " " + self.type + " does not need water")
