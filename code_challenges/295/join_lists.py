from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if len(lst_of_lst) == 0:
        return None
    result = []
    for l in lst_of_lst:
        for item in l:
            result.append(item)
        if l == lst_of_lst[-1]:
            return result
        else:
            result.append(sep)
