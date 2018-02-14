from random import random

from kivy.app import App
from kivy.graphics import Ellipse
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.clock import Clock


class Ball(Ellipse):
    """A movable Ellipse shape that slowly moves and increases in speed."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = 1

    def fall(self):
        if self.pos[1] > 0:
            self.pos = (self.pos[0], self.pos[1] - self.speed)
            if self.speed < 20:
                self.speed *= 1.05

    def at_bottom(self):
        return self.pos[1] <= 0


class Display(Widget):
    """The display area for the ball objects."""
    def __init__(self):
        super().__init__()
        Clock.schedule_interval(self.move_points, 0.025)

    def move_points(self, _):
        for point in self.canvas.children:
            if isinstance(point, Ball):
                point.fall()
                if point.at_bottom():
                    self.canvas.remove(point)

    @staticmethod
    def generate_color():
        """Generate a random colour."""
        red = random()
        green = random()
        blue = random()
        alpha = 0.25 + random() * 0.75
        return Color(red, green, blue, alpha)

    def on_touch_down(self, touch):
        with self.canvas:
            Display.generate_color()
            Ball(pos=(touch.x, touch.y), size=(20, 20))

    def on_touch_move(self, touch):
        with self.canvas:
            Ball(pos=(touch.x, touch.y), size=(10, 10))


class FallingDrawingApp(App):
    """Kivy Demo app."""
    def build(self):
        self.root = Builder.load_file("falling_drawing.kv")
        return self.root


FallingDrawingApp().run()
