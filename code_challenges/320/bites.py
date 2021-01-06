from dataclasses import dataclass
from enum import IntEnum
from typing import List  # TODO: can remove >= 3.9


class BiteLevel(IntEnum):
    INTRO = 1
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4


@dataclass
class Bite:
    number: int
    title: str
    level: BiteLevel

    def __lt__(self, other) -> bool:
        return self.number < other.number


def create_bites(numbers: List[int],
                 titles: List[str],
                 levels: List[BiteLevel]):
    """Generate a generator of Bite dataclass objects"""
    return (Bite(number, title, level)
            for number, title, level
            in zip(numbers, titles, levels))
