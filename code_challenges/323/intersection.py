from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    args = [set(arg) for arg in args if arg]
    if len(args) == 0:
        return set()
    elif len(args) == 1:
        return args[0]
    else:
        return set.intersection(*args)
