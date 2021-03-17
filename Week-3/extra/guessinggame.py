import random

bullseye = random.randint(1,100)

def newGame():
    print("==================================")
    print("    PLEASE SELECT A DIFFICULTY    ")
    print("==================================")
    print("")
    print("  - 1: 0 - 10                     ")
    print("  - 2: 0 - 100                    ")
    print("  - 3: 0 - 1000                   ")
    print("")
    difficulty = input("Enter a number to select! ")
    print("==================================")
    print(f"You have selected.... Level {difficulty}!")
    print("==================================")

    if difficulty == "1":
        bullseye = random.randint(1,10)
        turnsRemain = 5
    elif difficulty == "2":
        bullseye = random.randint(1,100)
        turnsRemain = 5
    elif difficulty == "3":
        bullseye = random.randint(1,1000)
        turnsRemain = 5
    else:
        print(f"{difficulty} is not a valid difficulty.")
        turnsRemain = -1
    
    winState = False

    while winState == False and turnsRemain >= 0:
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

