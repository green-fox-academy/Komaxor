# Create a method that find the 5 most common lottery numbers in lottery.csv
import csv

lottery_file = 'week5/lottery.csv'

def five_most_frequent():
    winning_numbers = []
    occurences = {}
    most_common = []
    common_numbers = []
    unique_values = []
    with open(lottery_file, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for line in csv_reader:
            winning_numbers.append(line[11])
            winning_numbers.append(line[12])
            winning_numbers.append(line[13])
            winning_numbers.append(line[14])
            winning_numbers.append(line[15])
        for number in range(1, 90):
            num = str(number)
            occurences[number] = winning_numbers.count(num)
            #print(occurences)
            number_list = list(occurences.keys())
            #print(number_list)
            frequency_list = list(occurences.values())
            #print(frequency_list)
        values = sorted(occurences.values())
        for i in range(0, len(values) - 1):
            if values[i] != values[i + 1]:
                unique_values.append(values[i])
        for i in range(0, 5):
            most_common.append(max(unique_values))
            unique_values.remove(max(unique_values))
            common_numbers.append(str(number_list[frequency_list.index(most_common[i])])) #TODO create list in list to have multiple number to occurence
        print("The most common numbers are: " + common_numbers[0])
        print("The second most common numbers are: " + common_numbers[1])
        print("The third most common numbers are: " + common_numbers[2])
        print("The fourth most common numbers are: " + common_numbers[3])
        print("The fifth most common numbers are: " + common_numbers[4])

five_most_frequent()