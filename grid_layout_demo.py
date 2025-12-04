from kivy.app import App
from kivy.lang import Builder


class GridLayoutDemo(App):
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Grid Layout Demo"
        self.root = Builder.load_file('grid_layout.kv')
        return self.root


GridLayoutDemo().run()
