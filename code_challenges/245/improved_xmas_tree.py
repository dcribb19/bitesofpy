from math import ceil

STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows: int = 10):
    """Generate a xmas tree with a star (+), leaves (*) and a trunk (|)
       for given rows of leaves (default 10).
       For more information see the test and the bite description"""
    max_row_len = rows * 2 - 1
    tree = []
    star = f'{STAR:^{max_row_len}}'
    tree.append(star)

    for row in range(1, rows + 1):
        num_leaves = row * 2 - 1
        tree.append(f'{LEAF * num_leaves:^{max_row_len}}')

    if rows % 2 == 0:
        trunk = f'{TRUNK * (ceil(max_row_len / 2) + 1):^{max_row_len}}'
    else:
        trunk = f'{TRUNK * ceil(max_row_len / 2):^{max_row_len}}'
    tree.append(trunk)
    tree.append(trunk)

    full_tree = '\n'.join(tree)
    return full_tree
