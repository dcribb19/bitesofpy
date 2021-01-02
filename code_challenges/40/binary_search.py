from math import floor
from typing import List, Union


def binary_search(sequence: List[Union[int, str]],
                  target: Union[int, str]
                  ) -> Union[int, None]:
    left_end = 0
    right_end = len(sequence) - 1
    while left_end <= right_end:
        middle = floor((left_end + right_end) / 2)
        if sequence[middle] < target:
            left_end = middle + 1
        elif sequence[middle] > target:
            right_end = middle - 1
        else:
            return middle
    return None
