from math import floor


def dec_to_base(number: int, base: int):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    remainders = []
    # Validate base
    if base not in [2, 6, 8]:
        raise ValueError('Base should be 2, 6, or 8.')
    while number != 0:
        r = number % base
        remainders.append(r)
        number = floor(number / base)
    remainders.reverse()
    return int(''.join([str(x) for x in remainders]))


def dec_to_base_recursion(number: int, base: int, result=''):
    # Validate Base
    if base not in [2, 6, 8]:
        raise ValueError('Base should be 2, 6, or 8.')
    if number == 0:
        return int(result)
    else:
        result = str(number % base) + result
        number = floor(number / base)
        return dec_to_base_recursion(number, base, result)
