#Paper-Scissors-Rock

import random

print("Lets try to play a game!")
should_continue = True
while should_continue:
    player_choice = input('Player choice: [R/S/P]').lower()
    if player_choice not in ['r', 's', 'p']:
        print("Incorrect input")
        continue
    gen = {1: "r", 2: "p", 3: "s"}
    computer_choice = gen[random.randint(1, 3)]

    print(f'Computer choice = {computer_choice}')

    winning_combinations = [("p", "r"), ("r", "s"), ("s", "p")]

    if player_choice == computer_choice:
        print("A draw")
    elif (player_choice, computer_choice) in winning_combinations:
        print("player wins")
    else:
        print("Computer wins")

    should_continue = input("Would u like to continue? [y/n]").lower() == "y"




