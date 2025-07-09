from .registry import Registry
from global_tools import config


class Module:
    def __init__(self, name, enabled=True):
        self.name = name
        self.enabled = enabled
        self.window_registry = Registry(name='window_registry')

    def toggle(self):
        self.enabled = not self.enabled

    def enable(self):
        if not self.enabled:
            self.enabled = True

    def disable(self):
        if self.enabled:
            self.enabled = False

    def register(self):
        config.registry_stack.module_registry[self.name] = self