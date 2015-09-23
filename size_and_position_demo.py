from kivy.app import App
from kivy.lang import Builder


class SizePositionDemo(App):
    def build(self):
        self.title = "Size and position demo"
        self.root = Builder.load_file('size_position.kv')
        return self.root


# create and start the App running
SizePositionDemo().run()
