from random_ship import random_row, random_col
from main import build_board, print_board


def play_game():
    board = build_board()
    ship_row = random_row(board)
    ship_col = random_col(board)

    print("Ship Row: ", ship_row)
    print("Ship Col: ", ship_col)

    for turn in range(4):
        print("Turn:", turn + 1)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sank my battleship")
            print_board(board)
            break
        else:
            if (guess_row not in range(5)) or (guess_col not in range(5)):
                print("Oops, that's not even in the ocean.")
            elif board[guess_row] == "X" and board[guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                print("Guess row:", guess_row)
                print("Guess Col:", guess_col)
                board[guess_row][guess_col] = "X"
                print_board(board)
                if turn == 3:
                    print("Game Over")