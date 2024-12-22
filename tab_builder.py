import tkinter as tk
from tkinter import ttk
import brewery_db_accessor as bda
from brewery_treeview import BreweryTreeview as btv

import btn_commands


def create_main_tab(tab_control):
    main_tab = tk.Frame(tab_control)
    btn_fix_server = tk.Button(main_tab, text="Fix Server Access", command=btn_commands.fix_server_access)
    btn_fix_server.pack()

    tab_control.add(main_tab, text="Main Controls")


def create_favorite_programs_tab(tab_control):
    favorite_programs_tab = tk.Frame(tab_control)

    # Include a list of the current favorites, options to add/remove programs, and so on
    btn_open_favorite_programs = tk.Button(favorite_programs_tab,
                                           text="Open Favorite Programs",
                                           command=btn_commands.open_favorite_programs)
    btn_open_favorite_programs.pack()

    tab_control.add(favorite_programs_tab, text="Favorite Programs")


def create_contacts_tab(tab_control):
    contacts_tab = tk.Frame(tab_control)

    contacts_treeview = btv(contacts_tab)
    contacts_treeview.heading('#0', text='Companies', anchor=tk.W)

    companies = bda.execute_db_command('select * from companies')
    if companies:
        for company in companies:
            company_id = company[0]
            company_name = company[1]
            company_contact_id = company[2]

            company_iid = contacts_treeview.add_node(company_name)

            company_contact_info_iid = contacts_treeview.add_node('Contact Details', company_iid)
            company_phone_numbers_iid = contacts_treeview.add_node('Phone Numbers',company_contact_info_iid)
            company_fax_numbers_iid = contacts_treeview.add_node('Fax Numbers', company_contact_info_iid)
            company_email_addresses_iid = contacts_treeview.add_node('Email Addresses', company_contact_info_iid)

            employees_iid = contacts_treeview.add_node('People', company_iid)

            # create people subnodes first, with all their relevant data
            # then create contact details subnodes for any remaining contact info
            #
            # that is, contact details which are associated with people, will go in the subnodes for those people,
            # but contact details which are associated only with the company and not with any individuals will go in
            # the contact appropriate details subnodes.

    '''
    contacts_treeview.insert('', tk.END, text='test company', iid=0, open=False)
    contacts_treeview.insert('', tk.END, text='nuther test company', iid=1, open=False)
    contacts_treeview.insert('', tk.END, text='test company again', iid=2, open=False)

    contacts_treeview.insert('', tk.END, text='People', iid=3, open=False)
    contacts_treeview.move(3,0,0)
    contacts_treeview.insert('', tk.END, text='Contact Info', iid=4, open=False)
    contacts_treeview.move(4,0,0)
    '''
    contacts_treeview.pack(fill=tk.BOTH, expand=1)

    btn_add_contact = tk.Button(contacts_tab,
                                text="Add Contact",
                                command=btn_commands.add_contact)
    btn_add_contact.pack()

    tab_control.add(contacts_tab, text="Contacts")
