# https://www.pythonguis.com/tutorials/create-gui-tkinter/
import os
from core.ui import WindowBuilder as wb


def main():
    # root = wb.create_main_window()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(BASE_DIR)
    root = wb.create_widget_from_file(rf"{BASE_DIR}\core\ui\ui_elements\windows\main_window.json")
    print('window should display in <1s')
    root.mainloop()



main()
