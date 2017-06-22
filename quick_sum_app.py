# This Python file uses the following encoding: utf-8

"""
QuickSum - a fast way to add up, with busy teachers in mind...
Original version: iOS app 2005
Ported to Kivy: Oct 2015
(c) 2015 Jason Holdsworth
"""

from math import modf
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import NumericProperty

__author__ = 'Jason'


class QuickSum(App):
    current_total = NumericProperty(0)
    NORMAL_DIGITS = ['3', '2', '1', '6', '5', '4', '9', '8', '7']
    MORE_DIGITS = ['13', '14', '15', '10', '11', '12', '½', '¼', '¾']
    FRACTIONS = {'½': 0.5, '¼': 0.25, '¾': 0.75}

    def __init__(self, **kwargs):
        super(QuickSum, self).__init__(**kwargs)
        self._digits_toggled = False

    def build(self):
        Window.size = 300, 600
        self.title = "QuickSum"
        self.root = Builder.load_file('quick_sum_gui.kv')
        self._set_digits(QuickSum.NORMAL_DIGITS)
        return self.root

    def _increment_total(self, source):
        # use the text of the button to figure out the
        # value to add to the current total
        digit = source.text
        if digit in QuickSum.FRACTIONS.keys():
            value = QuickSum.FRACTIONS[digit]
            self._toggle_digits()
        else:
            value = int(digit)
        result = self.current_total + value
        if modf(result)[0] == 0:
            self.current_total = int(result)
        else:
            self.current_total = result

    def _clear_total(self):
        self.current_total = 0

    def _toggle_digits(self):
        self._digits_toggled = not self._digits_toggled
        self._set_digits(QuickSum.MORE_DIGITS if self._digits_toggled else QuickSum.NORMAL_DIGITS)

    def _set_digits(self, digits):
        for i in range(9):
            self.root.ids.digits.children[i].text = str(digits[i])


if __name__ == '__main__':
    app = QuickSum()
    app.run()
