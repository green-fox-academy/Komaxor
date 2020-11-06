# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def check_nums(nums):
    if all(x in nums for x in [4, 8, 12, 16]):
        return True

print(check_nums(list_of_numbers))