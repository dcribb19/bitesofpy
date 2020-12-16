from math import factorial
from typing import List


def _binomial_coefficient(n: int, k: int) -> int:
    '''Return binomial coefficient'''
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    if N == 0:
        return []
    else:
        n = N - 1
        return [_binomial_coefficient(n, k) for k in range(N)]
