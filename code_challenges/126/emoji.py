import sys
from typing import Dict
import unicodedata


START_EMOJI_RANGE = 100000  # estimate


def what_means_emoji(emoji: str):
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    try:
        return unicodedata.name(emoji)
    except TypeError:
        return 'Not found'
    except ValueError:
        return 'none such name'


def _make_emoji_mapping() -> Dict[str, str]:
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""
    emoji_map = {}
    for x in range(START_EMOJI_RANGE, sys.maxunicode + 1):
        name = what_means_emoji(chr(x))
        if name not in ['Not found', 'none such name']:
            emoji_map[chr(x)] = name
    return emoji_map


def find_emoji(term: str):
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""
    term = term.upper()

    emoji_mapping = _make_emoji_mapping()

    for k, v in emoji_mapping.items():
        if term in v:
            print(f'{v:60} | {k}')


if __name__ == '__main__':
    find_emoji(sys.argv[1])
