def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.
    cm / 2.54 = in
    in * 2.54 = cm
    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.lower()
    if isinstance(value, int) == False and isinstance(value, float) == False:
        raise TypeError
    if fmt != 'in' and fmt != 'cm':
        raise ValueError
    if fmt == 'in':
        return round(value / 2.54, 4)
    if fmt == 'cm':
        return round(value * 2.54, 4)