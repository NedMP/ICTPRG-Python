# This is the most basic version of this code, there are a number of ways to break it. I am not checking for these.

# Define the running total
total = 0

# Define the most recent input as a string
current = 0

# Track whether the program has finished running  
finished = 0

# Continue looping while finished is equal to 0
while finished == 0: 

    # Check if the most recent input was an x
    if current == "x":
        
        # Convert the current to a string and print it
        print("Your total is: " + str(total))

        # Set finished to 1 and break the loop - this is just a switch
        finished = 1
    
    # If the current input isn't x run this code
    else:
        
        # Convert current to an integer and add it to the total 
        total = total + int(current)

        # Take a new input and set it to current
        current = input("Enter a number: ")