import textwrap

INDENTS = 4


def print_hanging_indents(poem):
    poem = textwrap.dedent(poem).strip()
    # split into paragraphs
    paragraphs = poem.split('\n\n')
    index = 0

    for paragraph in paragraphs:
        # create lines from paragraph
        lines = paragraph.splitlines()
        while index < len(lines):
            # no indent for first line
            if index == 0:
                print(lines[0])
                index += 1
            # indent all other lines
            else:
                print(' ' * INDENTS + lines[index])
                index += 1
        # reset index for additional paragraphs
        index = 0
