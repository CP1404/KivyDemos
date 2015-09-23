from kivy.app import App
from kivy.lang import Builder


class AnchorLayoutDemo(App):
    def build(self):
        self.title = "Anchor Layout Demo"
        self.root = Builder.load_file('anchor_layout.kv')
        return self.root


# create and start the App running
AnchorLayoutDemo().run()
