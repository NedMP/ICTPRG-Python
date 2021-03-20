vowels = ["a", "e", "i", "o", "u"]
word = input("Enter a word: ")
vowelInWord = [i for i in vowels if i in word]
finalStr = ""

for i in vowelInWord: 
    finalStr = f"{finalStr}, {i}"

if len(vowelInWord) == 0: 
    print(f"There were no vowels found in {word}.")
elif len(vowelInWord) == 1: 
    print(f"{finalStr[2:]} was found in {word}.")
else:
    print(f"{word} contained {finalStr[2:]}.")