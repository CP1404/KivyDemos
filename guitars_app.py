"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on custom class objects
For something to do, pressing the guitar buttons changes the cost in the guitar objects
Note we can either associate the buttons with the guitar objects by name (then use name to find object in list)
or directly assign the object reference to the button (this is a REFERENCE to the existing object, not a copy).
Lindsay Ward
30/01/2018
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from guitar import Guitar

DISCOUNT_RATE = 0.9


class GuitarsApp(App):
    """Main program - Kivy app to demo combining classes and Kivy."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app.
        """
        super().__init__(**kwargs)
        # Basic data example - list of Guitar objects - could be loaded from a file or something
        self.guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40),
                        Guitar("Line 6 JTV-59", 2010, 1512.9),
                        Guitar("Ukelele", 2017, 99.95)]

    def build(self):
        """
        Build the Kivy GUI.
        :return: reference to the root Kivy widget
        """
        self.title = "Kivy + Classes = Guitars"
        self.root = Builder.load_file('guitars_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create buttons from list of objects and add them to the GUI.
        :return: None
        """
        self.status_text = "Click on a guitar to reduce its cost by {:.1%}%".format(1 - DISCOUNT_RATE)
        for guitar in self.guitars:
            # Create a button for each Guitar object, specifying the text
            temp_button = Button(text=str(guitar))
            temp_button.bind(on_release=self.press_entry)
            # Store a reference to the guitar object in the button object
            temp_button.guitar = guitar
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handle pressing buttons, changing price of guitar and updating display.
        :param instance: the Kivy button instance
        :return: None
        """
        # Each button was given its own ".guitar" object reference, so we can get it directly
        guitar = instance.guitar
        old_cost = guitar.cost
        guitar.cost *= DISCOUNT_RATE
        # Update button text and label
        instance.text = str(guitar)
        self.status_text = "Your {} was ${:,.2f} but now costs ${:,.2f}".format(guitar.name, old_cost, guitar.cost)


GuitarsApp().run()
