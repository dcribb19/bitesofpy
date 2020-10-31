import inspect
from string import ascii_uppercase


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""
    return [cls[0] for cls in inspect.getmembers(mod, inspect.isclass)
            if cls[0][0] in ascii_uppercase]
