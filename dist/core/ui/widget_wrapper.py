import config
import importlib
import json
import tkinter
from tkinter import ttk
from typing import Union
from core.meta import utilities
from .window_wrapper import WindowWrapper

tk = tkinter


class WidgetWrapper:
    def __init__(self, full_dict, window: WindowWrapper, parent: Union['WidgetWrapper', 'WindowWrapper']=None):
        self.window = window

        self.parent = parent
        if parent is None:
            self.parent = window

        self.children = []

        self.full_dict = full_dict
        self.name = self.full_dict['name']

        self.pre_widget_creation_tasks()
        self.widget = self.create_widget()
        self.post_widget_creation_tasks()
        self.register()

        self.create_children()
        self.pack_widget()

    def register(self):
        self.window.widget_registry[self.name] = self

    def create_widget(self):
        if self.full_dict.get('type','') == "file":
            file = self.full_dict.get('file','')
            return self.load_widget_from_file(file, self.window, self.parent)
        else:
            widget_library_name = self.full_dict.get("library")
            widget_library = utilities.get_or_import(widget_library_name)
            widget_type = self.full_dict.get("type")
            properties = utilities.get_objectified_dict(self.full_dict.get("properties", {}))

            widget_class = getattr(widget_library, widget_type)
            if isinstance(self.parent, WindowWrapper):
                widget = widget_class(self.parent.window, **properties)
            else:
                widget = widget_class(self.parent.widget, **properties)

                if self.parent.full_dict.get('type', '') == 'Notebook':
                    print(rf'{self.name} is the direct child of a notebook')
                    notebook = self.parent.widget
                    notebook.add(widget, text=self.full_dict['title'])

            return widget

    def create_children(self):
        child_list = self.full_dict.get('children', [])
        if child_list:
            for child_dict in child_list:
                self.create_child(child_dict)

    def create_child(self, child_dict):
        child = WidgetWrapper(full_dict=child_dict, window=self.window, parent=self)
        self.children.append(child)

    def pack_widget(self):
        if self.parent.full_dict.get('type', '') != 'Notebook':
            pack_props = utilities.get_objectified_dict(self.full_dict.get("pack_properties", {}))
            self.widget.pack(**pack_props)

    def check_widget_exists(self, widget_name):
        return widget_name in self.window.widget_registry.keys()

    def pre_widget_creation_tasks(self):
        properties = self.full_dict.get("properties", {})
        command = properties.get("command", '')
        if command:
            command_path = '.'.join(command['path'].split('.'))
            command_class = command.get('class', '')
            func_name = command['function']

            if self.check_widget_exists(command_path):
                module = self.window.widget_registry[command_path].widget
            else:
                module = utilities.get_or_import(command_path, command_class)

            func = getattr(module, func_name)
            properties["command"] = func

    def post_widget_creation_tasks(self):
        if self.full_dict.get('type', '') == "Scrollbar":
            self.parent.widget.configure(yscrollcommand=self.widget.set)

        binds = self.full_dict.get("binds", {})
        if binds:
            for event_name, event_config in binds.items():
                event_config['class'] = utilities.get_or_import(event_config["module"], event_config['class'])
                func = getattr(event_config['class'], event_config['function'])
                args = event_config['args']
                args['widget'] = self.widget

                self.widget.bind(event_name, lambda e, function=func, arguments=args.copy(): function(e, **arguments))

        populate_function = self.full_dict.get("populate_function",'')
        if populate_function:
            module_name = populate_function["module"]
            class_name = populate_function["class"]
            func_name = populate_function["function_name"]

            event_class = utilities.get_or_import(module_name, class_name)
            if event_class:
                func = getattr(event_class, func_name)
                func(self.widget)

    @staticmethod
    def load_widget_from_file(file, window, parent=None):
        with open(file, 'r') as f:
            widget_json = json.load(file)

        return WidgetWrapper(full_dict=widget_json, window=window, parent=parent)
