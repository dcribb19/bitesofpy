import re
from typing import List


def get_sentences(text: str) -> List[str]:
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    text = text.replace('\n', ' ').strip()
    return re.findall(r'[A-Z].*?(?<![A-Z(])\.*[.?!]', text)
