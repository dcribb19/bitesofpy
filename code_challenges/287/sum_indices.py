from collections import defaultdict
from itertools import accumulate
from typing import List


def sum_indices(items: List[str]) -> int:
    ...
    indices = 0
    d = defaultdict(list)
    for x in range(len(items)):
        d[items[x]].append(x)

    for value in d.values():
        indices += sum(accumulate(value))

    return indices
