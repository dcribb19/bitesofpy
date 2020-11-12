from string import whitespace
from typing import List


def split_once(text: str, separators: str = None) -> List[str]:
    '''Takes a string and splits text on separators but only on
    first instance of the delimiter.'''
    split_list = []

    if not separators:
        separators = whitespace

    if not any(separator in text for separator in separators):
        return [text]
    else:
        for char in text:
            if char in separators:
                start, end = text.split(char, maxsplit=1)
                split_list.append(start)
                text = end
                separators = separators.replace(char, '')

                if not any(separator in text for separator in separators):
                    split_list.append(text)
                    break
        return split_list
