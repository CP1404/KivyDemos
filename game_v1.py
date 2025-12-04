from kivy.app import App
from kivy.lang import Builder


class TicTacToe(App):
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Tic Tac Toe! Version 1"
        self.root = Builder.load_file('game_v1.kv')
        return self.root


# Create and run the App
TicTacToe().run()
