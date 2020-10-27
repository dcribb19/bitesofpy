from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def decorator(func):
        @wraps(func)
        def wrapper(text, start=start, end=end):
            # Make sure start and end fit index ranges.
            if start > len(text):
                return text
            if start < 0:
                start = 0
            if end > len(text):
                end = len(text)
            # Convert text into list of chars.
            text_str = func(text=text)
            text_str = [char for char in text_str]
            # Replace chars with DOT by index range.
            for x in range(start, end):
                text_str[x] = DOT
            # Convert list back to string.
            return ''.join(text_str)
        return wrapper
    return decorator
