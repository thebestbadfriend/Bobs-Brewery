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

    ^actually, since I am restructuring as RegistryStack>ModuleRegistry>WindowRegistry>WidgetRegistry>, the widget
    registry only needs to be

    [
        {
            widget_name: BBWidgetWrapper object
        }
    ]

    as the overall structure will be something like

    RegistryStack object =
    {
        module_registry : [
            module: {
                enabled: True,
                window_registry: [
                    window: {
                        widget_registry: [
                            widget: BBWidgetWrapper object
                        ]
                    }
                ]
            }
        ]
    }
    '''
    global_widget_registry = {}

    def __init__(self, full_dict, window, parent=None):
        self.window = window

        self.parent = parent
        if parent is None:
            self.parent = window

        self.children = []

        self.full_dict = full_dict
        self.name = self.full_dict['name']
        self.widget = None

        self.create_widget()
        self.create_children()
        self.pack()

    def create_widget(self):
        widget_library_name = self.full_dict.get("library")
        widget_library = self.get_or_import_library(widget_library_name)
        widget_type = self.full_dict.get("type")
        properties = self.get_objectified_dict(self.full_dict.get("properties", {}))

        self.widget = getattr(widget_library, widget_type)(self.parent, **properties)

        BBWidgetWrapper.global_widget_registry[self.window][self.name] = self

    def create_children(self):
        child_list = self.full_dict.get('children', [])
        if child_list:
            for child_dict in child_list:
                self.create_child(child_dict)

    def create_child(self, child_dict):
        child = BBWidgetWrapper(full_dict=child_dict, window='test', parent=self)
        self.children.append(child)

    @staticmethod
    def get_objectified_dict(dictionary):
        objectified_dict = dictionary.copy()

        for key, val in dictionary.items():
            if isinstance(val, str) and hasattr(tkinter, val):
                objectified_dict[key] = getattr(tkinter, val)

        return objectified_dict

    @staticmethod
    def get_or_import_library(library_name):
        return importlib.import_module(library_name)

    def check_widget_exists(self, widget_name, current_window_only=True):
        widget_exists = False
        searchable_windows = []

        if current_window_only:
            searchable_windows.append(self.window)
        else:
            for window in BBWidgetWrapper.global_widget_registry.keys():
                searchable_windows.append(window)

        for window in searchable_windows:
            if widget_name in BBWidgetWrapper.global_widget_registry[window].keys():
                widget_exists = True

        return widget_exists

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
            
            1) done, reduction of get_or_import_library to eliminate reliance on globals().get()
            2) it only works for importable or global things
              a) that is, module.function works, but widget.function (such as tv_contacts.yview) does not unless
                 widget has been added to globals()
              b) probably a check_widget_exists() function and logic to either use the widget if one exists or proceed
                 to get_or_import_library if not is a good way to go here
            '''

            if self.check_widget_exists(command_path):
                pass
            else:
                module = self.get_or_import_library(command_path)
                if module:
                    func = getattr(module, func_name)
                    properties["command"] = func
                else:
                    print(rf'could not find module: {command_path}')