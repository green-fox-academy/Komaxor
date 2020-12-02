from petrol_station.tire import Tire

class Car:
    fuel_amount = 0
    capacity = 0

    def __init__(self, capacity):
        self.fuel_amount = 20
        self.capacity = capacity
        self.tires = [Tire(), Tire(), Tire(), Tire()]

    def get_fuel_amount(self):
        return self.fuel_amount

    def set_fuel_amount(self, fuel_amount):
        self.fuel_amount = fuel_amount

    def get_capacity(self):
        return self.capacity

    def drive(self):
        if self.fuel_amount == 0:
            print('No fuel. Car is not drivable.')
            return

        for tire in self.tires:
            print(tire.wear)
            if not tire.is_usable():
                print('Tire is not usable. Car is not drivable.')
                return

        self.fuel_amount -= 1
        for tire in self.tires:
            tire.drive()

        print('I am driving')