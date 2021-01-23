import re
from typing import List


def _get_code_tags(text: str) -> List[str]:
    '''Return all <code> to </code> tags.'''
    return re.findall(r'<code>.*?</code>', text)


def _get_pre_tags(text: str) -> List[str]:
    '''Return all <pre> to </pre> tags.'''
    return re.findall(r'<pre>.*?</pre>', text, re.DOTALL)


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    # org tags
    code_tags = _get_code_tags(org_text)
    pre_tags = _get_pre_tags(org_text)

    # trans tags
    rep_code_tags = _get_code_tags(trans_text)
    rep_pre_tags = _get_pre_tags(trans_text)

    for x, tag in enumerate(rep_code_tags):
        trans_text = trans_text.replace(tag, code_tags[x])

    for x, tag in enumerate(rep_pre_tags):
        trans_text = trans_text.replace(tag, pre_tags[x])

    return trans_text
