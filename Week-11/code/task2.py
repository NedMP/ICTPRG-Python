# Write a program called 'GetWordsFromUser' that takes a Min and Max as a parameter. The function then takes an input from the user and ensures that the input has at least or at most the specified amount of words. Keep on asking the user until the amount of words is within range, the program then outputs all words lowercase and separated in a list.

def GetWordsFromUser(min, max):
    wordList = []

    while len(wordList) not in range(min, (max + 1)):
        words = input("Enter some words: ")
        for i in words.lower().split(" "): wordList.append(i)

    print(wordList)

GetWordsFromUser(8, 15)