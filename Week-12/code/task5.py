#! python3
# task5.py - Write a Python function that checks whether a passed string is palindrome or not called 'IsPalindrome' that returns either True or False.

def IsPalindrome(s):
    s = s.replace(' ', '').lower()
    return True if s == s[::-1] else False

print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))