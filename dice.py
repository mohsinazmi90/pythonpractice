# 1. The Automated Dice Roller (Difficulty: Easy)

# Instead of a static script, this forces you to learn how to import external code (modules) and 
# use random generation.

# The Goal: A program that asks the user how many sides their dice has (e.g., 6, 20), 
# generates a random number between 1 and that number, prints it, and asks if they want to roll again.

# Core Concepts: import random, while loops, type casting (int()).

import random


def dice_side():
    dice_sides = None
    
    while dice_sides is None:
        try:
            dice_sides = int(input("How many sides does the dice have? "))
        except:
            print("Invalid input. Please use a number! ")
            
    return dice_sides
            

def check_roll(sides):
    
    while True:
        
        try:
            print("1. Roll Dice")
            print("2. Exit")

            selection = int(input("Make your choice: "))
        
            if selection == 1:
                roll = random.randint(1, sides)
                print(f"Dice Roll: {roll}\n")
            elif selection == 2:
                print("Exiting program")
                break
            else:
                print("Invalid Choice!")
        except:
            print("Please use numbers only!")
    
        
def main():
    
    sides = dice_side()
    check_roll(sides)
        
        
if __name__ == "__main__":
    main()