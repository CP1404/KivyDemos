from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class MVCDemo(App):
    message = StringProperty()

    def build(self):
        self.title = "Simple MVC Demo"
        self.root = Builder.load_file('mvc.kv')
        return self.root

    def handle_press(self):
        self.message = self.root.ids.user_input.text



# create and start the App running
MVCDemo().run()
