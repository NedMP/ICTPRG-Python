#! python3
# task6.py - Write a Python function to add two numbers and return the valuWrite a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically called 'SortWordsAlphabetically'.

def SortWordsAlphabetically(s):
    s = [c for c in s.lower().split('-')]
    s.sort()
    return '-'.join(s)
    
print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))