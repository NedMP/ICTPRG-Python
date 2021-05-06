import math

outputFile = open('factorial.txt', 'w')

for i in range(1, 11):
    outputFile.write(f"{math.factorial(i)}\n")