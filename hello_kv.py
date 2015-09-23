from kivy.app import App
from kivy.lang import Builder


# The custom App class
#   Widget creation code is removed
#   Another example of abstraction at work!
class HelloKv(App):
    def build(self):
        self.title = "Hello world!"
        self.root = Builder.load_file('widget.kv')
        return self.root


# create and start the App running
HelloKv().run()
