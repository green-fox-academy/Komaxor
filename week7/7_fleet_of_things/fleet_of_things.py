from fleet import Fleet
from thing import Thing

fleet = Fleet()
# - You have the `Thing` class
# - You have the `Fleet` class
# - You have the `fleet_of_things.py` file
# - Download those, use those
# - In the `fleet_of_things` file create a fleet
# - Achieve this output:
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch
first = Thing("Get milk")
second = Thing("Remove the obstacles")
third = Thing("Stand up")
fourth = Thing("Eat lunch")
third.complete()
fourth.complete()
fleet.add(first)
fleet.add(second)
fleet.add(third)
fleet.add(fourth)
print(fleet)