

'''
def substr(str, keyword):
    pos = str.find(keyword)
    print(pos)

substr("this is what I'm searching in", "search")
'''

def substr(str, keyword):
    for i in range (0, len(str) - len(keyword)):
        for j in range (0, len(keyword)):
            if str[i + j] != keyword[j]:
                break
            elif j == len(keyword) - 1:
                print(i)

substr("this is what I'm searching in", "is")