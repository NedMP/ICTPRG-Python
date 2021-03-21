current = input("Enter a number: ")
nums = []

while current != "x":
    nums.append(int(current))
    current = input("Enter a number: ")

print(f"You entered: {nums}")