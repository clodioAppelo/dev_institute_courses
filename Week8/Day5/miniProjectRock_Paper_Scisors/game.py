# Mini-Project: Rock, Paper, Scissors
# game.py – this file/module should contain a class called Game. It should have 4 methods:
# get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.

# get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).

# get_game_result(self, user_item, computer_item) – Determine the result of the game.
# Parameters:
# user_item – the user’s chosen item (rock/paper/scissors)
# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
# Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
# Get the user’s item (rock/paper/scissors) and remember it

# Get a random item for the computer (rock/paper/scissors) and remember it

# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”

# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

import random


class Game:
    def __init__(self) -> None:
        self.game_list = ["r", "p", "s"]

    def get_user_item(self):
        user_item = input(
            "Please select (R)ock, (P)aper, (S)cisors to play: ").lower()
        while True:
            if user_item not in self.game_list:
                print(" Please enter r, p, or s")
            else:
                return user_item

    def get_computer_item(self):
        self.computer_pick = random.choice(["r", "p", "s"])
        return random.choice("r", "p", "s")
        # return win, draw or loss

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            print(f"Both players selected {user_item}. It's a tie!")
        elif user_item == "r":
            if computer_item == "s":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_item == "p":
            if computer_item == "r":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_item == "s":
            if computer_item == "p":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

    def play(self):
        user_item = Game.get_user_item
        computer_item = Game.get_computer_item
        print(f"You Picked {user_item}, The computer picked {computer_item}.")
        Game.get_game_result()


game = Game()
game.play
