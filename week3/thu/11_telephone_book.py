'''
We are going to represent our contacts in a map where the keys are going to be strings and the values are going to be strings as well.

Create a map with the following key-value pairs.

Name (key)	Phone number (value)
William A. Lathan	405-709-1865
405-709-1865	402-247-8568
Hortensia E. Foster	606-481-6467
Amanda D. Newland	319-243-5613
Brooke P. Askew	307-687-2982
Create an application which solves the following problems.

What is John K. Miller's phone number?
Whose phone number is 307-687-2982?
Do we know Chris E. Myers' phone number?
'''

phone_book = {"William A. Lathan": "405-709-1865", "Hortensia E. Foster": "606-481-6467", "Amanda D. Newland": "319-243-5613", "Brooke P. Askew": "307-687-2982"}

def contact():
    hisnum = "Name"
    if "John K. Miller" in phone_book:
        hisnum = phone_book["John K. Miller"]
    else:
        hisnum = "I don't know"

    whosnum = "I don't know"
    for k, v in phone_book.items():
        if "307-687-2982" in v:
            whosnum = k
        else:
            whosnum = "I don't know"

    ishein = "Maybe"
    if "Chris E. Myers" in phone_book:
        ishein = "Yes"
    else:
        ishein = "No"

    print(hisnum)
    print(whosnum)
    print(ishein)

contact()