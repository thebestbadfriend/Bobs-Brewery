import json
import tkinter as tk
from tkinter import ttk
import importlib
from core.ui import btn_commands
import modules.contact_management as contact_management
from modules.contact_management import ContactsTreeviewPopulator


class WindowBuilder:
    widget_registry = {}

    @staticmethod
    def create_widget_from_file(file_path, parent=None):
        with open(file_path, "r") as file:
            ui_config = json.load(file)

        widget_library_name = ui_config["library"]
        widget_type = ui_config["type"]
        properties = ui_config.get("properties", {})
        children = ui_config.get("children", [])

        widget_library = WindowBuilder.get_or_import_library(widget_library_name)

        if widget_type == "Tk":
            widget = WindowBuilder.create_window(properties, True)
        elif widget_type == "Toplevel":
            widget = WindowBuilder.create_window(properties)
        else:
            # For non-Tk types, initialize widget normally
            widget = getattr(widget_library, widget_type)(parent, **properties)

        # Recursively create child widgets
        for child_config in children:
            child_element = WindowBuilder.create_widget_from_json(child_config, widget)
            if child_element:
                child_element["widget"].pack()

        return widget

    @staticmethod
    def create_modal_window_from_file(file_path):
        modal_root = WindowBuilder.create_widget_from_file(file_path)
        modal_root.transient(tk._default_root)
        modal_root.grab_set()

        return modal_root

    @staticmethod
    def create_widget_from_json(element, parent):
        widget_name = element["name"]
        widget_library_name = element["library"]
        widget_type = element["type"]
        properties = element.get("properties", {})
        children = element.get("children", [])

        widget_library = WindowBuilder.get_or_import_library(widget_library_name)

        if widget_type == "Button":
            module_name = '.'.join(properties["command"].split('.')[:-1])
            func_name = properties["command"].split('.')[-1]

            module = WindowBuilder.get_or_import_library(module_name)
            if module:
                func = getattr(module, func_name)
                properties["command"] = func
            else:
                print(rf'could not find module: {module_name}')
        elif widget_type == "Scrollbar":
            container, view = properties["command"].split('.')
            container = WindowBuilder.widget_registry.get(container)
            if container:
                properties["command"] = getattr(container, view)
                parent = container


        # Create the widget from the library and properties
        widget = getattr(widget_library, widget_type)(parent, **properties)

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
    def create_window(properties, is_root=False):
        # Create the Tk instance first, then set properties separately
        if is_root:
            widget = tk.Tk()
        else:
            widget = tk.Toplevel()
        widget.title(properties.get("title", ""))
        widget.minsize(properties.get("min_width", 200), properties.get("min_height", 200))
        widget.maxsize(properties.get("max_width", 3000), properties.get("max_height", 3000))
        widget.geometry(properties.get("geometry_string", "800x600"))
        # Set position if provided
        if "xpos" in properties and "ypos" in properties:
            widget.geometry(f'+{properties["xpos"]}+{properties["ypos"]}')
        if "resizable" in properties:
            widget.resizable(*properties["resizable"])

        return widget

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

                WindowBuilder.create_widget_from_json(child, tab)["widget"].pack(**child["pack_properties"])
            else:
                WindowBuilder.create_widget_from_json(child, tab)["widget"].pack()

        notebook.add(tab, text=tab_json["title"])
