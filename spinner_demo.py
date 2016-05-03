"""
CP1404 Spinner Demo - loads values at run-time
Lindsay Ward, IT@JCU
14/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ListProperty

__author__ = 'Lindsay Ward'
STATES = {'QLD': "Queensland", 'NSW': "New South Wales", 'VIC': "Victoria", 'WA': "Western Australia",
          'TAS': "Tasmania", 'NT': "Northern Territory", 'SA': "South Australia", 'ACT': "Canberra",
          'NQ': "Cowboys!", 'NZ': "New Zealand"}


class SpinnerDemo(App):
    """ SpinnerDemo is a Kivy App using a spinner to display state names """
    current_state = StringProperty()
    state_codes = ListProperty()

    def build(self):
        """ build Kivy app from the kv file """
        self.title = "Spinner Demo"
        self.root = Builder.load_file('spinner_demo.kv')
        self.state_codes = sorted(STATES.keys())
        self.current_state = self.state_codes[0]
        return self.root

    def change_state(self, state_code):
        """ handle change of spinner selection, output result to label widget """
        self.root.ids.output_label.text = STATES[state_code]
        print("changed to", state_code)


SpinnerDemo().run()
