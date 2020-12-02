class PetrolStation:
    fuel_amount = 0

    def __init__(self, fuel_amount):
        self.fuel_amount = fuel_amount

    def fill(self, car):
        difference = car.get_capacity() - car.get_fuel_amount()
        car.set_fuel_amount(car.getcapacity)
        self.fuel_amount -= difference
