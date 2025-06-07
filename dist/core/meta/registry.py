class Registry(dict):
    def __init__(self, name):
        super().__init__()
        self.name = name