from f16 import F16
from f35 import F35
from carrier import Carrier

ally1 = F35()
ally2 = F35()
ally3 = F35()
ally_carrier = Carrier()

enemy1 = F16()
enemy2 = F16()
enemy3 = F16()
enemy_carrier = Carrier()

ally_carrier.add(ally1)
ally_carrier.add(ally2)
#ally_carrier.add(ally3)

enemy_carrier.add(enemy1)
#enemy_carrier.add(enemy2)
#enemy_carrier.add(enemy3)

def attack():
    print("Fill")
    ally_carrier.fill()
    enemy_carrier.fill()
    ally_carrier.getStatus()
    enemy_carrier.getStatus()
    print("Fight")
    ally_carrier.fight(enemy_carrier)
    enemy_carrier.fight(ally_carrier)
    ally_carrier.getStatus()
    enemy_carrier.getStatus()

for _ in range(0, 5):
    attack()