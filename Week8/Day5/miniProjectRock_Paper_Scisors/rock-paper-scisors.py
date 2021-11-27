# pla again, quit, show scores
from typing import ValuesView


def get_user_menu_choice():
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        return
    else:
        menu = input('''Menu: 
        (P)lay a new game
        (S)how Scores
        (Q)uit
        your option here: ''').lower()

        while True:
            if menu not in ["p", "s", "q"]:
                print("Sorry, please enter a valid Key")
            return menu


def print_results(results):
    print("These are your results: ")
    for ker, value in Game.results.items():
        print(f"{key}: {Value}")


def main():
    menU = get_user_menu_choice
    while True:
        if menU == "q":
            print(" Good Bye! Thanks for playing, Come back soon!")
        elif menU == "p":
            new_game = Game()
            new_game.play()
        elif menU == "s":
            print_results(Game.reults)


main()
