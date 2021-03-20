# This imports the random number generator library for Python
import random

# Define a new game
def newGame():

    # This is ugly, it is just a multiline difficulty menu though. I could use multiple print statements but this works 
    print("""==================================
    PLEASE SELECT A DIFFICULTY    
==================================
    
      - 1: 0 - 10                     
      - 2: 0 - 100                    
      - 3: 0 - 1000                   
    """)
    difficulty = input("Enter a number to select! ")
    print(f"""==================================
You have selected.... Level {difficulty}!
==================================""")

    # The following code takes the selected difficulty level and generates a random number based on the complexity selection
    if difficulty == "1":
        bullseye = random.randint(1,10)
        turnsRemain = 5
    elif difficulty == "2":
        bullseye = random.randint(1,100)
        turnsRemain = 5
    elif difficulty == "3":
        bullseye = random.randint(1,1000)
        turnsRemain = 5

    # Throw an error and end the game if the user did not select a valid difficulty 
    else:
        print(f"{difficulty} is not a valid difficulty.")
        turnsRemain = -1
    
    # Has the user won the game?
    winState = False

    # The following runs while the user has not won and the player has 0 or more turns remaining
    while winState == False and turnsRemain >= 0:
        guess = int(input("Take a guess! "))

        # If the player gets the number, set the winState to True and end the game
        if guess == bullseye:
            print("You got it!")
            winState = True

        # This runs if the users turns remaining hits 0 - End the game
        elif turnsRemain == 0:
            print(f"You lost the game! The answer was... {bullseye}")
            break

        # States whether the player guessed high or low, and how many turns remain
        elif guess > bullseye:
            print(f"You're a bit high! - {turnsRemain} turns remain.")
            turnsRemain -= 1
        elif guess < bullseye:
            print(f"You're a bit low! - {turnsRemain} turns remain.")
            turnsRemain -= 1

        # This runs if something goes wrong
        else:
            print("Error!")
            break

# Start a new game
newGame()