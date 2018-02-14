"""
CP1404 IT@JCU
Kivy Demo showing drawing an object at the location of the mouse cursor
Note: there seems to be a Kivy bug with mouse locations on Retina (high DPI) screens
https://github.com/kivy/kivy/issues/3960
"""

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Ellipse
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.uix.widget import Widget


class MoveWithMouse(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (500, 300)
        self.ball = Ellipse()

    def build(self):
        # update the screen every 1/100th of a second (ideally)
        Clock.schedule_interval(self.update, 0.01)
        self.root = Widget()
        self.ball.size = (100, 100)
        self.ball.pos = 20, 20
        self.root.canvas.add(Color(1, 0, 0, 1))
        self.root.canvas.add(self.ball)
        return self.root

    def update(self, seconds):
        # print(self.root_window.mouse_pos)
        # account for the width of the ball
        self.ball.pos = self.root_window.mouse_pos[0] - self.ball.size[0] / 2, self.root_window.mouse_pos[1] - self.ball.size[1] / 2


MoveWithMouse().run()
