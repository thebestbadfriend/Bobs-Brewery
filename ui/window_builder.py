import json
import tkinter as tk
from ui import NotebookBuilder


class WindowBuilder:
    nb = NotebookBuilder()

    def create_window(self, title, min_width, min_height, max_width, max_height, xpos, ypos, geometry_string):
        window = tk.Tk()
        window.title(title)
        window.minsize(min_width, min_height)
        window.maxsize(max_width, max_height)
        window.geometry(geometry_string)

        return window

    def create_main_window(self):
        root = self.create_window(title="Bob's Brewery",
                                  min_width=300,
                                  min_height=300,
                                  max_width=3000,
                                  max_height=3000,
                                  xpos=800,
                                  ypos=200,
                                  geometry_string="800x600")

        tab_control = self.nb.create_main_window_tab_control(root)
        tab_control.pack(expand=1, fill="both")

        return root

    @staticmethod
    def apply_layout(widget, layout):
        if "pack" in layout:
            widget.pack(**layout["pack"])
        elif "grid" in layout:
            widget.grid(**layout["grid"])
        elif "place" in layout:
            widget.place(**layout["place"])

    @staticmethod
    def create_window_from_file(file_path, parent=None):
        with open(file_path, "r") as file:
            ui_config = json.load(file)

        widget_type = ui_config["type"]
        properties = ui_config.get("properties", {})
        children = ui_config.get("children", [])

        # Create the root window if parent is None
        widget = getattr(tk, widget_type)(parent, **properties) if parent else getattr(tk, widget_type)()

        # Apply layout (if any)
        # if parent and "pack" in ui_config:
            # WindowBuilder.apply_layout(widget, {"pack": ui_config["pack"]})

        # Recursively create child widgets
        for child_config in children:
            child_element = WindowBuilder.create_widget_from_json(child_config, widget)
            if child_element:
                child_element.pack()

        return widget

    @staticmethod
    def create_widget_from_json(element, parent):
        widget_type = element["type"]
        properties = element.get("properties", {})
        children = element.get("children", [])
        widget = None

        if widget_type == "file":
            pass
        else:
            widget = getattr(tk, widget_type)(parent, **properties)

        for child in children:
            WindowBuilder.create_widget_from_json(child, widget)

        if widget:
            return widget
