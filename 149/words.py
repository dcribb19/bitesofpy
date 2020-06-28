from string import digits

def sort_words_case_insensitively(words: list):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    # ignore case
    words.sort(key=str.lower)
    # sort numbers last
    words.sort(key=lambda word: word[0] in digits)
    return words
