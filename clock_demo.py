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
        self.clock_event = None

    def build(self):
        Config.set('graphics', 'width', '200')
        Config.set('graphics', 'height', '200')

        # Creates a ClockEvent object and schedule the callback function
        self.clock_event = Clock.schedule_interval(self.update, 1)
        self.root = Builder.load_file('clock_demo.kv')
        return self.root

    # this method is called by the ClockDemo object
    def update(self, seconds):
        print('counter {:2} dt {}'.format(self.counter, seconds))
        self.counter += 1
        if self.counter >= 10:
            # Cancel the callback function
            self.clock_event.cancel()
            # (Or unschedule using a reference to the ClockEvent object)
            # Clock.unschedule(self.clock_event)


ClockDemo().run()
