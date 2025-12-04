"""CP1404/CP5632 - Kivy Demo"""
from kivy.app import App
from kivy.lang import Builder


class AnchorLayoutDemo(App):
    """Demo of AnchorLayout"""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Anchor Layout Demo"
        self.root = Builder.load_file('anchor_layout.kv')
        return self.root


# Create and start the App running
AnchorLayoutDemo().run()
