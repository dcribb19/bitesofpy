def is_anagram(word1: str, word2: str):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')
    chars_1 = [char for char in word1]
    chars_2 = [char for char in word2]

    if (all(char in word2 for char in chars_1) and
       all(char in word1 for char in chars_2) and
       len(word1) == len(word2)):
        return True
    else:
        return False
