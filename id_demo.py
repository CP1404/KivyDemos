from kivy.app import App
from kivy.lang import Builder
import random


class IDDemo(App):
    def build(self):
        self.title = "Demoing the id attribute"
        self.root = Builder.load_file('id_demo.kv')
        return self.root

    def handle_pressed(self):
        if random.randint(1, 10) <= 5:
            self.root.ids.my_label.text = "ouch!!"
        else:
            self.root.ids.my_label.text = "stop that!!"


# create and start the App running
app = IDDemo()
app.run()
