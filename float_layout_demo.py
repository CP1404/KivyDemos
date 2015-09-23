from kivy.app import App
from kivy.lang import Builder


class FloatLayoutDemo(App):
    def build(self):
        self.title = "Float Layout Demo"
        self.root = Builder.load_file('float_layout.kv')
        return self.root


FloatLayoutDemo().run()
