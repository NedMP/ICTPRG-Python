# I KNOW THIS IS NOT THE SOLUTION WE ARE MEANT TO BE USING BUT I FEEL LIKE IT IS MORE EFFICIENT THAN WORRYING ABOUT ELIF

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