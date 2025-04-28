import config as cfg

def btn_add_contacts_clicked(window):
    from core.ui import WindowWrapper
    WindowWrapper.create_modal_window_from_file(rf'{cfg.source_root}\core\ui\ui_elements\windows\add_contacts_window.json')
