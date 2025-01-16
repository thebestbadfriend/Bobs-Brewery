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
        companies = ContactsTreeviewPopulator.bda.execute_db_command('select * from companies')

        if companies:
            for company in companies:
                company_details = {
                    "id": company[0],
                    "name": company[1],
                    "contact_id": company[2]
                }

                company_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, company_details['name'])
                locations_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Locations', parent=str(company_iid))

                people_without_locations_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'People (no location)', parent=str(company_iid))
                other_contact_info_iid = ContactsTreeviewPopulator.add_node(contacts_treeview, 'Other Contact Info', parent=str(company_iid))
