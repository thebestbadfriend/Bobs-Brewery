import config as cfg

def btn_add_contacts_clicked():
    from core.ui.window_builder import WindowBuilder as WB
    WB.create_modal_window_from_file(rf'{cfg.source_root}\core\ui\ui_elements\windows\add_contacts_window.json')
