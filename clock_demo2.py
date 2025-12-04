"""CP1404/CP5632 - Kivy Demo for Clock scheduler."""
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.core.window import Window


class ClockDemo(App):
    """Kivy Clock Demo."""
    message = StringProperty()

    def __init__(self, **kwargs):
        """Construct the App object."""
        super().__init__(**kwargs)
        self.counter = 0
        Window.size = (500, 200)
        self.clock_event = None

    def build(self):
        """Build the Kivy app from the kv file."""
        self.root = Builder.load_file('clock_demo2.kv')
        return self.root

    def update(self, seconds):
        """Update the app; method called by scheduler."""
        self.message = f"Counter {self.counter:2} dt {seconds:20}"
        self.counter += 1

    def start(self):
        """Start the schedule."""
        self.stop()
        self.clock_event = Clock.schedule_interval(self.update, 0.5)

    def stop(self, *largs):
        """Stop the schedule."""
        if self.clock_event:
            self.clock_event.cancel()


ClockDemo().run()
