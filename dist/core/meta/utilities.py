import importlib
import tkinter

def get_or_import(module_path, class_name=''):
    importer = importlib.import_module(module_path)

    if class_name:
        importer = getattr(importer, class_name)

    return importer


def resolve_special_string(string_value, context):
    resolution_map = {
        '@obj@': resolve_object_reference_from_string,
        '@text@': resolve_text_from_function_reference
    }
    resolver_string = rf"@{string_value.split('@')[0]}@"
    string_remainder = string_value[len(resolver_string):]
    resolution_map[resolver_string](string_remainder, context)


def resolve_object_reference_from_string(string_value, context):
    obj = context

    for attr in string_value:
        obj = getattr(obj, attr)

    return obj


def resolve_text_from_function_reference(string_value, context):
    pass


def get_objectified_dict(dictionary):
    objectified_dict = dictionary.copy()

    for key, val in dictionary.items():
        if isinstance(val, str) and hasattr(tkinter, val):
            objectified_dict[key] = getattr(tkinter, val)

    return objectified_dict