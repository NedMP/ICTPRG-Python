largeNum = input("Enter a large number: ")
subTotal = 0
finalStr = ""

for i in largeNum:
    finalStr = f"{finalStr}{i} + "
    subTotal = subTotal + int(i)

print(f"{finalStr[:-3]} = {subTotal}")