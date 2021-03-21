# Define a list of vowels
vowels = ["a", "e", "i", "o", "u"]

# Take a word from the user 
word = input("Enter a word: ")

# Add each vowel in a list of vowels to a new list if it is found in the string word
vowelInWord = [i for i in vowels if i in word]

# Define a new string
finalStr = ""

# For each vowel in found in the word, add it to a string with a , between each one
for i in vowelInWord: 
    finalStr = f"{finalStr}, {i}"

# Check how many vowels were found and respond to it - [2:] is slicing the finalStr to prevent an extra ,
if len(vowelInWord) == 0: 
    print(f"There were no vowels found in {word}.")
elif len(vowelInWord) == 1: 
    print(f"{finalStr[2:]} was found in {word}.")
else:
    print(f"{word} contained {finalStr[2:]}.")