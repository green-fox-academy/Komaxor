from aircraft import Aircraft

class F16(Aircraft):
    type = ''
    max_ammo = 0
    base_damage = 0
    ammo_stock = 0

    def __init__(self):
        self.type = "F35"
        self.max_ammo = 12
        self.base_damage = 50
        self.ammo_stock = 0

one = F16()

one.getStatus()