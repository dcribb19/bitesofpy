from math import trunc
from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError('n must be positive.')
    r_numbers = []
    numbers = [str(number * 10**(n-1)) for number in numbers]
    for number in numbers:
        if number.startswith('-'):
            r_numbers.append(int(number[:n+1]))
        else:
            r_numbers.append(int(number[:n]))
    return r_numbers
