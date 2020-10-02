STAR = '*'


def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    rows = []
    for row in range(1, width + 1, 2):
        padding = int((width - row) / 2)
        rows.append(f"{' ' * padding}{STAR * row}{' ' * padding}")

    bottom = rows.copy()
    bottom.reverse()
    bottom.pop(0)

    rows = rows + bottom
    for row in rows:
        yield row
