import random

bullseye = random.randint(1,100)

def newGame():
    bullseye = random.randint(1,100)
    winState = False

    while winState == False:
        guess = input("Take a guess! ")
        if guess == str(bullseye):
            print("You got it!")
            winState = True
        elif guess == "x":
            print(bullseye)
        else:
            print("WRONG!")


newGame()