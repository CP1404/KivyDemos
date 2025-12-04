"""
CP1404/CP5632 - Kivy Demo
Using the "model" class Game to play via the console "view"
"""

from board_game import TicTacToeGame, GameError


def main():
    """Console version of Tic Tac Toe game."""
    game = TicTacToeGame()
    while not game.is_over():
        try:
            display_board(game.board)
            row = int(input('Enter row: '))
            column = int(input('Enter column: '))
            try:
                game.make_move(row, column)
            except GameError as error:
                print(error)
        except ValueError:
            print('Invalid input.Try again.')
    display_board(game.board)


def display_board(board):
    """Print the current state of the game board."""
    for row in board:
        print(f"{row[0]} {row[1]} {row[2]}")


main()
