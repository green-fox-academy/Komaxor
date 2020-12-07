class Aircraft:

    def __init__(self):
        self.type = ''
        self.max_ammo = 0
        self.base_damage = 0
        self.ammo_stock = 0

    def fight(self):
        damage = self.ammo_stock * self.base_damage
        self.ammo_stock = 0
        return damage

    def refill(self, available_ammo):
        ammo_needed = self.max_ammo - self.ammo_stock
        if ammo_needed <= available_ammo:
            self.ammo_stock += ammo_needed
        elif ammo_needed > available_ammo:
            self.ammo_stock += available_ammo
        return self.ammo_stock

    def getType(self):
        print(self.type)

    def getStatus(self):
        print("Type: " + self.type + ", Ammo: " + str(self.ammo_stock) +
              ", Base damage: " + str(self.base_damage) + ", Total damage: "
              + str(self.ammo_stock * self.base_damage))

    def isPriority(self):
        if self.type == 'F35':
            return True
        elif  self.type == 'F16':
            return False