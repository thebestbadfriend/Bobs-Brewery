import tkinter as tk
from ui import notebook_builder as nb


def create_window(title, min_width, min_height, max_width, max_height, xpos, ypos, geometry_string):
    window = tk.Tk()
    window.title(title)
    window.minsize(min_width, min_height)
    window.maxsize(max_width, max_height)
    window.geometry(geometry_string)

    return window


def create_main_window():
    root = create_window(title="Bob's Brewery",
                         min_width=300,
                         min_height=300,
                         max_width=3000,
                         max_height=3000,
                         xpos=800,
                         ypos=200,
                         geometry_string="800x600")

    tab_control = nb.create_main_window_tab_control(root)
    tab_control.pack(expand=1, fill="both")

    return root
