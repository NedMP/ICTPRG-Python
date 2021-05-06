outputFile = open('maths.txt', 'w')

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

sum = x + y

outputFile.write(str(sum))

outputFile.close()