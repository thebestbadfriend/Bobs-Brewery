from dal import BreweryDBAccessor
import tkinter as tk


class ContactsTreeviewPopulator:
    # probably de-static the methods here and make this class more instance-dependant
    # this will allow different populators for different treeviews and will make it easier to just
    # set a `treeview` var at initialization which binds each populator to its associated treeview.
    # should make everything a lot simpler.
    treeview = None
    bda = BreweryDBAccessor()
    contact_data = {}
    current_filtered_data = {}
    companies_iid = None
    people_iid = None
    next_iid = 1

    @staticmethod
    def add_node(treeview, text, parent='', iid=None):
        if not iid:
            iid = ContactsTreeviewPopulator.next_iid

            while iid in ContactsTreeviewPopulator.contact_data.keys():
                iid += 1

            ContactsTreeviewPopulator.next_iid = iid + 1


        treeview.insert(parent, tk.END, text=text, iid=iid, open=False)

        iid_exists = ContactsTreeviewPopulator.contact_data.get(iid)
        if not iid_exists:
            ContactsTreeviewPopulator.contact_data[iid] = (text, parent)

        return iid

    @staticmethod
    def populate_contacts_treeview(contacts_treeview):
        ContactsTreeviewPopulator.treeview = contacts_treeview
        contacts_treeview.heading('#0', text='Contacts', anchor=tk.W)

        ContactsTreeviewPopulator.companies_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Companies')
        companies_iid = ContactsTreeviewPopulator.companies_iid

        ContactsTreeviewPopulator.people_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'People')
        people_iid = ContactsTreeviewPopulator.people_iid

        companies = ContactsTreeviewPopulator.bda.execute_db_command('select id, name, contact_id from companies')
        if companies:
            for company in companies:
                company_details = {
                    "id": company[0],
                    "name": company[1],
                    "contact_id": company[2]
                }

                company_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, company_details['name'], companies_iid)

                company_locations_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Locations', parent=str(company_iid))
                company_locations_query = (rf'''select id, street_address, po_box, city, state, zip_code
                                              from addresses
                                              join contacts_addresses on
                                              addresses.id = contacts_addresses.address_id
                                              where contacts_addresses.contact_id = {company_details['contact_id']}''')
                company_locations = ContactsTreeviewPopulator.bda.execute_db_command(company_locations_query)
                if company_locations:
                    for location in company_locations:
                        company_location_details = {
                            "id": location[0],
                            "street_address": location[1],
                            "po_box": location[2],
                            "city": location[3],
                            "state": location[4],
                            "zip_code": location[5]
                        }

                        address_string = ''
                        for k, v in list(company_location_details.items())[1:]:
                            if v:
                                if not address_string:
                                    address_string = str(v)
                                elif k == 'zip_code':
                                    address_string = address_string + ' ' + str(v)
                                else:
                                    address_string = address_string + ', ' + str(v)

                        company_location_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, address_string, parent=str(company_locations_iid))

                        location_people_query = rf'''select people.contact_id, first_name, last_name, suffix, nickname
                                                     from people
                                                     join contacts_addresses on people.contact_id = contacts_addresses.contact_id
                                                     join addresses on addresses.id = contacts_addresses.address_id
                                                     where addresses.id = {company_location_details['id']}'''
                        location_people = ContactsTreeviewPopulator.bda.execute_db_command(location_people_query)
                        if location_people:
                            location_people_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'People', parent=str(company_location_iid))
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

                                person_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, person_string, parent=str(location_people_iid))

                                # person phone numbers
                                person_phone_numbers_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Phone Numbers', parent=str(person_iid))
                                phone_numbers_query = rf'''select phone_number
                                                          from phone_numbers
                                                          join contacts_phone_numbers
                                                          on phone_numbers.id = contacts_phone_numbers.phone_number_id
                                                          join people on contacts_phone_numbers.contact_id = people.contact_id
                                                          where people.contact_id = {person_details['contact_id']}'''
                                phone_numbers = ContactsTreeviewPopulator.bda.execute_db_command(phone_numbers_query)
                                if phone_numbers:
                                    for number in phone_numbers:
                                        phone_number = number[0]
                                        ContactsTreeviewPopulator.add_node(contacts_treeview, phone_number, parent=str(person_phone_numbers_iid))

                                # person email addresses
                                person_email_addresses_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Email Addresses', parent=str(person_iid))
                                email_addresses_query = rf'''select email_address
                                                             from email_addresses
                                                             join contacts_email_addresses
                                                             on email_addresses.id = contacts_email_addresses.email_address_id
                                                             join people on contacts_email_addresses.contact_id = people.contact_id
                                                             where people.contact_id = {person_details['contact_id']}'''
                                email_addresses = ContactsTreeviewPopulator.bda.execute_db_command(email_addresses_query)
                                if email_addresses:
                                    for e in email_addresses:
                                        email_address = e[0]
                                        ContactsTreeviewPopulator.add_node(contacts_treeview, email_address, parent=str(person_email_addresses_iid))

                        # location phone numbers not assigned to person ("other phone numbers")
                        personless_phone_numbers_iid = ""

                people_without_locations_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'People (no location)', parent=str(company_iid))
                people_without_locations_query = rf'''select p.contact_id, first_name, last_name, suffix, nickname
                                                      from people p
                                                      join people_companies pc on p.id = pc.person_id
                                                      where pc.company_id = {company_details['id']}
                                                      and p.contact_id not in (select contact_id from contacts_addresses)'''
                people_without_locations = ContactsTreeviewPopulator.bda.execute_db_command(people_without_locations_query)
                if people_without_locations:
                    for p in people_without_locations:
                        person = {
                            'contact_id': p[0],
                            'first_name': p[1],
                            'last_name': p[2],
                            'suffix': p[3],
                            'nickname': p[4]
                        }
                        person_string = ''
                        if person['first_name']:
                            person_string = str(person['first_name'])
                        if person['nickname']:
                            person_string += ' "' + person['nickname'] + '"'
                        if person['last_name']:
                            person_string += ' ' + person['last_name']
                        if person['suffix']:
                            person_string += ' ' + person['suffix']

                        person_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, person_string,
                                                                        parent=str(people_without_locations_iid))

                        phone_numbers_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Phone Numbers',
                                                                        parent=str(person_iid))
                        phone_numbers_query = rf'''select phone_number
                                                   from phone_numbers
                                                   join contacts_phone_numbers
                                                   on phone_numbers.id = contacts_phone_numbers.phone_number_id
                                                   where contacts_phone_numbers.contact_id = {person['contact_id']}'''
                        phone_numbers = ContactsTreeviewPopulator.bda.execute_db_command(phone_numbers_query)
                        if phone_numbers:
                            for pn in phone_numbers:
                                phone_number = pn[0]
                                ContactsTreeviewPopulator.add_node(contacts_treeview, phone_number, parent=str(phone_numbers_iid))

                        email_addresses_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Email Addresses',
                                                                        parent=str(person_iid))
                        email_addresses_query = rf'''select email_address
                                                     from email_addresses
                                                     join contacts_email_addresses
                                                     on email_addresses.id = contacts_email_addresses.email_address_id
                                                     where contacts_email_addresses.contact_id = {person['contact_id']}'''
                        email_addresses = ContactsTreeviewPopulator.bda.execute_db_command(email_addresses_query)
                        if email_addresses:
                            for e in email_addresses:
                                email_address = e[0]
                                ContactsTreeviewPopulator.add_node(contacts_treeview, email_address, parent=str(email_addresses_iid))

                other_contact_info_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Other Contact Info', parent=str(company_iid))
                other_phone_numbers_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Phone Numbers', parent=str(other_contact_info_iid))
                other_email_addresses_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Email Addresses', parent=str(other_contact_info_iid))

        # get unattached people
        people_query = rf'''select first_name, last_name, suffix, nickname, contact_id from people'''
        people = ContactsTreeviewPopulator.bda.execute_db_command(people_query)

        # for person in unattached people
        for p in people:
            # unattached person
            person = {
                'first_name': p[0],
                'last_name': p[1],
                'suffix': p[2],
                'nickname': p[3],
                'contact_id': p[4]
            }

            person_string = ''
            if person['first_name']:
                person_string = str(person['first_name'])
            if person['nickname']:
                person_string += ' "' + person['nickname'] + '"'
            if person['last_name']:
                person_string += ' ' + person['last_name']
            if person['suffix']:
                person_string += ' ' + person['suffix']

            person_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, person_string, parent=str(people_iid))

            # address(es)
            person_addresses_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Address(es)', parent=str(person_iid))
            addresses_query = rf'''select id, street_address, po_box, city, state, zip_code
                                   from addresses
                                   join contacts_addresses on
                                   addresses.id = contacts_addresses.address_id
                                   where contacts_addresses.contact_id = {person['contact_id']}'''
            addresses = ContactsTreeviewPopulator.bda.execute_db_command(addresses_query)
            if addresses:
                for a in addresses:
                    address = {
                        'id': a[0],
                        'street_address': a[1],
                        'po_box': a[2],
                        'city': a[3],
                        'state': a[4],
                        'zip_code': a[5]
                    }


                    address_string = ''

                    for k, v in list(address.items())[1:]:
                        if v:
                            if not address_string:
                                address_string = str(v)
                            elif k == 'zip_code':
                                address_string = address_string + ' ' + str(v)
                            else:
                                address_string = address_string + ', ' + str(v)

                    ContactsTreeviewPopulator.add_node(contacts_treeview, address_string, parent=str(person_addresses_iid))

            # phone numbers
            person_phone_numbers_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Phone Numbers', parent=str(person_iid))
            phone_numbers_query = rf'''select phone_number
                                       from phone_numbers
                                       join contacts_phone_numbers
                                       on phone_numbers.id = contacts_phone_numbers.phone_number_id
                                       where contacts_phone_numbers.contact_id = {person['contact_id']}'''
            phone_numbers = ContactsTreeviewPopulator.bda.execute_db_command(phone_numbers_query)
            if phone_numbers:
                for pn in phone_numbers:
                    phone_number = pn[0]
                    ContactsTreeviewPopulator.add_node(contacts_treeview, phone_number, parent=str(person_phone_numbers_iid))

            # email addresses
            person_email_addresses_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Email Addresses', parent=str(person_iid))
            email_addresses_query = rf'''select email_address
                                         from email_addresses
                                         join contacts_email_addresses
                                         on email_addresses.id = contacts_email_addresses.email_address_id
                                         where contacts_email_addresses.contact_id = {person['contact_id']}'''
            email_addresses = ContactsTreeviewPopulator.bda.execute_db_command(email_addresses_query)
            if email_addresses:
                for e in email_addresses:
                    email_address = e[0]
                    ContactsTreeviewPopulator.add_node(contacts_treeview, email_address, parent=str(person_email_addresses_iid))

    @staticmethod
    def filter_contacts_treeview(event, filter_by, widget=None):
        treeview = ContactsTreeviewPopulator.treeview
        filtered_data_set = ContactsTreeviewPopulator.current_filtered_data

        filter_text = ''
        if widget:
            filter_text = widget.get()
        else:
            print('No widget found')

        if not filter_text:
            print('No filter text found')
            ContactsTreeviewPopulator.clear_contacts_treeview_filter()
            filtered_data_set.clear()
        else:
            filtered_data_set.clear()
            if filter_by == 'companies':
                companies_iid = ContactsTreeviewPopulator.companies_iid
                companies = treeview.get_children(companies_iid)

                filtered_data_set[companies_iid] = ('Companies', '')
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
        print('Clearing contacts treeview filter')
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
