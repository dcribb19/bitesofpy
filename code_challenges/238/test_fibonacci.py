# test_fibonacci.py

import pytest
from fibonacci import fib

@pytest.mark.parametrize('n, expected', [
    (0, 0),
    (1, 1),
    (2, 1),
    (5, 5),
    (10, 55),
    (25, 75025),
    (30, 832040),
])


def test_fib(n, expected):
    assert fib(n) == expected


def test_fib_out_of_range():
    with pytest.raises(ValueError):
        fib(-1)
