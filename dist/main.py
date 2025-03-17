# https://www.pythonguis.com/tutorials/create-gui-tkinter/
import config as cfg
from core.ui import WindowBuilder as wb


def main():
    print('If this window is open, then the program is running.')
    print("It can take a few minutes to load. I'm working on improving that.")
    print()
    print("Note: closing this window will close Bob's Brewery.")

    root = wb.create_widget_from_file(rf"{cfg.source_root}\core\ui\ui_elements\windows\main_window.json")

    print('window should display in <1s')
    root.mainloop()


main()
