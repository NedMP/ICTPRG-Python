num1 = int(input("Enter your first number: "))
oper = input("Enter +, -, *, / or ^ ")
num2 = int(input("Enter your second number: "))

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
else:
    print("There was an error, please try again!")