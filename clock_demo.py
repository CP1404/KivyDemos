"""
Basic example of how to use the Clock API

This program uses a Clock to schedule a callback function
to be called on a regular basis.

A counter field is updated every second
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.config import Config


class ClockDemo(App):
    def __init__(self, **kwargs):
        super(ClockDemo, self).__init__(**kwargs)
        self.counter = 0
        self.clock = None

    def build(self):
        Config.set('graphics', 'width', '200')
        Config.set('graphics', 'height', '200')

        self.clock = Clock.schedule_interval(self.update, 1)  # define the ClockEvent object
        self.root = Builder.load_file('clock_demo.kv')
        return self.root

    # this method is called by the ClockDemo object
    def update(self, dt):
        print('counter {} dt {}'.format(self.counter, dt))
        self.counter += 1


if __name__ == '__main__':
    app = ClockDemo()
    app.run()
