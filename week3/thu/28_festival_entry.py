watchlist = []

security_alcohol_loot = 0

queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Mark', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

# Queue of festivalgoers at entry
# no. of alcohol units
# no. of guns

# Create a security_check function that returns a list of festivalgoers who can enter the festival (only the names)

# If guns are found, remove them and put them on the watchlist (only the names), they can not enter the festival
# If alcohol is found confiscate it (set it to zero and add it to security_alchol_loot) and let them enter the festival


def check(loot):
    for item in queue:
        for i in item:
            if i == 'alcohol':
                loot += item[i]
                item[i] = 0
            if i == 'guns' and item[i] != 0:
                watchlist.append(item['name'])
    print(loot) #NOTE return or not?
    #return loot

check(security_alcohol_loot)
print(watchlist)