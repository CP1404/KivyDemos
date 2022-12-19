"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on custom class objects
For something to do, pressing the guitar buttons changes the cost in the guitar objects
Note we can directly assign the object to the button.
This is a REFERENCE to the existing object, not a copy.
Lindsay Ward
30/01/2018
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from guitar import Guitar
from guitars_console import load_guitars

DISCOUNT_RATE = 0.9


class GuitarsApp(App):
    """Main program - Kivy app to demo combining classes and Kivy."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main Kivy app."""
        super().__init__(**kwargs)
        # Basic data example - list of Guitar objects - could be loaded from a file or something
        self.guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40),
                        Guitar("Line 6 JTV-59", 2010, 1512.9),
                        Guitar("Ukulele", 2017, 99.95)]
        # self.guitars = load_guitars("guitars.json")

    def build(self):
        """Build the Kivy GUI."""
        Window.size = 1000, 800
        self.title = "Kivy + Classes = Guitars"
        self.root = Builder.load_file('guitars_app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from list of objects and add them to the GUI."""
        self.status_text = f"Click on a guitar to reduce its cost by {1 - DISCOUNT_RATE:.1%}"
        for guitar in self.guitars:
            # Create a button for each Guitar object, specifying the text
            temp_button = Button(text=str(guitar))
            temp_button.bind(on_release=self.press_entry)
            # Store a reference to the guitar object in the button object
            temp_button.guitar = guitar
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """Handle pressing guitar buttons."""
        # Each button was given its own ".guitar" object reference, so we can get it directly
        guitar = instance.guitar
        old_cost = guitar.cost
        guitar.cost *= DISCOUNT_RATE
        # Update button text and label
        instance.text = str(guitar)
        self.status_text = f"Your {guitar.name} was ${old_cost:,.2f} but now costs ${guitar.cost:,.2f}"


GuitarsApp().run()
