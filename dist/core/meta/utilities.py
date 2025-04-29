import importlib
import tkinter

def get_or_import(module_path, class_name=''):
    importer = importlib.import_module(module_path)

    if class_name:
        importer = getattr(importer, class_name)

    return importer


def resolve_object_reference_from_string(string_value, context):
    if not string_value.startswith('@@'):
        return string_value

    object_path = string_value[2:].split('.')
    obj = context

    for attr in object_path:
        obj = getattr(obj, attr)

    return obj


def get_objectified_dict(dictionary):
    objectified_dict = dictionary.copy()

    for key, val in dictionary.items():
        if isinstance(val, str) and hasattr(tkinter, val):
            objectified_dict[key] = getattr(tkinter, val)

    return objectified_dict