# Set the correct user details
correctUser = "bob"
correctPass = "password1234"

# Request a username and password from the user save them as variables
username = input("Enter username: ")
password = input("Enter password: ")

# check if the username and password match the correct login
if username == correctUser and password == correctPass:
    print("Access Granted!")
else:
    print("Access Denied!")
