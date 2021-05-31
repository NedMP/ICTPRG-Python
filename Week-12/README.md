# WEEK TWELVE 
---
1. *Write a Python function to add two numbers and return the value*
```python
# Write the function between the START and END tags
# START



# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(AddTwoNumbers(1, 2) == 3))
print("Test 2 Passed: " + str(AddTwoNumbers(5, 6) == 11))
print("Test 3 Passed: " + str(AddTwoNumbers(9, 0) != 10))
```
2. *Write a Python function to add a string in-between two strings and return it.*
```python
# Write the function between the START and END tags
# START



# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(AddInString("Hello, ", "bob", ". How are you today?") == "Hello, bob. How are you today?"))
print("Test 2 Passed: " + str(AddInString("Woah there ", "frank", ", watch your step!") == "Woah there frank, watch your step!"))
print("Test 3 Passed: " + str(AddInString("Whats the , ", "meaning", " of all of this?") != "What is the meaning of all of this"))
print("Test 4 Passed: " + str(AddInString("Happy ", "Lappy", " Tappy") == "Happy Lappy Tappy"))
```
3. *Write a Python function that returns the sum of all numbers of Fibonacci to the provided count.*
```python
# Write the function between the START and END tags
# START



# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))
```
4. *Write a Python function to multiply all the numbers in a list called 'MultiplyElementsInList'.*
```python
# Write the function between the START and END tags
# START



# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(MultiplyElementsInList([1, 2, 3]) == 6))
print("Test 2 Passed: " + str(MultiplyElementsInList([0, 2, 3]) == 0))
print("Test 3 Passed: " + str(MultiplyElementsInList([2, 2, 2]) == 8))
print("Test 4 Passed: " + str(MultiplyElementsInList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 30414093201713378043612608166064768844377641568960512000000000000))
```
5. *Write a Python function that checks whether a passed string is palindrome or not called 'IsPalindrome' that returns either True or False.
> Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., `madam` or `nurses run`.*
```python
# Write the function between the START and END tags
# START



# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))
```
6. *Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically called 'SortWordsAlphabetically'.*
```python
# Write the function between the START and END tags
# START



# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))
```
7. *Write a function called 'PrintBoxByWidth' that prints out a box that looks like below, at the specified width. DO NOT add or edit any print statements in the code provided; you may only move them around your code.*
```
PrintBoxByWidth(60) => 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x                                                          x
xoooooooooooooooooooooooooooooooooooooooooooooooooooooooooox
x                                                          x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
```python
print("x", end='')
print("o", end='')
print(" ", end='')
print("")
```