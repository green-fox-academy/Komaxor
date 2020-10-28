num_list = [10, 30, 20, 30, 20, 40, 40]

def unique(my_list):
    new_list = []
    for number in my_list:
        if number not in new_list: 
            new_list.append(number)
    return new_list
    
print(unique(num_list))