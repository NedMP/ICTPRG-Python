peopleList = []

while True:
    name = input("Enter a name: ")
    if name == "":
        break
    peopleList.append(name)

outputFile = open('people.txt', 'w')

for i in peopleList:
    outputFile.write(f"{i}\n")

outputFile.close()