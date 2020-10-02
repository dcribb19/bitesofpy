from fizzbuzz import fizzbuzz
import pytest


@pytest.mark.parametrize('n, expected', [
    (15, 'Fizz Buzz'),
    (30, 'Fizz Buzz'),
    (9, 'Fizz'),
    (12, 'Fizz'),
    (10, 'Buzz'),
    (200, 'Buzz'),
    (2, 2),
    (17, 17)
])
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected
