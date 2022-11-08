from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from board_game import TicTacToeGame


class TicTacToe(App):
    status_message = StringProperty('shall we play a game?')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game = TicTacToeGame()

    def build(self):
        self.title = "Tic Tac Toe! Version 2"
        self.root = Builder.load_file('game_v2.kv')
        return self.root

    def pressed(self, button):
        move = self.game.make_move(button.row, button.column)
        button.text = move
        if self.game.is_over():
            self.status_message = "game over!"
            self.root.ids.game_grid.disabled = True


TicTacToe().run()
