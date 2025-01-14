from dal import brewery_db_accessor as bda
import tkinter as tk


def add_node_to_treeview(treeview, text, parent=''):
    iid = treeview.next_iid
    treeview.insert(parent, tk.END, text=text, iid=iid, open=False)
    treeview.next_iid += 1
    return iid


def populate_contacts_treeview():
    print("reached populate_contacts_treeview")
