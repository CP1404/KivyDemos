"""
Kivy Phonebook example for CP1404, IT@JCU
- dynamically create buttons based on content of dictionary
- demo of a 'popup' window
Lindsay Ward
01/05/2016
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class PhonebookApp(App):
    """
    Main program - Kivy app to demo phonebook system
    """
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super(PhonebookApp, self).__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        self.phonebook = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Phonebook Demo - Popup & Buttons"
        self.root = Builder.load_file('popup_demo.kv')
        self.create_entry_buttons()
        return self.root

    def create_entry_buttons(self):
        """
        Create the entry buttons and add them to the GUI
        :return: None
        """
        for name in self.phonebook:
            # create a button for each phonebook entry
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.press_entry)
            # add the button to the "entries_box" using add_widget()
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """
        Handler for pressing entry buttons
        :param instance: the Kivy button instance
        :return: None
        """
        # update status text
        name = instance.text
        self.status_text = "{}'s number is {}".format(name, self.phonebook[name])
        # set button state
        # print(instance.state)
        instance.state = 'down'

    def press_clear(self):
        """
        Clear any buttons that have been selected (visually) and reset status text
        :return: None
        """
        # use the .children attribute to access all widgets that are "in" another widget
        for instance in self.root.ids.entries_box.children:
            instance.state = 'normal'
        self.status_text = ""

    def press_add(self):
        """
        Handler for pressing the add button
        :return: None
        """
        self.status_text = "Enter details for new phonebook entry"
        # this opens the popup
        self.root.ids.popup.open()

    def press_save(self, added_name, added_number):
        """
        Handler for pressing the save button in the add entry popup - save a new entry to memory
        :param added_name: name text input (from popup GUI)
        :param added_number: phone number text input (string)
        :return: None
        """
        self.phonebook[added_name] = added_number
        # change the number of columns based on the number of entries (no more than 5 rows of entries)
        self.root.ids.entries_box.cols = len(self.phonebook) // 5 + 1
        # add button for new entry (same as in create_entry_buttons())
        temp_button = Button(text=added_name)
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entries_box.add_widget(temp_button)
        # close popup
        self.root.ids.popup.dismiss()
        self.clear_fields()

    def clear_fields(self):
        """
        Clear the text input fields from the add entry popup
        If we don't do this, the popup will still have text in it when opened again
        :return: None
        """
        self.root.ids.added_name.text = ""
        self.root.ids.added_number.text = ""

    def press_cancel(self):
        """
        Handler for pressing cancel in the add entry popup
        :return: None
        """
        self.root.ids.popup.dismiss()
        self.clear_fields()
        self.status_text = ""


PhonebookApp().run()
