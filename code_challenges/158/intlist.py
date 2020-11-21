from decimal import Decimal
from statistics import mean, median


class IntList(list):
    def __init__(self, lst):
        super().__init__(lst)

    def append(self, value):
        if isinstance(value, int):
            super().append(value)
        elif isinstance(value, float) or isinstance(value, Decimal):
            super().append(int(value))
        elif isinstance(value, list):
            if all([isinstance(x, int) for x in value]):
                for item in value:
                    super().append(item)
            else:
                raise TypeError
        else:
            raise TypeError

    def __add__(self, x):
        return self.append(x)

    def __iadd__(self, x):
        self.append(x)
        return self

    @property
    def mean(self):
        return mean(self)

    @property
    def median(self):
        return median(self)
