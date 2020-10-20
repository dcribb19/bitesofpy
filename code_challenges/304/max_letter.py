from collections import Counter
import re
from string import digits, punctuation, ascii_letters
from typing import Tuple


def remove_emoji(string):
    '''Remove emojis from string.'''
    emoji_pattern = re.compile(
        "["u"\U0001F600-\U0001F64F"  # emoticons
           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
           u"\U0001F680-\U0001F6FF"  # transport & map symbols
           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
           u"\U00002702-\U000027B0"
           u"\U000024C2-\U0001F251"
           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


def strip_non_ascii_punctuation(string):
    strip_chars = ''
    for char in string:
        if char not in ascii_letters:
            strip_chars += char
    return string.strip(strip_chars)


def max_letter_word(text: str) -> Tuple[str, str, int]:
    """
    Find the word in text with the most repeated letters. If more than one word
    has the highest number of repeated letters choose the first one. Return a
    tuple of the word, the (first) repeated letter and the count of that letter
    in the word.
    >>> max_letter_word('I have just returned from a visit...')
    ('returned', 'r', 2)
    >>> max_letter_word('$5000 !!')
    ('', '', 0)
    """
    # Validate input as str.
    if not isinstance(text, str):
        raise ValueError
    # Case: Empty string.
    if text == '':
        return (text, text, 0)
    # Case: No ascii_letters, so no words.
    if not any(letter in ascii_letters for letter in text):
        return ('', '', 0)

    text = remove_emoji(text)
    text = strip_non_ascii_punctuation(text)

    # Split string into words.
    text = text.split()

    letter_counts = []
    for word in text:
        count_word = word.casefold()
        for letter in count_word:
            # Don't count digits or punctuation.
            if letter in digits:
                count_word = word.replace(letter, '')
            if letter in punctuation:
                count_word = count_word.replace(letter, '')
        if count_word == '':
            # Don't use counter on empty string.
            letter_counts.append((word, [('', 0)]))
        else:
            c = Counter(count_word)
            letter_counts.append((word.strip(punctuation), c.most_common(1)))

    max_count = sorted(
        letter_counts,
        key=lambda x: x[1][0][1],
        reverse=True
        )[0]

    return (max_count[0], max_count[1][0][0], max_count[1][0][1])
