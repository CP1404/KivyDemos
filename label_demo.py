from kivy.app import App
from kivy.lang import Builder


class LabelDemo(App):
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = ""
        self.root = Builder.load_file('label.kv')
        return self.root


# create and start the App running
LabelDemo().run()
