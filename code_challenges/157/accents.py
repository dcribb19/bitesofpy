from string import printable


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return sorted([char.lower() for char in text if char not in printable])
