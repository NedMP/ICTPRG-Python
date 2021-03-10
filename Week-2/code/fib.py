num1 = 0
num2 = 1
count = 0

while count < 16:
  print(num1) 
  current = num1 + num2
  num1 = num2
  num2 = current
  count += 1