from pprint import pformat
from typing import Any


def pretty_string(obj: Any) -> str:
    return pformat(obj, width=60, depth=2)
