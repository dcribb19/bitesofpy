from typing import List


def minimum_number(digits: List[int]) -> int:
    if len(digits) == 0:
        return 0
    # remove duplicates
    digits = set(digits)
    digits = sorted(digits)
    
    num_str = ''
    for n in digits:
        num_str += str(n)
    if num_str.startswith('0') and len(num_str) > 1:
        return int(num_str[1:])
    else:
        return int(num_str)
    