import inspect
from string import ascii_uppercase


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""
    members = inspect.getmembers(mod)
    return [cls[0] for cls in members
            if inspect.isclass(cls[1])
            and cls[0][0] in ascii_uppercase]
