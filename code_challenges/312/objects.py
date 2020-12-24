import builtins
from keyword import iskeyword
from importlib import import_module
from typing import Dict, List

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
    score = 0
    for obj in objects:
        # obj can be BOTH KEYWORD AND BUILTIN
        if obj in dir(builtins) and iskeyword(obj):
            score += scores['builtin'] + scores['keyword']
        elif obj in dir(builtins):
            score += scores['builtin']
        elif iskeyword(obj):
            score += scores['keyword']
        else:
            try:
                import_module(obj)
                score += scores['module']
            except ModuleNotFoundError:
                continue
    return score
