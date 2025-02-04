from dal import BreweryDBAccessor


class Company(object):
    bda = BreweryDBAccessor()

    id = 0
    contact_id = 0
    name = ""

    addresses = []
    people = []

    def __init__(self, id, contact_id, name):
        self.id = id
        self.contact_id = contact_id
        self.name = name
