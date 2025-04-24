import importlib

def get_or_import_library(library_name):
    return importlib.import_module(library_name)