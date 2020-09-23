from functools import wraps

def make_html(element):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            return f'<{element}>' + text + f'</{element}>'
        return wrapper
    return decorator
