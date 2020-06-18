import string

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    for char in input_string:
        if char in string.punctuation:
            input_string = input_string.replace(char, '')
    return input_string

    # return [input_string.replace(char, '') for char in input_string if char in string.punctuation]
    