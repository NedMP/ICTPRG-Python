currentIn = input("Enter a number: ")
seen = []
duplicates = []

while currentIn != "x":
    current = int(currentIn)
    if current in duplicates:
        seen.append(current)
    elif current in seen:
        duplicates.append(current)
    else:
        seen.append(current)
    currentIn = input("Enter a number: ")

print(duplicates)