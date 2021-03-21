fullName = input("Full Name: ")
nameList = fullName.split(" ")

print("Initials: ", end="")
for i in nameList:
    print(i[0].upper(), end="")
print()