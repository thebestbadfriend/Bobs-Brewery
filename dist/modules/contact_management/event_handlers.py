import config as cfg
from core.meta import utilities
from . import dal


def btn_open_wnd_add_contact_clicked(window):
    window.create_modal_window_from_file(rf'{cfg.source_root}\core\ui\ui_elements\windows\wnd_add_contact.json', window)


def btn_update_contact_clicked(window):
    window.create_modal_window_from_file(rf'{cfg.source_root}\core\ui\ui_elements\windows\update_contact_window.json', window)


def btn_submit_add_company_clicked(window):
    company_name = window.widget_registry.get('txt_company_name').widget.get()
    dal.insert_company(company_name)


def btn_submit_add_person_clicked(window):
    first_name = window.widget_registry.get('txt_person_first_name').widget.get()
    last_name = window.widget_registry.get('txt_person_last_name').widget.get()
    suffix = window.widget_registry.get('txt_person_suffix').widget.get()
    nickname = window.widget_registry.get('txt_person_nickname').widget.get()

    dal.insert_person(first_name, last_name, nickname, suffix)