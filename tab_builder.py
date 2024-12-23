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

    contacts_treeview = create_contacts_treeview(contacts_tab)

    contacts_treeview.pack(fill=tk.BOTH, expand=1)

    btn_add_contact = tk.Button(contacts_tab,
                                text="Add Contact",
                                command=btn_commands.add_contact)
    btn_add_contact.pack()

    '''
    btn_edit_contact = tk.Button(contacts_tab)
    
    need to an option to say "if this phone number is associated with a specific location, add it to that
    location with this button or context menu"
    '''

    tab_control.add(contacts_tab, text="Contacts")


def create_contacts_treeview(contacts_tab):
    contacts_treeview = btv(contacts_tab)
    contacts_treeview.heading('#0', text='Companies', anchor=tk.W)

    companies = bda.execute_db_command('select * from companies')
    if companies:
        for company in companies:
            company_details = {
                "id": company[0],
                "name": company[1],
                "contact_id": company[2]
            }

            build_contacts_treeview_company(contacts_treeview, company_details)

    contacts_treeview.add_node('(No Company)')

    return contacts_treeview


def build_contacts_treeview_company(contacts_treeview, company_details):
    company_iid = contacts_treeview.add_node(company_details['name'])
    company_contact_info_iid = contacts_treeview.add_node('Contact Details', company_iid)

    company_phone_numbers_iid = contacts_treeview.add_node('Phone Numbers', company_contact_info_iid)
    # Soon, I would like to make this only put phone numbers which are associated with the company but not with
    # any individuals in this section. For now though, it is ok that phone numbers belonging to individuals also show
    # up here. I might even make it toggleable rather than strictly the other way. Maybe some people like it better.
    results = bda.execute_db_command(f"""select phone_number
                                         from phone_numbers
                                         join contacts_phone_numbers
                                         on phone_numbers.id = contacts_phone_numbers.phone_number_id
                                         where contacts_phone_numbers.contact_id = {company_details['contact_id']}""")
    if results:
        for result in results:
            contacts_treeview.add_node(str(result[0]), company_phone_numbers_iid)

    company_fax_numbers_iid = contacts_treeview.add_node('Fax Numbers', company_contact_info_iid)
    results = bda.execute_db_command(f"""select fax_number
                                         from fax_numbers
                                         join contacts_fax_numbers
                                         on fax_numbers.id = contacts_fax_numbers.fax_number_id
                                         where contacts_fax_numbers.contact_id = {company_details['contact_id']}""")
    if results:
        for result in results:
            contacts_treeview.add_node(str(result[0]), company_fax_numbers_iid)

    company_email_addresses_iid = contacts_treeview.add_node('Email Addresses', company_contact_info_iid)
    results = bda.execute_db_command(f"""select email_address
                                         from email_addresses
                                         join contacts_email_addresses
                                         on email_addresses.id = contacts_email_addresses.email_address_id
                                         where contacts_email_addresses.contact_id = {company_details['contact_id']}""")
    if results:
        for result in results:
            contacts_treeview.add_node(str(result[0]), company_email_addresses_iid)

    company_websites_iid = contacts_treeview.add_node('Websites', company_contact_info_iid)
    results = bda.execute_db_command(f"""select url
                                         from websites
                                         join contacts_websites
                                         on websites.id = contacts_websites.website_id
                                         where contacts_websites.contact_id = {company_details['contact_id']}""")
    if results:
        for result in results:
            contacts_treeview.add_node(str(result[0]), company_websites_iid)

    company_addresses_iid = contacts_treeview.add_node('Addresses', company_contact_info_iid)
    results = bda.execute_db_command(f"""select street_address, po_box, city, state, zip_code
                                         from addresses
                                         join contacts_addresses
                                         on addresses.id = contacts_addresses.address_id
                                         where contacts_addresses.contact_id = {company_details['contact_id']}""")
    if results:
        for result in results:
            parsed_result = result[0] + ', ' + result[1] + ', ' + result[2] + ', ' + result[3] + ' ' + result[4]
            contacts_treeview.add_node(str(parsed_result), company_addresses_iid)

    employees_iid = contacts_treeview.add_node('People', company_iid)
