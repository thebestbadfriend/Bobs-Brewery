# https://www.pythonguis.com/tutorials/create-gui-tkinter/
import json
import tkinter as tk
from tkinter import ttk
import os


def create_window(title, min_width, min_height, max_width, max_height, xpos, ypos, geometry_string):
    window = tk.Tk()
    window.title(title)
    window.minsize(min_width, min_height)
    window.maxsize(max_width, max_height)
    window.geometry(geometry_string)

    return window


def create_main_window_tab_control(window):
    tab_control = ttk.Notebook(window)

    # First Tab
    main_tab = tk.Frame(tab_control)
    btn_fix_server = tk.Button(main_tab, text="Fix Server Access", command=fix_server_access)
    btn_fix_server.pack()

    tab_control.add(main_tab, text="Main Controls")

    # Second Tab
    favorite_programs_tab = tk.Frame(tab_control)
    # Include a list of the current favorites, options to add/remove programs, and so on
    btn_open_favorite_programs = tk.Button(favorite_programs_tab, text="Open Favorite Programs", command=open_favorite_programs)
    btn_open_favorite_programs.pack()

    tab_control.add(favorite_programs_tab, text="Favorite Programs")

    return tab_control


def create_main_window():
    root = create_window(title="Bob's Brewery",
                         min_width=300,
                         min_height=300,
                         max_width=3000,
                         max_height=3000,
                         xpos=800,
                         ypos=200,
                         geometry_string="")

    tab_control = create_main_window_tab_control(root)
    tab_control.pack(expand=1, fill="both")

    return root


def fix_server_access():
    os.system("net use")


def open_favorite_programs():
    with open("favorite_programs.json", "r") as favorite_programs_file:
        data = json.load(favorite_programs_file)

        for program in data:
            os.system(program["path"])


def main():
    root = create_main_window()
    root.mainloop()


main()
