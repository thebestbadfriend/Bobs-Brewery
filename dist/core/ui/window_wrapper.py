import json
import config
from core.meta.module import Module
from core.meta.registry import Registry
from core.meta import utilities

class WindowWrapper:
    def __init__(self, full_dict, module:Module=None):
        self.full_dict = full_dict
        self.name = full_dict['name']

        self.module = module if module is not None else config.registry_stack.module_registry['core']
        self.register()

        self.widget_registry = Registry(name='widget_registry')
        self.window = self.create_window()
        self.create_children()

    def register(self):
        self.module.window_registry[self.name] = self

    def create_window(self):
        library_name = self.full_dict['library']
        library = utilities.get_or_import(library_name)
        window_type = self.full_dict.get("type")
        window = getattr(library, window_type)()

        properties = self.full_dict.get("properties", {})
        window.title(properties.get("title", ""))
        window.minsize(properties.get("min_width", 200), properties.get("min_height", 200))
        window.maxsize(properties.get("max_width", 3000), properties.get("max_height", 3000))
        window.geometry(properties.get("geometry_string", "800x600"))
        # Set position if provided
        if "xpos" in properties and "ypos" in properties:
            window.geometry(f'+{properties["xpos"]}+{properties["ypos"]}')
        if "resizable" in properties:
            window.resizable(*properties["resizable"])

        return window

    def create_children(self):
        module_path = 'core.ui.widget_wrapper'
        class_name = 'WidgetWrapper'
        WidgetWrapper = utilities.get_or_import(module_path, class_name)

        for child in self.full_dict.get("children", []):
            # full_dict, window: WindowWrapper, parent: Union['WidgetWrapper', 'WindowWrapper']=None
            child = WidgetWrapper(child, self, self)

    @staticmethod
    def load_window_from_file(file, module: Module=None):
        with open(file, 'r') as f:
            window_json = json.load(f)

        return WindowWrapper(full_dict=window_json, module=module)

    @staticmethod
    def create_modal_window_from_file(file, parent_window:'WindowWrapper', module: Module=None):
        if module is None:
            module = parent_window.module

        modal_root = WindowWrapper.load_window_from_file(file, module=module)
        modal_root.window.transient(parent_window.window)
        modal_root.window.grab_set()

        return modal_root
