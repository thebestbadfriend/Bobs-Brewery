from contact_method import ContactMethod


class Contact(object):
    contact_methods = []

    def add_contact_method(self, contact_method: ContactMethod):
        if contact_method not in self.contact_methods:
            self.contact_methods.append(contact_method)

    def remove_contact_method(self, contact_method: ContactMethod):
        if contact_method in self.contact_methods:
            self.contact_methods.remove(contact_method)
