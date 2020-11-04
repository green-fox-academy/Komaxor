'''
We are going to represent our expenses in a list containing integers.

Create a list with the following items.
500, 1000, 1250, 175, 800 and 120
Create an application which solves the following problems.
How much did we spend?
Which was our greatest expense?
Which was our cheapest spending?
What was the average amount of our spendings?
'''
expense = [500, 1000, 1250, 175, 800, 120]

def calc():
    total = sum(expense)
    greatest = max(expense)
    cheapest = min(expense)
    avg = round(total / len(expense), 2)
    print(total, greatest, cheapest, avg)

calc()