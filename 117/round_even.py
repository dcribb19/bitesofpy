import decimal


def round_even(number):
    """Takes a number and returns it rounded even"""
    # number = decimal.Decimal(number)
    number = decimal.Decimal(number)
    number = number.to_integral(rounding=decimal.ROUND_HALF_EVEN)
    return number
