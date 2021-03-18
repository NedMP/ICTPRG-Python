# Ask what year the user was born and save it as birthYear
birthYear = int(input("What year were you born? "))

# Convert the birth year to an age and save as age
age = 2021 - birthYear

# Print You are age years old. 
print(f"You are {age} years old.")

# If you are under 18 years old print Go Away. Child. 
if age < 18:
    print("Go away. Child.")

# Otherwise print Come in and have a drink.
else: 
    print("Come in and have a drink!")