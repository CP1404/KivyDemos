from kivy.app import App
from kivy.lang import Builder


class TicTacToe(App):
    def build(self):
        self.title = "Tic Tac Toe! Version 1"
        self.root = Builder.load_file('game_v1.kv')
        return self.root


# create and start the App running
TicTacToe().run()
