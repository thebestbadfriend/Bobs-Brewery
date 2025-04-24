import tkinter as tk
from tkinter import ttk


class BBTreeview(ttk.Treeview):
    next_iid = 0

    def add_node(self, text, parent=''):
        iid = self.next_iid
        self.insert(parent, tk.END, text=text, iid=iid, open=False)
        self.next_iid += 1
        return iid
