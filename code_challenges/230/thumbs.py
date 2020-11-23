THUMBS_UP, THUMBS_DOWN = '👍', '👎'


class Thumbs:
    def __mul__(self, other):
        if other == 0:
            raise ValueError('Specify a number')
        elif other > 0 and other < 4:
            return THUMBS_UP * other
        elif other >= 4:
            return f'{THUMBS_UP} ({other}x)'
        elif other < 0 and other > -4:
            return THUMBS_DOWN * abs(other)
        else:
            return f'{THUMBS_DOWN} ({abs(other)}x)'

    def __rmul__(self, other):
        if other == 0:
            raise ValueError('Specify a number')
        elif other > 0 and other < 4:
            return THUMBS_UP * other
        elif other >= 4:
            return f'{THUMBS_UP} ({other}x)'
        elif other < 0 and other > -4:
            return THUMBS_DOWN * abs(other)
        else:
            return f'{THUMBS_DOWN} ({abs(other)}x)'
