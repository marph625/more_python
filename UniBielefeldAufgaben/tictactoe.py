# A Game of Tic Tac Toe
print("Let's play a Game of Tic Tac Toe o_O")

game_active = True
player_current = "X"

# As lists begin with the index [0] I create an empty first element to avoid confusions later
field = [" ",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]


# Set ANSI-Colors
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'


# Print field
def field_print():
    print(field[1] + "|" + field[2] + "|" + field[3] + RESET + "\n" +
          field[4] + "|" + field[5] + "|" + field[6] + RESET + "\n" +
          field[7] + "|" + field[8] + "|" + field[9] + RESET)


# Player Input and error checking
def player_input():
    global game_active
    while True:
        player_turn = input("Enter a field: ")
        # End the game prematurely by entering 'q'
        if player_turn == "q":
            game_active = False
            print("Program successfully shut down.")
            return
        try:
            player_turn = int(player_turn)
        except ValueError:
            print("Please enter a number from 1 to 9")
        else:
            if 1 <= player_turn <= 9:
                if field[player_turn] == "X" or field[player_turn] == "O":
                    print("This field is already occupied - choose another one!")
                else:
                    return player_turn
            else:
                print("Number must be between 1 and 9")


# Pretty self explaining
def player_change():
    global player_current
    if player_current == "X":
        player_current = "O"
    else:
        player_current = "X"


# Check if a player has won
def check_win():
    # if 3 fields in a row are the same, player has won
    # check for rows
    if field[1] == field[2] == field[3]:
        return field[1]
    if field[4] == field[5] == field[6]:
        return field[4]
    if field[7] == field[8] == field[9]:
        return field[7]
    # check for columns
    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[2]
    if field[3] == field[6] == field[9]:
        return field[3]
    # Check for diagonals
    if field[1] == field[5] == field[9]:
        return field[5]
    if field[3] == field[5] == field[7]:
        return field[5]


def check_draw():
    if (field[1] == "X" or field[1] == "O") \
        and (field[2] == "X" or field[2] == "O") \
        and (field[3] == "X" or field[3] == "O") \
        and (field[4] == "X" or field[4] == "O") \
        and (field[5] == "X" or field[5] == "O") \
        and (field[6] == "X" or field[6] == "O") \
        and (field[7] == "X" or field[7] == "O") \
        and (field[8] == "X" or field[8] == "O") \
            and (field[9] == "X" or field[9] == "O"):
        return "draw"


# print field
field_print()

# MAIN GAME LOOP
while game_active:
    # Active player's input
    print(f"It's player {player_current}'s turn")
    turn = player_input()
    if turn:
        # overwrite field with turn
        field[turn] = GREEN + "X" + RESET if player_current == "X" else RED + "O" + RESET
        # print field
        field_print()
        # check if player won
        win = check_win()
        if win:
            print(f"Player {win} has won!")
            game_active = False
        # check if draw
        draw = check_draw()
        if draw:
            print("It's a draw!")
            game_active = False
        # Change player
        player_change()
