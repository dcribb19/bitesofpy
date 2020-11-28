import re


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    sentences = re.findall(r'[^.!?]*[.!?]', text)
    return ' '.join([sentence.strip().capitalize() for sentence in sentences])
