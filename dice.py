#!/home/nate/python/python_env/bin/python3
import random

name = input(f"What" "s your name?\n")
welcome = f"Hello, {name}!\n\nWelcome to Dice Rolling.\nYou will be rolling two six-sided dice."
die_6_1 = [1, 2, 3, 4, 5, 6]
die_6_2 = [1, 2, 3, 4, 5, 6]


def begin():
    while True:
        quit = ["quit", "Quit"]
        d = ""
        d = input(f'\nPress Enter to roll your dice. Type "quit" to quit.\n')
        if d in quit:
            break
        random.shuffle(die_6_1)
        random.shuffle(die_6_2)
        if (die_6_1[-3] + die_6_2[-3]) == 7:
            print(
                f"\nYou rolled {die_6_1[-3]} and {die_6_2[-3]}.\n\nSeven out. Game over.\n"
            )
            break
        else:
            print(f"You rolled\n\n {die_6_1[-3]} and {die_6_2[-3]}.\n")


print(welcome)
begin()
