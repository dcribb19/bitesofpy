def round_to_next(number: int, multiple: int):
    next_mult = 0
    if number % multiple == 0:
        return number
    elif multiple < 0:
        multiple = abs(multiple)
        while next_mult < abs(number):
            next_mult += multiple
        return -(next_mult)
    else:
        while next_mult < number:
            next_mult += multiple
        return next_mult
