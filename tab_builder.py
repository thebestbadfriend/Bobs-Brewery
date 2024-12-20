import tkinter as tk
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

    btn_add_contact = tk.Button(contacts_tab,
                                text="Add Contact",
                                command=btn_commands.add_contact)
    btn_add_contact.pack()

    tab_control.add(contacts_tab, text="Contacts")