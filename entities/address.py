class Address:
    street_address = ""
    po_box = ""
    city = ""
    state = ""
    zip_code = ""
    contacts = []

    def __init__(self, street, po_box, city, state, zipcode):
        self.street = street
        self.po_box = po_box
        self.city = city
        self.state = state
        self.zipcode = zipcode
