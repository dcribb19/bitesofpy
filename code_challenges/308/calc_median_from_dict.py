from statistics import median


def _yield_nums(d):
    '''Helper to yield k v times from dict.'''
    for k, v in d.items():
        x = 0
        while x < v:
            yield k
            x += 1


def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    if not all(isinstance(v, int) or isinstance(v, float) for v in d.values()):
        raise TypeError

    if sum(d.values()) < 1_000_000_000:
        nums = _yield_nums(d)
        return median(nums)  # does not work for large numbers - MemoryError
    else:  # LARGE NUMBERS
        num = sum([k*v for k, v in d.items()])
        denom = sum(d.values())
        return round(num / denom)

        '''
        # TOO SLOW - LIST
        lst = []
        for k, v in d.items():
            x = 0
            while x < v:
                lst.append(k)
                x += 1
        return median(lst)
        '''

        # return median(Counter(d).elements())  # TOO SLOW - ITERTOOLS CHAIN
