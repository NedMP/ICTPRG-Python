# Write a program called 'InputNumber' that will keep asking the user to enter a value until the value is a valid number, then print it.

while True:
    isInt = input("Enter an... Integer? ")

    try: 
        print(f"You entered... {int(isInt)}... That is an integer!")
        break
    except ValueError:
        print(f"{isInt}... Is not an integer... Try again.")