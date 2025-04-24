from core.meta.module import Module
from core.meta.registry import Registry

class WindowWrapper:
    def __init__(self, full_dict, module:Module=None):
        self.full_dict = full_dict
        self.name = full_dict['name']
        self.module = module

        if module:
            self.register()

        self.widget_registry = Registry(name='widget_registry')
        self.window = self.create_window()

    def register(self):
        self.module.window_registry[self.name] = self

    def create_window(self):
        library_name = self.full_dict['library']

        widget_library = self.get_or_import_library(widget_library_name)
        widget_type = self.full_dict.get("type")
        properties = self.get_objectified_dict(self.full_dict.get("properties", {}))

        ### copied from window_builder.py but not  yet edited
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
        ###

        return getattr(widget_library, widget_type)(self.parent, **properties)
