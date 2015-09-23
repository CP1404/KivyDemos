from kivy.app import App
from kivy.app import Widget
from kivy.config import Config


class HelloWorld(App):
    def build(self):
        self.title = "Hello world!"
        return Widget()


# Config.set('graphics', 'resizable', True)
# Config.set('graphics', 'width', 300)
# Config.set('graphics', 'height', 200)

HelloWorld().run()
