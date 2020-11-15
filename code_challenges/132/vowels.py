from collections import Counter
VOWELS = list('aeiou')


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    words = [word.casefold() for word in text.split()]
    c = Counter()
    for word in words:
        if word not in c.keys():
            for char in word:
                if char in VOWELS:
                    c[word] += 1
    return c.most_common(1)[0]
