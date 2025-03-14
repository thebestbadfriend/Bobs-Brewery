# https://www.pythonguis.com/tutorials/create-gui-tkinter/
import config as cfg
from core.ui import WindowBuilder as wb


def main():
    root = wb.create_widget_from_file(rf"{cfg.project_root}\core\ui\ui_elements\windows\main_window.json")
    print('window should display in <1s')
    root.mainloop()



main()
