from typing import List


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a list of words in case insensitive ways.
    Output: Common words appearing in both sentences.
            Capital and lowercase words are treated as the same word.

            If there are duplicate words in the results, just choose one word.
            Returned words should be sorted by word's length.
    """
    return sorted({x.lower() for x in sentence1} &
                  {x.lower() for x in sentence2},
                  key=len)
