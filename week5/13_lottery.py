# Create a method that find the 5 most common lottery numbers in lottery.csv
import csv

lottery_file = 'week5/lottery.csv'

def five_most_frequent():
    winning_numbers = []
    occurences = {}
    with open(lottery_file, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for line in csv_reader:
            winning_numbers.append(line[11])
            winning_numbers.append(line[12])
            winning_numbers.append(line[13])
            winning_numbers.append(line[14])
            winning_numbers.append(line[15])
        for i in range(1, 90):
            num = str(i)
            occurences[i] = winning_numbers.count(num)
        print(occurences)

five_most_frequent()