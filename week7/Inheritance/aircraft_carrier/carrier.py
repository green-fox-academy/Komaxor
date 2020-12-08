class Carrier:

    def __init__(self):
        self.ammo_stock = 2300
        self.aircrafts = []
        self.health = 5000
        self.total_dmg = 0

    def add(self, aircraft):
        self.aircrafts.append(aircraft)

    def total_damage(self):
        self.total_dmg = 0
        for aircraft in self.aircrafts:
            self.total_dmg += (aircraft.calculate_damage())
        return self.total_dmg

    def ammo_needed(self):
        ammo_needed = 0
        for aircraft in self.aircrafts:
            ammo_needed += (aircraft.max_ammo - aircraft.ammo_stock)
        return ammo_needed

    def fill(self):
        if len(self.aircrafts) <= 0:
            return "No aircrafts available, Jim!"
        else:
            needed_ammo = self.ammo_needed()
            if self.ammo_stock <= 0:
                print("Jim, we are out of ammo!")
            elif self.ammo_stock < needed_ammo:
                queue = []
                for aircraft in self.aircrafts:
                    if aircraft.isPriority() == True:
                        queue.insert(0, aircraft)
                    else:
                        queue.append(aircraft)
                for aircraft in queue:
                    aircraft.refill(self.ammo_stock)
                    self.ammo_stock -= aircraft.ammo_stock
            else:
                for aircraft in self.aircrafts:
                    aircraft.refill(self.ammo_stock)
                    self.ammo_stock -= aircraft.ammo_stock

    def fight(self, another_carrier):
        for aircraft in self.aircrafts:
            another_carrier.health -= aircraft.fight()
        if another_carrier.health <= 0:
            another_carrier.die()

    def getStatus(self):
        print("HP: " + str(self.health) + ", Aircraft count: " +
              str(len(self.aircrafts)) + ", Ammo storage: " + str(self.ammo_stock) +
              ", Total damage: " + str(self.total_damage()))
        for aircraft in self.aircrafts:
            aircraft.getStatus()

    def die(self):
        print("It's dead Jim :(")
