class BBWidgetWrapper:
    '''
    probably use all the json stuff here. So like, in the json, there is a children list for many widgets. That should
    translate to a children list here. Pack_props there = pack_props here. Etc

    yeah! And then self can be passed into populate children which can call a create function and pass self as the
    parent. Should, I think, create a proper traversable family tree.
    '''
    widget = None
    name = ''
    parent = None
    properties_json = {}
    pack_properties_json ={}
    children = []

    def __init__(self):
        pass

    def populate_children(self):
        pass