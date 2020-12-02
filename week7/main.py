from petrol_station.car import Car
from petrol_station.petrol_station import PetrolStation
from speed_trap.speed_trap import SpeedTrap

opel = Car(50)
suzuki = Car(40)

shell = PetrolStation(5000)

for i in range(0, 10):
    opel.drive()

'''
print(opel.fuel_amount)
print(shell.fuel_amount)
shell.fill(opel)
print(opel.fuel_amount)
print(shell.fuel_amount)

print(suzuki.fuel_amount)
print(shell.fuel_amount)
shell.fill(suzuki)
print(suzuki.fuel_amount)
print(shell.fuel_amount)
'''

speed_trap = SpeedTrap()
speed_trap.measure()
print("Your speed in km/h is: " + str(speed_trap.get_speed()))