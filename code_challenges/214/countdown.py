def countdown():
    """Write a generator that counts from 100 to 1"""
    x = 100
    while x > 0:
        yield x
        x -= 1