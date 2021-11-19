# What You Will Create
# Create a TicTacToe game in python, where two users can play together.

'''This program was my first option, but i must admit is a too bit complicated, and after talking to my daughter i have decided to do something similar to her, since it is much more simple and readible, but I leave the code in case it you would like to see it'''

# def drawfield(field):
#     for row in range(5):  # 0,1,2,3,4
#         if row % 2 == 0:  # print wrtitting lines
#             practical_row = int(row/2)
#             for column in range(5):    # 0,1,2,3,4
#                 if column % 2 == 0:
#                     practical_column = int(column/2)
#                     if column != 4:
#                         print(field[practical_column][practical_row], end="")
#                     else:
#                         print(field[practical_column][practical_row])
#                 else:
#                     print("|", end="")
#         else:
#             print("-----")


# player = 1
# current_Field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
# drawfield(current_Field)

# while True:
#     print("players turn: \n", player)
#     moveRow = int(input("please, enter the row: \n"))
#     moveColumn = int(input("Please enter the column: \n"))
#     if player == 1:
#         # make move for player 1
#         current_Field[moveColumn][moveRow] = "X"
#         player = 2
#     else:
#         # make move for player 2
#         current_Field[moveColumn][moveRow] = "O"
#         player = 1
#     drawfield(current_Field)


board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


game_still_going = True


winner = None


current_player = "X"


# Play a game of tic tac toe
def play_game():

    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # Since the game is over, print the winner or tie
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner is None:
        print("Tie.")


def display_board():
    print("\n")
    print("*************")
    print("* " + board[0] + " | " + board[1] +
          " | " + board[2] + " *" + "     1 | 2 | 3")
    print("* " + board[3] + " | " + board[4] +
          " | " + board[5] + " *" + "     4 | 5 | 6")
    print("* " + board[6] + " | " + board[7] +
          " | " + board[8] + " *" + "     7 | 8 | 9")
    print("*************")
    print("\n")


# Handle a turn for player
def handle_turn(player):

    print(f"{player}'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("That position is taken. Choose again.")

    board[position] = player

    display_board()


# Check if game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# Check if somebody has won
def check_for_winner():

    global winner
    # Check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# Check the rows for a win
def check_rows():
    # Set global variables
    global game_still_going
    # Check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
        # Or return None if there was no winner
    else:
        return None


# Check the columns for a win
def check_columns():

    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    else:
        return None


# Check the diagonals for a win
def check_diagonals():

    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    else:
        return None


# Check if there is a tie
def check_for_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if "-" not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False


# Flip the current player from X to O, or O to X
def flip_player():
    # Global variables we need
    global current_player
    # If the current player was X, make it O
    if current_player == "X":
        current_player = "O"
    # Or if the current player was O, make it X
    elif current_player == "O":
        current_player = "X"


play_game()
