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


@pytest.mark.parametrize('out', [
    [1, 5, -5],
    [10], 
    [-1000, 52],
])


def test_list_out_of_range(out):
    with pytest.raises(ValueError):
        list_to_decimal(out)


@pytest.mark.parametrize('wrong_type', [
    [6, 2, True],
    [3.6, 4, 1],
    ['4', 5, 3, 1],
    True,
    5, 
    {'type' : 'error'},
])

def test_list_wrong_type(wrong_type):
    with pytest.raises(TypeError):
        list_to_decimal(wrong_type)
