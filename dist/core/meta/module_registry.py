from core.meta.bb_registry import BBRegistry


class ModuleRegistry(BBRegistry):
    def __init__(self):
        super().__init__()
        self.modules = {}

    def __getitem__(self, key):
        return self.modules[key]