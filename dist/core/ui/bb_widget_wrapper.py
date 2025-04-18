import importlib
import tkinter
from tkinter import ttk

tk = tkinter

class BBWidgetWrapper:
    '''
    up to now, windows have been treated more or less as widgets. Now, windows should be their own class and should have
    widgets as children. Window creation is to be handled by the window class. Again, they are /not/ to be treated as
    regular widgets anymore.
    '''
    widget = None
    full_dict = {}

    name = ''
    parent = None
    children = []

    def __init__(self, full_dict, parent=None):
        self.parent = parent
        self.full_dict = full_dict
        self.create_widget()
        self.create_children()
        self.pack()

    def create_widget(self):
        widget_library_name = self.full_dict.get("library")
        widget_library = self.get_or_import_library(widget_library_name)
        widget_type = self.full_dict.get("type")
        properties = self.get_objectified_dict(self.full_dict.get("properties", {}))

        self.widget = getattr(widget_library, widget_type)(self.parent, **properties)

    def create_children(self):
        child_list = self.full_dict.get('children', [])
        if child_list:
            for child_dict in child_list:
                self.create_child(child_dict)

    def create_child(self, child_dict):
        child = BBWidgetWrapper(full_dict=child_dict, parent=self)
        self.children.append(child)

    @staticmethod
    def get_objectified_dict(self, dictionary):
        objectified_dict = dictionary.copy()

        for key, val in dictionary.items():
            if isinstance(val, str) and hasattr(tkinter, val):
                objectified_dict[key] = getattr(tkinter, val)

        return objectified_dict

    @staticmethod
    def get_or_import_library(self, library_name):
        widget_library = None

        try:
            # If the library is already imported, use it directly
            widget_library = globals().get(library_name)  # Get the module from the globals() dictionary

            if widget_library is None:
                # If it's not imported, we can either raise an error or try to import it dynamically
                raise ImportError(f"Module '{library_name}' not found in the global scope. Attempting to import it.")

        except ImportError:
            widget_library = importlib.import_module(library_name)

        return widget_library

    def pack(self):
        if self.parent.full_dict.get('type', '') == 'Notebook':
            notebook = self.parent.widget
            tab = tkinter.Frame(notebook)
            notebook.add(tab, text=self.full_dict.get("title"))
        else:
            pack_props = self.get_objectified_dict(self.full_dict.get("pack_properties", {}))
            self.widget.pack(**pack_props)
