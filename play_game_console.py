# Using the "model" class Game to play via the console "view"

from board_game import TicTacToeGame, GameError

game = TicTacToeGame()
while not game.is_over():
    try:
        print(game)
        row = int(input('Enter row: '))
        column = int(input('Enter column: '))
        try:
            game.make_move(row, column)
        except GameError as error:
            print(error)
    except ValueError:
        print('invalid input, try again')
print(game)
