from dal import BreweryDBAccessor
import tkinter as tk


class TreeviewPopulators:
    bda = BreweryDBAccessor()
    next_iid = 0

    @staticmethod
    def add_node_to_treeview(treeview, text, parent=''):
        iid = TreeviewPopulators.next_iid
        treeview.insert(parent, tk.END, text=text, iid=iid, open=False)
        TreeviewPopulators.next_iid += 1
        return iid

    @staticmethod
    def populate_contacts_treeview(contacts_treeview):
        contacts_treeview.heading('#0', text='Companies', anchor=tk.W)
        companies = TreeviewPopulators.bda.execute_db_command('select * from companies')

        if companies:
            for company in companies:
                company_details = {
                    "id": company[0],
                    "name": company[1],
                    "contact_id": company[2]
                }

                company_iid = TreeviewPopulators.add_node_to_treeview(contacts_treeview, company_details['name'])
                locations_iid = TreeviewPopulators.add_node_to_treeview(contacts_treeview, 'Locations', parent=str(company_iid))
                people_without_locations_iid = TreeviewPopulators.add_node_to_treeview(contacts_treeview, 'People (no location)', parent=str(company_iid))
                other_contact_info_iid = TreeviewPopulators.add_node_to_treeview(contacts_treeview, 'Other Contact Info', parent=str(company_iid))

