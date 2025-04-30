import config as cfg
from core.meta import utilities
from . import dal

def btn_add_contacts_clicked(window):
    window.create_modal_window_from_file(rf'{cfg.source_root}\core\ui\ui_elements\windows\add_contacts_window.json', window)


def btn_add_company_clicked(window):
    company_name = window.widget_registry.get('txt_company_name').widget.get()
    dal.insert_company(company_name)


def btn_add_person_clicked(window):
    pass