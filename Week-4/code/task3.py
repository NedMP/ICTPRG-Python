number = int(input("Enter a number: "))

while not(number in range(50, 71)):
    print(f"{number} is not within range.")
    number = int(input("Enter a number: "))

print(f"{number} is within range.")