class Garden:

    def __init__(self):
        self.plants = []

    def water(self, amount):
        needs_water = []
        for plant in self.plants:
            if plant.water_level <= plant.needs_water_at:
                needs_water.append(plant)
        if len(needs_water) == 0:
            print("No plant needs water")
            return
        else:
            each_gets = amount / len(needs_water)
            for plant in needs_water:
                plant.water_level += each_gets

    def add(self, plant):
        self.plants.append(plant)

    def get_Status(self):
        for plant in self.plants:
            plant.get_Status()