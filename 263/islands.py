def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continously
        connected vertically or horizontically  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    islands = 0
    # completely mark grid
    for y in range(len(grid)):
        for x in range(len(grid)):
            try:
                if grid[x][y] == 1:
                    mark_islands(x, y, grid)
            except IndexError:
                return 0

    for y in range(len(grid)):
        for x in range(len(grid)):
            # RIGHT EDGE: Check up if not top.
            if x == len(grid[0]) - 1 and y != 0:
                if grid[y][x] == '#':
                    if grid[y-1][x] == 0:
                        islands += 1
            # BOTTOM: Check right if not right edge.
            elif y == len(grid) - 1:
                if grid[y][x] == '#':
                    if grid[y][x+1] == 0:
                        islands += 1
            # LEFT EDGE: Check right and down if not bottom.
            elif x == 0:
                if grid[y][x] == '#':
                    # Check right
                    if grid[y][x+1] == 0:
                        # Check down
                        if grid[y+1][x] == 0:
                            islands += 1
            # TOP: Check left and down if not left edge.
            elif y == 0:
                if grid[y][x] == '#':
                    # Check left
                    if grid[y][x-1] == 0:
                        # Check down
                        if grid[y+1][x] == 0:
                            islands += 1
            # MIDDLE
            else:
                if grid[y][x] == '#':
                    # Check right
                    if grid[y][x+1] == 0:
                        # Check down
                        if grid[y+1][x] == 0:
                            islands += 1
    return islands


def mark_islands(i, j, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visisted islands as in-place operation.
    """
    grid[i][j] = '#'
