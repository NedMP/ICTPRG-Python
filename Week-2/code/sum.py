# Take two numbers as strings and save them as num1 and num2
num1 = input("What is your first number? ")
num2 = input("What is your second number? ") 

# Convert the two numbers to integers
intNum1 = int(num1)
intNum2 = int(num2)

# Display basic mathmatics for each
print(num1 + " x " + num2 + " = " + str(intNum1 * intNum2))
print(num1 + " + " + num2 + " = " + str(intNum1 + intNum2))
print(num1 + " - " + num2 + " = " + str(intNum1 - intNum2)) 

if intNum1 // intNum2 == 0:
  print(num1 + " / " + num2 + " = " + str(intNum1 / intNum2)) 
elif intNum1 % intNum2 != 0:
  print(num1 + " / " + num2 + " = " + str(intNum1 // intNum2) + " With a remainder of " + str(intNum1 % intNum2)) 
else:
  print("ERROR!")