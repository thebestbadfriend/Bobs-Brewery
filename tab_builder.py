import tkinter as tk
from tkinter import ttk

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

    contacts_treeview = ttk.Treeview(contacts_tab)
    contacts_treeview.heading('#0', text='Companies', anchor=tk.W)

    contacts_treeview.insert('', tk.END, text='test company', iid=0, open=False)
    contacts_treeview.insert('', tk.END, text='nuther test company', iid=1, open=False)
    contacts_treeview.insert('', tk.END, text='test company again', iid=2, open=False)

    contacts_treeview.insert('', tk.END, text='People', iid=3, open=False)
    contacts_treeview.move(3,0,0)
    contacts_treeview.insert('', tk.END, text='Contact Info', iid=4, open=False)
    contacts_treeview.move(4,0,0)

    contacts_treeview.pack()

    btn_add_contact = tk.Button(contacts_tab,
                                text="Add Contact",
                                command=btn_commands.add_contact)
    btn_add_contact.pack()

    tab_control.add(contacts_tab, text="Contacts")