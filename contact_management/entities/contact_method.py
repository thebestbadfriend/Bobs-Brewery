class ContactMethod(object):
    contact_type = ""
    text = ""
    value = {}

    def __init__(self, contact_type, text, value):
        self.contact_type = contact_type
        self.text = text
        self.value = value
