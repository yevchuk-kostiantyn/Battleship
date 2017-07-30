from play import play_game


def build_board():
    board = []
    for x in range(0, 5):
        board.append(["O"] * 5)
    return board


def print_board(board):
    for row in board:
        print(" ".join(row))


def run_game():
    play_game()
