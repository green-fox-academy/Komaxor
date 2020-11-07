#  Create a function that takes a string and a list of string as a parameter
#  Returns the index of the string in the list where the first string is part of
#  Only need to find the first occurence and return the index of that
#  Returns `-1` if the string is not part any of the strings in the list

def substrlist(str, words):
    for item in words:
        match = item.find(str)
        if match != -1:
            break
    print(match)
'''
        for i in item:
            for j in range (0, len(item) - len(str)):
                print(i, str[j], j, len(str) - 1)
                if i != str[j]:
                    print(i)
                    break
                elif j == len(str) - 1:
                    print(words.index(item))

                if str[i + j] != keyword[j]:
                    break
                elif j == len(keyword) - 1:
                    print(i)


'''
#  Example
print(substrlist("ching", ["this", "is", "what", "I'm", "searching", "in"]))
#  should print: `4`
print(substrlist("not", ["this", "is", "what", "I'm", "searching", "in"]))
#  should print: `-1`