import pytest

from numbers_to_dec import list_to_decimal

@pytest.mark.parametrize('numbers, expected', [
    ([1, 7, 5], 175),
    ([0, 3, 1, 2], 312),
    ([0, 4, 2, 8], 428),
    ([3], 3),
])


def test_list_to_decimal(numbers, expected):
    assert list_to_decimal(numbers) == expected


def test_list_out_of_range():
    with pytest.raises(ValueError):
        list_to_decimal([1, 5, -5])
        list_to_decimal([15])


def test_list_wrong_type():
    with pytest.raises(TypeError):
        list_to_decimal([6, 2, True])
        list_to_decimal([3.6, 4, 1])
        list_to_decimal(['4', 5, 3, 1])
