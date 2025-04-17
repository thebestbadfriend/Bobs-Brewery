import importlib

class BBWidgetWrapper:
    '''
    probably use most or all of the json stuff here. So like, in the json, there is a children list for many widgets.
    That should translate to a children list here. Pack_props there = pack_props here. Etc

    yeah! And then self can be passed into populate children which can call a create function and pass self as the
    parent. Should, I think, create a proper traversable family tree.

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
        properties = self.full_dict.get("properties", {})

        self.widget = getattr(widget_library, widget_type)(self.parent, **properties)

    def create_children(self):
        child_list = self.full_dict.get('children', [])
        if child_list:
            for child_dict in child_list:
                self.create_child(child_dict)

    def create_child(self, child_dict):
        child = BBWidgetWrapper(full_dict=child_dict, parent=self)
        self.children.append(child)

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
        pass
