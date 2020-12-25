from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    groupings = _split_list(names, cols)
    for group in groupings:
        row = ''
        for name in group:
            row += f'| {name:<10}'
        print(row)


def _split_list(names: List[str], cols: int) -> List[List[str]]:
    '''Group names by number of columns'''
    splits = []
    lower_limit = 0
    upper_limit = cols
    while upper_limit <= len(names) + cols:
        splits.append(names[lower_limit:upper_limit])
        lower_limit += cols
        upper_limit += cols
    # remove last slice if empty
    if not splits[-1]:
        splits = splits[:-1]
    return splits
