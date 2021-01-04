from itertools import zip_longest
from textwrap import TextWrapper
from typing import List

COL_WIDTH = 20
COL_SPACING = ' ' * 6


def _format_lines(lines: List[str]) -> List[str]:
    '''Return list of strings, all of width COL_WIDTH'''
    return [f'{line:{COL_WIDTH}}' for line in lines]


def _zip_join(*args):
    """
    Zip paragraphs together by line,
    join lines together,
    return lines
    """
    lines = list(zip_longest(*args, fillvalue=' ' * COL_WIDTH))
    # convert tuples to lists
    lines = [list(line) for line in lines]
    lines = '\n'.join([COL_SPACING.join(line) for line in lines])
    return lines


def text_to_columns(text: str) -> str:
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    # split into paragraphs by double newlines
    paragraphs = text.split('\n\n')
    # strip whitespace
    paragraphs = [txt.strip() for txt in paragraphs]

    wrapper = TextWrapper(width=COL_WIDTH)
    paragraphs = [wrapper.wrap(txt) for txt in paragraphs]
    paragraphs = [_format_lines(paragraph) for paragraph in paragraphs]

    if len(paragraphs) == 1:
        return '\n'.join(paragraphs[0])
    elif len(paragraphs) == 2:
        a, b = paragraphs
        return _zip_join(a, b)
    elif len(paragraphs) == 3:
        a, b, c = paragraphs
        return _zip_join(a, b, c)
    elif len(paragraphs) == 4:
        a, b, c, d = paragraphs
        return _zip_join(a, b, c, d)
    else:
        print("I'm not quite sure how to scale this.")


if __name__ == '__main__':
    text1 = """My house is small but cosy."""
    text2 = """My house is small but cosy.

    It has a white kitchen and an empty fridge."""
    text4 = """My house is small but cosy.

    It has a white kitchen and an empty fridge.

    I have a very comfortable couch, people love to sit on it.

    My mornings are filled with coffee and reading, if only I had a garden"""
    p = text_to_columns(text2)
    print(p)
