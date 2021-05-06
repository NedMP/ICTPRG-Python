username = input("Username? ")
password = input("Password? ")

userPass = f"{username}:{password}"

inputFile = open('logins.txt', 'r')

for i in inputFile:
    if userPass == i.strip():
        print("Access Granted!")
        exit()

inputFile.close()

print("Access Denied...")