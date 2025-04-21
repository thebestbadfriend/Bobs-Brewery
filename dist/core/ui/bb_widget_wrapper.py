import importlib
import tkinter
from tkinter import ttk

tk = tkinter

class BBWidgetWrapper:
    '''
    up to now, windows have been treated more or less as widgets. Now, windows should be their own class and should have
    widgets as children. Window creation is to be handled by the window class. Again, they are /not/ to be treated as
    regular widgets anymore.

    also remember that in python, instance variables are not only assinged but declared in __init__.

    variables declared at the root of the class - such as global_widget_registry here - are static variables

    global_widget_registry should have the following structure:
    {
        window_name: {
            widget_name: BBWidgetWrapper object
        }
    }
    '''
    global_widget_registry = {}

    def __init__(self, full_dict, window, parent=None):
        self.window = window

        self.parent = parent
        if parent == None:
            self.parent = window

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

    def pre_widget_creation_tasks(self):
        properties = self.full_dict.get("properties", {})
        if properties.get('command',''):
            command_path = '.'.join(properties["command"].split('.')[:-1])
            func_name = properties["command"].split('.')[-1]

            '''
            the below needs to be changed for a couple reasons:
            
            1) it only works for single-layer modules
              a) that is, module.function works, but module.submodule.function does not
                i) specifically, importlib.import_module can handle 'module' or 'module.submodule', but globals().get()
                   cannot handle the 'module.submodule' string.
                ii) preserve the string as is for use in importlib.import_module as needed
                iii) for globals().get() need to use importlib.import_module to import the whole importable path to the
                     module (not including the function /within/ the module) (e.g.
                     importlib.import_module(some_module.submodule.subsubmodule)) and then use
                     getattr(current_iteration, next_part, None) for all subsequent levels (usually just the function
                     portion). For example
                     
                     if the full string is 'my_module.my_submodule.my_sub_submodule.my_sub_sub_submodule.my_function'
                     
                     base_mod = importlib.import_module('my_module.my_submodule.my_sub_submodule.my_sub_sub_submodule')
                     getattr(base_mod, 'my_function', None)
                     
              b) the change for this part actually should go in the get_or_import_library function so that paths can
                 be passed as strings as is already the case here and the logic to go through the path and get the right
                 module does not have to be duplicated everywhere it is needed.
            2) it only works for importable or global things
              a) that is, module.function works, but widget.function (such as tv_contacts.yview) does not unless
                 widget has been added to globals()
              b) probably a check_widget_exists() function and logic to either use the widget if one exists or proceed
                 to get_or_import_library if not is a good way to go here
            '''

            module = self.get_or_import_library(command_path)
            if module:
                func = getattr(module, func_name)
                properties["command"] = func
            else:
                print(rf'could not find module: {command_path}')