accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account in a list
def get_name_and_balance(a, num):
    for item in a:
        if item['account_number'] == num:
            print(item['client_name'] + ",", item['balance'])

#egyszerusitve!
get_name_and_balance(accounts, 11234543)

# The output should be: "Igor", "203004099.2"

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

def transfer_amount(_from, _to, amount):
    account_numbers = []
    for item in accounts:
        account_numbers.append(item['account_number'])
    if _from not in account_numbers or _to not in account_numbers:
        print("404 - account not found")
    else:
        for item in accounts:
            if item ['account_number'] == _from:
                item['balance'] -= amount
            elif item ['account_number'] == _to:
                item['balance'] += amount
        print(accounts)


transfer_amount(43546731, 23456311, 500.0)
#After printing the "accounts" it should look like:
# accounts = [
#	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
#	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204099571.23 },
#	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1354100.0 }
#]