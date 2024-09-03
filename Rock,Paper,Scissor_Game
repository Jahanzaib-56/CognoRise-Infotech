import random
import time

print("Rock, Paper, Scissor")

choices = ["Rock", "Paper", "Scissor"]

# Initial game state
You_Won = 0
Computer_Won = 0
Games_tied = 0

# Using for loop for a 3-rounds game
for _ in range(3):
    user_choice = input("Enter your choice: ")
    print(f"Your choice is: {user_choice}")

    time.sleep(2)
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    time.sleep(2)

    # Using COnditionals to get result
    if (user_choice == computer_choice):
        result = "Game tied"
        print(result)
    elif (user_choice == "Rock" and computer_choice == "Paper"):
        result = "Computer Won"
        print(result)
    elif (user_choice == "Rock" and computer_choice == "Scissor"):
        result = "You Won"
        print(result)        
    elif (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Won"
        print(result)
    elif (user_choice == "Paper" and computer_choice == "Scissor"):
        result = "Computer Won"
        print(result)
    elif (user_choice == "Scissor" and computer_choice == "Paper"):
        result = "You Won"
        print(result)
    elif (user_choice == "Scissor" and computer_choice == "Rock"):
        result = "Computer Won"
        print(result)

    time.sleep(2)    


    # Final Game State
    if (result == "Computer Won"):
        Computer_Won += 1
    elif (result == "You Won"):
        You_Won += 1
    elif (result == "Game tied"):
        Games_tied += 1

time.sleep(2)

# Displaying final result
print(f"You have won {You_Won} games.")
print(f"Computer has won {Computer_Won} games.")
print(f"{Games_tied} games have no result.")                                    

