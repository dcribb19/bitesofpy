import string
import re

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    filtered_names = []
    for name in names:
        if name.startswith(QUIT_CHAR):
            break
        if name.startswith(IGNORE_CHAR):
            continue
        if re.search(r'\d', name):
            continue
        if len(filtered_names) < MAX_NAMES:
            filtered_names.append(name)
    return filtered_names