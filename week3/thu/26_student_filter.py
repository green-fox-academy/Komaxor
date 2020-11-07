students = [
        {'name': 'Mark', 'age': 9.5, 'candies': 2},
        {'name': 'Sean', 'age': 10, 'candies': 1},
        {'name': 'Clark', 'age': 7, 'candies': 3},
        {'name': 'Paul', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

total_candies = []
def many_candies(students):
    for item in students:
        for i in item:
            if i == 'candies' and item[i] > 4:
                total_candies.append(item['name'])
    print(total_candies)

many_candies(students)

# create a function that takes a list of students and prints:
#  - how many candies they have on average

total_candies = []
def avg_candies(students):
    for item in students:
        for i in item:
            if i == 'candies':
                total_candies.append(item[i])
    print(sum(total_candies) / len(students))

avg_candies(students)
