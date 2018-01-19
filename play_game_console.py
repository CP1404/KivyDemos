# Using the "model" class Game to play via the console "view"

from board_game import TicTacToeGame, GameError


def display_board(board):
    for row in board:
        print("{} {} {}".format(*row))


def main():
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


main()
