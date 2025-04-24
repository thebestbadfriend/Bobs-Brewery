from core.meta.module import Module

class Window:
    def __init__(self, name, module:Module=None):
        self.name = name
        self.module = module

        if module:
            self.register()

    def register(self):
        self.module.window_registry[self.name] = self
