import config
import importlib
import json
import tkinter
from tkinter import ttk
from core.meta import utilities
from .window_wrapper import WindowWrapper

tk = tkinter


class WidgetWrapper:
    def __init__(self, full_dict, window: WindowWrapper, parent=None):
        self.window = window

        self.parent = parent
        if parent is None:
            self.parent = window

        self.children = []

        self.full_dict = full_dict
        self.name = self.full_dict['name']
        self.widget = self.create_widget()

        self.create_widget()
        self.create_children()
        self.pack()

    def register(self):
        self.window.widget_registry[self.name] = self

    def create_widget(self):
        widget_library_name = self.full_dict.get("library")
        widget_library = utilities.get_or_import_library(widget_library_name)
        widget_type = self.full_dict.get("type")
        properties = utilities.get_objectified_dict(self.full_dict.get("properties", {}))

        return getattr(widget_library, widget_type)(self.parent, **properties)

    def create_children(self):
        child_list = self.full_dict.get('children', [])
        if child_list:
            for child_dict in child_list:
                self.create_child(child_dict)

    def create_child(self, child_dict):
        child = WidgetWrapper(full_dict=child_dict, window='test', parent=self)
        self.children.append(child)

    # TODO
    # Move check_widget_exists from widget_wrapper, whose concern it is not, into window_wrapper.
    # Does not need to be able to search other windows either. If there's a need later, I can explore that.
    def check_widget_exists(self, widget_name, current_window_only=True):
        widget_exists = False
        searchable_windows = []

        if current_window_only:
            searchable_windows.append(self.window)
        else:
            for window in WidgetWrapper.global_widget_registry.keys():
                searchable_windows.append(window)

        for window in searchable_windows:
            if widget_name in WidgetWrapper.global_widget_registry[window].keys():
                widget_exists = True

        return widget_exists

    def pack(self):
        if self.parent.full_dict.get('type', '') == 'Notebook':
            notebook = self.parent.widget
            tab = tkinter.Frame(notebook)
            notebook.add(tab, text=self.full_dict.get("title"))
        else:
            pack_props = utilities.get_objectified_dict(self.full_dict.get("pack_properties", {}))
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
                module = utilities.get_or_import_library(command_path)
                if module:
                    func = getattr(module, func_name)
                    properties["command"] = func
                else:
                    print(rf'could not find module: {command_path}')

    @staticmethod
    def load_widget_from_file(file, window, parent=None):
        with open(file, 'r') as f:
            widget_json = json.load(file)

        return WidgetWrapper(full_dict=widget_json, window=window, parent=parent)
