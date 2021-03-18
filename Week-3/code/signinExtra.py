# Create a key:value dictionary using the format username:password
users = {
    "bob": "password1234",
    "fred": "happyPass122",
    "lock": "passwithlock44"
}

# Request the user's credentials and save them as variables
username = input("Enter your username: ")
password = input("Enter your password: ")

# Try will attempt to run some code in case of an error
try:

    # Check if the dictionary key (username) matches the associated password
    if users[username] == password:
        print("Access Granted!")
    else:
        print("Access Denied!")

# Except KeyError handles errors if the username is not found in the dictionary as a key
except KeyError:
    print("Access Denied!")

# ========================================================================================

# username == input("Enter your username: ")
# password == input("Enter your password: ")

# if username == "bob" and password == "password1234": 
#     print("Access Granted!")
# elif username == "fred" and password == "happyPass122": 
#     print("Access Granted!")
# elif username == "lock" and password == "passwithlock44": 
#     print("Access Granted!")
# else: 
#     print("Access Denied!")