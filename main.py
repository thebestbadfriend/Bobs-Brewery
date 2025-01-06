# https://www.pythonguis.com/tutorials/create-gui-tkinter/

# from window_builder import WindowBuilder as wb
from ui import WindowBuilder as wb



def main():
    # root = wb.create_main_window()
    root = wb.create_window_from_file(r"C:\Toolbox\Coding\Brewers Truss\Bobs-Brewery\ui\ui_elements\windows\main_window.json")
    root.mainloop()


main()
