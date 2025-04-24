import importlib
import tkinter

def get_or_import_library(library_name):
    return importlib.import_module(library_name)


def get_objectified_dict(dictionary):
    objectified_dict = dictionary.copy()

    for key, val in dictionary.items():
        if isinstance(val, str) and hasattr(tkinter, val):
            objectified_dict[key] = getattr(tkinter, val)

    return objectified_dict