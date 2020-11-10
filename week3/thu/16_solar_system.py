# Saturn is missing from the planet_list
# Insert it into the correct position

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
# Expected output: "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"

def put_saturn(planet_list):
    index = planet_list.index("Jupiter", )
    planet_list.insert(index + 1, "Saturn")
    return planet_list

print(put_saturn(planet_list))