from collections import OrderedDict

roman_numerals = OrderedDict({
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    500: 'D',
    900: 'CM',
    1000: 'M'
})


def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    nums = []
    rn = ''

    if not isinstance(decimal_number, int):
        raise ValueError
    if decimal_number <= 0 and decimal_number >= 4000:
        raise ValueError

    while decimal_number != 0:
        for num in list(roman_numerals.keys()):
            if decimal_number >= num:
                nums.append(num)

        rn += roman_numerals[nums[-1]]
        decimal_number = decimal_number - nums[-1]
        nums = []
    return rn
