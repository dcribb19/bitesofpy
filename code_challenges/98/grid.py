from string import digits
from typing import List, Tuple

DOWN, UP, LEFT, RIGHT = '⇓', '⇑', '⇐', '⇒'
START_VALUE = 1


def _convert_grid(grid: str) -> List[List[int]]:
    '''Convert grid str into 2D matrix of ints'''
    lines = [x.replace('-', '') for x in grid.splitlines()]
    lines = [line.split() for line in lines
             if any(digit in line for digit in digits)]
    arr = []
    for line in lines:
        a_line = []
        for x in line:
            a_line.append(int(x))
        arr.append(a_line)
    return arr


def _get_coords(grid: List[List[int]]) -> List[Tuple[int, int, int]]:
    coords = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            coords.append((grid[i][j], i, j))
    return sorted(coords)


def _same_dir(line: List[int],
              num: int,
              i: int,
              j: int) -> Tuple[List[int], int, int]:
    '''Add num to line if same direction'''
    line.append(num)
    return line, i, j


def _diff_dir(line: List[int],
              d: str,
              num: int,
              i: int,
              j: int) -> Tuple[List[int], int, int, int]:
    '''Add turn to line for different direction, reset line and add num'''
    line.append(d)
    print(' '.join(str(x) for x in line))
    line = []
    line.append(num)
    return line, i, j, d


def print_sequence_route(grid: str) -> None:
    """Receive grid string, convert to 2D matrix of ints, find the
       START_VALUE coordinates and move through the numbers in order printing
       them.  Each time you turn append the grid with its corresponding symbol
       (DOWN / UP / LEFT / RIGHT). See the TESTS for more info."""
    grid = _convert_grid(grid)
    coords = _get_coords(grid)

    # initial point
    num, last_i, last_j = coords[0]
    line = []
    line.append(num)
    last_dir = RIGHT

    for coord in coords[1:]:
        num, i, j = coord
        if j - last_j == 1:  # RIGHT
            d = RIGHT
            if d == last_dir:
                line, last_i, last_j = _same_dir(line, num, i, j)
            else:
                line, last_i, last_j, last_dir = _diff_dir(line, d, num, i, j)
        elif last_j - j == 1:  # LEFT
            d = LEFT
            if d == last_dir:
                line, last_i, last_j = _same_dir(line, num, i, j)
            else:
                line, last_i, last_j, last_dir = _diff_dir(line, d, num, i, j)
        elif i - last_i == 1:  # DOWN
            d = DOWN
            if d == last_dir:
                line, last_i, last_j = _same_dir(line, num, i, j)
            else:
                line, last_i, last_j, last_dir = _diff_dir(line, d, num, i, j)
        else:  # last_y - y == 1, UP
            d = UP
            if d == last_dir:
                line, last_i, last_j = _same_dir(line, num, i, j)
            else:
                line, last_i, last_j, last_dir = _diff_dir(line, d, num, i, j)
    print(' '.join(str(x) for x in line))
