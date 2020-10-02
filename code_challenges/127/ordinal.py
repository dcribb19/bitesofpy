def get_ordinal_suffix(number: int):
    """Receives a number int and returns it appended with its ordinal suffix,
       so 1 -> 1st, 2 -> 2nd, 4 -> 4th, 11 -> 11th, etc.

       Rules:
       https://en.wikipedia.org/wiki/Ordinal_indicator#English
       - st is used with numbers ending in 1 (e.g. 1st, pronounced first)
       - nd is used with numbers ending in 2 (e.g. 92nd, pronounced ninety-second)
       - rd is used with numbers ending in 3 (e.g. 33rd, pronounced thirty-third)
       - As an exception to the above rules, all the "teen" numbers ending with
         11, 12 or 13 use -th (e.g. 11th, pronounced eleventh, 112th,
         pronounced one hundred [and] twelfth)
       - th is used for all other numbers (e.g. 9th, pronounced ninth).
       """
    if number == 11 or number == 12 or number == 13:
        return str(number) + 'th'
    number = str(number)
    if number.endswith('11'):
        return number + 'th'
    elif number.endswith('1'):
        return number + 'st'
    elif number.endswith('2'):
        return number + 'nd'
    elif number.endswith('3'):
        return number + 'rd'
    else:
        return number + 'th'
