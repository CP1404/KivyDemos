from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.graphics import Ellipse, Rectangle
from kivy.core.window import Window
from kivy.graphics import Color


class SimpleAnimation(App):
    info_message = StringProperty()

    def __init__(self, **kwargs):
        super(SimpleAnimation, self).__init__(**kwargs)
        Window.size = (500, 300)
        self.ball = None

    def build(self):
        Clock.schedule_interval(self.update, 0.02)
        self.root = Builder.load_file("simple_animation_demo.kv")
        self.ball = Ellipse()
        self.ball.size = (100, 100)
        self.ball.pos = 20, 20
        self.root.canvas.add(Color(1, 0, 0, 1))
        self.root.canvas.add(self.ball)
        self.root.canvas.add(Color(1, 1, 0, 1))
        self.root.canvas.add(Rectangle())
        return self.root

    def update(self, seconds):
        self.info_message = '{:.5f}'.format(seconds)
        _x, _y = self.ball.pos
        self.ball.pos = _x + 1, _y


SimpleAnimation().run()
