from tkinter import ttk
from ui import TabBuilder


class NotebookBuilder:
    def create_main_window_tab_control(self, window):
        tab_control = ttk.Notebook(window)
        tab_builder = TabBuilder()

        tab_builder.create_main_tab(tab_control)
        tab_builder.create_favorite_programs_tab(tab_control)
        tab_builder.create_contacts_tab(tab_control)

        return tab_control
