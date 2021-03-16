# Ask the user for their name and save it to the variable name
name = input("What is your name? ")

# Check if the users name is frank or george - this will only work on all lowercase eg. "frank" != "Frank"
if name == "frank" or name == "george": 

    # Say hello to frank or george
    print("Hello " + name)

# If their name is not frank or george
else:

    # Ask who they are
    print("Sorry, who are you?")