#Lab03.py
def integerDivision(n, k):
    if n < k:
        return 0
    return integerDivision(n-k, k) + 1

def collectEvenInts(listOfInt):
    if len(listOfInt) == 0:
        return []
    elif listOfInt[0] % 2 == 0:
        return [listOfInt[0]] + collectEvenInts(listOfInt[1:])
    else:
        return collectEvenInts(listOfInt[1:])

def countVowels(someString):
    vowelList = ['A','E','I','O','U','a','e','i','o','u']
    if len(someString) == 0:
        return 0
    elif someString[0] in vowelList:
        return 1 + countVowels(someString[1:])
    else:
        return countVowels(someString[1:])
        
def reverseString(s):
    if len(s) == 0:
        return ''
    else:
        return s[-1] + reverseString(s[:-1])
def removeSubString(s, sub):
    if len(s) == 0:
        return ''
    elif s[:len(sub)] == sub:
        return removeSubString(s[len(sub):], sub)
    else:
        return s[0] + removeSubString(s[1:], sub)

