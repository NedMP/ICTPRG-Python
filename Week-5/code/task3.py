import math

values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
subTotal = 0
mean = 0
maxNum = 0

for i in values:
    subTotal = subTotal + i
    mean = math.floor(subTotal / len(values))
    maxNum = i if i > maxNum else maxNum

print(f"Sub Total: {subTotal}")
print(f"Average: {mean}")
print(f"Maximum Number: {maxNum}")