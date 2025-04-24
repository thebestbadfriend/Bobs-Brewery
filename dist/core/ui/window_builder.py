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
A lot of this functionality - if not all of it - will eventually go into the Window and WidgetWrapper classes.

That is actually what I am working on now, starting with the widget wrapper
'''

class WindowBuilder:
    widget_registry = {} # To be replaced by the widgets list
    widgets = []

    @staticmethod
    def create_widget_from_file(file_path, parent=None):
        with open(file_path, "r") as file:
            ui_config = json.load(file)

        widget_library_name = ui_config["library"]
        widget_type = ui_config["type"]
        json_properties = ui_config.get("properties", {})
        children = ui_config.get("children", [])

        widget_library = WindowBuilder.get_or_import_library(widget_library_name)

        if widget_type in ("Tk", "TopLevel"):
            widget = WindowWrapper.load_window_from_file(file_path)
        else:
            # For non-Tk types, initialize widget normally
            widget = WidgetWrapper(ui_config)

        return widget

    @staticmethod
    def create_modal_window_from_file(file_path):
        print('\n\n\n\n')
        modal_root = WindowBuilder.create_widget_from_file(file_path)
        modal_root.transient(tk._default_root)
        modal_root.grab_set()

        print(f'\n\n\n\n modal root is {modal_root}')

        return modal_root

    @staticmethod
    def create_widget_from_json(element, parent):
        widget_name = element["name"]
        widget_library_name = element["library"]
        widget_type = element["type"]
        json_properties = element.get("properties", {})
        children = element.get("children", [])

        widget_library = WindowBuilder.get_or_import_library(widget_library_name)

        if widget_type == "Button":
            module_name = '.'.join(json_properties["command"].split('.')[:-1])
            func_name = json_properties["command"].split('.')[-1]

            module = WindowBuilder.get_or_import_library(module_name)
            if module:
                func = getattr(module, func_name)
                json_properties["command"] = func
            else:
                print(rf'could not find module: {module_name}')
        elif widget_type == "Scrollbar":
            container, view = json_properties["command"].split('.')
            container = WindowBuilder.widget_registry.get(container)
            if container:
                json_properties["command"] = getattr(container, view)
                parent = container


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

    @staticmethod
    def get_or_import_library(library_name):
        widget_library = None

        try:
            # If the library is already imported, use it directly
            widget_library = globals().get(library_name)  # Get the module from the globals() dictionary

            if widget_library is None:
                # If it's not imported, we can either raise an error or try to import it dynamically
                raise ImportError(f"Module '{library_name}' not found in the global scope.")

        except ImportError:
            widget_library = importlib.import_module(library_name)

        return widget_library

    @staticmethod
    def create_tab_in_notebook(tab_json, notebook):
        tab = tk.Frame(notebook)
        children = tab_json.get("children",[])

        for child in children:
            if "pack_properties" in child:
                if "fill" in child["pack_properties"]:
                    child["pack_properties"]["fill"] = getattr(tk, child["pack_properties"]["fill"])
                if "side" in child["pack_properties"]:
                    child["pack_properties"]["side"] = getattr(tk, child["pack_properties"]["side"])

                w = WindowBuilder.create_widget_from_json(child, tab)["widget"]
                w.pack(**child["pack_properties"])
            else:
                w = WindowBuilder.create_widget_from_json(child, tab)["widget"]
                w.pack()

        notebook.add(tab, text=tab_json["title"])
