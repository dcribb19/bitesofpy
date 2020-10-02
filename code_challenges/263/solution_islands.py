def count_islands(grid):
    """
    Input: 2D matrix
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continously
        connected vertically or horizontically  by '1's.
    It's advised to check the grid boundary while iterating -
    as you don't go overboard.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                islands += 1
                mark_islands(r, c, grid)
    return islands


def mark_islands(i, j, grid):
    """
    Helper function to mark all visited islands, to avoid duplicate counts
    No return value. Modify the grid in-place.
    """
    dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    grid[i][j] = '#'
    rows, cols = len(grid), len(grid[0])

    for dir in dirs:
        nr, nc = i + dir[0], j + dir[1]
        if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
            if grid[nr][nc] == 1:  # Found it
                mark_islands(nr, nc, grid)
