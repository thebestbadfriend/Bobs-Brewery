from core.dal import BreweryDBAccessor
import tkinter as tk


class ContactsTreeviewPopulator:
    # probably de-static the methods here and make this class more instance-dependant
    # this will allow different populators for different treeviews and will make it easier to just
    # set a `treeview` var at initialization which binds each populator to its associated treeview.
    # should make everything a lot simpler.
    #
    # Only thing is, that will mean the data hierarchy has to be described in the yaml or that the data will have to be
    # put together into a list or dictionary or some such in a file unique to each module and then this class will
    # exclusively handle throwing that data into the treeview, not actually collecting and formatting it.
    # Though, come to think of it, that would be a more proper separation of concerns anyway and more modular

    treeview = None
    bda = BreweryDBAccessor()
    contact_data = {}
    current_filtered_data = {}
    companies_iid = None
    people_iid = None
    next_iid = 1

    @staticmethod
    def add_node(treeview, text, parent='', iid=None, node_type='bb_contacts_treeview_default_node_type', contact_id=None):
        if not iid:
            iid = ContactsTreeviewPopulator.next_iid

            while iid in ContactsTreeviewPopulator.contact_data.keys():
                iid += 1

            ContactsTreeviewPopulator.next_iid = iid + 1

        iid = int(iid)

        treeview.insert(parent, tk.END, text=text, iid=iid, open=False)

        iid_exists = ContactsTreeviewPopulator.contact_data.get(iid)
        if not iid_exists:
            ContactsTreeviewPopulator.contact_data[iid] = (text, parent, node_type, contact_id)

        return iid

    @staticmethod
    def populate_contacts_treeview(contacts_treeview):
        ContactsTreeviewPopulator.treeview = contacts_treeview
        contacts_treeview.heading('#0', text='Contacts', anchor=tk.W)

        companies = ContactsTreeviewPopulator.bda.execute_db_command('select id, name, contact_id from companies')
        if companies:
            ContactsTreeviewPopulator.companies_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Companies')
            companies_iid = ContactsTreeviewPopulator.companies_iid

            for company in companies:
                company_details = {
                    "id": company[0],
                    "name": company[1],
                    "contact_id": company[2]
                }

                company_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, company_details['name'],
                                                                 str(companies_iid), node_type='company', contact_id=company_details['contact_id'])

                ContactsTreeviewPopulator.add_node(contacts_treeview, 'Loading company details...', str(company_iid))

        people = ContactsTreeviewPopulator.bda.execute_db_command('select first_name, last_name, suffix, nickname, contact_id from people')
        if people:
            ContactsTreeviewPopulator.people_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'People')
            people_iid = ContactsTreeviewPopulator.people_iid

            for person in people:
                person_details = {
                    'first_name': person[0],
                    'last_name': person[1],
                    'suffix': person[2],
                    'nickname': person[3],
                    'contact_id': person[4]
                }

                person_string = ''
                if person_details['first_name']:
                    person_string = str(person_details['first_name'])
                if person_details['nickname']:
                    person_string += ' "' + person_details['nickname'] + '"'
                if person_details['last_name']:
                    person_string += ' ' + person_details['last_name']
                if person_details['suffix']:
                    person_string += ' ' + person_details['suffix']

                person_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, person_string,
                                                                str(people_iid), node_type='person', contact_id=person_details['contact_id'])

                ContactsTreeviewPopulator.add_node(contacts_treeview, 'Loading person details...', str(person_iid))

    @staticmethod
    def load_details_for_contact(_event, widget=None):
        treeview = widget
        selected_node_iid = treeview.focus()
        node_type = ContactsTreeviewPopulator.contact_data[int(selected_node_iid)][2]
        node_contact_id = ContactsTreeviewPopulator.contact_data[int(selected_node_iid)][3]

        if node_type in ('company', 'person'):
            children = ContactsTreeviewPopulator.treeview.get_children(selected_node_iid)
            for child in children:
                treeview.delete(child)

            if node_type == 'company':
                ContactsTreeviewPopulator.populate_company_node_details(treeview, selected_node_iid, node_contact_id)
            else:
                ContactsTreeviewPopulator.populate_person_node_details(treeview, selected_node_iid, node_contact_id)

    @staticmethod
    def populate_company_node_details(treeview, company_node_iid, company_contact_id):
        addresses = ContactsTreeviewPopulator.load_addresses_by_contact_id(company_contact_id)

        if addresses:
            contact_locations_iid = ContactsTreeviewPopulator.add_node(treeview, 'Locations', company_node_iid)

            for address in addresses:
                address_id = address['id']
                address_string = address['address_string']
                company_location_iid = ContactsTreeviewPopulator.add_node(treeview, address_string, parent=str(contact_locations_iid))

                # load people
                people = ContactsTreeviewPopulator.load_people_by_address_id(address_id)
                if people:
                    location_people_iid = ContactsTreeviewPopulator.add_node(treeview, 'People', str(company_location_iid))
                    for person in people:
                        location_person_iid = ContactsTreeviewPopulator.add_node(treeview, person['person_string'], parent=str(location_people_iid))
                        ContactsTreeviewPopulator.populate_person_node_details(treeview, location_person_iid, person['contact_id'], standalone=False)

                # load non-peopled contact info

        # load non-addressed contact info (phone, fax, email, website, etc) along with non-addressed people and their
        # info

    @staticmethod
    def populate_person_node_details(treeview, person_node_iid, node_contact_id, standalone=True):
        if standalone:
            # load companies (no contact details necessary for companies in this context, just a list of companies the
            # person is associated with)

            # load addresses
            addresses = ContactsTreeviewPopulator.load_addresses_by_contact_id(node_contact_id)
            if addresses:
                contact_locations_iid = ContactsTreeviewPopulator.add_node(treeview, 'Locations', person_node_iid)
                for address in addresses:
                    pass

        # load phone numbers
        phone_numbers = ContactsTreeviewPopulator.load_phone_numbers_by_contact_id(node_contact_id)
        if phone_numbers:
            person_phone_numbers_iid = ContactsTreeviewPopulator.add_node(treeview, 'Phone Numbers', str(person_node_iid))
            for phone_number in phone_numbers:
                ContactsTreeviewPopulator.add_node(treeview, phone_number, parent=str(person_phone_numbers_iid))

        # load fax numbers
        # load email addresses
        # load websites

    @staticmethod
    def load_addresses_by_contact_id(contact_id):
        addresses = []

        contact_locations_query = rf'''select id, street_address, po_box, city, state, zip_code
                                          from addresses
                                          join contacts_addresses on
                                          addresses.id = contacts_addresses.address_id
                                          where contacts_addresses.contact_id = {contact_id}'''
        contact_locations = ContactsTreeviewPopulator.bda.execute_db_command(contact_locations_query)

        if contact_locations:
            for contact_location in contact_locations:
                contact_location_details = {
                    "id": contact_location[0],
                    "street_address": contact_location[1],
                    "po_box": contact_location[2],
                    "city": contact_location[3],
                    "state": contact_location[4],
                    "zip_code": contact_location[5]
                }

                address_string = ''
                for k, v in list(contact_location_details.items())[1:]:
                    if v:
                        if not address_string:
                            address_string = str(v)
                        elif k == 'zip_code':
                            address_string = address_string + ' ' + str(v)
                        else:
                            address_string = address_string + ', ' + str(v)

                contact_location_details['address_string'] = address_string
                addresses.append(contact_location_details)

        return addresses

    @staticmethod
    def load_phone_numbers_by_contact_id(contact_id):
        phone_numbers_list = []

        phone_numbers_query = rf'''select phone_number
                                   from phone_numbers
                                   join contacts_phone_numbers
                                   on phone_numbers.id = contacts_phone_numbers.phone_number_id
                                   join people on contacts_phone_numbers.contact_id = people.contact_id
                                   where people.contact_id = {contact_id}'''
        phone_numbers = ContactsTreeviewPopulator.bda.execute_db_command(phone_numbers_query)

        if phone_numbers:
            for phone_number in phone_numbers:
                phone_numbers_list.append(phone_number[0])

        return phone_numbers

    @staticmethod
    def load_people_by_address_id(address_id):
        people = []

        location_people_query = rf'''select people.contact_id, first_name, last_name, suffix, nickname
                                     from people
                                     join contacts_addresses on people.contact_id = contacts_addresses.contact_id
                                     join addresses on addresses.id = contacts_addresses.address_id
                                     where addresses.id = {address_id}'''
        location_people = ContactsTreeviewPopulator.bda.execute_db_command(location_people_query)
        if location_people:
            for person in location_people:
                person_details = {
                    'contact_id': person[0],
                    'first_name': person[1],
                    'last_name': person[2],
                    'suffix': person[3],
                    'nickname': person[4]
                }

                person_string = ''
                if person_details['first_name']:
                    person_string = str(person_details['first_name'])
                if person_details['nickname']:
                    person_string += ' "' + person_details['nickname'] + '"'
                if person_details['last_name']:
                    person_string += ' ' + person_details['last_name']
                if person_details['suffix']:
                    person_string += ' ' + person_details['suffix']

                person_details['person_string'] = person_string
                people.append(person_details)
        return people

    @staticmethod
    def filter_contacts_treeview(_event, filter_by, widget=None):
        treeview = ContactsTreeviewPopulator.treeview
        filtered_data_set = ContactsTreeviewPopulator.current_filtered_data

        filter_text = ''
        if widget:
            filter_text = widget.get()
        else:
            print('No widget found')

        filtered_data_set.clear()

        ContactsTreeviewPopulator.clear_contacts_treeview_filter()

        if filter_text:
            if filter_by == 'companies':
                companies_iid = ContactsTreeviewPopulator.companies_iid
                filtered_data_set[companies_iid] = ('Companies', '')

                companies = treeview.get_children(companies_iid)

                for company_iid in companies:
                    company_name = treeview.item(company_iid, 'text')
                    if filter_text.upper() in company_name.upper():
                        filtered_data_set[company_iid] = (company_name, companies_iid)
                        all_descendents = ContactsTreeviewPopulator.get_all_descendants(ContactsTreeviewPopulator.treeview, company_iid)
                        for descendent_iid in all_descendents:
                            descendent_name = treeview.item(descendent_iid, 'text')
                            parent = treeview.parent(descendent_iid)
                            filtered_data_set[descendent_iid] = (descendent_name, parent)
            else:
                people_iid = ContactsTreeviewPopulator.people_iid
                people = treeview.get_children(people_iid)

                filtered_data_set[people_iid] = ('People', '')

                for person_iid in people:
                    person_name = treeview.item(person_iid, 'text')
                    if filter_text.upper() in person_name.upper():
                        filtered_data_set[person_iid] = (person_name, people_iid)
                        all_descendents = ContactsTreeviewPopulator.get_all_descendants(ContactsTreeviewPopulator.treeview, person_iid)
                        for descendent_iid in all_descendents:
                            descendent_name = treeview.item(descendent_iid, 'text')
                            parent = treeview.parent(descendent_iid)
                            filtered_data_set[descendent_iid] = (descendent_name, parent)

            for item in ContactsTreeviewPopulator.treeview.get_children():
                treeview.delete(item)

            for iid in filtered_data_set.keys():
                text, parent = filtered_data_set[iid]
                ContactsTreeviewPopulator.add_node(treeview, text, parent, iid)

    @staticmethod
    def clear_contacts_treeview_filter():
        for item in ContactsTreeviewPopulator.treeview.get_children():
            ContactsTreeviewPopulator.treeview.delete(item)

        for iid in ContactsTreeviewPopulator.contact_data.keys():
            text, parent = ContactsTreeviewPopulator.contact_data[iid]
            ContactsTreeviewPopulator.add_node(ContactsTreeviewPopulator.treeview, text, parent, iid)

    @staticmethod
    def get_all_descendants(treeview, parent_iid):
        descendants = []
        children = treeview.get_children(parent_iid)
        for child in children:
            descendants.append(child)  # Add the immediate child
            descendants.extend(ContactsTreeviewPopulator.get_all_descendants(treeview, child))  # Add its descendants
        return descendants
