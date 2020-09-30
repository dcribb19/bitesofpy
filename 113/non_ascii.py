from string import ascii_letters, digits, punctuation, whitespace


def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    text = text.split()
    # return [word for word in text]
    return [word for word in text if not all(
        [letter in ascii_letters or
         letter in digits or
         letter in punctuation or
         letter in whitespace
         for letter in word
         ]) and word not in punctuation]
