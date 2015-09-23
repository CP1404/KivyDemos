from kivy.app import App
from kivy.app import Widget


# Create a custom derived Kivy App class
class HelloWorld(App):
    def build(self):
        self.root = Widget()
        return self.root  # build() always returns a widget object


# create a custom app object and start it running
HelloWorld().run()
