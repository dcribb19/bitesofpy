from dataclasses import dataclass, field
from heapq import nlargest, nsmallest
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str
    bites: int

    def __lt__(self, other) -> bool:
        return self.bites < other

    def __gt__(self, other) -> bool:
        return self.bites > other

    def __eq__(self, other) -> bool:
        return self.bites == other

    def __str__(self) -> str:
        return f'[{self.bites}] {self.name}'


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an
            optional count parameter indicating how many of the highest
            ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking
            Ninjas, also supports an optional count parameter returns how
            many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    rankings: List[Ninja] = field(default_factory=list)

    def add(self, ninja: Ninja):
        self.rankings.append(ninja)

    def dump(self):
        low_rank = self.lowest()[0]
        self.rankings.remove(low_rank)
        return low_rank

    def highest(self, count: int = 1):
        return nlargest(count, self.rankings)

    def lowest(self, count: int = 1):
        return nsmallest(count, self.rankings)

    def __len__(self):
        return len(self.rankings)

    def pair_up(self, count: int = 3) -> List[Tuple]:
        high = self.highest(count)
        low = self.lowest(count)
        return list(zip(high, low))
