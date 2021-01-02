import re
from typing import Any, List


def has_timestamp(text: str) -> bool:
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    if re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', text):
        return True
    return False


def is_integer(number: Any) -> bool:
    """Return True if number is an integer"""
    if isinstance(number, int):
        return True
    return False


def has_word_with_dashes(text: str) -> bool:
    """Returns True if text has one or more words with dashes"""
    if re.search(r'\w-\w', text):
        return True
    return False


def remove_all_parenthesis_words(text: str) -> str:
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    return re.sub(r'\s\(\S+\)', '', text)


def split_string_on_punctuation(text: str) -> List[str]:
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    splits = re.split(r'[?!.,;]', text)
    # remove empty splits and strip whitespace
    return [split.strip() for split in splits if split]


def remove_duplicate_spacing(text: str) -> str:
    """Replace multiple spaces by one space"""
    return re.sub(r'\s+', ' ', text)


def has_three_consecutive_vowels(word: str) -> str:
    """Returns True if word has at least 3 consecutive vowels"""
    word = word.lower()
    if re.search(r'[aeiou]{3}', word):
        return True
    return False


def convert_emea_date_to_amer_date(date: str) -> str:
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    if re.search(r'\d{2}/\d{2}/\d{4}', date):
        date = f'{date[3:5]}/{date[:2]}{date[-5:]}'
    return date
