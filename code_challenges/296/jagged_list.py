from typing import List


def jagged_list(lst_of_lst: List[List[int]],
                fillvalue: int = 0) -> List[List[int]]:
    new_lst_of_lst = []

    try:
        max_len = max([len(lst) for lst in lst_of_lst])
    except ValueError:
        return new_lst_of_lst

    for lst in lst_of_lst:
        new_lst = lst.copy()
        while len(new_lst) < max_len:
            new_lst.append(fillvalue)
        new_lst_of_lst.append(new_lst)
    return new_lst_of_lst
