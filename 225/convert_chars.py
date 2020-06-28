PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    new_text = ''
    for char in text:
       if char.lower() in PYBITES:
          char = char.swapcase()
       new_text += char
    return new_text
    