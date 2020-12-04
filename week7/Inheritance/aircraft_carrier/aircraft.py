class Aircraft:
    ammo_stock = 0

    def fight(self):
        damage = self.ammo_stock * self.base_damage
        self.ammo_stock = 0
        return damage

    def refill(self, available_ammo):
        space = self.max_ammo - self.ammo_stock
        if space <= available_ammo:
            self.ammo_stock =+ space
        elif space > available_ammo:
            self.ammo_stock =+ available_ammo

    def __init__(self):
        self.type = ''
        self.max_ammo = 0
        self.base_damage = 0
        self.ammo_stock = 0

    def getType(self):
        print(self.type)

    def getStatus(self):
        print("Type: " + self.type + ", Ammo: " + str(self.ammo_stock) + ", Base damage: " + str(self.base_damage) + ", Total damage: " + str(self.fight()))

    def isPriority(self):
        print(self.type)