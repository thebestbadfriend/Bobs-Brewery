# https://www.pythonguis.com/tutorials/create-gui-tkinter/
import config as cfg
from core.ui import WindowBuilder as wb


def main():
    print("Note: closing this window will close Bob's Brewery.")

    root = wb.create_widget_from_file(rf"{cfg.source_root}\core\ui\ui_elements\windows\main_window.json")

    root.mainloop()


main()
