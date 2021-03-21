# Ask the user for their grade and save it as a variable
try:
    grade = int(input("What was your grade? "))
except ValueError:
    print("Please enter a valid grade.")
    quit()

if grade > 100:
    print("Please enter a valid grade.")

# A high distinction is greater than or equal to 90
elif grade <= 100 and grade >= 90:
    print("You will recieve a \"High Distinction\"")

# A distinction is less than 90 and greater than or equal to 80
elif grade < 90 and grade >= 80:
    print("You will recieve a \"Distinction\"")

# A distinction is less than 80 and greater than or equal to 70
elif grade < 80 and grade >= 70:
    print("You will recieve a \"Credit\"")

# A distinction is less than 70 and greater than or equal to 50
elif grade < 70 and grade >= 50:
    print("You will recieve a \"Pass\"")

# Any other grade is a fail
else: 
    print("You failed.") 