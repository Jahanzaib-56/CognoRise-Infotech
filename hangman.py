import random
import hangman_stages

# Defining a function for game content
def play_game():

    # List of 50 Animals
    animals = ["tiger", "lion", "elephant", "rabbit", "snake", "alligator", "bear", "sparrow", "eagle", "wolf", "giraffe", "kangaroo", "panda", "penguin", "zebra", "cheetah", "dolphin", "whale", "otter", "leopard", "shark", "hippo", "rhinoceros", "crocodile", "chimpanzee", "orangutan", "koala", "sloth", "armadillo", "ostrich", "peacock", "moose", "reindeer", "bison", "buffalo", "antelope", "hedgehog", "squirrel", "raccoon", "fox", "badger", "porcupine", "goat", "sheep", "donkey", "horse", "camel", "jaguar", "panther", "hyena"]

    # Total Chances 
    chances = 6

    # Choosing a random animal from list
    choice = random.choice(animals)

    # Displaying blank spaces instead of animal
    display = ['_'] * len(choice)
    print (display)

    # Building logics for Game function
    Game_Over = False
    while not Game_Over:

        # Taking Guess from the user
        Guess = input("Enter your Guess: ").lower()

        # Checking if guess is correct, displaying it at its respective blank space.
        for position in range(len(choice)):
            letter = choice[position]
            if letter == Guess:
                display[position] = Guess
        print(display)

        # If Guess is incorrect, Decrementing Chance(life) by 1
        if Guess not in choice:        
            chances -= 1

            # If Chances are ended
            if chances == 0:
                Game_Over = True
                print("YOU LOSE!!!")
                print(f"It was {choice}")

        # Checking if no blank space is remaining, meaning user won
        if '_' not in display:
            Game_Over = True
            print("YOU WON!!!")    

        # To display hangman at each stage of chance
        print(hangman_stages.stages[chances]) 

# Defining main function to call
def main():
    while True:
        play_game()

        # Taking user choice to Play Again
        replay = input("Do you want to play again? y/n: ").lower()
        if (replay != 'y'):
            print("Thanks for playing with us!")
            break

# Calling main function
if __name__ == "__main__":
    main()        