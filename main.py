# https://www.pythonguis.com/tutorials/create-gui-tkinter/

from core.ui import WindowBuilder as wb


def main():
    # root = wb.create_main_window()
    root = wb.create_widget_from_file(r"core\ui\ui_elements\windows\main_window.json")
    root.mainloop()


main()
