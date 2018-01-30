"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on custom class objects
For something to do, pressing the guitar buttons changes the cost in the guitar objects
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
        # basic data example - list of Guitar objects
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
            # create a button for each Guitar object, specifying the text and id
            temp_button = Button(text=str(guitar), id=guitar.name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entries_box" using add_widget()
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handle pressing buttons.
        :param instance: the Kivy button instance
        :return: None
        """
        # get guitar object from list based on the id of Button we clicked on (id = guitar name)
        name = instance.id
        for guitar in self.guitars:
            if guitar.name == name:
                break

        # update guitar cost in the original object
        # note: we can safely ignore the warning "local variable might be referenced before assignment"
        # pylint: disable=undefined-loop-variable
        old_cost = guitar.cost
        guitar.cost *= DISCOUNT_RATE
        # update button text and label
        instance.text = str(guitar)
        self.status_text = "Your {} was ${:,.2f} but now costs ${:,.2f}".format(name, old_cost, guitar.cost)


GuitarsApp().run()
