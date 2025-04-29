import config as cfg

def btn_add_contacts_clicked(window):
    from core.ui import WindowWrapper
    WindowWrapper.create_modal_window_from_file(rf'{cfg.source_root}\core\ui\ui_elements\windows\add_contacts_window.json', window)


def btn_add_company_clicked(window):
    print(window.widget_registry['txt_company_name'].widget.get())

def btn_add_person_clicked(window):
    pass