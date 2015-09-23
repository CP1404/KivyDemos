from kivy.app import App
from kivy.lang import Builder


class HintsDemo(App):
    def build(self):
        self.title = "Layout Hints Demo"
        self.root = Builder.load_file('hints_demo.kv')
        return self.root


# create and start the App running
HintsDemo().run()
