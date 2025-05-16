import importlib
from jinja2 import Template
import tkinter
import re

def get_or_import(module_path, class_name=''):
    importer = importlib.import_module(module_path)

    if class_name:
        importer = getattr(importer, class_name)

    return importer


def resolve_special_string(string_value, context):
    resolution_map = {
        '@obj@': resolve_object_reference_from_string,
        '@jinja@': parse_jinja_text
    }

    regex = r'^(@\w+@)(.+)'
    match = re.match(regex, string_value)

    if not match:
        return string_value

    prefix, remainder = match.groups()
    resolver = resolution_map.get(prefix)

    if not resolver:
        raise ValueError(f'Unknown prefix: {prefix}')

    return resolver(remainder, context)


def resolve_object_reference_from_string(string_value, context):
    obj = context
    string_value = string_value.split('.')

    for attr in string_value:
        obj = getattr(obj, attr)

    return obj


def parse_jinja_text(string_value, context):
    template = Template(string_value)
    '''
    need to figure out how to handle this. probably context here needs to not be the windowwrapper at all but
    a dictionary whose keys match the {{ }} parts of the template such that if the template is
    
    "now editing {{ contact_name }}"
    
    the dictionary might look like this:
    
    {
        "contact_name": "Michael"
    }
    
    For the update contact window, for example, the name of the contact being edited would need to be
    passed from the main window to the update contact window. This seems to require the use of something like
    window_kwargs (see update_contact_window.json), but--
    
    actually, yeah, context can be the windowwrapper, the window_kwargs can be an optional dictionary in the
    json, and it can have a key like "additional_jinja_patterns" which is itself a dictionary of jinja patterns.
    This dictionary can then - if it exists - be added to the full_dict["jinja_patterns"] dictionary which
    should be optionally available to all windows so that if it exists, it is used to process jinja templates
    by default and if it does not exist (or if that default parameter (cuz this should be in the form of a
    function with something like a "jinja_map" arg which defaults to context.full_dict['jinja_patterns'] or
    some such)) then attempts to process jinja patterns can be directed to a different pattern map or raise
    an error saying that no valid jinja pattern map was found.
    '''


def get_objectified_dict(dictionary):
    objectified_dict = dictionary.copy()

    for key, val in dictionary.items():
        if isinstance(val, str) and hasattr(tkinter, val):
            objectified_dict[key] = getattr(tkinter, val)

    return objectified_dict