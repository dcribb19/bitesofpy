import os
import urllib.request
import re
from collections import Counter


# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)

non_alnum_strip = re.compile(r'[\W_]+')

def get_harry_most_common_word():
    with open(harry_text, encoding='utf8') as f:
        words = f.read().lower()
    with open(stopwords_file) as sf:
        stopwords = sf.read().lower()

    words = words.split()
    stopwords = stopwords.split()
    new_words = []

    for word in words:
        word = non_alnum_strip.sub('', word)
        if word not in stopwords and len(word) != 0:
            new_words.append(word)

    return Counter(new_words).most_common(1)[0]
