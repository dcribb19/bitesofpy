import os
import re
from difflib import SequenceMatcher
from itertools import permutations, combinations
from urllib.request import urlretrieve

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
TEMPFILE = os.path.join('/tmp', 'feed')
MIN_TAG_LEN = 10
IDENTICAL = 1.0
SIMILAR = 0.95

urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/tags.xml',
    TEMPFILE
)


def _get_tags(tempfile=TEMPFILE):
    """Helper to parse all tags from a static copy of PyBites' feed,
       providing this here so you can focus on difflib"""
    with open(tempfile) as f:
        content = f.read().lower()
    # take a small subset to keep it performant
    tags = TAG_HTML.findall(content)
    tags = [tag for tag in tags if len(tag) > MIN_TAG_LEN]
    return set(tags)


def get_similarities(tags=None):
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or _get_tags()
    return (tag for tag in permutations(tags, 2)
            if SequenceMatcher(None, tag[0], tag[1]).ratio() > SIMILAR)


def get_similarities_comb(tags=None):
    tags = tags or _get_tags()
    '''Also works, slightly slower for 1 execution .0066 vs .0042.'''
    return (tag for tag in combinations(tags, 2)
            if SequenceMatcher(None, tag[0], tag[1]).ratio() > SIMILAR
            or SequenceMatcher(None, tag[1], tag[0]).ratio() > SIMILAR)
