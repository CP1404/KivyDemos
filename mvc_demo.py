"""
Kivy example for CP1404/CP5632, IT@JCU
This shows the use of a StringProperty object to store the "model" of MVC
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MVCDemo(App):
    """The class variable in the app is the 'model'."""
    message = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Simple MVC Demo"
        self.root = Builder.load_file('mvc.kv')
        self.message = "Type in the field & press Enter"
        return self.root

    def handle_update(self):
        """Handle changes to the text input by updating the model from the view."""
        self.message = self.root.ids.user_input.text


# create and start the App running
MVCDemo().run()
