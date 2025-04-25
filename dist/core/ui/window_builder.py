import config
import json
import tkinter
from tkinter import ttk
import importlib
from core.ui.widget_wrapper import WidgetWrapper, WindowWrapper
from core.ui import btn_commands
import modules.contact_management as contact_management
from modules.contact_management import ContactsTreeviewPopulator

tk = tkinter

'''
Working on moving all of this functionality to its appropriate classes. Once those are built and all dependency on this
file has been switched to rely on those instead, this file will be deleted
'''

class WindowBuilder:
    widget_registry = {} # To be replaced by the widgets list
    widgets = []

    @staticmethod
    def create_widget_from_json(element, parent):
        widget_name = element["name"]
        widget_library_name = element["library"]
        widget_type = element["type"]
        json_properties = element.get("properties", {})
        children = element.get("children", [])

        widget_library = WindowBuilder.get_or_import_library(widget_library_name)

        # Create the widget from the library and properties
        widget = getattr(widget_library, widget_type)(parent, **json_properties)

        if widget_type == "Scrollbar":
            parent.configure(yscrollcommand=widget.set)

        if "binds" in element:
            for event, config in element["binds"].items():
                config['module'] = globals().get(config["module"])
                func = getattr(config['module'], config['function'])
                args = config['args']
                args['widget'] = widget

                widget.bind(event, lambda e, function=func, arguments=args.copy(): function(e, **arguments))

        if widget_type == "file":
            widget = WindowBuilder.create_widget_from_file(widget, parent)
        elif widget_type == "Notebook":
            for child in children:
                WindowBuilder.create_tab_in_notebook(child, widget)
        else:
            for child in children:
                WindowBuilder.create_widget_from_json(child, widget)

        if "populate_function" in element:
            module_name = element["populate_function"]["module"]
            func_name = element["populate_function"]["function_name"]

            module = globals().get(module_name)
            if module:
                func = getattr(module, func_name)
                func(widget)

        WindowBuilder.widget_registry[widget_name] = widget

        print(rf'widget {widget_name} type is {widget_type}')

        widget_dict = {
            "widget": widget,
            "dict": element,
        }

        return widget_dict
