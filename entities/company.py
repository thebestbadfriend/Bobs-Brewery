from dal import BreweryDBAccessor


class Company(object):
    bda = BreweryDBAccessor()

    id = 0
    contact_id = 0
    name = ""

    addresses = []
    people = []

    def __init__(self, id, contact_id, name, addresses, people):
        self.id = id
        self.contact_id = contact_id
        self.name = name
        self.addresses = addresses
        self.people = people

    def get_people(self):
        people = self.bda.execute_db_command(f"select * from contacts where id = {self.id}")
