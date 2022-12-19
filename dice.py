#!/home/nate/python/python_env/bin/python3
import random

name = input("What's your name?\n")
welcome = f"Hello, {name}!\n\nWelcome to Dice Rolling.\nYou will be rolling two six-sided dice."

def six_sided_2_dice():
    while True:
        x = input(f'\nPress Enter to roll your dice. Type "quit" to quit.\n')
        if x.lower() == "quit":
            break

        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)

        if (die_1 + die_2) == 7:
            print(f"\nYou rolled {die_1} and {die_2}.\n\nSeven out. Game over.\n")
            break
        else:
            print(f"\nYou rolled {die_1} and {die_2}.\n")

print(welcome)
six_sided_2_dice()
