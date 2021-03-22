# Define a number based on user input
number = int(input("Enter a number: "))

# Loop while the number is not between 50 and 70
while not(number in range(50, 71)):
    print(f"{number} is not within range.")
    number = int(input("Enter a number: "))

# Alert the user when a number is within the defined range 
print(f"{number} is within range.")