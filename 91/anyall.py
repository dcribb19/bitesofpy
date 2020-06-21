import string

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return all(char in VOWELS for char in input_str.lower())


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return any(char in PYTHON for char in input_str.lower())


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return any(char in string.digits for char in input_str)