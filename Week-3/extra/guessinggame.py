import random

bullseye = random.randint(1,100)

def newGame():
    bullseye = random.randint(1,100)
    winState = False
    turnsRemain = 5

    while winState == False:
        guess = int(input("Take a guess! "))

        if guess == bullseye:
            print("You got it!")
            winState = True
        elif turnsRemain == 0:
            print(f"You lost the game! The answer was... {bullseye}")
            break
        elif guess > bullseye:
            print(f"You're a bit high! - {turnsRemain} turns remain.")
            turnsRemain -= 1
        elif guess < bullseye:
            print(f"You're a bit low! - {turnsRemain} turns remain.")
            turnsRemain -= 1
        else:
            print("Error!")
            turnsRemain = 0


newGame()