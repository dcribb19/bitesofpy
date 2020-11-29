from typing import List


def two_sums(numbers: List[int], target: int):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    sort_nums = sorted(numbers)
    for x in sort_nums:
        for y in sort_nums:
            if x + y == target:
                return numbers.index(x), numbers.index(y)
    return None
