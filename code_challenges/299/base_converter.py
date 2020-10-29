from math import floor
from string import ascii_uppercase, digits

BASES = digits + ascii_uppercase


def convert(number: int, base: int = 2) -> str:
    """Converts an integer into any base between 2 and 36 inclusive

    Args:
        number (int): Integer to convert
        base (int, optional): The base to convert the integer to.
        Defaults to 2.

    Raises:
        Exception (ValueError): If base is less than 2 or greater than 36

    Returns:
        str: The returned value as a string
    """
    if not isinstance(number, int):
        raise TypeError
    # Validate Base
    if base < 2 or base > 36:
        raise ValueError

    new_num = []
    while number != 0:
        r = number % base
        new_num.append(r)
        number = floor(number / base)

    new_num.reverse()
    return ''.join(BASES[x] for x in new_num)
