total = 0
current = 0

while current != "x":
    total = total + int(current)
    current = input("Enter a number: ")

print(f"Your total is: {total}")