from string import ascii_uppercase
from itertools import cycle

DIGITS = [x for x in range(1, 27)]


def sequence_generator():
    seq = zip(DIGITS, ascii_uppercase)
    return cycle(i for item in seq for i in item)
