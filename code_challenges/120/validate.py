from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapper(*args):
        if not all(isinstance(arg, int) for arg in args):
            raise TypeError('All args must be integers.')
        if not all(arg >= 0 for arg in args):
            raise ValueError('All args must be >= 0.')
        return func(*args)
    return wrapper
