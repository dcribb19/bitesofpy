def positive_divide(numerator: int, denominator: int) -> int:
    try:
        div = numerator / denominator
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise
    if div < 0:
        raise ValueError
    return div