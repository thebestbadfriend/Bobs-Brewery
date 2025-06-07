from .registry import Registry
from .module import Module


class RegistryContainer:
    def __init__(self):
        self.module_registry = Registry(name='module_registry')
        self.module_registry['core'] = Module('core')
