class Registry(dict):
    def __init__(self, name):
        super().__init__()
        self.items = {}
        self.name = name

    def __getitem__(self, key):
        return self.items[key]