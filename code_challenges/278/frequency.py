from collections import Counter

def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """

    n = Counter(numbers).most_common()
    major = n[0][0]
    minor = n[-1][0]

    return major, minor