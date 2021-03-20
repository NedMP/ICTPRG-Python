vowels = ["a", "e", "i", "o", "u"]
word = input("Enter a word: ")
vowelInWord = [i for i in vowels if i in word]
finalStr = ""

for i in vowelInWord: 
    finalStr = f"{finalStr}, {i}"

print(finalStr)