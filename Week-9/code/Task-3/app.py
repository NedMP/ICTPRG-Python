inputFile = open('names.txt', 'r')
outputFile = open('names-formatted.txt', 'w')

for l in inputFile:
    name = l.title()
    outputFile.write(name)

inputFile.close()
outputFile.close()