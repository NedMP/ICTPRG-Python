# Request two numbers and an Arithmetic Operator
num1 = int(input("Enter your first number: "))
oper = input("Enter +, -, *, / or ^ ")
num2 = int(input("Enter your second number: "))

# Check the Operator and perform MATHMATICS!
if oper == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif oper == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif oper == "*":
    print(f"{num1} x {num2} = {num1 * num2}")
elif oper == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif oper == "^":
    print(f"{num1} ^ {num2} = {num1 ** num2}")

# ERROR
else:
    print("There was an error, please try again!")