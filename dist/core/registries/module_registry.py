from core.registries.registry import Registry


class ModuleRegistry(Registry):
    def __init__(self):
        super().__init__()
        self.modules = {}

    def __getitem__(self, key):
        return self.modules[key]