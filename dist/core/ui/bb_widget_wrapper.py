class BBWidgetWrapper:
    '''
    probably use most or all of the json stuff here. So like, in the json, there is a children list for many widgets.
    That should translate to a children list here. Pack_props there = pack_props here. Etc

    yeah! And then self can be passed into populate children which can call a create function and pass self as the
    parent. Should, I think, create a proper traversable family tree.
    '''
    widget = None

    full_dict = {}
    name = ''
    parent = None
    properties = {}
    pack_properties = {}
    children = []

    def __init__(self, full_dict, parent=None):
        self.parent = parent
        self.full_dict = full_dict
        self.create_children()

    def create_children(self):
        child_list = self.full_dict.get('children', [])
        if child_list:
            for child_dict in child_list:
                self.create_child(child_dict)

    def create_child(self, child_dict):
        child = BBWidgetWrapper(full_dict=child_dict, parent=self)
        self.children.append(child)

    def get_or_import_library(self, library_name):
        pass

    def pack(self):
        pass
