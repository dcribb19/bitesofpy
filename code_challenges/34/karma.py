from collections import namedtuple
from datetime import datetime
from typing import List

Transaction = namedtuple('Transaction', 'giver points date')
# https://twitter.com/raymondh/status/953173419486359552
Transaction.__new__.__defaults__ = (datetime.now(),)


class User:
    def __init__(self, name: str):
        self.name: str = name
        self._transactions: List[Transaction] = []

    def __str__(self) -> str:
        if self.fans == 1:
            return (f'{self.name} has a karma of {self.karma} '
                    f'and {self.fans} fan')
        else:
            return (f'{self.name} has a karma of {self.karma} '
                    f'and {self.fans} fans')

    def __add__(self, trans: Transaction):
        self._transactions.append(trans)

    @property
    def points(self) -> List[int]:
        return [t.points for t in self._transactions]

    @property
    def karma(self) -> int:
        return sum(self.points)

    @property
    def fans(self) -> int:
        return len(set([t.giver.name for t in self._transactions]))
