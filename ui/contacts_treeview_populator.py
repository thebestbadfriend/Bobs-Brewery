from dal import BreweryDBAccessor
import tkinter as tk


class ContactsTreeviewPopulator:
    bda = BreweryDBAccessor()
    next_iid = 0

    @staticmethod
    def add_node(treeview, text, parent=''):
        iid = ContactsTreeviewPopulator.next_iid
        treeview.insert(parent, tk.END, text=text, iid=iid, open=False)
        ContactsTreeviewPopulator.next_iid += 1
        return iid

    @staticmethod
    def populate_contacts_treeview(contacts_treeview):
        contacts_treeview.heading('#0', text='Companies', anchor=tk.W)

        companies = ContactsTreeviewPopulator.bda.execute_db_command('select id, name, contact_id from companies')
        if companies:
            for company in companies:
                company_details = {
                    "id": company[0],
                    "name": company[1],
                    "contact_id": company[2]
                }

                company_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, company_details['name'])

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
                                    phone_number = phone_numbers[0]
                                    ContactsTreeviewPopulator.add_node(contacts_treeview, phone_number, parent=str(person_phone_numbers_iid))

                                # person email addresses
                                person_email_addresses_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Email Addresses', parent=str(person_iid))


                        # location phone numbers not assigned to person ("other phone numbers")

                people_without_locations_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'People (no location)', parent=str(company_iid))
                other_contact_info_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Other Contact Info', parent=str(company_iid))

        # get unattached people
        unattached_people_query = rf'''select first_name, last_name, suffix, nickname
                                       from people
                                       left join people_companies on people.id = people_companies.person_id
                                       where people_companies.company_id is null'''
        unattached_people = ContactsTreeviewPopulator.bda.execute_db_command(unattached_people_query)
        # if unattached people
        if unattached_people:
            print(unattached_people)
            unattached_people_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'People Not Attached To Companies')
            # for person in unattached people
            for person in []:
                # unattached person
                person_details = {}
                person_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, '', parent=str(unattached_people_iid))

                # address(es)
                person_addresses_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Address(es)', parent=str(unattached_people_iid))

                # phone numbers
                person_phone_numbers_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Phone Numbers', parent=str(person_iid))

                # email addresses
                person_email_addresses_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Email Addresses', parent=str(person_iid))
