import os
from collections import Counter
import urllib.request
import re

# prep
if not os.path.exists('/tmp'):
    os.makedirs('/tmp')

tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()

# start coding
# tags are reflected as <category>tag</category>
tags = re.findall(r'(?<=<category>)\w+\s*\w+(?=</category>)', content)

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    return Counter(tags).most_common(n)
