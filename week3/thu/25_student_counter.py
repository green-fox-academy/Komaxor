
students = [
        {'name': 'Theodor', 'age': 3, 'candies': 2},
        {'name': 'Paul', 'age': 9.5, 'candies': 2},
        {'name': 'Mark', 'age': 12, 'candies': 5},
        {'name': 'Peter', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'George', 'age': 10, 'candies': 1}
]

# create a function that takes a list of students and prints:
# - how many candies are owned by students altogether
total_candies = []
def candies(students):
    for item in students:
        for i in item:
            if i == 'candies':
                total_candies.append(item[i])
    print(sum(total_candies))

candies(students)
# create a function that takes a list of students and prints:
# - The sum of the age of people who have less than 5 candies
total_age = []
def addage(students):
    for item in students:
        for i in item:
            if i == 'candies' and item[i] < 5:
                total_age.append(item['age'])
    print(sum(total_age))

addage(students)
