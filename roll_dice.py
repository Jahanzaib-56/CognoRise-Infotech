from random import randint

print("Roll Dice Simulator")

def dice_roll():
    for i in range(3):
        call = randint(1, 6)
        print(call)
        if (call != 6):
            break

def main():
    dice_roll()

if __name__ == "__main__":
    main()    