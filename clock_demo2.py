from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.core.window import Window


class ClockDemo(App):
    message = StringProperty()

    def __init__(self, **kwargs):
        super(ClockDemo, self).__init__(**kwargs)
        self.counter = 0
        Window.size = (500, 200)
        self.clock = None

    def build(self):
        self.root = Builder.load_file('clock_demo2.kv')
        return self.root

    def update(self, dt):
        self.message = 'counter {} dt {}'.format(self.counter, dt)
        self.counter += 1

    def start(self):
        self.stop()
        self.clock = Clock.schedule_interval(self.update, 0.5)

    def stop(self):
        if self.clock:
            self.clock.cancel()


if __name__ == '__main__':
    app = ClockDemo()
    app.run()
