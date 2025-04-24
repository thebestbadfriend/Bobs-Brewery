# https://www.pythonguis.com/tutorials/create-gui-tkinter/
import config as cfg
from core.ui import WindowWrapper


def main():
    print("Note: closing this window will close Bob's Brewery.")

    root = WindowWrapper.load_window_from_file(rf"{cfg.source_root}\core\ui\ui_elements\windows\main_window.json")
    root.window.mainloop()


main()
